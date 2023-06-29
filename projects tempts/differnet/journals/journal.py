date = input('enter tha todays')
rate = input(f'rate this day from 1 to 10:') + '\n'
explain = input(f'what are your thought about this day?\n')
with open(f'../journals/{date}.txt', 'w') as file:
    file.write(rate + 2 * '\n')
    file.write(explain + '\n')