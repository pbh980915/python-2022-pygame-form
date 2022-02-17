# 사용할 코드들을 설정합니다.
from SetApp import *


class App:
    # 1. 앱이 설정되고 실행합니다.
    def __init__    (self): 
        self.set_prof()
        self.run()
    
    
    # 2. 앱이 실행되는 부분입니다.    
    def run (self):
        while self.running==True:
            self.control()
            self.update()
            self.display()
            
        
    # 프로그램의 내부 기능을 설정하는 부분입니다.    
    def set_prof (self): 
        pass
            
            
    # 2-1. 조작이 일어나는 부분입니다.        
    def control (self): 
        for event in pygame.event.get():			
            if event.type == pygame.QUIT: 
                self.running = False
                sys.exit()	
            
            if event.type == pygame.MOUSEBUTTONDOWN: pass
            if event.type == pygame.MOUSEBUTTONUP: pass
            if event.type == pygame.MOUSEMOTION: 
                pos = pygame.mouse.get_pos()
                
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_ESCAPE: 
                    self.running = False
            if event.type == pygame.KEYUP: pass
                
                			
    # 2-2. 갱신이 일어나는 부분입니다.    
    def update (self): 
        pass
        
    # 2-3. 출력이 일어나는 부분입니다.
    def display (self): 
        self.screen.fill(AppData.bgColor)	
        
        pygame.display.update()	
        AppData.clock.tick(60)
        


if __name__ == "__main__":
    app = App()