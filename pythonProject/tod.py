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
Foxrun = False
stasis = False
Foxjump = False
Falling = False
reversecolor = False
vertical = 0
fuchsia = (255, 0, 128)  # Transparency color
dark_red = (255, 100, 0)
dark_orange = (255, 255, 0)
clicked = 1
display_width = 1920
display_height = 1080
frame = 0
frame2 = 0
task = False
foxstand = False
programstart = True
RunAnim = True
count = 0
mouseclickcount = 1
runAnim = False
msgdone = False
Y = 0
X = 0
yheight = 0
bheight = 0
iheight = 0
rheight = 0
theight = 0
hheight = 0
dheight = 0
aheight = 0
y2height = 0
exlaimationheight = 0


foxrun = False
secondmsg = False
thirdmsg = False
startfalling = False
letterfalling = True
Yfalling = True
Xfalling = False
yfalling = False
bfalling = False
ifalling = False
rfalling = False
tfalling = False
hfalling = False
dfalling = False
afalling = False
y2falling = False
exclaimationfalling = False

fourthmsg = False
fifthmsg = False
Letters = False
firstmsg = False
Color = False
sixthmsg = False
offscreen = True
seventhmsg = False
eigthmsg = False
ninthmsg = False
finished = False
secondanimation = False

# x = (display_width *0.45)
# y = (display_height *0.8)
gameDisplay = pygame.display.set_mode((display_width,display_height))
sprite_sheet = pygame.image.load('spritesheet.png').convert_alpha()
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
    image.blit(sheet, (0,0), ((frame*width), 0 ,width, height))
    image = pygame.transform.scale(image, (width*scale, height*scale))
    image.set_colorkey((0,0,0))
    return image

def get_image2(sheet, frame, width, height, scale):
    image = pygame.Surface((width , height)).convert_alpha()
    image.blit(sheet, (0,0), ((frame*width), 524 ,width, height))
    image = pygame.transform.scale(image, (width*scale, height*scale))
    image.set_colorkey((0,0,0))
    return image

def get_image3(sheet, frame, width, height, scale):
    image = pygame.Surface((width , height)).convert_alpha()
    image.blit(sheet, (0,0), ((frame*width), 1081 ,width, height))
    image = pygame.transform.scale(image, (width*scale, height*scale))
    image.set_colorkey((0,0,0))
    return image

def get_image4(sheet, frame, width, height, scale):
    image = pygame.Surface((width , height)).convert_alpha()
    image.blit(sheet, (0,0), ((frame*width), 1232 ,width, height))
    image = pygame.transform.scale(image, (width*scale, height*scale))
    image.set_colorkey((0,0,0))
    return image

def get_image5(sheet, frame, width, height, scale):
    image = pygame.Surface((width , height)).convert_alpha()
    image.blit(sheet, (0,0), ((frame*width), 1390 ,width, height))
    image = pygame.transform.scale(image, (width*scale, height*scale))
    image.set_colorkey((0,0,0))
    return image

def get_image6(sheet, frame, width, height, scale):
    image = pygame.Surface((width , height)).convert_alpha()
    image.blit(sheet, (0,0), ((frame*width), 1544 ,width, height))
    image = pygame.transform.scale(image, (width*scale, height*scale))
    image.set_colorkey((0,0,0))
    return image

def get_image7(sheet, frame, width, height, scale):
    image = pygame.Surface((width , height)).convert_alpha()
    image.blit(sheet, (0,0), ((frame*width), 1699 ,width, height))
    image = pygame.transform.scale(image, (width*scale, height*scale))
    image.set_colorkey((0,0,0))
    return image

def get_image8(sheet, frame, width, height, scale):
    image = pygame.Surface((width , height)).convert_alpha()
    image.blit(sheet, (0,0), ((frame*width), 1884 ,width, height))
    image = pygame.transform.scale(image, (width*scale, height*scale))
    image.set_colorkey((0,0,0))
    return image

def get_image9(sheet, frame, width, height, scale):
    image = pygame.Surface((width , height)).convert_alpha()
    image.blit(sheet, (0,0), ((frame*width), 2074 ,width, height))
    image = pygame.transform.scale(image, (width*scale, height*scale))
    image.set_colorkey((0,0,0))
    return image

def get_image10(sheet, frame, width, height, scale):
    image = pygame.Surface((width , height)).convert_alpha()
    image.blit(sheet, (0,0), ((frame*width), 2247 ,width, height))
    image = pygame.transform.scale(image, (width*scale, height*scale))
    image.set_colorkey((0,0,0))
    return image

def get_image11(sheet, frame, width, height, scale):
    image = pygame.Surface((width , height)).convert_alpha()
    image.blit(sheet, (0,0), ((frame*width), 2420 ,width, height))
    image = pygame.transform.scale(image, (width*scale, height*scale))
    image.set_colorkey((0,0,0))
    return image

def get_image12(sheet, frame, width, height, scale):
    image = pygame.Surface((width , height)).convert_alpha()
    image.blit(sheet, (0,0), ((frame*width), 2600 ,width, height))
    image = pygame.transform.scale(image, (width*scale, height*scale))
    image.set_colorkey((0,0,0))
    return image

def get_image13(sheet, frame, width, height, scale):
    image = pygame.Surface((width , height)).convert_alpha()
    image.blit(sheet, (0,0), ((frame*width), 2760 ,width, height))
    image = pygame.transform.scale(image, (width*scale, height*scale))
    image.set_colorkey((0,0,0))
    return image

def get_image14(sheet, frame, width, height, scale):
    image = pygame.Surface((width , height)).convert_alpha()
    image.blit(sheet, (0,0), ((frame*width), 2940 ,width, height))
    image = pygame.transform.scale(image, (width*scale, height*scale))
    image.set_colorkey((0,0,0))
    return image

def get_image15(sheet, frame, width, height, scale):
    image = pygame.Surface((width , height)).convert_alpha()
    image.blit(sheet, (0,0), ((frame*width), 3120 ,width, height))
    image = pygame.transform.scale(image, (width*scale, height*scale))
    image.set_colorkey((0,0,0))
    return image

def get_image16(sheet, frame, width, height, scale):
    image = pygame.Surface((width , height)).convert_alpha()
    image.blit(sheet, (0,0), ((frame*width), 3270 ,width, height))
    image = pygame.transform.scale(image, (width*scale, height*scale))
    image.set_colorkey((0,0,0))
    return image

def get_image17(sheet, frame, width, height, scale):
    image = pygame.Surface((width , height)).convert_alpha()
    image.blit(sheet, (0,0), ((frame*width), 3642 ,width, height))
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
enteranimation_steps = 4
foxrun_animationlist = []
foxrunanimation_steps = 10
reversefoxrun_animationlist = []
reversefoxrunanimation_steps = 4
H_list = []
H_steps = 2
a_list = []
a_steps = 2
p_list = []
p_steps = 2
p2_list = []
p2_steps = 2
y_list = []
y_steps = 2
b_list = []
b_steps = 2
i_list = []
i_steps = 2
r_list = []
r_steps = 2
t_list = []
t_steps = 2
h2_list = []
h2_steps = 2
d_list = []
d_steps = 2
a2_list = []
a2_steps = 2
y2_list = []
y2_steps = 2
countcount = 0
exclaimation_list =[]
exclaimation_steps = 2

last_update = pygame.time.get_ticks()
last_update2 = pygame.time.get_ticks()
animation_cooldown = 120
animation_cooldown2 = 250
animation_cooldown3 = 75
for x in range(enteranimation_steps):
        enter_animationlist.append(get_image(sprite_sheet, x, 92, 83, 1))
for x in range(foxrunanimation_steps):
        foxrun_animationlist.append(get_image2(sprite_sheet, x, 139, 68, 1.5))
for x in range(reversefoxrunanimation_steps):
        reversefoxrun_animationlist.append(get_image17(sprite_sheet, x, 139, 68, 1.5))
for x in range(H_steps):
        H_list.append(get_image3(sprite_sheet, x, 174, 80, 2))
for x in range(a_steps):
        a_list.append(get_image4(sprite_sheet, x, 174, 80, 2))
for x in range(p_steps):
        p_list.append(get_image5(sprite_sheet, x, 174, 80, 2))
for x in range(p2_steps):
        p2_list.append(get_image6(sprite_sheet, x, 174, 80, 2))
for x in range(y_steps):
        y_list.append(get_image7(sprite_sheet, x, 174, 80, 2))
for x in range(b_steps):
        b_list.append(get_image8(sprite_sheet, x, 174, 80, 2))
for x in range(i_steps):
        i_list.append(get_image9(sprite_sheet, x, 174, 80, 2))
for x in range(r_steps):
        r_list.append(get_image10(sprite_sheet, x, 174, 80, 2))
for x in range(t_steps):
        t_list.append(get_image11(sprite_sheet, x, 174, 80, 2))
for x in range(h2_steps):
        h2_list.append(get_image12(sprite_sheet, x, 174, 80, 2))
for x in range(d_steps):
        d_list.append(get_image13(sprite_sheet, x, 174, 80, 2))
for x in range(a2_steps):
        a2_list.append(get_image14(sprite_sheet, x, 174, 80, 2))
for x in range(y2_steps):
        y2_list.append(get_image15(sprite_sheet, x, 174, 80, 2))
for x in range(exclaimation_steps):
        exclaimation_list.append(get_image16(sprite_sheet, x, 174, 80, 2))


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


    if programstart:
        current_time = pygame.time.get_ticks()
        if current_time - last_update >= animation_cooldown:
            frame+= 1
            X+= 50
            last_update = current_time
        if frame >= len(enter_animationlist):
            frame = 0
        screen.blit(enter_animationlist[frame],(X,960))
        if X > 700:
            programstart = False
            secondanimation = True
            print(done)
            X = 0
    if secondanimation:
        screen.blit(enter_animationlist[0], (750, 960))
        # pygame.time.delay(500)
        # if count == 1:
        #     foxrun = True
        #     count+= 1
    # if foxrun:
        current_time = pygame.time.get_ticks()
        if current_time - last_update >= animation_cooldown:
            frame+= 1
            X+= 50
            last_update = current_time
        if frame >= len(foxrun_animationlist):
            frame = 0
        screen.blit(foxrun_animationlist[frame],(X, 940))
        if X > 500:
            secondanimation = False
            foxstand = True
            X = 0
    if foxstand:
        screen.blit(enter_animationlist[0], (750, 960))
        current_time = pygame.time.get_ticks()
        screen.blit(foxrun_animationlist[0], (600, 940))
        screen.blit(enter_animationlist[0], (750, 960))
        if current_time - last_update >= animation_cooldown:
            X+= 100
            last_update = current_time
        screen.blit(H_list[1], (-100, X))
        if X > 800:
            foxstand = False
            Foxjump = True
            X = 950
    if Foxjump:
        screen.blit(enter_animationlist[0], (750, 960))
        current_time = pygame.time.get_ticks()
        screen.blit(H_list[1], (-100, 875))
        if current_time - last_update >= animation_cooldown:
            X+= -100+Y
            last_update = current_time
            Y+=25
        screen.blit(foxrun_animationlist[0], (600, X))
        screen.blit(enter_animationlist[0], (750, 960))
        if Y > 200:
            Foxjump = False
            Foxrun = True
            X = 600
            Y = 0
    if Foxrun:
        # screen.blit(enter_animationlist[0], (750, 960))
        screen.blit(H_list[1], (-100, 875))
        current_time = pygame.time.get_ticks()
        # foxrunanimation_steps = 16
        if count < 4:
            screen.blit(enter_animationlist[0], (750, 960))
            if current_time - last_update >= animation_cooldown2:
                count += 1
                last_update = current_time
            if count % 2 == 0:
                screen.blit(foxrun_animationlist[0], (600, 940))
            if not count %2 ==0:
                screen.blit(reversefoxrun_animationlist[0], (600, 940))
        else:
            foxrunanimation_steps = 15
            if current_time - last_update >= animation_cooldown:
                X+= 100
                last_update = current_time
                frame+= 1
                frame2 += 1
            if frame2 >= len(enter_animationlist):
                frame2 = 0
            screen.blit(foxrun_animationlist[frame], (X, 940))
            screen.blit(enter_animationlist[frame2], (X + 150, 960))
            if X > 1000:
                Foxrun = False
                Falling = True
                count = 0
                Y = -500
    if Falling:
        # screen.blit(enter_animationlist[0], (750, 960))
        screen.blit(H_list[1], (-100, 875))
        current_time = pygame.time.get_ticks()
        if offscreen:
            if current_time - last_update >= animation_cooldown:
                X+= 100
                last_update = current_time
                frame+= 1
                count+= 1
                Y+= 100
            if frame >= len(foxrun_animationlist):
                frame = 0
            if frame2 >= len(enter_animationlist):
                frame2 = 0
            screen.blit(foxrun_animationlist[frame], (X, 950))
            screen.blit(enter_animationlist[frame2], (X + 150, 960))
        if count > 3:
            startfalling = True
            count = 0
        if startfalling:
            screen.blit(a_list[1], (50, Y))
        if Y>=800:
            startfalling = False
            screen.blit(a_list[1], (50, 875))
            Falling = False
            Letters = True
            Y = 0
            X = 0
        if X>5000:
            offscreen = False
            X = 0
            Y = 0

    if Letters:
        # screen.blit(enter_animationlist[0], (860, 960))
        screen.blit(H_list[1], (-100, 875))
        screen.blit(a_list[1], (200-150, 875))
        if Yfalling:
            Y += 10
            screen.blit(p_list[1], (350-150, Y))
            if Y > 350:
                Xfalling = True
        if Y > 860:
            Yfalling = False
            screen.blit(p_list[1], (350-150, 875))
        if Xfalling:
            X += 10
            screen.blit(p2_list[1], (500-150, X))
            if X > 350:
                yfalling = True
        if X > 860:
            Xfalling = False
            screen.blit(p2_list[1], (500-150, 875))
        if yfalling:
            yheight += 10
            screen.blit(y_list[1], (650-150, yheight))
            if yheight > 350:
                bfalling = True
        if yheight > 860:
            yfalling = False
            screen.blit(y_list[1], (650-150, 875))
        if bfalling:
            bheight += 10
            screen.blit(b_list[1], (800-150, bheight))
            if bheight > 350:
                ifalling = True
        if bheight > 860:
            bfalling = False
            screen.blit(b_list[1], (800-150, 875))
        if ifalling:
            iheight += 10
            screen.blit(i_list[1], (950-150, iheight))
            if iheight > 350:
                rfalling = True
        if iheight > 860:
            ifalling = False
            screen.blit(i_list[1], (950-150, 875))
        if rfalling:
            rheight += 10
            screen.blit(r_list[1], (1100-150, rheight))
            if rheight > 350:
                tfalling = True
        if rheight > 860:
            rfalling = False
            screen.blit(r_list[1], (1100-150, 875))
        if tfalling:
            theight += 10
            screen.blit(t_list[1], (1250-150, theight))
            if theight > 350:
                hfalling = True
        if theight > 860:
            tfalling = False
            screen.blit(t_list[1], (1250-150, 875))
        if hfalling:
            hheight += 10
            screen.blit(h2_list[1], (1400-150, hheight))
            if hheight > 350:
                dfalling = True
        if hheight > 860:
            hfalling = False
            screen.blit(h2_list[1], (1400-150, 875))
        if dfalling:
            dheight += 10
            screen.blit(d_list[1], (1550-150, dheight))
            if dheight > 350:
                afalling = True
        if dheight > 860:
            dfalling = False
            screen.blit(d_list[1], (1550-150, 875))
        if afalling:
            aheight += 10
            screen.blit(a2_list[1], (1700-150, aheight))
            if aheight > 350:
                y2falling = True
        if aheight > 860:
            afalling = False
            screen.blit(a2_list[1], (1700-150, 875))
        if y2falling:
            y2height += 10
            screen.blit(y2_list[1], (1850-150, y2height))
            if y2height > 350:
                y2falling = True
        if y2height > 860:
            exclaimationfalling = False
            screen.blit(y2_list[1], (1850-150, 875))
            Letters = False
            Color = True
            count = 0
        if exclaimationfalling:
            exlaimationheight += 10
            screen.blit(exclaimation_list[1], (2000-150, exlaimationheight))
        if exlaimationheight > 860:
            exlaimationheight = False
            screen.blit(exclaimation_list[1], (2000-150, 875))
            Letters = False
            Color = True
            count = 0
    if Color:
        current_time = pygame.time.get_ticks()
        print(count)
        if current_time - last_update >= animation_cooldown3:
            count+= 1
            last_update = current_time
        if count < 1 :
            screen.blit(H_list[1], (-100, 875))
        else:
            screen.blit(H_list[0], (-100, 875))
        if count < 2:
            screen.blit(a_list[1], (200 - 150, 875))
        else:
            screen.blit(a_list[0], (200 - 150, 875))
        if count < 3:
            screen.blit(p_list[1], (350 - 150, 875))
        else:
            screen.blit(p_list[0], (350 - 150, 875))
        if count < 4:
            screen.blit(p2_list[1], (500 - 150, 875))
        else:
            screen.blit(p2_list[0], (500 - 150, 875))
        if count < 5:
            screen.blit(y_list[1], (650 - 150, 875))
        else:
            screen.blit(y_list[0], (650 - 150, 875))
        if count < 6:
            screen.blit(b_list[1], (800 - 150, 875))
        else:
            screen.blit(b_list[0], (800 - 150, 875))
        if count < 7:
            screen.blit(i_list[1], (950 - 150, 875))
        else:
            screen.blit(i_list[0], (950 - 150, 875))
        if count < 8:
            screen.blit(r_list[1], (1100 - 150, 875))
        else:
            screen.blit(r_list[0], (1100 - 150, 875))
        if count < 9:
            screen.blit(t_list[1], (1250 - 150, 875))
        else:
            screen.blit(t_list[0], (1250 - 150, 875))
        if count < 10:
            screen.blit(h2_list[1], (1400 - 150, 875))
        else:
            screen.blit(h2_list[0], (1400 - 150, 875))
        if count <11:
            screen.blit(d_list[1], (1550 - 150, 875))
        else:
            screen.blit(d_list[0], (1550 - 150, 875))
        if count < 12:
            screen.blit(a2_list[1], (1700 - 150, 875))
        else:
            screen.blit(a2_list[0], (1700 - 150, 875))
        if count < 13:
            screen.blit(y2_list[1], (1850 - 150, 875))
        else:
            screen.blit(y2_list[0], (1850 - 150, 875))
            if countcount == 0:
                Color = False
                reversecolor = True
                count = 0
                countcount += 1
    if reversecolor:
        current_time = pygame.time.get_ticks()
        print(count)
        if current_time - last_update >= animation_cooldown3:
            count+= 1
            last_update = current_time
        if count < 1 :
            screen.blit(H_list[0], (-100, 875))
        else:
            screen.blit(H_list[1], (-100, 875))
        if count < 2:
            screen.blit(a_list[0], (200 - 150, 875))
        else:
            screen.blit(a_list[1], (200 - 150, 875))
        if count < 3:
            screen.blit(p_list[0], (350 - 150, 875))
        else:
            screen.blit(p_list[1], (350 - 150, 875))
        if count < 4:
            screen.blit(p2_list[0], (500 - 150, 875))
        else:
            screen.blit(p2_list[1], (500 - 150, 875))
        if count < 5:
            screen.blit(y_list[0], (650 - 150, 875))
        else:
            screen.blit(y_list[1], (650 - 150, 875))
        if count < 6:
            screen.blit(b_list[0], (800 - 150, 875))
        else:
            screen.blit(b_list[1], (800 - 150, 875))
        if count < 7:
            screen.blit(i_list[0], (950 - 150, 875))
        else:
            screen.blit(i_list[1], (950 - 150, 875))
        if count < 8:
            screen.blit(r_list[0], (1100 - 150, 875))
        else:
            screen.blit(r_list[1], (1100 - 150, 875))
        if count < 9:
            screen.blit(t_list[0], (1250 - 150, 875))
        else:
            screen.blit(t_list[1], (1250 - 150, 875))
        if count < 10:
            screen.blit(h2_list[0], (1400 - 150, 875))
        else:
            screen.blit(h2_list[1], (1400 - 150, 875))
        if count < 11:
            screen.blit(d_list[0], (1550 - 150, 875))
        else:
            screen.blit(d_list[1], (1550 - 150, 875))
        if count < 12:
            screen.blit(a2_list[0], (1700 - 150, 875))
        else:
            screen.blit(a2_list[1], (1700 - 150, 875))
        if count < 13:
            screen.blit(y2_list[0], (1850 - 150, 875))
        else:
            screen.blit(y2_list[1], (1850 - 150, 875))
            Color = True
        # screen.blit(exclaimation_list[1], (2000 - 150, 875))
# if y > 800:




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