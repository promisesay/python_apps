PASS = input("enter new password:")
result = {}
leng = False
if len(PASS) >= 8:
    leng = True
result['leng'] = leng

kow = False
for i in PASS:
    if i.isdigit():
        kow = True
result['kow'] = kow

Upper = False
for i in PASS:
    if i.isupper():
        Upper = True
result['Upper'] = Upper
print(result)
print(all(result.values()))
if False == all(result.values()):
    print('the password is weak')
else:
    print('the password is strong')