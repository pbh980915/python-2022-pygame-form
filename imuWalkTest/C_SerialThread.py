import threading
import serial
import time
import numpy as np

class SerialThread:
    def __init__(self):
        self.ser = None
        self.baud = 115200
        self.port = None
        self.get_serial()
        
        self.threadRun = True
        self.thread = threading.Thread(target = self.loop)
        self.thread.start()
        
        self.readCurrent = ""
        
        self.movement = [0 for i in range(30)]
        self.moveSum = 0
        self.y = -1
        self.p = -1
        self.r = -1
        self.y_c = 0
        
        
    def loop (self):
        while True:
            if not self.check_connect(): 
                self.serial_reconnect()
            
            try:   
                if self.threadRun:
                    # 코드를 넣어주세요
                    #self.ser.write('hi\n'.encode())
                    self.serial_read()
                    data = self.readCurrent.split(' ')
                    
                    sub = 0
                    sub += abs(self.p-float(data[1])); self.p = round(float(data[1]),1)
                    sub += abs(self.r-float(data[2])); self.r = round(float(data[2]),1)
                    if float(data[0])>0 :
                        sub += abs(self.y-float(data[0]))/2
                        self.y = round(float(data[0]),1)
                    else :
                        sub += abs(self.y-float(data[0])-360)/2
                        self.y = 360+round(float(data[0]),1)
                    
                    #irr filter
                    self.y_c = self.y*0.01+self.y_c*0.99
                        
                    self.movement.append(sub)
                    del(self.movement[0])
                    self.moveSum = sum(i for i in self.movement)/30
                    
                        
                    
                    
                
                else:
                    print(self.port+" serial_thread stop...")
                    print("waiting thread restart...")
                    while not self.threadRun: pass
            except: pass
                
                
    def serial_read (self):
        if self.ser.readable():
            time.sleep(0.03)
            data = self.ser.read_all().decode()[:-2]
            if data != "": 
                self.readCurrent = data
            

    def get_serial(self):
        for i in range(3,50):
            try: 
                self.ser = serial.Serial('COM'+str(i), self.baud)
                self.port = 'COM'+str(i)
                print("connect ser "+self.port)
                
                return
            except: pass
        print("not conneting serial....")
        
        
    def check_connect(self):
        try: self.ser.inWaiting()
        except: 
            if self.ser != None: 
                print("ser "+self.port+" disconnect")
                print("trying... reconnect")
            self.ser = None
            return False
        return True


    def serial_disconnect (self):
        self.ser.close()
        self.ser = None
        self.y = -1
        self.p = -1
        self.r = -1
        
        
    def serial_reconnect (self): 
        try: 
            self.ser = serial.Serial(self.port, self.baud)
            print("reconnect ser "+self.port)
            
            ts = time.time()
            while ts+3>time.time():
                self.serial_read()
                print(ts+3-time.time())
        except: pass
        
        
    
def get_motion (y,p,r,m,y_c):
    motion = ""
    if m<0.5: motion = "rest"
    if m>1.5: motion = "walk"
    if m>3.5: motion = "run"
    if m>6.0: motion = "atk"
    if y-y_c<-50: motion = "sightL"
    if y-y_c>+50: motion = "sightR"
    if r<-30: motion = "avoidL"
    if r>+30: motion = "avoidR"
    return motion


if __name__ == "__main__":
    import time
    test = SerialThread()
    test.threadRun = True
    #time.sleep(5)
    #test.serial_disconnect()
    #test.threadRun = False
    
    
    
