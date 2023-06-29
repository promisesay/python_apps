pack = {'tool': False}
print(pack.values())
while all(pack.values()) is False:
    password = input('enter:')
    tool = False
    if len(password) > 7:
        tool = True

    pack['tool'] = tool

    onn = False
    for i in password:
        if i.isdigit():
            onn = True
    pack['length'] = onn
    up = False
    for i in password:
        if i.isupper():
            up = True
    pack['upper case'] = up

    print(pack)
    package = all(pack.values())
    print(package)
    if package:
        print('password is good')
    else:
        print('stronger password needed')
