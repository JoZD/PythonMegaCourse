
#This is a match case with python

todos = []


while True:
    todo = input("Please enter 'add' to enter a task, or enter 'show' to show all your taks")
    match todo:
        case "add":
            todos.append(todo)
        case "show":
            for i in todo: 
                print(i.title())
            break
