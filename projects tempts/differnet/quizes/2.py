import json

with open('quiz2.json') as file:
    data = file.read()

mind = json.loads(data)
emt = 0
answers = []
for question in mind:
    print(question['question_text'])
    for index, alt in enumerate(question['alternative']):
        print(f'{index+1}_{alt}')
    try:
        answer = int(input('enter the number of alternative'))
    except ValueError:
        print('enter the number of alternative')
        continue
    try:
        if answer == question['answer']:
            anuss = f'{question["alternative"[answer]]} is correct'
            emt = emt + 1
            answers.append(anuss)
        else:
            anuss = f'{question["alternative"[answer]]} is not correct'
            answers.append(anuss)
    except ValueError:
        print('try again')
        continue

for i in answers:
    print(i)
print(emt)
