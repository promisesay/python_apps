def password(password):
    while True:
        password = input('enter :')
        if len(password) == 8:
            print('the password is not very strong')
        elif len(password) > 8:
            print('the password is strong')
            break
        elif len(password) < 8:
            print('the password is weak')
while True:
    passcheck = input('please enter again:')
    if passcheck == password:
        print('corect .')
        break
    elif passcheck != password:
        print('the password is not match')
        password(password())
