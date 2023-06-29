def convert_to_m(entered_numbers):
    number = entered_numbers.split(" ")
    inches = float(number[1])
    feet = float(number[0])
    meter = float(feet * 0.3648 + inches * 0.0254)
    return meter


def convert_to_cm(var):
    give_numbers = var.split(" ")
    feet = float(give_numbers[0])
    inches = float(give_numbers[1])
    centimeter_converter = feet * 30.48 + inches * 2.54
    return centimeter_converter


def get_data(filepath='converts.txt'):
    with open(filepath) as file_locally:
        data = file_locally.readlines()
    return data


def write_data(given_data, filepath='converts.txt'):
    with open(filepath, 'w') as file_locally:
        file_locally.writelines(given_data)


while True:
    todos = get_data()
    try:

        command = input('convert to cm or meter?')
        if not command.startswith('exit'):
            numbers = input('enter the numbers:')
        if command.startswith('c'):
            centimeter = convert_to_cm(numbers)
            print(centimeter)
            results = f'{numbers} inches = {centimeter} centimeters'
            todos.append(results + '\n')
        elif command.startswith('m'):
            meters = convert_to_m(numbers)
            whole = meters.split(' ')
            results = f'{whole[0]}feet and {whole[1]} inches = {meters} meters'
            print(results)
            todos.append(results + '\n')
        elif command.startswith('exit'):
            break
        else:
            print('enter a number like"34 11"')
    except TypeError:
        print('try somthing like "x = feet, y = inches"')
        continue
    except IndexError:
        print('please type the zero for the none value!!')
        continue
    except ValueError:
        print('please enter a number like "x y"')
        continue
    new_data = [i.strip('\n') for index, i in enumerate(todos)]
    write_data(new_data)

