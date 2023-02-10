
#This is a match case with python

todos = []


while True:
    user_action = input("Please enter 'add' to enter a task, or enter 'show' to show all your taks")
    user_action = user_action.strip()
    match user_action:
        case "add":
            todo = input("Enter a to DO something: \n")
            todos.append(todo)
        case "show":
            for i in user_action: 
                print(i.title())
        case "exit":
            break

print("See ya later! :D ")
