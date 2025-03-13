import json

with open('pi.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

r=[]
for i in range(len(data)):
    d = int(data[i]['数字'])
    if d==230 or d==231 or d==431 or d==631 or d==931 or d==1131:
        r.append(data[i])
for t in r:
    data.remove(t)


for i in range(len(data)):
    for j in range(i+1,len(data)):
        if data[i]['位数']>data[j]['位数']:
            data[i] , data[j] = data[j] , data[i]

z = []
for i in range(len(data)):
    z.append({'数字':data[i]['数字'],'位数':data[i]['位数'],'百分比':int((1-i/(len(data)-1))*100000)/1000})


with open('pi.json', 'w', encoding='utf-8') as file:
    json.dump(z, file, ensure_ascii=False, indent=2)
