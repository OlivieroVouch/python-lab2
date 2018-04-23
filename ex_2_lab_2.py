from sys import argv
script, first = argv
print("The file is called",script)
print("The parameter is",first)
txt = open(first,"r")
task = []
task = txt.readlines()  # read task_list and put it in a string 'task'
txt.close()  # close FILE
task = [line.rstrip('\n') for line in task] # read the string and clean it from newlines
index=0
boolean=0


while index!=4 :

    print("MENU:")
    print("1: Insert a new task")
    print("2: Remove a task")
    print("3: Show all the tasks")
    print("4: Close the program")
    print(" CHOOSE AN ACTION")
    index = int(input())

    if index==1:
        task.append(input())
    elif index==2:
     boolean = False
     print("Insert task to be removed")
     tmp = input()
     for tasks in task:
         if tasks==tmp:
             boolean = True
             print("Removing task",tmp)
             task.remove(tasks)

     if boolean==0:
         print("Task not found")
    elif index==3:
        for tasks in task:
            print(tasks)
    elif index==4:
        break
    else:
        print("Invalid choice ==> REPEAT")

txt = open(first,'w')
for tasks in task:
    txt.write(tasks)
    txt.write("\n")
txt.close()