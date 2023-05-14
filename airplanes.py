import simpy
import random
import matplotlib.pyplot as plt

# Define a class for the airplane
class Airplane:
    def __init__(self, env, name, route, fly_time, takeoff_time, landing_time):
        self.env = env
        self.name = name
        self.route = route
        self.fly_time = fly_time
        self.takeoff_time = takeoff_time
        self.landing_time = landing_time
        self.arrival_time = None

    def takeoff(self):
        print(f" {self.name} is taking off from {self.route[0]} at {env.now}")
        yield self.env.timeout(self.takeoff_time)

    def fly(self):
        print(f" {self.name} is flying from {self.route[0]} to {self.route[1]}")
        yield self.env.timeout(self.fly_time)

    def land(self):
        yield self.env.timeout(self.fly_time)
        print(f" {self.name} is landing at {self.route[1]} at {env.now}")
        self.arrival_time = self.env.now
        yield self.env.timeout(self.landing_time)
    
# Define a function for the airplane's arrival schedule
def arrival_schedule(env, airplanes):
    while True:
        yield env.timeout(random.randint(1, 5))
        route = random.choice(routes)
        fly_time = random.randint(5, 10)
        takeoff_time = random.randint(2, 5)
        landing_time = random.randint(2, 5)
        airplane = Airplane(env, f"{random.choice(airlines)}", route, fly_time, takeoff_time, landing_time)
        airplanes.append(airplane)
        env.process(airplane.takeoff())
        env.process(airplane.fly())
        env.process(airplane.land())
    
# Define the airplane routes and their schedules
routes = [("New Delhi", "Dubai"), ("New Delhi", "London"), ("Dubai", "New Delhi"),("New Jersy", "New Delhi"),("New Delhi", "New Jersy"),("Mumbai", "New Delhi"), ("New Delhi", "Mumbai"),("Banglore" , "New Delhi"),("New Delhi", "Bangalore")]
airlines = ["Boeing 747", "Emirates", "Lufthansa Airlines", "Swiss Air","Air India","Air Canada","Ehtihad","Airbus A380"]
# Create a SimPy environment and start the simulation
env = simpy.RealtimeEnvironment(factor=0.1, strict=False)
airplanes = []
env.process(arrival_schedule(env, airplanes))
env.run(until=60)


# Create a dot plot of the arrival and departure times of the airplanes
fig, ax = plt.subplots()
for i, airplane in enumerate(airplanes):
    ax.scatter(airplane.takeoff_time, i, s=100, c="tab:orange")
    ax.scatter(airplane.arrival_time, i, s=100, c="tab:blue")
ax.scatter(airplane.takeoff_time,i,s=100,c="tab:orange",marker = "o",label = "Take-Off")
ax.scatter(airplane.arrival_time,i,s=100,c="tab:blue",marker = "o",label = "Landing")
ax.set_ylim(-1, len(airplanes))
ax.set_xlim(0, env.now)
ax.set_xlabel("Time (s)") 
ax.set_yticks(range(len(airplanes)))
ax.set_yticklabels([airplane.name for airplane in airplanes])
ax.set_title("Airplane Schedule")
ax.legend()
plt.show()
