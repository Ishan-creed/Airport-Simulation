
from tkinter import messagebox
import ast
import simpy
import random
import time
import matplotlib.pyplot as plt
from tkinter import *
from PIL import ImageTk, Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


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
        yield env.timeout(takeoff_time)

    def fly(env, name, route, fly_time):
        out1.append(f" {name} is flying from {route[0]} to {route[1]}")
        yield env.timeout(fly_time)

    def land(env, name, route, landing_time, airplanes):
        yield env.timeout(airplanes[name]["fly_time"])
        out1.append(f" {name} is landing at {route[1]} at {env.now}")
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

    env = simpy.RealtimeEnvironment(factor=0.1, strict=False)
    airplanes = {}
    env.process(arrival_schedule(env, airplanes))
    env.run(until=60)
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