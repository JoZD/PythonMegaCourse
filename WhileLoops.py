

#While loops 




active = True


tasks = []

while active: 
    tasks.append(input("Enter task: "))
    if input("Do you want to add another task? (y/n): ") == "y":
        continue
    else: 
        active = False


for i in tasks: 
    print(i.title())