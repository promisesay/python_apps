while True:
    try:
        weight = int(input('enter weight:'))
        height = int(input('enter height:'))
        area = height * weight
    except ValueError:
        print('enter a number')
        continue
    print(area)
