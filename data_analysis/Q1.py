class_num={'SAM': '2',
            'TOM': '1',
            'JAMY': '3'}

#json파일 저장
import json
with open('A1.json', 'w') as f:
    json.dump(class_num, f)

#json파일 불러오기
import json
with open('A1.json') as f:
    data = json.load(f)

type(data)

print(data)