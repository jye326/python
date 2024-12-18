#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# get_ipython().system('pip install librosa')


# In[ ]:


# get_ipython().system('pip install audioread filetype moviepy')


# In[21]:


import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import matplotlib.animation as animation
import soundfile as sf
import base64
import sys
import threading
import boto3
from urllib.parse import unquote
from IPython.display import Audio, display, HTML
from matplotlib import rc
from IPython.display import Video
from urllib.parse import urlparse

rc('animation', html='jshtml')

def download_from_s3(s3_url, local_path):
    """S3에서 파일 다운로드: HTTPS 형식의 S3 URL을 받아 로컬에 다운로드"""
    parsed_url = urlparse(s3_url)
    bucket_name = parsed_url.netloc.split('.')[0]
    key = unquote(parsed_url.path.lstrip('/'))  # URL 디코딩된 키 사용

    print(bucket_name, key)
    
    # 경로 자동 설정
    if os.name == 'nt':  # Windows
        local_path = f"C:\\temp\\{os.path.basename(local_path)}"
    else:  # Linux
        local_path = f"/tmp/{os.path.basename(local_path)}"

    # S3에서 파일 다운로드
    s3 = boto3.client(
        's3',
       
    )
    s3.download_file(bucket_name, key, local_path)
    return local_path  # 변경된 경로 반환

# 오디오 파일 경로
import filetype
from moviepy.editor import AudioFileClip

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(1)
    
    file1 = sys.argv[1]  # 첫번째 인자
    file2 = sys.argv[2]  # 두번째 인자

    # HTTPS S3 URL인지 확인하여 로컬로 다운로드
    if file1.startswith("https://") and "amazonaws.com" in file1:
        file1_local = download_from_s3(file1, "/tmp/file1.wav")
    else:
        file1_local = file1

    if file2.startswith("https://") and "amazonaws.com" in file2:
        file2_local = download_from_s3(file2, "/tmp/file2.wav")
    else:
        file2_local = file2


def convert_to_mp3(input_file, output_file):
    try:
        audio_clip = AudioFileClip(input_file)
        audio_clip.write_audiofile(output_file, codec='mp3')
        # print(f"Converted {input_file} to {output_file}")
    except Exception as e:
        print(f"Error converting {input_file} to MP3: {e}")

# 파일 형식 확인
def check_and_convert(file_path):
    kind = filetype.guess(file_path)
    if kind is None:
        # print(f"Cannot guess file type for {file_path}!")
        return file_path #변환하지 않고 원본파일 사용
    # print(f"File extension: {kind.extension}")
    # print(f"File MIME type: {kind.mime}")
    
    if kind.extension != 'mp3':
        output_file = os.path.splitext(file_path)[0] + ".mp3"
        convert_to_mp3(file_path, output_file)
        return output_file # 변환된 파일 경로 반환
    else:
        return file_path#이미 MP3인 경우 원본 파일 반환
    
file1 = check_and_convert(file1_local)  #파일 확장자 문제 있었음. 음원 파일이 mp3가 아니라 mp4등의 비디오 파일인 경우는 librosa에서 지원하지 않으므로 moviepy를 이용해서 mp3로 변환 한 후에 사용
file2 = check_and_convert(file2_local)  # 파일 확장자만 바꾼다고 형식이 바뀌지는 않음.

    
# 오디오 파일 로드
y1, sr1 = librosa.load(file1)
y2, sr2 = librosa.load(file2)


# 기본 주파수 추정
f0, voiced_flag, voiced_probs = librosa.pyin(y1,sr=sr1, fmin = librosa.note_to_hz('C2'), fmax=librosa.note_to_hz('C7'))
f0_2, voiced_flag_2, voiced_probs_2 = librosa.pyin(y2, sr = sr2, fmin = librosa.note_to_hz('C2'), fmax=librosa.note_to_hz('C7'))


# NaN 값을 선형 보간법으로 채우기
f0_interpolated = pd.Series(f0).interpolate().to_numpy()
f0_2_interpolated = pd.Series(f0_2).interpolate().to_numpy()


from datetime import datetime
# jupyter전용 : 정적인 그래프 처리용 백엔드 모드
# get_ipython().run_line_magic('matplotlib', 'inline')

# 시간 축 계산
times = librosa.times_like(f0, sr=sr1)
times_2 = librosa.times_like(f0_2, sr=sr2)


# 그래프로 주파수 시각화
plt.figure(figsize=(14, 6))
plt.plot(times, f0_interpolated, label='Estimated F0 - File 1', color='r')
plt.plot(times_2, f0_2_interpolated, label='Estimated F0 - File 2', color='b')


plt.ylim([librosa.note_to_hz('C2'), 650])

current_time = datetime.now().strftime('%Y%m%d_%H%M%S') # 'YYYYMMDD_HHMMSS' 형식

plt.savefig(f'sim_wave_{current_time}.png', dpi=300, facecolor='white', edgecolor='black',orientation='portrait', format='png', transparent=False, bbox_inches = 'tight', pad_inches=0.1)
#plt.show()

import json


# 분석 위한 데이터 전처리
def music_prep(music_1, music_2):
  # 두 주파수 데이터의 최소 길이 맞추기
  min_length = min(len(music_1), len(music_2))
  music_1 = music_1[:min_length]
  music_2 = music_2[:min_length]

  # NaN 값이 있는 인덱스 제거
  valid_idx = ~np.isnan(music_1) & ~np.isnan(music_2)
  music_1_valid = music_1[valid_idx]
  music_2_valid = music_2[valid_idx]
  return music_1_valid, music_2_valid

# 평균 유사도 계산
def calc_similarity(music_1, music_2):
  # 전처리
  music_1, music_2 = music_prep(music_1, music_2)

  # 두 주파수 값의 차이 계산
  music_difference = np.abs(music_1 - music_2)

  # 평균 절대 차이 계산
  mean_difference = np.mean(music_difference)


  # 최대 주파수 범위, 비교 기준인 music_1의 주파수 범위
  freq_scope =  max(music_1) - min(music_1)


  # 평균 유사도 계산 (1-(평균 차이 / 주파수 범위))
  similarity = (1 - (mean_difference / freq_scope)) * 100
  similarity = round(similarity, 2)
  # print(f'The overall frequency similarity between the two audio files is approximately {similarity:.2f}%')
  return similarity
  

def upload_to_s3(file_path, bucket_name, s3_key):
    """S3에 파일 업로드"""
    s3 = boto3.client(
        's3',
        
    )
    try:
        s3.upload_file(file_path, bucket_name, s3_key)
        print(f"File {file_path} uploaded to {bucket_name}/{s3_key}")
        s3_url = f"https://{bucket_name}.s3.amazonaws.com/{s3_key}"
        return s3_url
    except Exception as e:
        print(f"Failed to upload {file_path} to S3: {e}")
        return None

# 가장 비슷한 부분, 가장 다른 부분 찾기
def find_segment(music_1, music_2, sr, hop_length, time_length):
  # 전처리
  music_1, music_2 = music_prep(music_1, music_2)

  # hop_length / sr = 한 프레임이 차지하는 시간
  valid_duration_seconds = len(music_1) * hop_length / sr

  # noticible_time_length (초) 만큼에 해당하는 프레임 갯수
  frame_length = int(time_length / (hop_length / sr))

  # print(f'Duration of valid (non-NaN) data: {valid_duration_seconds:.2f} seconds')

  # 두 주파수 값의 차이 계산
  music_difference = np.abs(music_1 - music_2)

  # 가장 큰 차이 값을 가지는 구간 찾기
  max_diff = 0
  max_index = 0
  for i in range(len(music_difference) - frame_length +1):
    current_diff = np.sum(music_difference[i:i+frame_length])
    if current_diff > max_diff :
      max_diff = current_diff
      max_index = i
  # print(f'Maximum difference found in the frame range starting at index {max_index} with a total difference of {max_diff}')

  # 가장 적은 차이 값을 가지는 구간 찾기
  min_diff = 650 * 5
  min_index = 0
  for i in range(len(music_difference) - frame_length +1):
    current_diff = np.sum(music_difference[i:i+frame_length])
    if current_diff < min_diff :
      min_diff = current_diff
      min_index = i
  # print(f'Minimum difference found in the frame range starting at index {min_index} with a total difference of {min_diff}')

  # 해당 구간의 시간대 계산
  worst_time = max_index * hop_length / sr
  best_time = min_index * hop_length / sr
  
  return worst_time, best_time, time_length


similarity = calc_similarity(music_1=f0_interpolated, music_2=f0_2_interpolated) # pyin defalut hop_length : 512
worst_time, best_time, time_length = find_segment(music_1=f0_interpolated, music_2=f0_2_interpolated, sr = sr1, hop_length= 512, time_length=5) # pyin defalut hop_length : 512


# json_object = {
#       "createTime":current_time,
#       "similarity":round(similarity, 2),
#       "worst_time":worst_time,
#       "best_time":best_time,
#       "time_length":time_length
# }




# # current_time -> pyplot이미지와 동일한 시간 변수 사용
# file_name = f'sim_result_{current_time}.json'
# file_path = f'./{file_name}'

# # 로컬 json 파일 생성
# with open(file_path, 'w') as json_file:
#     json.dump(json_object, json_file, indent=4) # indent 4 는 가독성을 위함.


# 이미지 파일 S3에 업로드
image_file_path = f'sim_wave_{current_time}.png'
s3_image_url = upload_to_s3(image_file_path, 'my-version-result-list', f"results/{image_file_path}")\

print("createTime:",current_time)
print("similarity:",round(similarity, 2))
print("worst_time:",worst_time)
print("best_time:",best_time)
print("time_length:",time_length)
print(f"{s3_image_url}")



# S3에서 다운로드한 로컬 파일 삭제
if 'file1' in locals() and os.path.exists(file1) and file1.startswith("/tmp/"):
    os.remove(file1)
    print(f"Deleted temporary file: {file1}")

if 'file2' in locals() and os.path.exists(file2) and file2.startswith("/tmp/"):
    os.remove(file2)
    print(f"Deleted temporary file: {file2}")

if f'sim_wave_{current_time}.png':
    os.remove(f'sim_wave_{current_time}.png')
