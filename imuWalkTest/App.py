# 사용할 코드들을 설정합니다.
from SetApp import *
from C_Mover import *
from C_SerialThread import *
from C_Stat import *

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
        self.sth = SerialThread()
        self.sth.threadRun = True
        
            
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
                if event.key == pygame.K_1:  self.sth.serial_disconnect()
            if event.type == pygame.KEYUP: 
                if event.key == pygame.K_1:  pass
                
                			
    # 2-2. 갱신이 일어나는 부분입니다.    
    def update (self): 
        print(get_motion(self.sth.y,self.sth.p,self.sth.r,self.sth.moveSum,self.sth.y_c))
        pass
        
    # 2-3. 출력이 일어나는 부분입니다.
    def display (self): 
        AppData.screen.fill(AppData.bgColor)	
        
        display_font(str(self.sth.y), (255,255,255), (10,10))
        display_font(str(self.sth.p), (255,255,255), (10,50))
        display_font(str(self.sth.r), (255,255,255), (10,90))
        display_font(str(round(self.sth.moveSum,2)), (255,255,255), (10,130))
        
        pygame.display.update()	
        AppData.clock.tick(60)
        


if __name__ == "__main__":
    app = App()