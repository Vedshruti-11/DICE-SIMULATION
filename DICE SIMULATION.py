import tkinter
from PIL import Image, ImageTk
import random

# initialising the variables
biased_die1 = 0
biased_die2 = 0
biased_die3 = 0
roll_times = 0

# toplevel widget which represents the main window of an application
root = tkinter.Tk()
root.geometry('1200x600')
root.configure(bg = 'black')
root.title('ROLL THE DICE')

# Adding label into the frame
l0 = tkinter.Label(root, text="")
l0.pack()

# adding label with different font and formatting
l1 = tkinter.Label(root, text="DICE SIMULATION", fg = "maroon",
        bg = "white",
        font = "Helvetica 16 bold italic")
l1.pack()

# images
dice = ['die1.png', 'die2.png', 'die3.png', 'die4.png', 'die5.png', 'die6.png']
face = [1,2,3,4,5,6]

# simulating the dice with random numbers between 0 to 6 and generating image
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
image3 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

# construct a label widget for image

label1 = tkinter.Label(root, image=image1)
label1.image = image1
label2 = tkinter.Label(root, image=image2)
label2.image = image2
label3 = tkinter.Label(root, image=image3)
label3.image = image3

#placing a widget in the parent widget
label1.place(x = 100,y = 100)
label2.place(x = 490,y = 100)
label3.place(x = 890,y = 100)

# function activated by button
def rolling_dice():
    global biased_die1,biased_die2,biased_die3,roll_times
    roll_times += 1
    #biasing or customising the die
    probability_die1=(biased_die1/roll_times)
    probability_die2=(biased_die2/roll_times)
    probability_die3=(biased_die3/roll_times)
    
    die1 = random.choice(face) if probability_die1 > 0.85 else 6
    die2 = random.choice(face) if probability_die2 > 0.85 else 2
    die3 = random.choice(face) if probability_die3 > 0.85 else 5
    
    if(die1 == 6):
        biased_die1 += 1
    if(die2 == 2):
        biased_die2 += 1
    if(die3 == 5):
        biased_die3 += 1
      
    image1 = ImageTk.PhotoImage(Image.open(dice[die1-1]))
    image2 = ImageTk.PhotoImage(Image.open(dice[die2-1]))
    image3 = ImageTk.PhotoImage(Image.open(dice[die3-1]))
    
    # update image
    label1.configure(image=image1)
    label2.configure(image=image2)
    label3.configure(image=image3)
    
    # keep a reference
    label1.image = image1
    label2.image = image2
    label3.image = image3

# adding button, and command will use rolling_dice function
button = tkinter.Button(root, text='Roll the Dice', fg='blue', command=rolling_dice)

# pack a widget in the parent widget
button.place(x=580,y=400)

# call the mainloop of Tk
# keeps window open
root.mainloop()
