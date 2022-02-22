import pygame
import numpy as np
import os


# 1,2,3,4,5,6,7,8,9 설정된 이미지
# 클릭 해당 그리드 이미지 넣기
# s : map txt파일 생성
# l : map txt파일 로드

pygame.init()
clock  = pygame.time.Clock()
screen = pygame.display.set_mode((800,600))
font   = pygame.font.SysFont('휴먼둥근헤드라인',30)

FPS = 60
running = True
app_path = ""
textures_path = [
    app_path + "textures/t0.png",
    app_path + "textures/t1.PNG",
    app_path + "textures/t2.PNG",
    app_path + "textures/t3.PNG",
    app_path + "textures/t4.PNG",
    app_path + "textures/t5.PNG",
    app_path + "textures/t6.PNG",
    app_path + "textures/t7.PNG",
    app_path + "textures/t8.PNG",
    app_path + "textures/t9.PNG",
]


def saveMapFile(): 
    fileName = input("저장 파일 이름 : ")
    filePath = app_path + "mapFiles/" + fileName
    print(filePath)
    file = open(filePath, 'w')
    for i in range(16):
        msg = ""
        for j in range(12):
            msg += str(mapData[i,j]) + " "
        file.write(msg+"\n")
    file.close()

def openMapFile(): 
    fileName = input("열기 파일 이름 : ")
    filePath = app_path + "mapFiles/" + fileName
    file = open(filePath, 'r')
    for i in range(16):
        data = file.readline().split(" ")
        print(data)
        data = [int(data[i]) for i in range(len(data)-1)]
        mapData[i,:] = data
    file.close()

select = 0
mouse_state = False
mapData = np.zeros((16,12),int)
def controller():
    global select, mouse_state
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_0:  select = 0
            if event.key == pygame.K_1:  select = 1
            if event.key == pygame.K_2:  select = 2
            if event.key == pygame.K_3:  select = 3
            if event.key == pygame.K_4:  select = 4
            if event.key == pygame.K_5:  select = 5
            if event.key == pygame.K_6:  select = 6
            if event.key == pygame.K_7:  select = 7
            if event.key == pygame.K_8:  select = 8
            if event.key == pygame.K_9:  select = 9
            if event.key == pygame.K_s:  saveMapFile() 
            if event.key == pygame.K_o:  openMapFile()
        if event.type == pygame.MOUSEBUTTONDOWN: mouse_state = True
        if event.type == pygame.MOUSEBUTTONUP  : mouse_state = False
        if (event.type == pygame.MOUSEMOTION)&mouse_state:
            click = pygame.mouse.get_pos()
            x,y = int(click[0]/50), int(click[1]/50)
            mapData[x,y] = select

def display ():
    def draw_grid():
        for i in range(16): pygame.draw.line(screen,(128,128,128),(i*50,0),(i*50,600),1)
        for j in range(12):  pygame.draw.line(screen,(128,128,128),(0,j*50),(800,j*50),1)

    def draw_grid_image():
        for i in range(16): 
            for j in range(12):  
                select_texture = mapData[i,j]
                img = pygame.image.load( textures_path[select_texture] )
                img = pygame.transform.scale(img, (50, 50))
                screen.blit(img, [50*i, 50*j])

    def draw_grid_data():
        for i in range(16): 
            for j in range(12):  
                msg = font.render(str(mapData[i,j]), True, (0,0,0))
                screen.blit(msg, [50*i+5, 50*j+5])

    screen.fill((255,255,255))
    draw_grid_image()
    draw_grid()
    clock.tick(FPS)
    pygame.display.flip()


while running:
    controller()
    display()
            
