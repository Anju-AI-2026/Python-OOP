# Robot class represents a simple simulation of a robot with movement, battery, and actions

class Robot:

    # Initialize robot with name, ID, battery level, and starting position (0,0)
    def __init__(self,name,R_id,):
        self.name = name
        self.R_id = R_id
        self.battery = 100
        self.X = 0
        self.Y = 0

    # Move robot in a specific direction and update position and battery level
    def move(self,direction,steps):
        if self.battery<=20:
            print("Battery running low, Please charge it!!!")
            return
        else:
            # Direction 1 = UP, 2 = DOWN, 3 = RIGHT, 4 = LEFT
            if direction == 1:
                self.Y=self.Y+steps 
                print("Robot moved in",direction,"by",steps,"steps")
                print("Current position :") 
                print("X position",self.X)
                print("Y position : ",self.Y)
                self.battery = self.battery-10
                print("Current battery",self.battery)
            elif direction == 2:
                self.Y=self.Y-steps
                print("Robot moved in",direction,"by",steps,"steps")
                print("Current position :") 
                print("X position",self.X)
                print("Y position : ",self.Y)
                self.battery = self.battery-10
                print("Current battery",self.battery)
            elif direction == 3:
                self.X=self.X+steps
                print("Robot moved in",direction,"by",steps,"steps")
                print("Current position :") 
                print("X position",self.X)
                print("Y position : ",self.Y) 
                self.battery = self.battery-10
                print("Current battery",self.battery)
            elif direction == 4:
                self.X=self.X-steps
                print("Robot moved in",direction,"by",steps,"steps")
                print("Current position :") 
                print("X position",self.X)
                print("Y position : ",self.Y) 
                self.battery = self.battery-10
                print("Current battery",self.battery)
            else:
                print("Enter correct choice")

    # Detect if there is an obstacle based on distance value
    def detect_obstacle(self,distance):
        if self.battery<=20:
            print("Battery running low, Please charge it!!!")
            return
        else:
            if (distance>5):
                print("Obstacle detected")
            else:
                print("Clear path!!")
                self.battery=self.battery-10
    
    # Display current position of robot and reduce battery slightly
    def show_status(self):
        if self.battery<=20:
            print("Battery running low, Please charge it!!!")
            return
        else:
            print("Showing current robot status")
            print("X position : ",self.X)    
            print("Y position : ",self.Y)  
            self.battery=self.battery-2       

    # Recharge robot battery only when it is at base position (0,0)
    def recharge(self): 
        if (self.battery==100):
            print("The charge is already full!!!")
        else:
            if (self.X == 0 and self.Y == 0):
                print("Robot is charging")  
                self.battery=100
            else:
                print("Please return to the base place")    

    # Reset robot position back to base coordinates (0,0)
    def back_to_place(self):
        print("Robot is back to it's place")
        self.X=0
        self.Y=0    

    # Display robot's basic information like name, ID, battery, and position          
    def show_details(self):
        if self.battery<=20:
            print("Battery running low, Please charge it!!!")
            return
        else:
            print("Robot name : ",self.name)
            print("Robot ID : ",self.R_id)
            print("Robot battery : ",self.battery)
            print("X position : ",self.X)
            print("Y position : ",self.Y)
            self.battery=self.battery-10

    # Display list of available robot actions for user interaction
    def see_menu(self):
        print("======Robot action menu======")
        print("1.Move robot")
        print("2.Detect obstacle")
        print("3.Show status")
        print("4.Recharge robot")
        print("5.Return to base ")
        print("6.Show details")
        print("7.See menu")
        print("8.Exit")
