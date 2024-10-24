#task 1
#****************************************Task 1*************************************************************************
attendees= int(input("Enter the number of attendees: "))
#this fixes the original problem by converting the original input from a string to an integer for the comparision to follow to avoid
#a type mismatch error

venue= "large hall" if attendees >100 else "conference room"
print(venue)
#******************************************************************************************#

#******************************************Task2****************************************************
#task 2
# added some branching and prettier output

attendees= int(input("Enter the number of attendees: "))
venue = ""
sound = ""
projector = "0"
available_chairs = 100
status = ""
chair_status = ""
catering = ""

if attendees > 100:
    venue = "large hall"
    sound = "Full PA system"
    projector = "Big Panasonic"
    if attendees > available_chairs:
        chair_status = "We do not have enough chairs"
    else: 
        chair_status = "We have enough chairs"
elif 20 < attendees <= 99:
    venue = "conference room"
    sound = "small pa"
    projector = "small samsung"
    chair_status = "the room seats 20 max"
    status = "confirmed"
elif 1 < attendees <= 20:
    venue = "small conference room"
    sound = "no audio system needed"
    projector = "large tv"
    status = "confirmed"
    if attendees >= 15:
        chair_status = "Conference room only has 15 chairs. Either reduce the number of attendees or be ready for some to stand."
elif attendees == 1:
        chair_status="What kind of meeting are you having?"
        status = "needs approval"
    
print (f"Venue: {venue}", end="\n")
print (f"Sound System: {sound}", end="\n")
print (f"Projector: {projector}", end="\n")
print (f"Chairs: {chair_status}", end="\n")
print (f"Meeting Status: {status}", end="\n")
print ("********************************************************")
print ("Thank you for using Meeting-tron 3000 from your friends at the Tyrell Corporation")


 #Task 3
 #****************************************Task 3*************************************************************************
attendees= int(input("Enter the number of attendees: "))
food = (input("Do you vegetarian catering? (y/n)"))
venue = ""
sound = ""
projector = "0"
available_chairs = 100
status = ""
chair_status = ""

if food == "y":
     catering = "Call Veggie Delight Caterers at 1-800-EAT-PLANT"
elif catering == "n":
     catering = "Call Gourment Meals Caterers at 1-888-SNOB-FOD"

if attendees > 100:
    venue = "large hall"
    sound = "Full PA system"
    projector = "Big Panasonic"
    if attendees > available_chairs:
        chair_status = "We do not have enough chairs"
    else: 
        chair_status = "We have enough chairs"
elif 20 < attendees <= 99:
    venue = "conference room"
    sound = "small pa"
    projector = "small samsung"
    chair_status = "the room seats 20 max"
    status = "confirmed"
elif 1 < attendees <= 20:
    venue = "small conference room"
    sound = "no audio system needed"
    projector = "large tv"
    status = "confirmed"
    if attendees >= 15:
        chair_status = "Conference room only has 15 chairs. Either reduce the number of attendees or be ready for some to stand."
elif attendees == 1:
        chair_status="What kind of meeting are you having?"
        status = "needs approval"
    
print (f"Venue: {venue}", end="\n")
print (f"Sound System: {sound}", end="\n")
print (f"Projector: {projector}", end="\n")
print (f"Chairs: {chair_status}", end="\n")
print (f"Meeting Status: {status}", end="\n")
print (F"Catering: {catering},", end="\n")
print ("********************************************************")
print ("Thank you for using Meeting-tron 3000 from your friends at the Tyrell Corporation")
print ("****************************************************************************************************************")

       