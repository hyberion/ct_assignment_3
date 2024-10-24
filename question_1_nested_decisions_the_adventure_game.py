#Task 1: 
print("*****************************Task 1********************************************")
place=input("Choose a place: forest or cave?")

if place=="forest":
    action = input("Climb a tree or cross a river?")
    if action == "climb a tree":
        print("You are attacked by a viscious squirrel and take 10 points of damage")
    elif action == "cross a river":
        print("You meet a very thin boatman in a dark boat.  He is *very* thin.  He seems nice.")
elif place=="cave":
    print("It's very dark.  You stub your toe on a rock.  Take 10 points of damage")
print("**********************************************************************************")

#task 2: Electric Boogaloo- this time it's personal
print("*******************************Task 2***********************************************")

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("Climb a tree or cross a river ")
    if action == "climb a tree":
        print("You are attacked by a vicious squirrel and take 10 points of damage")
        action = input("fight the squirrel or negotiate? ")
        if action == "negotiate":
            print("You trade 6 nuts for a mystical leaf. You don't know what it does...yet")
        elif action == "fight the squirrel":
            print("The squirrel easily defeats you. You wake up with no possessions in the trunk of a dead tree. You die of embarrassment.")
    elif action == "cross a river":
        print("You meet a very thin boatman in a dark boat. He is *very* thin. He seems nice.")
    else:
        print("You are adopted by a family of bears, only later to die in the first skirmish of the Great Porridge War")
elif place == "cave":
    print("It's very dark. You stub your toe on a rock. Take 10 points of damage")
    action = input("light a torch or sing a dwarven mining song? ")
    if action == "light a torch":
        print("You fail a dex role and set yourself on fire. Take 10 points of fire damage and you now have no clothes")
    elif action == "sing a dwarven mining song":
        print("You are sued for copyright infringement by the Disney Corporation (C). Lose 100 gold")
    else:
        print("Indecision leads to your ultimate demise as you fall into a coma from inactivity")

print("**********************************************************************************")