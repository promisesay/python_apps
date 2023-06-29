from newGoal import check_goal

while True:

    command = input('do you have a new goal? (yes/no)')
    if command.startswith('no'):
        goals = get_goals()
        goal = input('enter the goal ')
    elif command.startswith('yes'):
        newtarget = input('enter the new goal:')
        newtarget = newtarget.title()
        check_goal(newtarget)

