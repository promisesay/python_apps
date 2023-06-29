from feet_to_cantimeter import cm
from feet_to_metters import mitter


def paras(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    call = {"feet": feet, "inches": inches}
    return call




while True:
    number = input('enter the major:')
    number = paras(number)
    ent = input('convert to mitter or centimetre')
    try:
        if ent.startswith('m'):
            anous = input(f'do major is  {number["feet"]} feet and {number["inches"]} inches')
            metter = mitter(number["feet"], number['inches'])
            print(metter)
        elif ent.startswith('c'):
            pardon = cm(number['feet'], number['inches'])
            print(pardon)
    except ValueError:
        print('enter a number("feet inches")')
        continue
    resume = input('do you want to continue?')
    match resume:
        case 'yes':
            continue
        case 'no':
            break

print('goodbye')
