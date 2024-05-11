import tkinter
import tkinter.messagebox
import pickle
root=tkinter.Tk()
root.title("ToDoList")
def add_task():
    task=En_try.get()
    if task!="":
        list_box.insert(tkinter.END,task)
        En_try.delete(0,tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!",message="You must enter a task.")
def del_task():
    try:
        task_del=list_box.curselection()[0]
        list_box.delete(task_del)
    except:
         tkinter.messagebox.showwarning(title="Warning!",message="You must select a task.")
def display_task():
    try:
        tasks=pickle.load(open("save.list","rb"))
        list_box.delete(0,tkinter.END)
        for task in tasks:
            list_box.insert(tkinter.END,task)
    except:
        tkinter.messagebox.showwarning(title="Warning!",message="File not found")    
def save_task():
    tasks=list_box.get(0,list_box.size())
    pickle.dump(tasks,open("save.list","wb"))
list_box=tkinter.Listbox(root,height=20,width=50)
list_box.pack()
scroll_bar=tkinter.Scrollbar(root)
scroll_bar.pack(side=tkinter.RIGHT,fill=tkinter.Y)
En_try=tkinter.Entry(root,width=50,)
En_try.pack()
add_button=tkinter.Button(root,text="Add Task",width=30,bg="grey",command=add_task)
add_button.pack()
del_button=tkinter.Button(root,text="Delete Task",width=30,bg="grey",command=del_task)
del_button.pack()
display_button=tkinter.Button(root,text="Display Task",width=30,bg="grey",command=display_task)
display_button.pack()
save_button=tkinter.Button(root,text="Save Task",width=30,bg="grey",command=save_task)
save_button.pack()







root.mainloop()
