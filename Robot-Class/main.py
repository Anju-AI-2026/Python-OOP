from robot_class import Robot

print("Fill the robot details")

# Take robot name input and validate it to avoid invalid entries
while True:
    name=input("Enter the robot name : ")
    if(name.isalnum()):
        break
    else:
        print("Please enter a valid name ")

# Take robot ID input and ensure it contains only digits
while True:
    R_id=input("Enter the robot id : ")
    if(R_id.isdigit()):
        break
    else:
        print("Please enter a valid ID")

# Create Robot object using validated user input
robot=Robot(name,R_id)

# Display available options for controlling the robot
print("======Robot action menu======")
print("1.Move robot")
print("2.Detect obstacal")
print("3.Show status")
print("4.Recharge robot")
print("5.Return to base ")
print("6.Show details")
print("7.See menu")
print("8.Exit")

# Infinite loop to continuously take user commands for robot control
while True:

    # Take user menu choice and execute corresponding robot action
    choice=input("Enter a choice number from the menu : ")
    
    if (choice.isdigit()):
        choice=int(choice)
        if choice==1:
            # Handle robot movement with direction and step validation
            while True:
                print("Moving robot")
                print("1.UP")
                print("2.DOWN")
                print("3.RIGHT")
                print("4.LEFT")
                direction=input("Enter a direction : ")
                if (direction.isdigit()):
                    direction=int(direction)
                    steps=input("Enter the steps : ")
                    if (steps.isdigit()):
                        steps=int(steps)
                        robot.move(direction,steps)
                        break
                    else:
                        print("Please enter a valid number")    
                else:
                    print("Choice should be integer. Enter again")    

        elif choice==2:
            # Handle obstacle detection input and validation
            while True:
                distance=input("Enter the distance :" )
                if (distance.isdigit()):
                    distance=int(distance)
                    robot.detect_obstacle(distance)
                    break
                else:
                    print("Please enter a valid input")    
        elif choice==3:
            robot.show_status()
        elif choice==4:
            robot.recharge()
        elif choice==5: 
            robot.back_to_place()   
        elif choice==6:
            robot.show_details()
        elif choice == 7:
            robot.see_menu()    
        elif choice==8:
            exit()
        else:
            print("Enter the correct choice")   
    else:
        print("String are not allowed ! please enter a valid choice") 
if __name__ == "__main__":
    main()
