import pygame
import sys

class AppData:
    screen_w, screen_h = 640,480
    pygame.init()
    pygame.display.set_caption("pygame form1")		
    screen = pygame.display.set_mode((screen_w, screen_h))	
    clock = pygame.time.Clock()	
    font = pygame.font.SysFont("arial", 30)
    bgColor = (0,0,0)
    running = True
        
        
        
        
# App Function



# image Function
def load_image(path, scale = None, rotate = None):
    img = pygame.image.load(path)
    if scale  != None : img = pygame.transform.scale ( img, scale )
    if rotate != None : img = pygame.transform.rotate( img, rotate )
    return img

def update_image(img, scale = None, rotate = None):
    if scale  != None : img = pygame.transform.scale ( img, scale )     
    if rotate != None : img = pygame.transform.rotate( img, rotate )
    return img

def display_image(img, location):
    AppData.screen.blit( img, location ) 



# font Function
def display_font (msg, color, location):
    text = AppData.font.render(msg, True, color)
    AppData.screen.blit(text, location)



# diagram Function
def pyCircle (location, radius, color, width=None):
    if width != None: pygame.draw.circle(AppData.screen, color, location, radius, width)
    else            : pygame.draw.circle(AppData.screen, color, location, radius)
    
def pyRect (shape, color, width=None):
    if width != None: pygame.draw.rect(AppData.screen, color, shape, width)
    else            : pygame.draw.rect(AppData.screen, color, shape)
    
def pyLine (posS, posE, color, width):
    pygame.draw.line(AppData.screen, color, posS, posE, width)
    
def pyPoly (shape, color, width=None):
    if width != None: pygame.draw.polygon(AppData.screen, color, shape, width)
    else            : pygame.draw.polygon(AppData.screen, color, shape)
    
    
    
# sound Function 
def load_sound(path):
    # sound mp3 not supported in raspberry
    return pygame.mixer.Sound(path)

def update_sound(sound, running):
    if running: sound.play(-1)
    else: sound.stop()
    
    
    
# set_button
def control_button (shape, pos, function):
    if (shape[0])<pos[0]<(shape[0]+shape[2]):
        if (shape[1])<pos[1]<(shape[1]+shape[3]):
            function()

def draw_button (shape, color, msg, msgColor = (0,0,0)):
    pyRect(shape, color)
    display_font(msg, msgColor, (shape[0],shape[1]))
    
def button_test ():
    print("button press")