# 사용할 코드들을 설정합니다.
from SetApp import *
from Mover import *


class App:
    # 1. 앱이 설정되고 실행합니다.
    def __init__    (self): 
        self.set_prof()
        self.run()
    
    
    # 2. 앱이 실행되는 부분입니다.    
    def run (self):
        while AppData.running==True:
            self.control()
            self.update()
            self.display()
            
        
    # 프로그램의 내부 기능을 설정하는 부분입니다.    
    def set_prof (self): 
        self.sound = load_sound('soundSample.mp3')
        self.image = load_image('imageSample.png',scale=[200,200], rotate=30)
        self.isKey2 = False
        
        self.obj1 = Mover()
        self.obj1.lpos = Vec2d(300,300)
        self.obj1.vpos = Vec2d(1,1)
        self.obj1.fixtureOrigin *= 10
        self.obj2 = Mover()
        self.obj2.lpos = Vec2d(300,310)
        self.obj2.vpos = Vec2d(1,-1)
        self.obj2.fixtureOrigin *= 10
        self.obj2.langle = 45
        self.obj2.set_fixture_angle(self.obj2.langle)
        
            
            
    # 2-1. 조작이 일어나는 부분입니다.        
    def control (self): 
        for event in pygame.event.get():			
            if event.type == pygame.QUIT: 
                AppData.running = False
                sys.exit()	
            
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN: 
                control_button([100,100,200,50],pos,button_test)
                
            if event.type == pygame.MOUSEBUTTONUP: pass
            if event.type == pygame.MOUSEMOTION: pass
            
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_1:  update_sound(self.sound, running = True)
                if event.key == pygame.K_2: self.isKey2 = True
                    
            if event.type == pygame.KEYUP: 
                if event.key == pygame.K_1:  update_sound(self.sound, running = False)
                if event.key == pygame.K_2: self.isKey2 = False
                
                			
    # 2-2. 갱신이 일어나는 부분입니다.    
    def update (self): 
        self.obj1.update()
        self.obj2.update()
        pass
        
        
    # 2-3. 출력이 일어나는 부분입니다.
    def display (self): 
        AppData.screen.fill(AppData.bgColor)	
        
        draw_button([100,100,200,50],(128,128,128),"button")
        
        display_font("press 1 to play mp3", (255,255,255), (10,10))
        display_font("press 2 to display cat", (255,255,255), (10,50))
        
        if collide_check(self.obj1, self.obj2):
            print("collide")
            
        pyPoly(self.obj1.fixture+self.obj1.lpos.tonp(), (255,0,0))
        pyPoly(self.obj2.fixture+self.obj2.lpos.tonp(), (0,255,0))
        
        if self.isKey2: display_image(self.image, (200,200))
        
        pygame.display.update()	
        AppData.clock.tick(60)
        


if __name__ == "__main__":
    app = App()