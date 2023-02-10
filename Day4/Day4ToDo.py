

#Day 4, adding a feature to edit an existing toDO

todos = []
x = 1 #This variable is used in case of edit 
while True:
    user_action = input("Please enter 'add' to enter a task, or enter 'show' to show all your taks or 'edit' to edit an existing task: \n")
    user_action = user_action.strip()
    match user_action:
        case "add":
            todo = input("Enter a to DO something: \n")
            todos.append(todo)
        case "show":
            for i in todos: 
                print( f" {str(x)}- {i}")
                x += 1
        case "edit":
            
            for i in todos:
                print( f" {str(x)}- {i}")
                x += 1
            variable = input("Please enter the number of the task, you want to edit: ")
            newTodo = input("Please enter a new value for the task: \n")
            ans = input(f"Are you sure you want to overwrite the task : {todos[int(variable) -1]} for the task? {newTodo}  y/n?: \n")
            match ans:
                case "y":
                    todos[int(variable)-1] = newTodo
                case "n":
                    print("Ok! Changes won't be saved! :D")

        case "exit":
            break

print("See ya later! :D ")
