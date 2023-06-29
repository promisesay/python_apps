def spliter(feet_inches):
    numbers = feet_inches.split(' ')
    feet = float(numbers[0])
    inches = float(numbers[1])
    call = {'feet': feet, 'inches': inches}
    return call
