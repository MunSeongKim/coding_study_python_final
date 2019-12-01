from abc import *

class Controller(metaclass=ABCMeta):
    # 필드 정의
    # Boolean True=ON|False=OFF
    powerState = False
    # Integer
    state = 0
    # Integer
    maxState = 0
    # Integer
    minState = 0
    
    # 객체 생성시 필드 초기화
    def __init__(self):
        pass
    
    # 공통으로 사용 가능한 메소드 정의
    def powerOn(self):
        self.powerState = True
    
    def powerOff(self):
        self.powerState = False
        
    def isPowerOn(self):
        return self.powerState
    
    # 추상 메소드 - 상속받은 클래스에서 강제로 구현하게 하는 기능
    @abstractmethod
    def setState(self):
        pass
    
    @abstractmethod
    def getState(self):
        pass
    
    @abstractmethod
    def upState(self):
        pass
    
    @abstractmethod
    def downState(self):
        pass