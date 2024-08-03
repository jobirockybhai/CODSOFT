from tkinter import *

mfrm = Tk()
mfrm.title("TO DO LIST")kkkkkkkkkkk
mfrm.geometry('450x600')
mfrm.resizable(False, False)



task_list = []

def addTask():
    task = task_entry.get()
    task_entry.delete(0,END)

    if task:
        with open('tasklist.txt','a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END, task)


def deleteTask():
    global task_list
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open('tasklist.txt','w') as taskfile:
            for task in task_list:
                taskfile.write(task+'\n')

        listbox.delete( ANCHOR )


def openTaskFile():
    try:
        global task_list
        with open('tasklist.txt','r') as taskfile:
            tasks = taskfile.readlines()

        for task in tasks:
            if task != '\n':
                task_list.append(task)
                listbox.insert(END, task)
    except:
        file=open('tasklist.txt','w')
        file.close()


image = PhotoImage(file='printable-daily-do-list-template_02.png')
mfrm.iconphoto(False, image)

main_image = PhotoImage(file = 'printable-daily-do-list-template_01.png')
smaller_image = main_image.subsample(3, 3)
Label(mfrm,image = smaller_image).pack()




frame = Frame(mfrm,width=400, height=45, bg='white')
frame.place(x=30,y=100)

task = StringVar()
task_entry = Entry(frame, width=26, font='arial 20', bd=0)
task_entry.place(x=1,y=3)
task_entry.focus()

b1 = Button(frame, text = "ADD", font = 'times 20 bold', width = 6, bg='#5a95ff', fg='white', bd=3, command= addTask)
b1.place(x=300,y=0)

frame1 = Frame(mfrm, bd=3, width = 300, bg='')
frame1.pack(pady=(100,10))

listbox = Listbox(frame1, font='arial 12', width = 40, height = 16, bg='#32405b', fg='white', cursor = 'hand2', selectbackground='#5a95ff')
listbox.pack(side=LEFT, fill=BOTH, padx=2, pady=10)
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)


openTaskFile()

b2 = Button(mfrm,text = "DELETE", font = 'times 20 bold', width = 6, bg='white', fg='red', bd=2, command = deleteTask)
b2.pack(side=BOTTOM, pady=20)





mfrm.mainloop()
