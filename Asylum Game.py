def intro ():
    print("""
    You spot a building deep in the forest, it's an abandoned asylum. You see lights flickering 
    inside so you enter out of curiosity. As you're looking around you find an article on the ground 
    with blood stains. It states that in the asylum the people there were constantly mistreated
    and doctors used some of them in horrendous experiments. 
    Suddenly you hear a thud, you notice the room getting foggy, and then suddenly see people running 
    towards you... but they aren't human!
    Do what you can to escape these tweaking flesh eating beings and escape!!!
    \nYou're in the middle of the main room and to your sides there's two dark hallways. 
    You see these monsters getting closer to you, growling and screeching. You have the
    choice of going either left or right. HURRY!
    """)
    
    choice = input("Do you want to go to the 'left hallway' or 'right hallway'? ").lower()
    
    if choice == 'left hallway':
        stairs()
    elif choice == 'right hallway':
        slide()
    else: 
        print ("Invalid choice! Try again!")
        intro()

def stairs():
    print("""
    You choose to go down the left hallway, at the very end there are stairs that go down. 
    You're trying to get away from the monsters as fast you can. They're right behind. 
    At the bottom there are two doors. One leads to a padded room while the other door 
    leads to a patient room.
    """)
    
    choice = input("Do you want to enter the 'padded' room or the 'patient' room? ").lower()
    
    if choice == 'padded':
        die("You enter the padded room and it's empty. You wait to see if you can go back out, waiting to hear any movement. As you're about to open the door, you can't. The door is locked. There's no way to escape. You go insane being by yourself in the padded room and slowly die.")
    elif choice == 'patient':
        hallway()
    else: 
        print ("Invalid choice! Try again!")
        stairs() 
        
def hallway():
    print("""
    You enter a patient room. On the other side there is another door, you decide to open it and it leads you to a hallway. 
    You run down the hallway and on the left you see an open office while on the right you see a restroom.      
    """)
    
    choice = input("Do you want to enter the 'office' on the left or the 'restroom' on the right? ").lower()
    
    if choice == 'office': 
        win()
    elif choice == 'restroom':
        die("You entered the restroom, it's very quiet. You get janked into a stall and eaten alive.")
    else: 
        print("Invalid choice! Try again!")
        hallway()
    
        
def slide(): 
    print("""
    The right hallway has led to a slide. You immediately enter the slide, however, a monster catches you by the shirt. 
    The creature's hand has a firm grip, you're kicking your feet and moving to get free. You pull with strength and 
    your shirt rips letting you free. When you reach the bottom you can either go to the cafeteria or go 
    inside a closet and hide while you wait for things to calm down.     
    """)
    
    choice = input("Do you want to go into the 'cafeteria' or go inside the 'closet'? ").lower()
    
    if choice == 'cafeteria':
        win()
    elif choice == 'closet':
        die("You enter the closet and get trapped. The creatures are banging on the door and suddenly break in. You die.")
    else: 
        print ("Invalid choice! Try again!")
        slide() 
        
def die(reason): 
    print("\nGAME OVER: ") + reason
    play_again()
   
    
def play_again(): 
    choice = input("\nDo you want to play again? (yes/no): ").lower()
    if choice == 'yes': 
       intro()
    else:
        print("Thank you for playing! Toodles!")
        
        
def win(): 
    print("""
    You find a big window in the office. Then you spot some curtains and sheets, you tie them together and use it as 
    a rope to get down. You succesfully escape! A few days later you go back and using bombs you destroy the asylum so 
    no one can get in or out.  
    """)
    play_again()