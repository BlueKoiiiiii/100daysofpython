import pygame
import win32api
import win32con
import win32gui
import pyautogui
import time
import spritesheet
import tkinter as tk
import random
import sys


pygame.init()
info = pygame.display.Info()
w = info.current_w
h = info.current_h
screen = pygame.display.set_mode((w, h), pygame.NOFRAME) # For borderless, use pygame.NOFRAME
done = False
stop = False
first_time = True
mouseclick = False
stasis = False
fuchsia = (255, 0, 128)  # Transparency color
dark_red = (255, 100, 0)
dark_orange = (255, 255, 0)
clicked = 1
display_width = 1920
display_height = 1080
frame = 0
frame2 = 0
task = False
X = -200
RunAnim = True
triggered = False
enterfinished = False
mouseclickcount = 1
runAnim = False
msgdone = False
secondmsg = False
thirdmsg = False
fourthmsg = False
fifthmsg = False
firstmsg = False
sixthmsg = False
seventhmsg = False
eigthmsg = False
ninthmsg = False
finished = False

# x = (display_width *0.45)
# y = (display_height *0.8)
gameDisplay = pygame.display.set_mode((display_width,display_height))
sprite_sheet = pygame.image.load('Fox Sprite Sheet(1).png').convert_alpha()
# msg_sprite_sheet = pygame.image.load('image(1).png').convert_alpha()
# sprite_sheet2 = spritesheet.SpriteSheet(msg_sprite_sheet)
clickeded = False
smallfont = pygame.font.SysFont('Corbel',35)
WHITE = (255,255,255)
text = smallfont.render('quit' , True , WHITE)
# stores the width of the
# screen into a variable
width = screen.get_width()

# stores the height of the
# screen into a variable
height = screen.get_height()



# idleAnim = [pygame.image.load('Fox Sprite Sheet_1.png'), pygame.image.load('Fox Sprite Sheet_2.png'), pygame.image.load('Fox Sprite Sheet_3.png'), pygame.image.load('Fox Sprite Sheet_4.png'), ]


# Create layered window
hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
# Set window transparency color
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchsia), 0, win32con.LWA_COLORKEY)
# font = pygame.font.SysFont("Arial", 72)
# text = []
# text.append((font.render("Invisible background", 0, dark_red), (0, 10)))
# text.append((font.render("Press Esc to close the window", 0, dark_red), (0, 100)))
# Create functions


def get_image(sheet, frame, width, height, scale):
    image = pygame.Surface((width , height)).convert_alpha()
    image.blit(sheet, (0,-104), ((frame*width), 5 ,width, height))
    image = pygame.transform.scale(image, (width*scale, height*scale))
    image.set_colorkey((0,0,0))
    return image

def get_image2(sheet, frame, width, height, scale):
    image = pygame.Surface((width,height)).convert_alpha()
    image.blit(sheet, (0,0), ((frame*width), 5 ,width, height))
    image = pygame.transform.scale(image, (width*scale, height*scale))
    image.set_colorkey((0,0,0))
    return image

def get_image3(sheet, frame, width, height, scale):
    image = pygame.Surface((width,height)).convert_alpha()
    image.blit(sheet, (0,-204), ((frame*width), 5 ,width, height))
    image = pygame.transform.scale(image, (width*scale, height*scale))
    image.set_colorkey((0,0,0))
    return image

def get_image4(sheet, frame, width, height, scale):
    image = pygame.Surface((width,height)).convert_alpha()
    image.blit(sheet, (0, 0), ((frame*width), 254 , width, height))
    image = pygame.transform.scale(image, (width*scale, height*scale))
    image.set_colorkey((0,0,0))
    return image

def get_image5(sheet, frame, width, height, scale):
    image = pygame.Surface((width,height)).convert_alpha()
    image.blit(sheet, (0, 0), ((frame*width), 438 , width, height))
    image = pygame.transform.scale(image, (width*scale, height*scale))
    image.set_colorkey((0,0,0))
    return image

def get_image6(sheet, frame, width, height, scale):
    image = pygame.Surface((width,height)).convert_alpha()
    image.blit(sheet, (0, 0), ((frame*width), 622 , width, height))
    image = pygame.transform.scale(image, (width*scale, height*scale))
    image.set_colorkey((0,0,0))
    return image

def get_image7 (sheet, frame, width, height, scale):
    image = pygame.Surface((width,height)).convert_alpha()
    image.blit(sheet, (0, 0), ((frame*width), 806 , width, height))
    image = pygame.transform.scale(image, (width*scale, height*scale))
    image.set_colorkey((0,0,0))
    return image

def get_image8 (sheet, frame, width, height, scale):
    image = pygame.Surface((width,height)).convert_alpha()
    image.blit(sheet, (0, 0), ((frame*width), 1016 , width, height))
    image = pygame.transform.scale(image, (width*scale, height*scale))
    image.set_colorkey((0,0,0))
    return image

def get_image9 (sheet, frame, width, height, scale):
    image = pygame.Surface((width,height)).convert_alpha()
    image.blit(sheet, (0, 0), ((frame*width), 1236 , width, height))
    image = pygame.transform.scale(image, (width*scale, height*scale))
    image.set_colorkey((0,0,0))
    return image

def get_image10 (sheet, frame, width, height, scale):
    image = pygame.Surface((width,height)).convert_alpha()
    image.blit(sheet, (0, 0), ((frame*width), 1438 , width, height))
    image = pygame.transform.scale(image, (width*scale, height*scale))
    image.set_colorkey((0,0,0))
    return image

def get_image11 (sheet, frame, width, height, scale):
    image = pygame.Surface((width,height)).convert_alpha()
    image.blit(sheet, (0, 0), ((frame*width), 1651 , width, height))
    image = pygame.transform.scale(image, (width*scale, height*scale))
    image.set_colorkey((0,0,0))
    return image

def get_image12 (sheet, frame, width, height, scale):
    image = pygame.Surface((width,height)).convert_alpha()
    image.blit(sheet, (0, 0), ((frame*width), 1842 , width, height))
    image = pygame.transform.scale(image, (width*scale, height*scale))
    image.set_colorkey((0,0,0))
    return image

def get_image13 (sheet, frame, width, height, scale):
    image = pygame.Surface((width,height)).convert_alpha()
    image.blit(sheet, (0, 0), ((frame*width), 2027 , width, height))
    image = pygame.transform.scale(image, (width*scale, height*scale))
    image.set_colorkey((0,0,0))
    return image

def get_image14 (sheet, frame, width, height, scale):
    image = pygame.Surface((width,height)).convert_alpha()
    image.blit(sheet, (0, 0), ((frame*width), 2233 , width, height))
    image = pygame.transform.scale(image, (width*scale, height*scale))
    image.set_colorkey((0,0,0))
    return image

def get_image15 (sheet, frame, width, height, scale):
    image = pygame.Surface((width,height)).convert_alpha()
    image.blit(sheet, (0, 0), ((frame*width), 2444 , width, height))
    image = pygame.transform.scale(image, (width*scale, height*scale))
    image.set_colorkey((0,0,0))
    return image

def get_image16 (sheet, frame, width, height, scale):
    image = pygame.Surface((width,height)).convert_alpha()
    image.blit(sheet, (0, 0), ((frame*width), 2657 , width, height))
    image = pygame.transform.scale(image, (width*scale, height*scale))
    image.set_colorkey((0,0,0))
    return image

def get_image17 (sheet, frame, width, height, scale):
    image = pygame.Surface((width,height)).convert_alpha()
    image.blit(sheet, (0, 0), ((frame*width), 2854 , width, height))
    image = pygame.transform.scale(image, (width*scale, height*scale))
    image.set_colorkey((0,0,0))
    return image

def get_image18 (sheet, frame, width, height, scale):
    image = pygame.Surface((width,height)).convert_alpha()
    image.blit(sheet, (0, 0), ((frame*width), 3036 , width, height))
    image = pygame.transform.scale(image, (width*scale, height*scale))
    image.set_colorkey((0,0,0))
    return image

def get_image19 (sheet, frame, width, height, scale):
    image = pygame.Surface((width,height)).convert_alpha()
    image.blit(sheet, (0, 0), ((frame*width), 3233 , width, height))
    image = pygame.transform.scale(image, (width*scale, height*scale))
    image.set_colorkey((0,0,0))
    return image

def get_image20 (sheet, frame, width, height, scale):
    image = pygame.Surface((width,height)).convert_alpha()
    image.blit(sheet, (0, 0), ((frame*width), 3419 , width, height))
    image = pygame.transform.scale(image, (width*scale, height*scale))
    image.set_colorkey((0,0,0))
    return image

def get_image21 (sheet, frame, width, height, scale):
    image = pygame.Surface((width,height)).convert_alpha()
    image.blit(sheet, (0, 0), ((frame*width), 3628 , width, height))
    image = pygame.transform.scale(image, (width*scale, height*scale))
    image.set_colorkey((0,0,0))
    return image

def get_image22 (sheet, frame, width, height, scale):
    image = pygame.Surface((width,height)).convert_alpha()
    image.blit(sheet, (0, 0), ((frame*width), 3826 , width, height))
    image = pygame.transform.scale(image, (width*scale, height*scale))
    image.set_colorkey((0,0,0))
    return image

def get_image23 (sheet, frame, width, height, scale):
    image = pygame.Surface((width,height)).convert_alpha()
    image.blit(sheet, (0, 0), ((frame*width), 4060 , width, height))
    image = pygame.transform.scale(image, (width*scale, height*scale))
    image.set_colorkey((0,0,0))
    return image

import tkinter as tk






window = tk.Tk()
window.title("To-Do List")
window.geometry('300x275')
window.minsize(300, 275)
window.maxsize(1920, 1080)




# frame_0 = get_image4(sprite_sheet2,0, 32,32,5)
# frame_1 = get_image(sprite_sheet,1, 32,32,5)

enter_animationlist = []
idle_animationlist = []
clicked_animationlist=[]
msg_animationlist = []
sixthidleanimationlist = []
idlemsganimationlist = []
secondmsganimationlist = []
idlesecondmsganimationlist = []
thirdmsganimationlist = []
idlethirdmsganimationlist = []
fourthmsganimationlist = []
idlefourthanimationlist = []
idlefifthanimationlist = []
fifthanimationlist = []
fifthsecondanimationlist = []
seventhanimationlist = []
seventhidleanimationlist = []
sixthanimationlist = []
eigthanimationlist= []
eigthsecondanimationlist = []
eigthidleanimationlist = []
animation_steps = 11
eigthanimation_steps = 15
eigthsecondanimation_steps = 8
eigthidleanimation_steps = 3
idleanimation_steps = 4
sixthidleanimation_steps = 3
sixthanimation_steps = 12
clickedanimation_steps = 7
msganimation_steps = 4
seventhanimation_steps = 13
seventhidleanimation_steps = 3
idlemsganimation_steps = 3
secondmsganimation_steps = 12
thirdmsganimation_steps = 16
fourthmsganimation_steps = 19
fifthmsganimation_steps = 19
fifthsecondmsganimation_steps = 16
idlethirdmsganimation_steps = 3
idlesecondmsganimation_steps = 3
idlefourthmsganimation_steps = 3
idlefifthmsganimation_steps = 3
last_update = pygame.time.get_ticks()
last_update2 = pygame.time.get_ticks()
animation_cooldown = 120
msganimation_cooldown = 450

for x in range (eigthanimation_steps):
        eigthanimationlist.append(get_image22(sprite_sheet, x, 274, 141, 2))

for x in range (eigthsecondanimation_steps):
        eigthsecondanimationlist.append(get_image20(sprite_sheet, x, 274, 141, 2))

for x in range (eigthidleanimation_steps):
        eigthidleanimationlist.append(get_image23(sprite_sheet, x, 274, 141, 2))

for x in range (seventhanimation_steps):
        seventhanimationlist.append(get_image17(sprite_sheet, x, 274, 141, 2))

for x in range (seventhidleanimation_steps):
        seventhidleanimationlist.append(get_image18(sprite_sheet, x, 274, 141, 2))

for x in range (fifthmsganimation_steps):
        fifthanimationlist.append(get_image12(sprite_sheet, x, 274, 141, 2))

for x in range (fifthsecondmsganimation_steps):
        fifthsecondanimationlist.append(get_image13(sprite_sheet, x, 274, 141, 2))

for x in range (idlefifthmsganimation_steps):
        idlefifthanimationlist.append(get_image14(sprite_sheet, x, 274, 141, 2))

for x in range(msganimation_steps):
        msg_animationlist.append(get_image4(sprite_sheet, x, 274, 141, 2))

for x in range (sixthanimation_steps):
        sixthanimationlist.append(get_image15(sprite_sheet, x, 274, 141, 2))

for x in range (sixthidleanimation_steps):
        sixthidleanimationlist.append(get_image16(sprite_sheet, x, 274, 141, 2))

for x in range(secondmsganimation_steps):
        secondmsganimationlist.append(get_image6(sprite_sheet, x, 274, 141, 2))

for x in range (thirdmsganimation_steps):
        thirdmsganimationlist.append(get_image8(sprite_sheet, x , 274, 141, 2))

for x in range (idlethirdmsganimation_steps):
        idlethirdmsganimationlist.append(get_image9(sprite_sheet, x, 274, 141, 2))

for x in range (idlesecondmsganimation_steps):
        idlesecondmsganimationlist.append(get_image7(sprite_sheet, x, 274, 141, 2))

for x in range (fourthmsganimation_steps):
        fourthmsganimationlist.append(get_image10(sprite_sheet, x, 274, 141, 2))

for x in range (idlefourthmsganimation_steps):
        idlefourthanimationlist.append(get_image11(sprite_sheet, x, 274, 141, 2))

for x in range (idlemsganimation_steps):
        idlemsganimationlist.append(get_image5(sprite_sheet, x, 274, 141, 2))

for x in range(animation_steps):
        enter_animationlist.append(get_image(sprite_sheet, x, 32, 128, 8))

for x in range(idleanimation_steps):
        idle_animationlist.append(get_image2(sprite_sheet, x, 32, 32, 8))

for z in range(clickedanimation_steps):
        clicked_animationlist.append(get_image3(sprite_sheet, z, 32, 228, 8))
#


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     mouseclickcount += 1
        #     time.sleep(0.1)

    screen.fill(fuchsia)  # Transparent background
    # pygame.image.load("index.png")
    left, middle, right = pygame.mouse.get_pressed()
    # print(x)
    # print(y)

    time.sleep((8/1000))

    # if left:
    #     clicked += 1
    #     time.sleep(0.1)
    # if stasis:
    #     y += 850
    # else:
    x, y = pyautogui.position()
    positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
    print(y)


# if y > 800:
    triggered = True
    if RunAnim:
        current_time = pygame.time.get_ticks()
        if current_time - last_update >= animation_cooldown:
            frame += 1
            X += 50
            last_update = current_time
        if frame >= len(enter_animationlist):
            frame = 0
            RunAnim = False
            enterfinished = True
        screen.blit(enter_animationlist[frame], (X, 800))

    # enterfinished = True
    if enterfinished:
            current_time = pygame.time.get_ticks()
            if current_time - last_update >= animation_cooldown:
                frame += 1
                frame2 += 1
                last_update = current_time
            if frame2 >= len(idle_animationlist):
                frame2 = 0
            if not msgdone:
                if frame >= len(msg_animationlist):
                    frame = 0
                    msgdone = True
                screen.blit(msg_animationlist[frame], (500, 500))
            else:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    enterfinished = False
                    secondmsg = True
                    msgdone = False
                if frame >= len(idlemsganimationlist):
                    frame = 0
                screen.blit(idlemsganimationlist[frame], (500, 500))
            screen.blit(idle_animationlist[frame2], (350, 740))

    if secondmsg:
        current_time = pygame.time.get_ticks()
        if current_time - last_update >= animation_cooldown:
            frame += 1
            frame2 += 1
            last_update = current_time
        if frame2 >= len(idle_animationlist):
            frame2 = 0
        if not msgdone:
            if frame >= len(secondmsganimationlist):
                frame = 0
                msgdone = True
            screen.blit(secondmsganimationlist[frame], (500, 500))
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                enterfinished = False
                secondmsg = False
                thirdmsg = True
                msgdone = False
            if frame >= len(idlemsganimationlist):
                frame = 0
            screen.blit(idlesecondmsganimationlist[frame], (500, 500))
        screen.blit(idle_animationlist[frame2], (350, 740))
            # print(frame)
    # screen.blit(sprite_sheet, (300,800))

    if thirdmsg:
            current_time = pygame.time.get_ticks()
            if current_time - last_update >= animation_cooldown:
                frame += 1
                frame2 += 1
                last_update = current_time
            if frame2 >= len(idle_animationlist):
                frame2 = 0
            if not msgdone:
                if frame >= len(thirdmsganimationlist):
                    frame = 0
                    msgdone = True
                screen.blit(thirdmsganimationlist[frame], (500, 500))
            else:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    enterfinished = False
                    secondmsg = False
                    thirdmsg = False
                    fourthmsg = True
                    msgdone = False
                if frame >= len(idlemsganimationlist):
                    frame = 0
                screen.blit(idlethirdmsganimationlist[frame], (500, 500))
            screen.blit(idle_animationlist[frame2], (350, 740))

    if fourthmsg:
        current_time = pygame.time.get_ticks()
        if current_time - last_update >= animation_cooldown:
            frame += 1
            frame2 += 1
            last_update = current_time
        if frame2 >= len(idle_animationlist):
            frame2 = 0
        if not msgdone:
            if frame >= len(fourthmsganimationlist):
                frame = 0
                msgdone = True
            screen.blit(fourthmsganimationlist[frame], (500, 500))
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                enterfinished = False
                secondmsg = False
                thirdmsg = False
                fourthmsg = False
                fifthmsg = True
                msgdone = False
            if frame >= len(idlemsganimationlist):
                frame = 0
            screen.blit(idlefourthanimationlist[frame], (500, 500))
        screen.blit(idle_animationlist[frame2], (350, 740))

    if fifthmsg:
        current_time = pygame.time.get_ticks()
        if current_time - last_update >= animation_cooldown:
            frame += 1
            frame2 += 1
            last_update = current_time
        if frame2 >= len(idle_animationlist):
            frame2 = 0
        if not msgdone and not firstmsg:
            if frame >= len(fifthanimationlist):
                frame = 0
                firstmsg = True
            screen.blit(fifthanimationlist[frame], (500, 500))
        if firstmsg:
            if frame >= len(fifthsecondanimationlist):
                frame = 0
                msgdone = True
            screen.blit(fifthsecondanimationlist[frame], (500 , 500))
        if msgdone:
            if event.type == pygame.MOUSEBUTTONDOWN:
                enterfinished = False
                secondmsg = False
                thirdmsg = False
                fourthmsg = False
                fifthmsg = False
                sixthmsg = True
                msgdone = False
                firstmsg = False
            if frame >= len(idlemsganimationlist):
                frame = 0
            screen.blit(idlefifthanimationlist[frame], (500, 500))
        screen.blit(idle_animationlist[frame2], (350, 740))

    if sixthmsg:
        current_time = pygame.time.get_ticks()
        if current_time - last_update >= animation_cooldown:
            frame += 1
            frame2 += 1
            last_update = current_time
        if frame2 >= len(idle_animationlist):
            frame2 = 0
        if not msgdone:
            if frame >= len(sixthanimationlist):
                frame = 0
                msgdone = True
            screen.blit(sixthanimationlist[frame], (500, 500))
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                enterfinished = False
                secondmsg = False
                thirdmsg = False
                fourthmsg = False
                fifthmsg = False
                sixthmsg = False
                seventhmsg = True
                msgdone = False
            if frame >= len(idlemsganimationlist):
                frame = 0
            screen.blit(sixthidleanimationlist[frame], (500, 500))
        screen.blit(idle_animationlist[frame2], (350, 740))

    if seventhmsg:
        current_time = pygame.time.get_ticks()
        if current_time - last_update >= animation_cooldown:
            frame += 1
            frame2 += 1
            last_update = current_time
        if frame2 >= len(idle_animationlist):
            frame2 = 0
        if not msgdone:
            if frame >= len(seventhanimationlist):
                frame = 0
                msgdone = True
            screen.blit(seventhanimationlist[frame], (500, 500))
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                enterfinished = False
                secondmsg = False
                thirdmsg = False
                fourthmsg = False
                fifthmsg = False
                sixthmsg = False
                seventhmsg = False
                eigthmsg = True
                msgdone = False
            if frame >= len(idlemsganimationlist):
                frame = 0
            screen.blit(seventhidleanimationlist[frame], (500, 500))
        screen.blit(idle_animationlist[frame2], (350, 740))

    if eigthmsg:
        current_time = pygame.time.get_ticks()
        if current_time - last_update >= animation_cooldown:
            frame += 1
            frame2 += 1
            last_update = current_time
        if frame2 >= len(idle_animationlist):
            frame2 = 0
        if not msgdone:
            if frame >= len(eigthanimationlist):
                frame = 0
                msgdone = True
            screen.blit(eigthanimationlist[frame], (500, 500))
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                enterfinished = False
                secondmsg = False
                thirdmsg = False
                fourthmsg = False
                fifthmsg = False
                sixthmsg = False
                seventhmsg = False
                eigthmsg = False
                finished = True
                msgdone = False
            if frame >= len(idlemsganimationlist):
                frame = 0
            screen.blit(eigthidleanimationlist[frame], (500, 500))
        screen.blit(idle_animationlist[frame2], (350, 740))

    if finished:
        current_time = pygame.time.get_ticks()
        if current_time - last_update >= animation_cooldown:
            frame += 1
            X += 50
            last_update = current_time
        if frame >= len(enter_animationlist):
            frame = 0
        screen.blit(enter_animationlist[frame], (X, 800))
        if X > 2000:
            done = True



# else:
#     if triggered:
#         current_time = pygame.time.get_ticks()
#         if current_time - last_update >= animation_cooldown:
#          frame += 1
#          X += 150
#          last_update = current_time
#         if frame >= len(enter_animationlist):
#          frame = 0
#         screen.blit(enter_animationlist[frame], (X, 800))
#         if X >= 1920:
#             triggered = False
#             X = -200




    pygame.display.update()

pygame.quit()