password = input('enter a new password:')
result = {}
lenght = False
if len(password) >= 8:
    lenght = True
result['lenght'] = lenght

digit = False
for i in password:
    if i.isdigit():
        digit = True
result['digit'] = digit

upper = False
for i in password:
    if i.isdigit():
        upper = True
result['upper'] = upper

print(all(result))
if all(result.values()):
    print('the password is strong')
else:
    print('the password is weak')
