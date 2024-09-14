'''import json


json_file = json.dumps(oecd_cnty)
'''
import json
# 딕셔너리 만듬
oecd_cnty={'AUS':'오스트레일리아',
           'KOR':'대한민국',
           'USA':'미국'
           }
# 딕셔너리 -> JSON 객체
json_object = json.dumps(oecd_cnty)

#JSON객체 -> JSON파일로 저장
with open('ex1.json', 'w', encoding='utf-8') as f:
    json.dump(json_object, f, indent="\t")
#JSON파일 읽어서 JSON 객체로 저장
with open('ex1.json', 'r') as f:
    json_object = json.load(f)
#JSON객체를 String으로 변환
print(json.loads(json_object))

