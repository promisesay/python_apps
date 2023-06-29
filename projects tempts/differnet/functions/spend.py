def get_data():
    with open('spend_data.txt', 'r') as file_local:
        data0 = file_local.readlines()
    return data0


def isfloat(expence):
    try:
        if float(expence):
            return True
    except ValueError:
        return False


def get_expenses():
    with open('spend_data.txt', 'r') as file_num:
        num = file_num.readlines()
    z = 0
    for i in num:
        local_number = i.split("=")
        for a in local_number:
            a = a.strip()
            if isfloat(a):
                x = float(a)
                print(a)
                z = z + x

    return z


data = []
while True:
    command = input('enter a command:')
    command = command.strip()
    print(data)
    if command.startswith('add'):
        try:
            data = get_data()
            item_name = input('enter the purchase item:')
            new_spend = float(input('enter  the price:'))
            item = f'{item_name} = {new_spend}'
            data.append(item + '\n')
            print(get_data())
            with open('spend_data.txt', 'w') as file:
                file.writelines(data)
        except ValueError:
            print('wrong')
            continue
    elif command.startswith('show'):
        try:
            data = get_data()

            for number, i in enumerate(data):
                i = i.strip('\n')
                print(f'{number + 1}_{i}')
        except ValueError:
            print('wrong')
            continue
    elif command.startswith('edit'):
        if command.endswith('edit') :
            r_c = input('remove or change?')
            data = get_data()
            try:
                if r_c.startswith('remove'):
                    remove = int(input('enter the index:'))
                    data.pop(remove)
                    with open('spend_data.txt', 'w') as file:
                        file.writelines(data)
                elif r_c.startswith('change'):
                    change = int(input('enter the index:'))
                    change_the = input('enter the new item:')
                    data[change] = change_the
                    with open('spend_data.txt', 'w') as file:
                        file.writelines(data)
                else:
                    print('what?!!')
                    continue
            except ValueError:
                print('you enter the wrong input:')
                continue
        elif command[5:].isdigit():
            data = get_data()
            parden = input('remove or change?')
            remove = int(command[5:])
            print(remove)
            parden = parden.strip()

            if parden.startswith('remove'):
                data.pop(remove)
            if parden.startswith('change'):
                change = input('enter new item:')
                data[remove] = change
            with open('spend_data.txt', 'w') as file:
                file.writelines(data)
    elif command.startswith('exit'):
        break
    elif command.startswith('total'):
        total = get_expenses()
    else:
        print('wrong command')
print('ok')
