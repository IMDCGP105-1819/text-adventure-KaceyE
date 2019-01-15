#While testing i have found a few bugs which work to advange but also cause a few problems mainly with the loops which i could not figure out.



# Covers simple imports and fdefining of variables to be used later on
import sys
import time
import random
in_hallway = False
no_wake = 0
choice = ""
crowbar = 0
key = 0
sixth_key = 0
room_five = 0



#Covers the lists used in checking inputs from the user.
yes = ['Yes', 'yes', 'y', 'Y']
no = ['No', 'no', 'n', 'N']
door = ['Door', 'door', 'Look door', 'look at door', 'look']
left = ['Left', 'left', 'l', 'L']
right = ['Right', 'right', 'r', 'R']
leave = ['Leave', 'leave']


#This whole section either defines function for repeated use or is only used to globalise a variable

def play():
    global game

def crowbar_up():
    global crowbar
    crowbar = crowbar + 1
    
def play_input():
    global choice
    choice = str(input("\tWhat would you like to do? "))

def door_one():
    print ("\tYou push the door open. it makes a low rumble as it moves showing a small room with nothing but a crowbar in the center")
    if crowbar == 1:
        print ("\tYou already have the crowbar")
        hallway()

    elif crowbar != 1:
        crowbar_take = input("\tWould you like to take the crowbar? ")
        if crowbar_take in yes:
            crowbar_up()
            hallway()

def hallway():
    print ("\tYou stand in the hallway.")
    


game = 1

load_menu = input("""

    1. Start

    2. Exit



    What say you?: """)


if load_menu == "1":
    game = game -1
    while game == 0:
        wake_up = str(input("\tWould you like to wake up? "))
        #While the rest of the code is fairly self explanitory this single line checks is the input given matched any predefined statements.
        if wake_up in yes:
            print ("\tAs you awake directly in front of your face are the roman numerals (VIII - V - XII - XVI)")
            play_input()
            if choice in door or leave:
                print ("\tThe door appears to have some sort of pincode")
                door_code = input ("\tPin: ")
                if door_code == "851216":
                    in_hallway = True
                    print ("\tThe door swings open with a slow screech showing a dingy hallway with 6 other doors all labelled One - Six")
                    while in_hallway == True:
                        play_input()

    
                        if choice == "1":
                                door_one()

                        elif choice == "2":
                            print ("\tYou push open this cracked door with relative ease")
                            print ("\tAs you enter the room opens up into two more rooms. one to the left and one to the right.")
                            play_input()

                            if choice in left:
                                print ("\tYou open the door walking in and nothing...")
                                print("\t.")
                                print("\t.")
                                print("\t.")
                                print("\tGame over")
                                break
                            #This is also checking predefined parameters however this one is also checking if a variable is met.
                            if choice in right and crowbar == 1:
                                print("\tThe door is slightly stiff. You use the crowbar to force the door open.")
                                print("\tIn the room sits a single lonely chair eminating a dark aura")
                                sit_in_chair = input ("\tWould you like to sit in the chair? ")
                                if sit_in_chair in yes:
                                    print("\tYou sit in the chair. the doom suddenly goes dark and you awaken... in the same chair. only with the door closed and a key on your lap")
                                    key = key + 1
                                    hallway()
                                    print ("\tYou stand outsode of room 4")
                                                                    
                            elif choice in right:
                                print("\tThe door is slightly stiff. Maybe there is a crowbar around")
                                hallway()
                                

                        elif choice == "3":
                            print ("\tAs you open the door you are greeted by a lockbox on a podium")
                            open_box = input ("\tWould you like to open the box? ")
                            if open_box in yes and key == 1:
                                print("\tYou open the box. All that is inside is the number 6")
                                sixth_key = sixth_key + 1
                                hallway()

                            elif open_box in yes:
                                print("\tYou need a key to open this box")
                                hallway()


                        elif choice == "4":
                            print("\tThis door seems to be licked from the inside")
                            hallway()


                        elif choice == "5":

                            if room_five == 1:
                                print ("\tThe rubble blocks this door remember")
                                hallway()

                            elif room_five == 0:
                                print ("\tThis door is rather heavy. As you force it open rubble from the ceiling falls down blocking the path.")
                                room_five = room_five + 1
                                hallway()

                        elif choice == "6":
                            print ("\tThis door is slightly different. it has a slot on the face for the number 6 with long slash marks on the outside")
                            open_six = input ("\tWould you like to open the door? ")
                            if open_six in yes and sixth_key == 1:
                                print ("\tYou place the 6 shaped key slot. The door automatically starts to churn and open revealing the outside.... A maze of the outside")
                                time.sleep(3)
                                print ("\tSoon we should be free from this place....")
                                time.sleep(3)
                                print("\tGame over. well done! Thank you for playing this short game!")
                                sys.exit
                                

        elif wake_up in no:
            no_wake = no_wake + 1
            if no_wake >4:
                print ("\tSweet dreams")
                sys.exit
                break

else:
    sys.exit
