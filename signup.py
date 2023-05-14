from tkinter import *
from tkinter import messagebox
import ast


window = Tk()
window.title("Sign-Up")
window.geometry('1920x1080')
window.configure(bg='#fff')
window.resizable(True, True)


def signup():

		username = user.get()
		password = user1.get()
		confirm_password = user2.get()

		if password == confirm_password:

				try:

					file = open('datasheet.txt', 'r+')
					d = file.read()
					r = ast.literal_eval(d)

					dict2 = {username: password}
					r.update(dict2)
					file.truncate(0)
					file.close()
					file = open('datasheet.txt', 'w')
					w = file.write(str(r))

					messagebox.showinfo("SignUp","Successfully Signed Up")
				except:
						file = open('datasheet.txt', W)
						pp = str({'Username':'password'})
						file.write(pp)
						file.close()
		else:
			messagebox.showerror('Make Sure, Both passwords are identical!')
	

def sign():
       window.destroy()
       
    

# img = PhotoImage(file='airplane.png')
Label(window,border=0,bg='white').place(x=50,y=90)

frame = Frame(window,width=550,height=750,bg='#fff')
frame.place(x=880,y=50)

heading = Label(frame,text='Sign Up',fg="#57a1f8",bg='white',font=('Microsoft Yahei UI Light',23,'bold'))
heading.place(x=200,y=100)


#-------------------------------Email

def on_enter(e):
    user.delete(0,'end')
    

    
def on_leave(e):
    if user.get()=='':
        user.insert(0,'Username')
    

    


user = Entry(frame,width=300,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
user.place(x=135,y=200)
user.insert(0,'Username')
user.bind("<FocusIn>",on_enter)
user.bind("<FocusOut>",on_leave)


Frame(frame,width=295,height=2,bg='black').place(x=135,y=230)

#---------------------------------Password


def on_enter(e):
    user1.delete(0,'end')
    

    
def on_leave(e):
    if user1.get()=='':
        user1.insert(0,'Password')

user1 = Entry(frame,width=300,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
user1.place(x=135,y=280)
user1.insert(0,'Password')
user1.bind("<FocusIn>",on_enter)
user1.bind("<FocusOut>",on_leave)


Frame(frame,width=295,height=2,bg='black').place(x=135,y=310)

#-----------------------Confirm Password

def on_enter(e):
    user2.delete(0,'end')
    

    
def on_leave(e):
    if user2.get()=='':
        user2.insert(0,'Confirm Password')

user2 = Entry(frame,width=300,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
user2.place(x=135,y=360)
user2.insert(0,'Confirm Password')
user2.bind("<FocusIn>",on_enter)
user2.bind("<FocusOut>",on_leave)


Frame(frame,width=295,height=2,bg='black').place(x=135,y=390)

#-----------------------------------------------------------------------

Button(frame,width=39,pady=7,text='Sign Up',bg='#57a1f8',fg='white',border=0,command=signup).place(x=142,y=450)
label = Label(frame,text='I already have an account !',fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=220,y=500)

signin = Button(frame,width=6,text='Sign in',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=sign)
signin.place(x=370,y=500)

window.mainloop()