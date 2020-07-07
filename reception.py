# Recieves Tourists

print("Hello There, Welcome to our hotel!")



legal_age = 18
identity = input("Can i check Your identity please?")
if identity == "yes": 
    print("Alright!")
    print("All good!")
    print("Now,You can choose the room that helps you!")
    print("We have rooms for Couple with 50$")
    print("And we have rooms for family with 80$")
    room = input("Can you tell me your choose?,please!") # Answer = "for couple" , "for family" !
    day = int(input("How long will you stay here?"))   
    request = "for couple"
    order = "for family"
    x = 50
    y = 80
    if room == request :
        print("You will pay",x * day,"dollars") 
    if room == order :
        print("You will pay",y * day,"dollars") 
    print("Now, you can take your key,sir!")
    print("Have A nice Stay in our Hotels!!!")       
else:
    age = int(input("how old are you?")) 
    if  ( age >= legal_age ):
        print("Sorry, but you have to let me check your identity,it's necessary!") 
    if ( age < legal_age ) :
        print("you don't be able to enter the hotel, please go out!")    

# IT's a small project to increase my skills in python, hope you like it! 



