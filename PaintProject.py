'''
Paint Project
By:Wafi Hassan
'''

from pygame import * # importing all pygame library functions to draw 
from math import *   # importing all math library functions to calculate sqrt for brush tools
from tkinter import *#importing files from tkinter to help with load/save functions
from tkinter import filedialog # importing filedialog functions from tkinter to use open and save file
from collections import deque
import math # importing all math for drawing circle
import pygame#importing from pygame
import time#importing from time
from pygame import mixer #The mixer system only supports a single music stream at once.

root=Tk()#creates a new window
root.withdraw() #hide the root window

##############Creating display area ###########################
width,height=1100,700#creates the parameters of the "Paint Project" window. x=1100 units to the right and y=700 units down
screen=display.set_mode((width,height))#Initializes a window or screen for display
display.set_caption('The Paint Project-League of Legends')#setting a caption/name for the tab that is going to be used in the Paint Project


##################Initialization of colours########################
RED=(255,0,0)#The RGB values to get "Red"
GREY=(127,127,127)#The RGB values to get "Grey" 
BLACK=(0,0,0)#The RGB values to get "Black" 
BLUE=(0,0,255)#The RGB values to get "Blue"
GREEN=(0,255,0)#The RGB values to get "Green"
YELLOW=(255,255,0)#The RGB values to get "Yellow" 
WHITE=(255,255,255)#The RGB values to get "White"
CREAM=(240,150,75)#The RGB values to get "Cream"


##################Backgroung Image Setup######################3
league=image.load("images/league.jpg")#loading the background image "league.jpg" from it's directory so that its prepared to be "blitted". Variable set to league
screen.blit(league,[0,0]) #blit(image, (left, top)) Drawing the image "league.jpg" to the screen at the given position.



toolstips=image.load("images/BLACK.png")#loading the background image "BLACK.jpg" from it's directory so that its prepared to be "blitted". Variable set to toolstips
screen.blit(toolstips,[176,6])#blit(image, (left, top)) Drawing the image "BLACK.jpg" to the screen at the given position.



#######################Writing Fonts For Tools################################
font.init() #It initializes the font module. The module must be initialized before any other functions will work.
comicFont=font.SysFont("comic Sans MS",20) # choosing font style and size. Set to variable comicFont so it can be rendered. 
word="Tools"#the word that I want to be blitted onto the Paint Project screen
wordPic=comicFont.render(word,True,GREEN)#renders the word with the font and adds some properties to the word such as colour
screen.blit(wordPic,(20,8))#blits the word onto the points(20,8) on the paint project screen


################Music Font####################################
wword="Background Music"#the word that I want to be blitted onto the Paint Project screen. Set to variable wword
musicPic=comicFont.render(wword,True,GREEN)#renders the word with the font and adds some properties to the word such as colour
screen.blit(musicPic,(855,20))#blits the sentence onto the point (855,20) on the paint project screen

comicFont=font.SysFont("comic Sans MS",15)# choosing font style and size. Set to variable comicFont2 so it can be rendered. 
startword="Play Music"#the word that I want to be blitted onto the Paint Project screen. Set to variable startword
musicPic=comicFont.render(startword,True,YELLOW)#renders the word with the font and adds some properties to the word such as colour
screen.blit(musicPic,(823,65))#blits the words onto the point (8235,65) on the paint project screen

stopword="Pause Music"#the word that I want to be blitted onto the Paint Project screen. Set to variable stopword
musicPic=comicFont.render(stopword,True,YELLOW)#renders the word with the font and adds some properties to the word such as colour
screen.blit(musicPic,(963,65))#blits the words onto the point (8235,65) on the paint project screen




######################Loading Circular Colour Pallette#########################
colour=image.load("images/colorCircleWafi.png")#loading the background image "colorCircleWafi.jpg" from it's directory so that its prepared to be "blitted". Variable set to colour
screen.blit(colour,(850,530))#blits the words onto the point (850,530) on the paint project screen


#########################For Highlighter###############################################
brushHead=Surface((20,20),SRCALPHA)#The A is "alpha". It controls how transparent/opaque the colour is(0=transparent 255=opaque). Variable set to brushHead
draw.circle(brushHead,(255,0,0,27),(10,10),10)#drawing the highlighter "circles" with properties from "brushhead", colour is (255,0,0,27) and radius is (10,10) and thickness is 10.


#############Array for Colour Pallete#########################
      #0    1    2     3     4      5     6
cols=[RED,BLUE,GREEN,YELLOW,BLACK,GREY,CREAM]#putting all the colours in a list will make it easier to draw since the person has a choice in which colour to draw with.


#########################Creating Tool Rectangles#################################################
InfoRect=Rect(175,7,220,110)#Creating rectangle named InfoRect with points (starting x point,starting y point,220pixels wide,110pixels tall)
undoRect=Rect(20,35,60,60)#Creating rectangle named undoRect with points (starting x point,starting y point,60 pixels wide,60 pixels tall)
redoRect1=Rect(100,35,60,60)#Creating rectangle named redoRect1 with points (starting x point,starting y point,60 pixels wide,60 pixels tall)
pencilRect=Rect(20,115,60,60)#Creating rectangle named pencilRect with points (starting x point,starting y point,60 pixels wide,60 pixels tall)
eraserRect=Rect(100,115,60,60)#Creating rectangle named eraserRect with points (starting x point,starting y point,60 pixels wide,60 pixels tall)
circleRect=Rect(20,200,60,60)#Creating rectangle named circleRect with points (starting x point,starting y point,60 pixels wide,60 pixels tall))
brushRect=Rect(100,200,60,60)#Creating rectangle named brushRect with points (starting x point,starting y point,60 pixels wide,60 pixels tall)
rectangleRect=Rect(20,300,60,60)#Creating rectangle named rectangleRect with points (starting x point,starting y point,60 pixels wide,60 pixels tall)
lineRect=Rect(100,300,60,60)#Creating rectangle named lineRect with points (starting x point,starting y point,60 pixels wide,60 pixels tall)
fillRect=Rect(20,400,60,60)#Creating rectangle named fillRect with points (starting x point,starting y point,60 pixels wide,60 pixels tall)
highlighterRect=Rect(100,400,60,60)#Creating rectangle named highlighterRect with points (starting x point,starting y point,60 pixels wide,60 pixels tall)
saveRect=Rect(20,500,60,60)#Creating rectangle named saveRect with points (starting x point,starting y point,60 pixels wide,60 pixels tall)
openRect=Rect(100,500,60,60)#Creating rectangle named openRect with points (starting x point,starting y point,60 pixels wide,60 pixels tall)
colorwheelRect=Rect(850,530,150,150)#Creating rectangle named colorwheelRect with points (starting x point,starting y point,150 pixels wide,150 pixels tall)
canvasRect=Rect(200,120,600,460)#Creating rectangle named InfoRect with points (starting x point,starting y point, 600 pixels wide,460 pixels tall))
paletteRect=Rect(450,600,350,50)#Creating rectangle named InfoRect with points (starting x point,starting y point,350 pixels wide,50 pixels tall)

#################Music Shapes#############################
playRect2=Rect(927,75,27,27)#Creating rectangle named InfoRect with points (starting x point,starting y point,27 pixels wide,27 pixels tall)
musicRect=Rect(810,10,265,110)#Creating rectangle named InfoRect with points (starting x point,starting y point,265 pixels wide,110 pixels tall)
playRect1=Rect(820,50,100,60)#Creating rectangle named InfoRect with points (starting x point,starting y point,100 pixels wide,60 pixels tall)
playRect3=Rect(960,50,100,60)#Creating rectangle named InfoRect with points (starting x point,starting y point,100 pixels wide,60 pixels tall)

#############For Stamp Framing#####################
frameRect=Rect(20,600,300,50)#Creating rectangle named InfoRect with points (starting x point,starting y point,300 pixels wide,50 pixels tall)
comicFont3=font.SysFont("comic Sans MS",15)# choosing font style and font size 15. Set to variable comicFont3 so it can be rendered.
word="Stamps"#the word that I want to be blitted onto the Paint Project screen
word3Pic=comicFont3.render(word,True,GREEN)#renders the word with the font and adds some properties to the word such as colour  
screen.blit(word3Pic,(20,575))#blits "word3Pic" onto the point (20,575) on the paint project screen

###############Creating Stamp Rectangles##########################
stamp1Rect=Rect(25,605,40,40)#creating rectangle at origin(25,605), 40 pixels wide and 40 pixels tall
stamp2Rect=Rect(75,605,40,40)#creating rectangle at origin(75,605), 40 pixels wide and 40 pixels tall
stamp3Rect=Rect(125,605,40,40)#creating rectangle at origin(125,605), 40 pixels wide and 40 pixels tall
stamp4Rect=Rect(175,605,40,40)#creating rectangle at origin(175,605), 40 pixels wide and 40 pixels tall
stamp5Rect=Rect(225,605,40,40)#creating rectangle at origin(225,605), 40 pixels wide and 40 pixels tall
stamp6Rect=Rect(275,605,40,40)#creating rectangle at origin(275,605), 40 pixels wide and 40 pixels tall


##############Drawing the Canvas#############################
draw.rect(screen,WHITE,canvasRect)#draws a rectangle on the screen, coloured white and coordinates are situated in the variable "canvasRect"


#######################Drawing the Palette#####################
draw.rect(screen,(200,200,200),paletteRect)#draws a rectangle on the screen, RGB coordinates are (200,200,200) and coordinates are situated in the variable "paletteRect"


#############Writing Colours On the Screen##############
comicFont2=font.SysFont("comic Sans MS",15)#choosing font style and has the font size set to 15. Set to variable comicFont2 so it can be rendered later on.
word="Colours"#the word that I want to be blitted onto the Paint Project screen
word2Pic=comicFont2.render(word,True,GREEN)#renders the word with the font and adds some properties to the word such as colour
screen.blit(word2Pic,(450,580))##displaying "Colours" on the screen at points (450,580)
                

##################Undo/Redo Lists Array###################
undolist=[]#creating an empty list to store anything written on the canvas, which will help with the function of undo
redolist=[]#creating an empty list to store anything written on the canvas, which will help with redo


###########Blank Canvas Added in Undolist#################
a=screen.subsurface(canvasRect).copy()#copies the blank canvas
undolist.append(a)#adds the blank canvas into the undo list since if someone draws right away and want to undo, then they will get blank screen again



####################Colour Choosing by Index######################################
for i in range(len(cols)):#adding a for loop for the colour palette in the bottom of the screen, using the previous list cols that held all the colours.
    draw.rect(screen,cols[i],(455+i*50,605,40,40))#draws a rectangle on the screen, with the colours in order in the list, starting at 455+i*50, and 605. 40 pixels wide and 40 pixels high. "i" meaning the number of colours. So if its on the third colour, 3i is 3 times further than i.


########################Initialization of Variables#############################
omx,omy,mx,my,nx,ny=0,0,0,0,0,0#setting all mx,my,omy,omx,nx,ny values to zero to help with the tools in the future.
running=True#this code means Paint Project is officially running, so anything behind this code was the "pre-code" and everything after will happen as its launching
tool="no tool"#default setting the tool to "no tool" since you aren't using a tool "yet"
mb=''#mb meaning mouse button, but currently I need to initialize this since I wont need it yet, so I used empty string.

col=BLACK#black is currently set to the default colour so when drawing, it will be in black if u dont change colour.

playlist=[]#creating empty list for the playlist music
mixer.pre_init(44100,16,2,4096)#pygame.mixer.pre_init(frequency, size, stereo, buffer)
mixer.init()#initializing the mixer
playlist.append ("music/Song1.ogg")#adding the music file into the list "playlist"
playlist.append ("music/Urf.ogg")#adding the music file into the list "playlist"

pygame.mixer.music.load (playlist.pop())#removes the first track from the playlist
pygame.mixer.music.queue (playlist.pop())#Queue the 2nd song
pygame.mixer.music.set_endevent (USEREVENT)#Setup the end track event
pygame.mixer.music.play()#Play the music recently loaded, which was in "playlist.pop()" so urf.ogg is currently playing

'''
The while loop in Python is used to iterate over a block of code as long as the test expression (condition) is true.
I use this loop I don't know beforehand, the number of times to iterate.
event.get returns a list of all the events that are currently in the event queue.
Doing so empties the queue. Each element in the list that event.get returns is an Event object with a .type attribute (pygame.KEYDOWN, pygame.MOUSEBUTTONUP, etc.)
and other attributes depending on what type of event it is.
'''

while running:#while the paint project is still running
    for evt in event.get():#get events from the queue
        if evt.type == USEREVENT:# if A track has ended
            playlist.append('music/Song1.ogg')#adds back the song into the playlist
            mixer.music.load('music/Song1.ogg')#loads up the song "Song1.ogg
            mixer.music.play()#plays the recently loaded song "Song1.ogg"

        if evt.type==QUIT:#when the user clicks the window's "X" button the tab will close and wont runn anymore
            running=False#paint project will no longer be running since running=False
        
        if evt.type == MOUSEBUTTONUP:#if mouse isnt being pressed or acted on
            mouse.set_visible(True)#mouse becomes visible on your screen
            mx,my=mouse.get_pos()

        if evt.type==MOUSEBUTTONUP: #If you let go of the mouse
            if canvasRect.collidepoint(mx,my): #If the canvas rect/s collidepoint is the mouse
                copy=screen.subsurface(canvasRect).copy() #This copies the surface of the canvas
                undolist.append(copy) #This appends the copied surface
        if evt.type==MOUSEBUTTONDOWN:#when the mouse is being pressed down
            click=True#click is currently true, this will be used for stamps
        mx,my=mouse.get_pos()#current mouse position
        mb=mouse.get_pressed()#every time you click, it puts it under the variable mb
        if mb[0]==1 and undoRect.collidepoint(mx,my):#if the mouse click on undoRect
            tool="undo"#tool becomes undo
            screen.blit(toolstips,[176,6])#blits a black screen over the "tool tips/function at point(176,6)
            Help17="Undoes your previous drawing!"#tool tip that will be written if tool=undo
            Help17=comicFont.render(Help17,True,GREEN)#the word will be rendered and put in colour green under variable Help17 
            screen.blit(Help17,(181,48))#image gets blitted at (181,48)
    
            if len(undolist)>1: #if undo list has more than one copy
                    
                    redolist.append(undolist[-1]) #redo gets the most recent picture in the undo list
                    undolist.remove(undolist[-1]) #undo gets rid of the most recent picture
                    screen.blit(undolist[-1],(canvasRect)) # blits the 2nd most recent picture
                    

        if mb[0]==1 and redoRect1.collidepoint(mx,my): #if the mouse click on redoRect           
            tool="redo"#tool becomes redo after clicking redo tool
            screen.blit(toolstips,[176,6])##blits a black screen over the "tool tips/function at point(176,6)
            Help18="Redos your previous drawing!"#tool tip that will be written if tool=redo
            Help18=comicFont.render(Help18,True,GREEN)#the word will be rendered and put in colour green under variable Help17
            screen.blit(Help18,(181,48))#image gets blitted at (181,48)
            if len(redolist)>0:#if the length of the redolist is greater than 0.
                    screen.blit(redolist[-1],(canvasRect)) #redo first blits the picture
                    undolist.append(redolist[-1])       #undo gets the picture
                    redolist.remove(redolist[-1])       #redo removes the most recent picture

    

########DRAWING MUSIC SHAPES############
    draw.rect(screen,GREEN,musicRect,2)
    draw.rect(screen,BLUE,playRect1,2)
    draw.rect(screen,BLUE,playRect2,2)
    draw.rect(screen,BLUE,playRect3,2)
    draw.rect(screen,BLUE,InfoRect,2)

##############Loading Images and Drawing Box for Tools##################
    draw.rect(screen,GREEN,undoRect,2)#draws a rectangle at the screen, colour is green and paramters arw within "undoRect", and size is 2
    undo1=image.load("images/tools/undo.png")#loading an image inside the tools folder and file is called undo.png under the variable undo1
    screen.blit(undo1,[26,40])#blits the picture in the coordinates(26,40)

    stops=image.load("images/Stop.png")#loading an image inside the images folder and file is called Stop.png under the variable stops
    screen.blit(stops,[929,76])#blits the picture in the coordinates(929,76)

    draw.rect(screen,GREEN,redoRect1,2)#draws a rectangle at the screen, colour is green and paramters arw within "redoRect1", and size is 2    
    redo1=image.load("images/tools/redo.png")#loading an image inside the tools folder and file is called redo.png under the variable redo1
    screen.blit(redo1,[104,40])#blits the picture in the coordinates(104,40)
    
    draw.rect(screen,GREEN,pencilRect,2)#draws a rectangle at the screen, colour is green and paramters arw within "pencilRect", and size is 2
    pen=image.load("images/tools/pen.png")#loading an image inside the tools folder and file is called pen.png under the variable pen
    screen.blit(pen,[26,120])#blits the picture in the coordinates(26,120)
    
    draw.rect(screen,GREEN,eraserRect,2)#draws a rectangle at the screen, colour is green and paramters arw within "eraserRect", and size is 2
    eraser=image.load("images/tools/eraser.png")#loading an image inside the tools folder and file is called eraser.png under the variable undo1
    screen.blit(eraser,[104,120])#blits the picture in the coordinates(26,40)
    
    draw.rect(screen,GREEN,circleRect,2)#draws a rectangle at the screen, colour is green and paramters arw within "circleRect", and size is 2
    circle=image.load("images/tools/circle.png")#loading an image inside the tools folder and file is called circle.png under the variable circle
    screen.blit(circle,[26,205])#blits the picture in the coordinates(26,205)
    
    draw.rect(screen,GREEN,brushRect,2)#draws a rectangle at the screen, colour is green and paramters arw within "brushRect", and size is 2
    brush=image.load("images/tools/brush.png")#loading an image inside the tools folder and file is called brush.png under the variable brush
    screen.blit(brush,[104,205])#blits the picture in the coordinates(104,205)
    
    draw.rect(screen,GREEN,rectangleRect,2)#draws a rectangle at the screen, colour is green and paramters arw within "rectangleRect", and size is 2
    rectangle=image.load("images/tools/rectangle.png")#loading an image inside the tools folder and file is called rectangle.png under the variable rectangle
    screen.blit(rectangle,[26,305])#blits the picture in the coordinates(26,305)
    
     
    draw.rect(screen,GREEN,saveRect,2)#draws a rectangle at the screen, colour is green and paramters arw within "saveRect", and size is 2
    save=image.load("images/tools/save.png")#loading an image inside the tools folder and file is called save.png under the variable save
    screen.blit(save,[26,505])#blits the picture in the coordinates(26,505)
    
     
    draw.rect(screen,GREEN,lineRect,2)#draws a rectangle at the screen, colour is green and paramters arw within "lineRect", and size is 2
    line=image.load("images/tools/line.png")#loading an image inside the tools folder and file is called line.png under the variable save
    screen.blit(line,[104,305])#blits the picture in the coordinates(104,305)
    
    draw.rect(screen,GREEN,openRect,2)#draws a rectangle at the screen, colour is green and paramters arw within "openRect", and size is 2
    open=image.load("images/tools/open.png")#loading an image inside the tools folder and file is called open.png under the variable open
    screen.blit(open,[104,505])#blits the picture in the coordinates(104,505)

    draw.rect(screen,GREEN,fillRect,2)#draws a rectangle at the screen, colour is green and paramters arw within "fillRect", and size is 2
    fill=image.load("images/tools/fill.png")#loading an image inside the tools folder and file is called fill.png under the variable fill
    screen.blit(fill,[24,403])#blits the picture in the coordinates(24,403)   

    draw.rect(screen,GREEN,highlighterRect,2)#draws a rectangle at the screen, colour is green and paramters arw within "highlighterRect", and size is 2
    spray=image.load("images/tools/spray.png")#loading an image inside the tools folder and file is called spray.png under the variable spray
    screen.blit(spray,[104,404])#blits the picture in the coordinates(104,404)
    
    draw.rect(screen,RED,canvasRect,2)#draws a rectangle at the screen, colour is green and paramters arw within "canvasRect", and size is 2
    draw.rect(screen,BLUE,paletteRect,2)#draws a rectangle at the screen, colour is green and paramters arw within "paletteRect", and size is 2
    
    draw.rect(screen,YELLOW,frameRect,2)#draws a rectangle at the screen, colour is green and paramters arw within "frameRect", and size is 2
    draw.rect(screen,GREEN,stamp1Rect,2)#draws a rectangle at the screen, colour is green and paramters arw within "stamp1Rect", and size is 2
    stamp1=image.load("images/stamp/warrior.png")#loading an image inside the tools folder and file is called warrior.png under the variable stamp1
    screen.blit(stamp1,[27,606])#blits the picture in the coordinates(27,606)

    draw.rect(screen,GREEN,stamp2Rect,2)#draws a rectangle at the screen, colour is green and paramters arw within "undoRect", and size is 2
    stamp2=image.load("images/stamp/Riot.png")#loading an image inside the tools folder and file is called Riot.png under the variable stamp2
    screen.blit(stamp2,[78,607])#blits the picture in the coordinates(78,607)
    
    draw.rect(screen,GREEN,stamp3Rect,2)#draws a rectangle at the screen, colour is green and paramters arw within "undoRect", and size is 2
    stamp3=image.load("images/stamp/Tibbers.png")#loading an image inside the tools folder and file is called Tibbers.png under the variable stamp3
    screen.blit(stamp3,[128,606])#blits the picture in the coordinates(128,606)
    
    draw.rect(screen,GREEN,stamp4Rect,2)#draws a rectangle at the screen, colour is green and paramters arw within "stamp4Rect", and size is 2
    stamp4=image.load("images/stamp/Teemo.png")#loading an image inside the stamp folder and file is called Teemo.png under the variable stamp4
    screen.blit(stamp4,[178,606])#blits the picture in the coordinates(178,606)
    
    draw.rect(screen,GREEN,stamp5Rect,2)#draws a rectangle at the screen, colour is green and paramters arw within "undoRect", and size is 2
    stamp5=image.load("images/stamp/Ryze.png")#loading an image inside the stamp folder and file is called Ryze.png under the variable stamp5
    screen.blit(stamp5,[228,606])#blits the picture in the coordinates(228,606)
    
    draw.rect(screen,GREEN,stamp6Rect,2)#draws a rectangle at the screen, colour is green and paramters arw within "undoRect", and size is 2
    stamp6=image.load("images/stamp/Victory.png")#loading an image inside the stamp folder and file is called Victory.png under the variable stamp6
    screen.blit(stamp6,[278,606])#blits the picture in the coordinates(278,606)


    
    #################################Hovering#########################################
    ################if user click on any perticular tool then it draws red rectangle(applied to every tool)################33
    if undoRect.collidepoint(mx,my):
        draw.rect(screen,RED,undoRect,2)
    if redoRect1.collidepoint(mx,my):
        draw.rect(screen,RED,redoRect1,2)
    if pencilRect.collidepoint(mx,my):
        draw.rect(screen,RED,pencilRect,2)
    if eraserRect.collidepoint(mx,my):
        draw.rect(screen,RED,eraserRect,2)
    if circleRect.collidepoint(mx,my):
        draw.rect(screen,RED,circleRect,2)
    if brushRect.collidepoint(mx,my):
        draw.rect(screen,RED,brushRect,2)
    if rectangleRect.collidepoint(mx,my):
        draw.rect(screen,RED,rectangleRect,2) 
    if saveRect.collidepoint(mx,my):
        draw.rect(screen,RED,saveRect,2)
    if highlighterRect.collidepoint(mx,my):
        draw.rect(screen,RED,highlighterRect,2)
    if lineRect.collidepoint(mx,my):
        draw.rect(screen,RED,lineRect,2)
    if openRect.collidepoint(mx,my):
        draw.rect(screen,RED,openRect,2)
    if fillRect.collidepoint(mx,my):
        draw.rect(screen,RED,fillRect,2)
    if playRect1.collidepoint(mx,my):
        draw.rect(screen,RED,playRect1,2)
    if playRect2.collidepoint(mx,my):
        draw.rect(screen,RED,playRect2,2)
    if playRect3.collidepoint(mx,my):
        draw.rect(screen,RED,playRect3,2)
    if stamp1Rect.collidepoint(mx,my):
        draw.rect(screen,RED,stamp1Rect,2)
    if stamp2Rect.collidepoint(mx,my):
        draw.rect(screen,RED,stamp2Rect,2)
    if stamp3Rect.collidepoint(mx,my):
        draw.rect(screen,RED,stamp3Rect,2)
    if stamp4Rect.collidepoint(mx,my):
        draw.rect(screen,RED,stamp4Rect,2)
    if stamp5Rect.collidepoint(mx,my):
        draw.rect(screen,RED,stamp5Rect,2)
    if stamp6Rect.collidepoint(mx,my):
        draw.rect(screen,RED,stamp6Rect,2)

    #selecting the tools
    if mb[0]==1 and pencilRect.collidepoint(mx,my):
        tool="pencil"
        screen.blit(toolstips,[176,6])
        Help3="Hold left click to draw!"
        Help3=comicFont.render(Help3,True,GREEN) 
        screen.blit(Help3,(185,48))
    if mb[0]==1 and eraserRect.collidepoint(mx,my):
        tool="eraser"
        screen.blit(toolstips,[176,6])
        Help4="Hold left click to erase!"
        Help4=comicFont.render(Help4,True,GREEN) 
        screen.blit(Help4,(185,48))
    if mb[0]==1 and circleRect.collidepoint(mx,my):
        tool="circle"
        screen.blit(toolstips,[176,6])
        Help5="Hold to draw circle"
        Help6="Use UP and Down arrow keys"
        Help7="to change fill-unfilled"
        Help5=comicFont.render(Help5,True,GREEN)
        Help6=comicFont.render(Help6,True,GREEN)
        Help7=comicFont.render(Help7,True,GREEN)
        screen.blit(Help5,(185,38))
        screen.blit(Help6,(185,58))
        screen.blit(Help7,(185,78))
    if mb[0]==1 and brushRect.collidepoint(mx,my):
        tool="brush"
        screen.blit(toolstips,[176,6])
        Help8="Hold left click to paint!"
        Help8=comicFont.render(Help8,True,GREEN) 
        screen.blit(Help8,(185,48))
    if mb[0]==1 and rectangleRect.collidepoint(mx,my):
        tool="rectangle"
        screen.blit(toolstips,[176,6])
        Help9="Hold to draw rectangle"
        Help10="Use UP and Down arrow keys"
        Help11="to change fill-unfilled"
        Help9=comicFont.render(Help9,True,GREEN)
        Help10=comicFont.render(Help10,True,GREEN)
        Help11=comicFont.render(Help11,True,GREEN)
        screen.blit(Help9,(185,38))
        screen.blit(Help10,(185,58))
        screen.blit(Help11,(185,78))
    if mb[0]==1 and saveRect.collidepoint(mx,my):
        tool="save"
        screen.blit(toolstips,[176,6])
        Help2="Select a file to save to!"
        Help2=comicFont.render(Help2,True,GREEN) 
        screen.blit(Help2,(190,48))
    if mb[0]==1 and highlighterRect.collidepoint(mx,my):
        tool="highlighter"
        screen.blit(toolstips,[176,6])
        Help12="Hold left click to highlight!"
        Help12=comicFont.render(Help12,True,GREEN) 
        screen.blit(Help12,(185,48))
    if mb[0]==1 and lineRect.collidepoint(mx,my):
        tool="line"
        screen.blit(toolstips,[176,6])
        Help13="Hold to draw line!"
        Help14="Use UP and Down arrow keys"
        Help15="to change thickness"
        Help13=comicFont.render(Help13,True,GREEN)
        Help14=comicFont.render(Help14,True,GREEN)
        Help15=comicFont.render(Help15,True,GREEN)
        screen.blit(Help13,(185,38))
        screen.blit(Help14,(185,58))
        screen.blit(Help15,(185,78))
    if mb[0]==1 and openRect.collidepoint(mx,my):
        tool="fileopen"
        screen.blit(toolstips,[176,6])
        Help1="Open a file to save your work!"
        Help1=comicFont.render(Help1,True,GREEN) 
        screen.blit(Help1,(181,48))
    if mb[0]==1 and fillRect.collidepoint(mx,my):
        tool="Fill"
        screen.blit(toolstips,[176,6])
        Help16="Hold left click to paint!"
        Help16=comicFont.render(Help16,True,GREEN) 
        screen.blit(Help16,(185,48))
        
    if mb[0]==1 and playRect1.collidepoint(mx,my):
        tool="Start Music"
        screen.blit(toolstips,[176,6])
        Help18="Starts music if paused"
        Help19="or stopped"
        Help18=comicFont.render(Help18,True,GREEN)
        Help19=comicFont.render(Help19,True,GREEN)
        screen.blit(Help18,(185,38))
        screen.blit(Help19,(185,58))
    if mb[0]==1 and playRect3.collidepoint(mx,my):
        tool="Pause Music"
        screen.blit(toolstips,[176,6])
        Help20="Pauses current music"
        Help20=comicFont.render(Help20,True,GREEN) 
        screen.blit(Help20,(185,48))
    if mb[0]==1 and playRect2.collidepoint(mx,my):
        tool="Stop Music"
        screen.blit(toolstips,[176,6])
        Help21="Stops current music!"
        Help21=comicFont.render(Help21,True,GREEN) 
        screen.blit(Help21,(185,48))

        
    if mb[0]==1 and stamp1Rect.collidepoint(mx,my):
        tool="warrior"
    if mb[0]==1 and stamp2Rect.collidepoint(mx,my):
        tool="ship"
    if mb[0]==1 and stamp3Rect.collidepoint(mx,my):
        tool="star"
    if mb[0]==1 and stamp4Rect.collidepoint(mx,my):
        tool="ball"
    if mb[0]==1 and stamp5Rect.collidepoint(mx,my):
        tool="face"
    if mb[0]==1 and stamp6Rect.collidepoint(mx,my):
        tool="color"





###################USING THE TOOLS########################################
    if mb[0]==1 and playRect3.collidepoint(mx,my):
        mixer.music.pause()

    if mb[0]==1 and playRect1.collidepoint(mx,my):
        mixer.music.unpause()
        if mixer.music.get_busy()==False:
            mixer.music.play()

    if mb[0]==1 and playRect2.collidepoint(mx,my):
        mixer.music.stop()
        
    if mb[0]==1 and openRect.collidepoint(mx,my):
        try:
            fname=filedialog.askopenfilename()#fname is just a string that has the full path to the selected file
            print(fname)
            mypic=image.load(fname)
            screen.blit(mypic,(100,100))
        except:
            print("load error")

        
    if mb[0]==1 and saveRect.collidepoint(mx,my):
        try:
            fname=filedialog.asksaveasfilename()
            image.save(screen.copy(),fname)
        except:
            print("saving error")
            
    if mb[0]==1 and canvasRect.collidepoint(mx,my):
        screen.set_clip(canvasRect)#only the canvas area can be updated
        if tool=="pencil":
            draw.line(screen,col,(omx,omy),(mx,my))
        if tool=="eraser":
            draw.circle(screen,WHITE,(mx,my),10)
        if tool=="brush":
            dx=mx-omx#run/width
            dy=my-omy#rise/height
            dist=sqrt(dx**2+dy**2)
            for i in range(1,int(dist)):
                cx=int(omx+i*dx/dist)
                cy=int(omy+i*dy/dist)
                draw.circle(screen,col,(cx,cy),10)

                    
        if tool=="warrior":
            if click:
                screen.blit(stamp1,(mx,my))

        if tool=="ship":
            if click:
                screen.blit(stamp2,(mx,my))

        if tool=="star":
            if click:
                screen.blit(stamp3,(mx,my))

        if tool=="ball":
            if click:
                screen.blit(stamp4,(mx,my))

        if tool=="face":
            if click:
                screen.blit(stamp5,(mx,my))

        if tool=="color":
            if click:
                screen.blit(stamp6,(mx-15,my-20))

        if tool=="line":
            lining = True
            linethick=1 # default line thickness
            while lining:
                        event.get()
                        nb = mouse.get_pressed()
                        nx, ny = mouse.get_pos()
                        keys = key.get_pressed()
                        copy = screen.copy()
                                                
                        if keys[K_UP]:
                                linethick+=1
                                if linethick > 10:
                                        linethick = 10
                        if keys[K_DOWN]:
                                linethick-=1
                                if linethick <1:
                                        linethick = 0

                        
                        display.flip()
                        screen.blit(line, (0, 0))
                        line = screen.copy()
                        
                        if nb[0] == 0:
                                lining = False
                        event.get()
                        nx, ny = mouse.get_pos()
                        draw.line (screen, (col), (mx, my), (nx, ny), linethick)

        if tool=="circle":
            lining = True
            linethick=1
            while lining:
                        event.get()
                        nb = mouse.get_pressed()
                        nx, ny = mouse.get_pos()
                        keys = key.get_pressed()
                        dist = math.sqrt((mx - nx)**2 + (my - ny)**2)
                        radius=int(dist)
                        copy = screen.copy()
                        if radius>1:
                            copy = screen.copy()
                            draw.circle(screen, col,(mx, my),radius,linethick)

                            if keys[K_UP]: # if up arrow key is pressed during draw then line thickness will change
                                    linethick+=1
                                    if linethick > 10:
                                            linethick = 10
                                            draw.circle(screen, col,(mx, my),radius,linethick)
                            if keys[K_DOWN]: # if down arrow key is pressed during draw then circle will be full filled with colour
                                    linethick-=1
                                    if linethick <1:
                                            linethick = 0
                                            draw.circle(screen, col,(mx, my),radius,linethick)
                            

                        
                        display.flip()# It allows only a portion of the screen to updated, instead of the entire area.
                                      # If no argument is passed it updates the entire Surface area like pygame.
                                      
                        screen.blit(copy, (0, 0))# It is a thin wrapper around a Pygame surface that allows you to easily draw images to the screen (“blit” them)
                                                 # blit() accepts either a Surface or a string as its image parameter.
                                                 # If image is a str then the named image will be loaded from the images/ directory.
                                                 
                        copy = screen.copy()
                        
                        if nb[0] == 0:
                                lining = False
                                draw.circle(screen,col,(mx, my),radius,linethick)
                                
                        event.get()
                        nx, ny = mouse.get_pos()
                        
        if tool=="highlighter":
            if mx!=omx or my!=omy:#moving the mouse
                if mb[0]==1:
##                    draw.circle(brushHead,(col),(10,10),10)
                    screen.blit(brushHead,(mx-10,my-10))

        if tool=="rectangle":
            drawing = True
            linethick=1
            while drawing:
                        event.get()
                        nb = mouse.get_pressed()
                        nx, ny = mouse.get_pos()
                        keys = key.get_pressed()
                        width= nx-mx
                        height=ny-my
                        copy = screen.copy()
                        draw.rect(screen,col,(mx, my,width,height),linethick)
                        if keys[K_UP]:
                                linethick+=1
                                if linethick > 10:
                                        linethick = 10
                        if keys[K_DOWN]:
                                linethick-=1
                                if linethick <1:
                                        linethick = 0
                            
                        
                        display.flip()
                        screen.blit(copy,(0, 0))
                        copy = screen.copy()
                        
                        if nb[0] == 0:
                                drawing = False
                                draw.rect(screen,col,(mx, my,width,height),linethick)
                                
                        event.get()
                        nx, ny = mouse.get_pos()

                        
        if tool=="Fill":
            screen.fill(col)
                                                
##        if tool=="Start Music":
##            if click:
##                    mixer.music.play(-1) # play the music again and again                                     
##        if tool=="Stop Music":
##            pygame.mixer.music.play.stop()
                        
                        
                        
        
    screen.set_clip(None)       

    print(tool) # it is only for the programmer to track the tools

    #select (change) colour with mouse position
    if mb[0]==1 and paletteRect.collidepoint(mx,my):
        col=screen.get_at((mx,my))
    if mb[0]==1 and colorwheelRect.collidepoint(mx,my):
        col=screen.get_at((mx,my))
    draw.rect(screen,col,(1025,545,70,70))


    display.flip()
    omx,omy=mx,my
    click=False
    

quit()
