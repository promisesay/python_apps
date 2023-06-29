import json
with open('quiz1.JSON') as file:
    data = file.read()

question = json.loads(data)
print(type(question))
print(question)

anss = []
emt = 0
for i in question:
    print(i['question'])
    anus = i['ansewers']
    for index, q in enumerate(anus):
        print(index + 1, "_", q)
    ans = int(input('enter the answer:')) - 1
    if ans != i['ansewr']:
        anw = f'fuck the {anus[ans]}'
        anss.append(anw)
    elif ans == i['ansewr']:
        anw = f'yeah it all fucking {anus[ans]}'
        anss.append(anw)
        emt = emt + 1

for i in anss :
    print(i)
print(f"{emt} is your correct answers")
