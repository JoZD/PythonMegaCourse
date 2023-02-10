

#Today I need to add a feature to complete a to Do, and delete it from the list

#Day 4, adding a feature to edit an existing toDO

todos = []
x = 1 #This variable is used in case of edit 

while True:


    #Prompt the user for action 
    user_action = input("Please enter 'add' to enter a task, or enter 'show' to show all your taks, 'edit' to edit an existing task or complete, to complete an existing task: \n")
    user_action = user_action.strip()

    #Match user action

    match user_action:
        case "add":
            todo = input("Enter a to DO something: \n")
            todos.append(todo)


        case "show":
            x = 1
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

            #Prompt the user for a confirmation
            match ans:
                case "y":
                    todos[int(variable)-1] = newTodo
                case "n":
                    print("Ok! Changes won't be saved! :D")

        case "complete":

            # Imma use the same code I use for case edit, just little changes 
            for i in todos:
                print( f" {str(x)}- {i}")
                x += 1
            variable = input("Please enter the number of the task, you want to complete: ")

            ans = input(f"Are you sure you want to finish the task : {todos[int(variable) -1]}? \n")

            match ans:
                case "y":
                    a = int(variable)-1
                    print(a)
                    todos.pop(a)
                    print("Ok! The task has been completed! ")
                case "n":
                    print("Ok! Changes won't be saved! :D")


        case "exit":
            break

print("See ya later! :D ")
