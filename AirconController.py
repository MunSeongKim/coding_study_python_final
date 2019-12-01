from Controller import *

class AirconController(Controller):
    
    # 객체 생성시 초기화 작업
    def __init__(self):
        self.maxState = 40
        self.minState = 18
    
    # 공통 메소드 오버라이딩
    def powerOn(self):
        super().powerOn()
        print("Airconditioner is up")
    
    def powerOff(self):
        super().powerOff()
        print("Airconditioner is down")
    
    # 추상 클래스 구현
    def setState(self):
        if not super().isPowerOn():
            self.printPowerMessage()
            return
        
        stateValue = int(input("설정할 온도를 입력하세요. >> "))
        
        if (stateValue < self.minState or stateValue > self.maxState):
            print("Cannot set temperature: %s" % stateValue)
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
            print("Cannot set temperature upper then %s" % self.maxState)
            return
        
        self.state = updatedState
        
    def downState(self):
        if not super().isPowerOn():
            self.printPowerMessage()
            return
        
        updatedState = self.state - 1
        if (updatedState < self.minState):
            print("Cannot set temperature lower then %s" % self.minState)
            return
        
        self.state = updatedState
        
    def printState(self):
        if not super().isPowerOn():
            self.printPowerMessage()
            return
        
        print("현재 설정된 온도는 %s 입니다." % self.state)
        
    def printPowerMessage(self):
        print("Cannot set temperature. Because Aircondiioner is not ON")
        
    def printMenu(self):
        return '''------ 메뉴 ------
1. 전원 ON
2. 온도 설정
3. 온도 +1
4. 온도 -1
5. 현재 온도 출력
6. 전원 OFF
0. 돌아가기
------------------
>> '''