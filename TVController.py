from Controller import *

class TVController(Controller):
    
    # 객체 생성시 초기화 작업
    def __init__(self):
        self.maxState = 128
        self.minState = 0
    
    # 공통 메소드 오버라이딩
    def powerOn(self):
        super().powerOn()
        print("TV is up")
    
    def powerOff(self):
        super().powerOff()
        print("TV is down")
    
    # 추상 클래스 구현
    def setState(self):
        if not super().isPowerOn():
            self.printPowerMessage()
            return
        
        stateValue = int(input("설정할 채널을 입력하세요. >> "))
        
        if (stateValue < self.minState or stateValue > self.maxState):
            print("Cannot set chnnels: %s" % stateValue)
            return
        
        self.state = stateValue
    
    def getState(self):
        if not super().isPowerOn():
            self.printPowerMessage()
            return
        
        return self.state
    
    def upState(self):
        if not super().isPowerOn():
            self.printPowerMessage()
            return
        
        updatedState = self.state + 1
        if (updatedState > self.maxState):
            updatedState = self.minState
        
        self.state = updatedState
        
    def downState(self):
        if not super().isPowerOn():
            self.printPowerMessage()
            return
        
        updatedState = self.state - 1
        if (updatedState < self.minState):
            updatedState = self.maxState
        
        self.state = updatedState
        
    def printState(self):
        if not super().isPowerOn():
            self.printPowerMessage()
            return
        
        print("현재 설정된 채널은 %s 입니다." % self.state)
        
    def printPowerMessage(self):
        print("Cannot set channels. Because TV is not ON")
        
    def printMenu(self):
        return '''------ 메뉴 ------
1. 전원 ON
2. 채널 설정
3. 채널 +1
4. 채널 -1
5. 현재 채널 출력
6. 전원 OFF
0. 돌아가기
------------------
>> '''