import pandas as pd 
file_path = 'read_csv_sample.csv'
df1 = pd.read_csv(file_path) 
print(df1)
df2 = pd.read_csv(file_path, header=None) 
print(df2)
df3 = pd.read_csv(file_path, index_col=None) 
print(df3)
df4 = pd.read_csv(file_path, index_col='c1')
print(df4)

import pandas as pd
df2 = pd.read_csv('mpg.csv', header=0)
print(df2)


import csv
f = open("data.csv", "r")
reader = csv.reader(f)
for row in reader:
    print(row)



import pandas as pd
data = {'name' : [ 'Jerry', 'Riah', 'Paul'],
'algol' : [ "A", "A+", "B"],
'basic' : [ "C", "B", "B+"],
'c++' : [ "B+", "C", "C+"]}
df = pd.DataFrame(data)
df.set_index('name', inplace=True) 
print(df)
df.to_csv("df_sample.csv")


import pandas as pd
data = {'name': ['Minsu', 'Juhee', 'Sujin'],
        'age': ["20", "25", "28"],
        'height': ["180", "150", "170"],
        'weight': ["80", "45", "55"]}
df2 = pd.DataFrame(data)
df2.set_index('name', inplace=True)
print(df2)
df2.to_csv("df_sample2.csv")




import csv
with open('test.csv', 'w', encoding='utf-8', newline='') as writer_csv:
    writer = csv.writer(writer_csv, delimiter=',')
    writer.writerow(['dave', 'david'])
    writer.writerow(['apple', 2])
    writer.writerow(['korea', 'japan', 'china'])
    
    
with open('test.csv', 'r', encoding='utf-8') as reader_csv:
    reader = csv.reader(reader_csv, delimiter=',')
    
    for row in reader:
        print(row)



import pandas as pd 
file_path1 = 'read_tsv_sample1.tsv'
file_path2 = 'read_tsv_sample2.tsv'
df1 = pd.read_csv(file_path1, sep = '\t')  #열려는 파일이 tsv 파일인 경우
print(df1)
df2 = pd.read_csv(file_path2, sep = ' ') # 공백을 기준으로 내용이 구분된 txt파일 인 경우
print(df2)



data = {'Name' : ['John Doe' , 'Jane Smith'] ,
         'Age' : [25, 30] ,
         'Country' : ['USA' , 'Canada']}
df = pd.DataFrame(data)
df.to_csv('output.tsv',sep='\t',index=False)



import pandas as pd
df1 = pd.read_excel('남북한발전전력량.xlsx')
df2 = pd.read_excel('남북한발전전력량.xlsx', header=None)
print(df1)
print(df2)



import pandas as pd

data = {'name' : [ 'Jerry', 'Riah', 'Paul'],
        'algol' : [ "A", "A+", "B"],
        'basic' : [ "C", "B", "B+"],
        'c++' : [ "B+", "C", "C+"],
        }

df = pd.DataFrame(data)
df.set_index('name', inplace=True)
print(df)

df.to_excel("df_sample.xlsx")



import pandas as pd

data1 = {'name' : [ 'Jerry', 'Riah', 'Paul'], 'algol' : [ "A", "A+", "B"], 
          'basic' : [ "C", "B", "B+"], 'c++' : [ "B+", "C", "C+"]}
data2 = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}

df1 = pd.DataFrame(data1)
df1.set_index('name', inplace=True) 

df2 = pd.DataFrame(data2)
df2.set_index('c0', inplace=True)

writer = pd.ExcelWriter("df_excelwriter.xlsx")
df1.to_excel(writer, sheet_name="sheet1")
df2.to_excel(writer, sheet_name="sheet2")
writer.close()





import pandas as pd

url ='sample.html'
tables = pd.read_html(url)
print(len(tables))

for i in range(len(tables)):
    print("tables[%s]" % i)
    print(tables[i])
    print('\n')

df = tables[1] 

df.set_index(['name'], inplace=True)
print(df)



import pandas as pd
df1 = pd.read_json('test.json')
print(df1)



import json

with open('test.json', 'r') as f:
    json_data = json.load(f)
print(json.dumps(json_data))



k5_price = json_data['K5']['price']
print(k5_price)


json_data['K5']['price'] = "7000"
print(json_data['K5']['price'])




import json

car_group = dict()

k5 = dict()
k5["price"] = "5000"
k5["year"] = "2015"
car_group["K5"] = k5

avante = dict()
avante["price"] = "3000"
avante["year"] = "2014"
car_group["Avante"] = avante
print(car_group)

with open('test.json', 'w', encoding='utf-8') as make_file:
    json.dump(car_group, make_file, indent="\t")
    
with open('test.json', 'r') as f:
    json_data = json.load(f)
print(json.dumps(json_data, indent="\t") )



import json
fruit_group = dict()

apple = dict()
apple['price'] = '2000'
apple['weight'] = '50'
fruit_group['apple'] = apple

banana = dict()
banana['price'] = '4000'
banana['weight'] = '70'
fruit_group['banana'] = banana

with open('test.json', 'w', encoding='utf-8') as make_file:
    json.dump(fruit_group, make_file, indent='\t')
    
with open('test.json', 'r') as f:
    json_data = json.load(f)
print(json.dumps(json_data, indent="\t") )




import xml.etree.ElementTree as ET
xml_path = "library.xml"
with open(xml_path) as f:
    tree = ET.parse(f)
    root = tree.getroor()




import xml.etree.ElementTree as ET
xml_save_path = "library.xml"
with open(xml_save_path, "wb") as file:
    tree.write(file, encoding='utf-8', xml_declaration=True)
    




tag = 'book'
for child in root.iter(tag):
    child.attrib['price'] = str(10 * float(child.attrib['price']))
    print(child, child.attrib['price'], "-->", str(10*float(child.attrib['price'])))
    
    
    
    
