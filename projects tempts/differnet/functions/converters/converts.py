from main import converter
from feet_to_cantimeter import cm


def spliter(feet_inches):
    numbers = feet_inches.split(' ')
    feet = float(numbers[0])
    inches = float(numbers[1])
    call = {'feet': feet, 'inches': inches}
    return call


ask = input('e')
both = spliter(ask)
command = input('cm or m:')
match command:
    case 'm':
        print(converter(both["feet"], both['inches']))
    case 'cm':
        print(cm(both['feet'], both['inches']))





