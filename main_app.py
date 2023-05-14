from tkinter import messagebox
import ast
import simpy
import random
import time
import matplotlib.pyplot as plt
from tkinter import *
from PIL import ImageTk, Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


window = Tk()
window.title("Sign-In")
window.geometry('1920x1080')
window.configure(bg='#fff')
window.resizable(True, True)
background_image = PhotoImage(file="a1.png")
background_label = Label(window, image=background_image)
background_label.place(relwidth=1, relheight=1)

def signin():

    username = user.get()
    password = user1.get()
            
    file = open('datasheet.txt','r') 
    d=file.read()
    r=ast.literal_eval(d)
    file.close()

    
       
    if username in r.keys() and password ==r[username]:
                root = Tk()
                root.title("New Delhi Airport Management System")
                root.geometry("1920x1080")

                # Create a frame to hold the widgets
                frame1 = Frame(root, bg="#B9E0FF", width=500, height=500)
                frame2 = Frame(root, bg="#F0F0F0", width=500, height=500)

                # pack the frames into the main window
                frame1.pack(side=LEFT, fill=BOTH, expand=True, padx=20, pady=20)
                frame2.pack(side=RIGHT, fill=BOTH, expand=True, padx=20, pady=20)

                airport_label2 =Label(frame2, text="Passenger Traffic", font=(
                    "Arial", 20, "bold"), fg="#333333", bg="#F0F0F0")
                airport_label2.pack(pady=30)

                # Create labels and entries for airport information
                airport_label = Label(frame1, text="Passenger Status", font=(
                    "Arial", 20, "bold"), fg="#333333", bg="#B9E0FF")
                airport_label.pack(pady=30)


                def sample(out):

                    global flight_listbox
                    flight_listbox = Listbox(frame1, height=100, width=100, bg="light gray")
                    flight_listbox.pack(padx=1, pady=5)
                    # scrollbar.config(command=flight_listbox.yview)

                    # Add some example flights to the listbox
                    for i in range(len(out)):
                        if i % 2 == 0:
                            flight_listbox.insert(i, out[i])
                            flight_listbox.itemconfig(i, bg='#333333', fg="white")
                        else:
                            flight_listbox.insert(i, out[i])
                            flight_listbox.itemconfig(i, bg='#728bd4', fg="white")

                    submit.destroy()


                domestic_routes = ["Mumbai", "Bangalore", "Kolkata",
                                "Chennai",  "Ahemadabad", "Hyderabad", "Pune"]
                # d_route_s = ["MUM","BAG","KOL","CHE","AHM","HYD","PUN"]
                international_routes = ["New Jersey", "Otawa",
                                        "Torronto", "Switzerland", "Qatar", "Frankfurt"]
                

                def run2():
                    window.destroy()
                    root.destroy()
                    root1 = Tk()

                    root1.title("Airport Management System - Airplane Traffic")
                    root1.geometry("1920x1080")

                    # Create a frame to hold the widgets
                    frame1 = Frame(root1, bg="#B9E0FF", width=500, height=500)
                    frame2 = Frame(root1, bg="#F0F0F0", width=500, height=500)

                    # pack the frames into the main window
                    frame1.pack(side=LEFT, fill=BOTH, expand=True, padx=20, pady=20)
                    frame2.pack(side=RIGHT, fill=BOTH, expand=True, padx=20, pady=20)

                    airport_label1 =Label(frame1, text="Airplane Schedules", font=(
                        "Arial", 20, "bold"), fg="#333333", bg="#F0F0F0")
                    airport_label1.pack(pady=30)


                    airport_label2 =Label(frame2, text="Airplane Traffic on Routes", font=(
                        "Arial", 20, "bold"), fg="#333333", bg="#F0F0F0")
                    airport_label2.pack(pady=30)



                    def sample1(out1):
                        
                        global flight1_listbox
                        flight1_listbox = Listbox(frame1, height=100, width=120, bg="light gray")
                        flight1_listbox.pack(padx=1, pady=5)
                        # scrollbar.config(command=flight_listbox.yview)

                        # Add some example flights to the listbox
                        for i in range(len(out1)):
                            if i % 2 == 0:
                                flight1_listbox.insert(i, out1[i])
                                flight1_listbox.itemconfig(i, bg='yellow', fg="black")
                            else:
                                flight1_listbox.insert(i, out1[i])
                                flight1_listbox.itemconfig(i, bg='black', fg="yellow")

                        submit1.destroy()


                    def run1():

                        global out1
                        out1 = []
                        def takeoff(env, name, route, takeoff_time):
                            out1.append(f" {name} is taking off from {route[0]} at {env.now}")
                            print(f" {name} is taking off from {route[0]} at {env.now}")
                            yield env.timeout(takeoff_time)

                        def fly(env, name, route, fly_time):
                            out1.append(f" {name} is flying from {route[0]} to {route[1]}")
                            print(f" {name} is flying from {route[0]} to {route[1]}\n")
                            yield env.timeout(fly_time)

                        def land(env, name, route, landing_time, airplanes):
                            yield env.timeout(airplanes[name]["fly_time"])
                            out1.append(f" {name} is landing at {route[1]} at {env.now}")
                            print(f" {name} is landing at {route[1]} at {env.now}\n")
                            airplanes[name]["arrival_time"] = env.now
                            yield env.timeout(landing_time)

                        def arrival_schedule(env, airplanes):
                            while True:
                                yield env.timeout(random.randint(1, 5))
                                route = random.choice(routes)
                                fly_time = random.randint(5, 10)
                                takeoff_time = random.randint(2, 5)
                                landing_time = random.randint(2, 5)
                                name = f"{random.choice(airlines)}"
                                airplanes[name] = {"route": route, "fly_time": fly_time, "takeoff_time": takeoff_time, "landing_time": landing_time, "arrival_time": None}
                                env.process(takeoff(env, name, route, takeoff_time))
                                env.process(fly(env, name, route, fly_time))
                                env.process(land(env, name, route, landing_time, airplanes))

                        routes = [("New Delhi", "Dubai"), ("New Delhi", "London"), ("Dubai", "New Delhi"),("New Jersy", "New Delhi"),("New Delhi", "New Jersy"),("Mumbai", "New Delhi"), ("New Delhi", "Mumbai"),("Banglore" , "New Delhi"),("New Delhi", "Bangalore")]
                        airlines = ["Boeing 747", "Emirates", "Lufthansa Airlines", "Swiss Air","Air India","Air Canada","Ehtihad","Airbus A380"]

                        env = simpy.RealtimeEnvironment(factor=0.1,strict=False)
                        airplanes = {}
                        env.process(arrival_schedule(env, airplanes))
                        env.run(until=120)
                        sample1(out1)

                        fig, ax = plt.subplots()
                        for i, (name, airplane) in enumerate(airplanes.items()):
                            ax.scatter(airplane["takeoff_time"], i, s=100, c="tab:orange")
                            ax.scatter(airplane["arrival_time"], i, s=100, c="tab:blue")

                        ax.scatter(airplane["arrival_time"],i,s=100,c="tab:blue",marker = "o",label = "Landing")
                        ax.scatter(airplane["takeoff_time"],i,s=100,c="tab:orange",marker = "o",label = "Take-Off")

                        ax.set_ylim(-1, len(airplanes))
                        ax.set_xlim(0, env.now)
                        ax.set_xlabel("Time (s)") 
                        ax.set_yticks(range(len(airplanes)))
                        ax.set_yticklabels([name for name in airplanes.keys()])
                        ax.set_title("Airplane Schedule")
                        ax.legend()
                        plt.show()

                        # fig, ax = plt.subplots(figsize=(9, 6))
                        # canvas = FigureCanvasTkAgg(fig, master=frame2)
                        # canvas.get_tk_widget().pack()

                        # ax.plot(time,airllin)
                        # ax.set_ylabel('Airlines')
                        # ax.set_xlabel('Airplane Timings')
                        # # photo.destroy()
                        # canvas.draw()

                        
                    submit1 = Button(frame1, text="Start Simulation", command=run1, font=(
                        "Arial", 16), fg='black', bg='#B9E0FF', activeforeground='#C47AFF', bd=5, width=16, height=1)
                    submit1.place(x=245, y=450)


                    root1.mainloop()
                    
                     
            
                def run():

                    global out
                    out = []
                    global route_bookings

                    def book_ticket(env, counters, route_bookings):

                        # Simulate passenger arriving at airport and selecting random route
                        choice = random.randint(0, 2)
                        if (choice == 0):
                            route = random.choice(domestic_routes)
                            out.append(
                                f"New Passenger has arrived and wants to book a ticket for domestic route: New Delhi to {route}\n")
                            print(
                                f"New Passenger has arrived and wants to book a ticket for domestic route: New Delhi to {route}\n")
                        else:
                            route = random.choice(international_routes)
                            out.append(
                                f"New Passenger has arrived and wants to book a ticket for an international route: New Delhi to {route}\n")
                            print(
                                f"New Passenger has arrived and wants to book a ticket for an international route: New Delhi to {route}\n")

                        # Request a counter to book the ticket, with priority based on arrival time
                        with counters.request(priority=time.time()) as counter:
                            yield counter

                            # Simulate time taken to book a ticket
                            yield env.timeout(random.randint(1, 5))

                            # Update route bookings
                            if route in route_bookings:
                                route_bookings[route] += 1
                            else:
                                route_bookings[route] = 1
                            out.append(
                                f"Ticket booking for the route: New Delhi to {route} has been completed on {env.now}\n ")
                            print(
                                f"Ticket booking for the route: New Delhi to {route} has been completed on {env.now}\n ")

                    def passenger_arrivals(env, counters, num_passengers, inter_arrival_time, route_bookings):
                        for i in range(num_passengers):
                            yield env.timeout(inter_arrival_time)
                            env.process(book_ticket(env, counters, route_bookings))

                        # Initialize simulation environment and airport
                    route_bookings = {}
                    env = simpy.RealtimeEnvironment(factor=0.1, strict=False)
                    counters = simpy.PriorityResource(env, capacity=3)
                    env.process(passenger_arrivals(env, counters, num_passengers=200,
                                inter_arrival_time=2, route_bookings=route_bookings))

                    # Start passenger arrivals process

                    # Run simulation
                    env.run(until=200)
                    sample(out)

                    routes = list(route_bookings.keys())
                    passengers = list(route_bookings.values())
                    plt.bar(routes, passengers)
                    plt.ylabel('Routes')
                    plt.xlabel('Passenger Traffic')
                    plt.plot()

                    fig, ax = plt.subplots(figsize=(9, 6))
                    canvas = FigureCanvasTkAgg(fig, master=frame2)
                    canvas.get_tk_widget().pack()

                    ax.plot(passengers, routes)
                    ax.set_ylabel('Routes')
                    ax.set_xlabel('Passenger Traffic')
                    # photo.destroy()
                    canvas.draw()

                    Button(frame2,text='Go to Airlines Status',command=run2,font=("Arial",16),fg='black',bg='white',bd=3,width=16,height=1).place(x=280,y=740)



                submit = Button(frame1, text="Start Simulation", command=run, font=(
                    "Arial", 16), fg='black', bg='#B9E0FF', activeforeground='#C47AFF', bd=5, width=16, height=1)
                submit.place(x=245, y=450)


                # Plot passenger traffic on different routes


                root.mainloop()

                

    elif username not in r.keys():
                messagebox.showerror('Error','User does not exist !')
    elif password != r[username]:
                messagebox.showerror('Error','Password is incorrect !')            



def sign():

   
       
    root2 = Toplevel(window)
    root2.title("Sign-Up")
    root2.geometry('1920x1080')
    root2.configure(bg='#fff')
    root2.resizable(True, True)
    background_image1 = PhotoImage(file="p5.png")
    background_label1 = Label(root2,image=background_image1)
    background_label1.place(relwidth=1, relheight=1)



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
        root2.destroy()
        
        

    # img = PhotoImage(file='airplane.png')
    Label(root2,border=0,bg='white').place(x=50,y=90)

    frame = Frame(root2,width=550,height=750,bg='#fff')
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
    
    root2.mainloop()
       
    
    
# img = PhotoImage(file='airplane.png')
Label(window,border=0,bg='white').place(x=50,y=90)

frame = Frame(window,width=550,height=750,bg='#fff')
frame.place(x=880,y=50)

heading = Label(frame,text='Sign In',fg="#57a1f8",bg='white',font=('Microsoft Yahei UI Light',23,'bold'))
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





#-----------------------------------------------------------------------

Button(frame,width=39,pady=7,text='Sign In',bg='#57a1f8',fg='white',border=0,command=signin).place(x=142,y=450)
label = Label(frame,text='I do not have an account !',fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=220,y=420)

signup = Button(frame,width=6,text='Sign up',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=sign)
signup.place(x=370,y=420)

window.mainloop()