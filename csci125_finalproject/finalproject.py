import tkinter
from tkinter import StringVar, PhotoImage
### functions start ##
def win():
    youwin=tkinter.Label(frame,text="You continue forward, stumbling across a large clearing. All your friends are there holding you a surprise party! -- The End")
    youwin.pack()

def lose():
    youlose=tkinter.Label(frame,text="You turn back, only to get lost in the woods even further -- The End")
    youlose.pack()

def goright2():
    death2 = tkinter.Label(frame,text="You are suddenly ambushed by a large, shadowy figure -- The End")
    death2.pack()

def goleft2():
    choice2 = tkinter.Label(frame,text="You continue walking only to stumble across a sign telling you to 'turn back' -- What do you do?")
    choice2.pack()
    if goright2:
        forward=tkinter.Button(frame,text="Go Forward",command=win)
        forward.pack()
        goback=tkinter.Button(frame,text="Go Back",command=lose)
        goback.pack()

def goleft1():
    death1 = tkinter.Label(frame,text="You turn left, walking only a few feet before falling into a hole -- The End")
    death1.pack()

def goright1():
    choice1=tkinter.Label(frame,text="You turn right, only to feel the eyes of some far off people watching you. You keep walking only to find a fork in the road. You're faced with a familar dilemma: right or left?")
    choice1.pack()
    if goright1:
        left2=tkinter.Button(frame,text="Go Left",command=goleft2)
        left2.pack()
        right2=tkinter.Button(frame,text="Go Right",command=goright2)
        right2.pack()

### functions end ###

### main window ###
app = tkinter.Tk()
app.title("The Woods")

### main frame ###
frame = tkinter.Frame(app,relief="raised",borderwidth=5,background="black")
frame.pack()

### images ###
image1 = PhotoImage(file="spookywoods.gif")

imglabel = tkinter.Label(frame)
imglabel['image']=image1
imglabel.pack(padx=20,pady=20)

### images end ##


### labels ###

textlabel=tkinter.Label(frame,text="You wake up in front of the woods...What do you do?")
textlabel.pack()

### buttons ###

left1 = tkinter.Button(frame,text="Go Left",command=goleft1)
left1.pack()
right1 = tkinter.Button(frame,text="Go Right",command=goright1)
right1.pack()

### keep open ###
app.mainloop()