list_of_works=[]
while True:      #the problem with uppercase 't' in true
    esme=input("what do you want to do?")
    esme=esme.strip()
    match esme:
        case "show":
            for index , i in enumerate(list_of_works):
                index= index +1
                print(f"{index}_{i}")
        case "back":
            break
        case  "add":
            add = input("what do you want to add to the list?") + "\n"
            file = open('list_of_works.txt', 'r')
            list_of_works = file.readlines()#readline for str and readlines for list and array
            file.close() #it just a close with the file{()} subtance nothing in it
            list_of_works.append(add)
            file = open('list_of_works.txt', 'w')
            file.writelines(list_of_works)
            file.close()
        case "edit":
            todo=int(input("witch one?"))
            list_of_works[todo]=input('enter a new work:')
        case "done":
            remove=int(input("enter the todo"))
            list_of_works.pop(remove)
        case o:
            print("try this command:edit/add/back/show/done")
print("good luck")

