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
