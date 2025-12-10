print('---to do list---')
task = []
while True:
    print('1. Add task')
    print('2. View tasks')
    print('3. Mark as Completed')
    print('4. Quit')

    choice = int(input('Enter your choice: '))

    if 0 < choice < 5:
        if choice == 1:
            task.append(input('Enter your task: '))
            print('Task added!')
        elif choice == 2:
            i = 1
            for t in task:
                print((str(i) + '. ' + t))
                i = i + 1
        elif choice == 3:
            t = int(input('which number task you want to mark to delete?'))
            task.pop(t-1)
            print('Task removed!')
        else:
            print("tata bye bye")
            break

    else:
        print('Invalid choice')