from AirconController import *
from TVController import *

def printMainMenu():
    return "Select the controller. (Aircon: 1/ TV: 2/ Quit: 0) >> "
    
if __name__ == "__main__":
    controllerList = [AirconController(), TVController()]
    
    while(1):
        selectedController = int(input(printMainMenu()))
        if selectedController == 0:
            break
        
        controller = controllerList[(selectedController -1)]
        while (1):
            selected = int(input(controller.printMenu()))
            
            if selected == 1:
                controller.powerOn()
            elif selected == 2:
                controller.setState()
            elif selected == 3:
                controller.upState()
            elif selected == 4:
                controller.downState()
            elif selected == 5:
                controller.printState()
            elif selected == 6:
                controller.powerOff()
            else:
                break
                