

user_prompt = "Enter a task you want to remember! :D \n"

todo1 = input(user_prompt)
todo2 = input(user_prompt)
todo3 = input(user_prompt)


tasks = [todo1, todo2, todo3]

for i in tasks: 
    print(i.title())