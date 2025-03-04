from turtle import *

guestbook =[]
while True:
    name = input("Enter your name here (or type 'exit' to finish): ")
    if name.lower() == 'exit':
        break
    costume = input("What are you dressing up as for Halloween?: ")
    message = input("Leave your wicked message: ")
    
    guest = {
    'name': name,
    'costume': costume, 
    'message': message
    }
    
    guestbook.append(guest)

def move():
    penup()
    right(90)
    forward(30)
    pendown()
    left(90)

setup(width = 800, height = 600)
bgcolor("black")
addshape("pink_ghosts.gif") 
ghost = Turtle()  
ghost.shape("pink_ghosts.gif")

#text
penup()
setposition(0, 250)
pendown()
pensize(10)
pencolor("white")
write("Welcome! Ghosts & Ghouls!", align="center", font = ("Savoye LET", 30, "normal"))
move()
pencolor("darksalmon")
write("Please leave your mark before you vanish into the night!", align="center", font = ("American Typewriter", 20, "normal"))
move()
write("Write your name, the character you dressed as, and a spooky message below:", align="center", font = ("American Typewriter", 20, "normal"))
move()

def guest_info(user): 
    pensize(5)
    pencolor("antiquewhite")
    return(f"Dear {user['name']},\n"
           f"You are {user['costume']} tonight.\n"
           f"Your inscription is:\n{user['message']}"
    )
        
def separator():
    pencolor("darksalmon")
    pensize(1)
    write("Bodoni Ornaments Bodoni Ornaments", align = "center", font = ("Bodoni Ornaments", 12, "normal"))

for guest in guestbook:
    new_guest = guest_info(guest)
    for line in new_guest.split("\n"):
        write(line, align = "center", font = ("Apple Chancery", 20, "normal"))
        move()
    separator()
    move()
    move()

hideturtle()
done()