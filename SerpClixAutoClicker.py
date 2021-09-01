#SerpClix Auto Clicker Version 1.0.5
#Functions: Clicks all offer types and completes them except for images (W.I.P) and map offers(auto deletes)
#Changelogs: BUG FIXES, DELETE ALL MAPS/IMAGES OFFERS, clicks captchas(only the checkmark box ones)
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#Instructions: Fill in the variables below 
#{~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~FILL BELOW~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~}

#Note: ALSO NEED TO MODIFY THE X AND Y (SCROLL DOWN TO SEE WHERE) (LINKCLICK + PASSWORD)


#coords for first task: X:982 Y:270 (anywhere x,y coordinate that can click the very first task that appears)
firstTaskX = 982
firstTaskY = 270


#page down arrow (1909, 1018) (this is the down arrow that you click to make page go down)
pageDownX = 1909
pageDownY = 1018

#page all the way down ( drags the slider all the way down) (cords are the top of slider bar)
pageADownTopX = 1905
pageADownTopY = 173
pageADownBotX = 1905
pageADownBotY = 1020

#search ommitted results (scroll all the way down when you see the ommitted results for searches)
omittedResultsX = 748
omittedResultsY = 730

#omitted videos     (scroll all the way down for ommitted results for videos)
omittedVideosX = 593
omittedVideosY = 783

#remove offer button 
removeOfferX = 1755
removeOfferY = 265


#coords for status icon ( the extension box, top right 'ok, go')X:1814 Y:73
statusX = 1814
statusY = 73


#scan for pink area 
pinkAreaScanX = 930
pinkAreaScanY = 410

#reset login button clicks
clickExtensionIconX = 1814
clickExtensionIconY = 73
clickPassX = 1595
clickPassY = 261
clickLoginX = 1593
clickLoginY = 317

#ALL THE COLORS USED  

#orange 'Go' icon color
#(255,165,0)
orangeR = 255
orangeG = 165
orangeB = 0

#blue search color
# (180,216,255)
blueR = 180
blueG = 216
blueB = 255

#grey URL color
#(240,240,240)
greyRGB = 240

#green map color
#(220, 248, 207)
greenR = 220
greenG = 248
greenB = 207

#red search color
#(255, 215, 215)
redR = 255
redG = 215
redB = 215

#reset page 
resetPageCheckOrangeX = 599
resetPageCheckOrangeY = 919
resetOrangeR = 255
resetOrangeG = 212
resetOrangeB = 79



#ur serpclix password, make extra variables if its more letters, mine is 8 chracters so you do you. . 
pass1 = ''
pass2 = ''
pass3 = ''
pass4 = ''
pass5 = ''
pass6 = ''
pass7 = ''
pass8 = ''

#google image button
imageX =1684
imageY = 178

#CAPTCHA
captchaX = 373
captchaY = 254
#the captcha blue color, top right most color of the three colors in the symbol
captchaColorR = 27
captchaColorG = 60
captchaColorB = 168



#[~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~IGNORE BELOW~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Clicks location at x,y
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1) #This pauses the script for 0.1 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


#clicks the very first offer
def clickFirstJob():
    pyautogui.moveTo(firstTaskX , firstTaskY , 0.5)
    click(firstTaskX ,firstTaskY )

#pastes and searches job')
def pasteSearch():
    pyautogui.hotkey('ctrl','v')
    sleep(1)
    pyautogui.hotkey('enter')
    captcha()


#Moves mouse to down click arrow
def pageDown():
    click(pageDownX, pageDownY)
    sleep(0.20)

#page all the way down
def pageADown():
    pyautogui.moveTo(pageADownTopX ,pageADownTopY )
    sleep(0.5)
    pyautogui.dragTo(pageADownBotX , pageADownBotY , 1.5, button= 'left')

#page all the way up
def pageAUp():
    for i in range(26):
        pyautogui.keyDown('pageup')
        sleep(0.01)
        pyautogui.keyUp('pageup')


#look at omitted results
def omittedResults():
    click(omittedResultsX ,omittedResultsY )

#look at omitted results
def omittedVideos():
    click(omittedVideosX,omittedVideosY)

#close tab
def closeTab():
    pyautogui.hotkey('ctrl', 'w')

#delete offer
def removeOffer():
    if pyautogui.pixelMatchesColor(clickExtensionIconX, clickExtensionIconY, (orangeR ,orangeG ,orangeB ), tolerance = 20) == False:
        closeTab()
        sleep(2)
        pyautogui.moveTo(removeOfferX,removeOfferY)
        click(removeOfferX, removeOfferY)
        sleep(1)
        pyautogui.hotkey('enter')
        sleep(1)




#search function until status is ok
def search():
    sleep(2)
    i = 0
    while (pyautogui.pixelMatchesColor(statusX , statusY , (255,165,0), tolerance = 30) == False):
        captcha()
        pyautogui.keyDown('n')
        sleep(0.01)
        pyautogui.keyUp('n')
        sleep(4)
        pageADown()
        omittedResults()
        i = i + 1
        if i == 6:
            break
        sleep(4)
        pageAUp()


#video search function until status is ok
def vidSearch():
    sleep(2)
    i = 0
    while (pyautogui.pixelMatchesColor(statusX, statusY, (255,165,0), tolerance = 30) == False):
        captcha()
        pyautogui.keyDown('n')
        sleep(0.01)
        pyautogui.keyUp('n')
        sleep(4)
        pageADown()
        omittedVideos()
        i = i + 1
        if i == 6:
            break
        sleep(4)
        pageAUp()    
#image search
def imageSearch():
    sleep(2)
    i = 0
    while (pyautogui.pixelMatchesColor(statusX, statusY, (255,165,0), tolerance = 30) == False):
        sleep(2)
        pyautogui.keyDown('pagedown')
        sleep(0.01)
        pyautogui.keyUp('pagedown')        
        i = i + 1
        if i == 15:
            break
    pageAUp()
#scans page for pink
def scan():
    sleep(1)
    while (pyautogui.pixelMatchesColor(pinkAreaScanX, pinkAreaScanY, (255,135,135), tolerance = 10)== False):
        pageDown()

        
#scans and clicks the image
def imageScan():
    while (pyautogui.pixelMatchesColor(statusX, statusY, (255,165,0), tolerance = 30) == True):
        im = pyautogui.locateOnScreen('green1.png')
        center = pyautogui.center(im)
        click(center.x,center.y)
    
#RECAPTCHA
def captcha():
    if pyautogui.pixelMatchesColor(captchaX, captchaY, (captchaColorR, captchaColorG, captchaColorB)) == True:
        click(69,273)
        sleep(1)
        print("captcha clicked")
        
    

        
# NEED TO MODIFY THE X AND Y HERE ~~~~~~~!!!!!!!!!!!!!!!!!!!!!!!!!
# NEED TO MODIFY THE X AND Y HERE ~~~~~~~!!!!!!!!!!!!!!!!!!!!!!!!!
# NEED TO MODIFY THE X AND Y HERE ~~~~~~~!!!!!!!!!!!!!!!!!!!!!!!!!
# NEED TO MODIFY THE X AND Y HERE ~~~~~~~!!!!!!!!!!!!!!!!!!!!!!!!!
# NEED TO MODIFY THE X AND Y HERE ~~~~~~~!!!!!!!!!!!!!!!!!!!!!!!!!
# NEED TO MODIFY THE X AND Y HERE ~~~~~~~!!!!!!!!!!!!!!!!!!!!!!!!!
# NEED TO MODIFY THE X AND Y HERE ~~~~~~~!!!!!!!!!!!!!!!!!!!!!!!!!
# NEED TO MODIFY THE X AND Y HERE ~~~~~~~!!!!!!!!!!!!!!!!!!!!!!!!!
# NEED TO MODIFY THE X AND Y HERE ~~~~~~~!!!!!!!!!!!!!!!!!!!!!!!!!
# NEED TO MODIFY THE X AND Y HERE ~~~~~~~!!!!!!!!!!!!!!!!!!!!!!!!!

#clicks the found link
def linkClick():
    click(235,400)
    sleep(0.01)
    click(235,405)
    sleep(0.01)
    click(235,410)
    sleep(0.01)
    click(235,415)
    sleep(0.01)
    click(235,420)
    sleep(0.01)
    click(235,425)
    sleep(0.01)
    click(235,430)
    sleep(0.01)
    click(235,435)
    sleep(0.01)
    click(235,440)
    sleep(0.01)
    click(235,445)
    sleep(0.01)
    click(235,450)
    sleep(0.01)
    

#ADD TO UR PASSWORD TO CLICK MORE LETTERS
#click and login
def resetLogin():
##   X: 1814 Y:73
    sleep(1)
    click(clickExtensionIconX,clickExtensionIconY)
    sleep(1)
    click(clickPassX,clickPassY)
    sleep(0.5)
    pyautogui.press(pass1)
    sleep(0.05)
    pyautogui.press(pass2)
    sleep(0.05)
    pyautogui.press(pass3)
    sleep(0.05)
    pyautogui.press(pass4)
    sleep(0.05)
    pyautogui.press(pass5)
    sleep(0.05)
    pyautogui.press(pass6)
    sleep(0.05)
    pyautogui.press(pass7)
    sleep(0.05)
    pyautogui.press(pass8)
    sleep(0.05)
    click(clickLoginX,clickLoginY)




#MAIN FUNCTION        checks color of pixel and proceeds accordingly
def colorCheck():
    sleep(1)
    #check if blue
    if pyautogui.pixelMatchesColor(firstTaskX , firstTaskY , (blueR,blueG,blueB), tolerance = 20):
        #opens offer and clicks 
        clickFirstJob()
        print("search offer clicked. . .")
        sleep(2)
        pasteSearch()
        sleep(2)
        #starts searching
        search()
        sleep(1)
        if pyautogui.pixelMatchesColor(clickExtensionIconX , clickExtensionIconY , (orangeR ,orangeG ,orangeB ), tolerance = 20) == True:
            #scans page
            scan()
            sleep(1)
            #clicks
            linkClick()
            sleep(100)
            print("Search offer clicked. . .")
        else:
            print("Offer not found. . . Removing. . . ")
            removeOffer()
            sleep(1)
            
        
    #check if grey 
    if pyautogui.pixelMatchesColor(firstTaskX , firstTaskY , (greyRGB ,greyRGB ,greyRGB )):
        print("URL offer clicked. . .")
        clickFirstJob()
        sleep(95)
        
    #check if green 
    if pyautogui.pixelMatchesColor(firstTaskX , firstTaskY , (greenR, greenG, greenB), tolerance = 20):
        clickFirstJob()
        sleep(1)
        sleep(1)
        removeOffer()
        print("Map offer not found. . . Removing. . . ")
        sleep(1)
        
        
    #check if red 
    if pyautogui.pixelMatchesColor(firstTaskX , firstTaskY , (redR, redG, redB), tolerance = 5):
        print('clicked red')
        clickFirstJob()
        sleep(2)
        pyautogui.hotkey('enter')
        sleep(2)
        pasteSearch()
        sleep(1)
        vidSearch()
        sleep(1)
        #scans page
        if pyautogui.pixelMatchesColor(clickExtensionIconX, clickExtensionIconY, (orangeR ,orangeG ,orangeB ), tolerance = 20) == True:
            #scans page
            scan()
            sleep(1)
            #clicks
            linkClick()
            print("Video offer clicked. . .")
            sleep(100)
        else:
            print("Offer not found. . . Removing. . . ")
            removeOffer()
            sleep(1)



    #check if need to reset page
    if pyautogui.pixelMatchesColor(resetPageCheckOrangeX, resetPageCheckOrangeY, (resetOrangeR, resetOrangeG, resetOrangeB))== True:
        sleep(1)
        resetLogin()
        print("Login reset")

    #checks for image offer
    if pyautogui.pixelMatchesColor(firstTaskX , firstTaskY , (244, 234, 216), tolerance = 5):
        clickFirstJob()
        sleep(1)
        sleep(1)
        removeOffer()
        print("Image offer not found. . . Removing. . . ")
        sleep(1)

x = 0
while x != 1:
    colorCheck()

