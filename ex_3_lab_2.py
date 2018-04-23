from sys import argv
script, first = argv
print("The file is called",script)
print("The parameter is",first)
txt = open(first,"r") #opens file with name of "test.txt"
task = []
for line in txt:
    task.append(line)
print(task)
index=0
boolean=False
tasks,word=''

def sub_string_remove(word):
    delete=0
    count=0
    boolean=False
    for tasks in task:
        word = tasks.split('')
        if word.




    if(delete==0): print("The indicated substring hasn't been found in any Task")

    else: print("Removed" + str(delete) + "Tasks")



while index!=5 :

    print("MENU:")
    print("1: Insert a new task")
    print("2: Remove a task")
    print("3: Show all the tasks")
    print("4: Remove All Task containing a specified substring")
    print("5: Close the program")
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
        tmp = input()
        if len(tmp)==0:
            print("Invalid substring")
        else:
            sub_string_remove(str(tmp))


    elif index==5:
        break
    else:
        print("Invalid choice ==> REPEAT")

txt = open(first,'w')
for tasks in task:
    txt.write(tasks)
    txt.write("\n")
txt.close()