from tkinter import *
from tkinter.font import Font
from tkinter import filedialog
import pickle

#Define Our font

root=Tk()
root.title("To Do List")
root.geometry("500x500")


my_font=Font(family="Brush Script MT", size=30, weight="bold")




my_frame=Frame(root)
my_frame.pack(pady=10)

my_list=Listbox(my_frame,font=my_font,width=25,height=5,bg="SystemButtonFace",bd=0,fg="#464646",highlightthickness=0,selectbackground="#a6a6a6",activestyle="none")


my_list.pack(side=LEFT,fill=BOTH)

stuff=["walk the dog","take a nap"]
for item in stuff:
    my_list.insert(END,item)


# Add Scrollbar
my_scrollbar=Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT,fill=BOTH)

my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)



my_entry=Entry(root,font=("Brush Script MT",24))
my_entry.pack(pady=20)

#FUNCTIONS
def delete_item():
    my_list.delete(ANCHOR)
def add_item():
    my_list.insert(END,my_entry.get())
    my_entry.delete(0,END)
def cross_off_item():
    my_list.itemconfig(my_list.curselection(),fg="#dedede")
    my_list.selection_clear(0,END)
def uncross_item():
    my_list.itemconfig(my_list.curselection(),fg="#464646")
    my_list.selection_clear(0,END)
def delete_crossed_item():
    count=0
    while count < my_list.size():
        if my_list.itemcget(count,"fg")=="#dedede":
            my_list.delete(my_list.index(count))
        else:
         count +=1
def save_list():
    file_name=filedialog.asksaveasfilename(
        initialdir="C:/data",
        title="Save File",
        filetypes=(("Dat Files","*.dat"),("All Files","."))

    )
    if file_name:
        if file_name.endswith(".dat"):
            pass
        else:
            file_name=f'{file_name}.dat'
    #Delete crossed off items before saving    
        count=0
    while count < my_list.size():
        if my_list.itemcget(count,"fg")=="#dedede":
            my_list.delete(my_list.index(count))
        else:
         count +=1

    
    
    
    #Grabb all the stuff from the list
    stuff=my_list.get(0,END)
    #Open the file
    output_file=open(file_name,'wb')
    #Actually add the stuf to the file
    pickle.dump(stuff,output_file)

    
def open_list():
    file_name=filedialog.askopenfilename(file_name=filedialog.asksaveasfilename(
        initialdir="C:/data.",
        title="Open File",
        filetypes=(("Dat Files","*.dat"),("All Files",".")))
    )
    if file_name:
        #Delete currently open list
        my_list.delete(0,END)

        #Open the file
        input_file=open(file_name,'rb')

        #Load the data from the file
        stuff=pickle.load(input_file)

        #Output stuff to the screen
        for item in stuff:
            my_list.insert(END,item)











def delete_list():
    my_list.delete(0,END)







#Create Menu
my_menu=Menu(root)
root.config(menu=my_menu)

#Add items to the menu
file_menu=Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="File",menu=file_menu)
#Add drowdown items
file_menu.add_command(label="Save List",command=save_list)
file_menu.add_command(label="Open List",command=open_list)
file_menu.add_command(label="Clear List",command=delete_list)
file_menu.add_separator()









button_frame=Frame(root)
button_frame.pack(pady=20)




delete_button=Button(button_frame, text="Delete Item",command=delete_item)
add_button=Button(button_frame,text="Add Item",command=add_item)
cross_offbutton=Button(button_frame,text="Cross of Item",command=cross_off_item)
uncross_button=Button(button_frame,text="Uncross Item",command=uncross_item)
delete_crossed_button=Button(button_frame,text="Delete Crossed Item",command=delete_crossed_item)
save_button=Button(button_frame,text="Save",command="save_item")




delete_button.grid(row=0, column=0,padx=5)
add_button.grid(row=0, column=1,padx=5)
cross_offbutton.grid(row=0,column=2,padx=10)
uncross_button.grid(row=0,column=3,padx=5)
delete_crossed_button.grid(row=1, column=0,pady=10,padx=5)
save_button.grid(row=2,column=5,padx=5)


























root.mainloop()