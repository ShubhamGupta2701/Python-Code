import copy
from pickle import TRUE
from xml.dom.minidom import Element

class EightPuzzle:
    def __init__(self,initial,goal):
        self.currentState = initial
        self.goalState = goal
        self.EmptyIndex = self.EmptyTileIndex()
        self.prevState = None

    def up(self):
        if self.EmptyIndex ==6 or self.EmptyIndex ==7 or self.EmptyIndex ==8:
            print("Can not move")
        else:
            self.prevState = copy.deepcopy(self)
            self.currentState[self.EmptyIndex] = self.currentState[self.EmptyIndex+3]
            self.currentState[self.EmptyIndex+3] = 0
            self.EmptyIndex = self.EmptyIndex+3
            return True

    def down(self):
        if self.EmptyIndex==0 or self.EmptyIndex==1 or self.EmptyIndex==2:
            print("cannot move")
            return False
        else:
            self.prevState = copy.deepcopy(self)
            self.currentState[self.EmptyIndex] = self.currentState[self.EmptyIndex-3]
            self.currentState[self.EmptyIndex-3] = 0
            self.EmptyIndex = self.EmptyIndex-3
            return True
    
    def left(self):
        if self.EmptyIndex==0 or self.EmptyIndex==3 or self.EmptyIndex==6:
            print("cannot move")
            return False
        else:
            self.prevState = copy.deepcopy(self)
            self.currentState[self.EmptyIndex] = self.currentState[self.EmptyIndex+1]
            self.currentState[self.EmptyIndex+1] = 0
            self.EmptyIndex = self.EmptyIndex+1
            return True
    
    def right(self):
        if self.EmptyIndex==2 or self.EmptyIndex==5 or self.EmptyIndex==8:
            print("cannot move")
            return False
        else:
            self.prevState = copy.deepcopy(self)
            self.currentState[self.EmptyIndex] = self.currentState[self.EmptyIndex-1]
            self.currentState[self.EmptyIndex-1] = 0
            self.EmptyIndex = self.EmptyIndex-1
            return True

    def EmptyTileIndex(self):
        for i in range(0,9):
            if self.currentState[i]==0:
                return i

    def displayState(self):
        print("------------------------------")
        for i in range(0,8,3):
            print(self.currentState[i],self.currentState[i+1],self.currentState[i+2])
        print("-----------------------------")

    def isGoalReached(self):
        return self.currentState == goalState

startState=[7,2,4,5,0,6,8,3,1]
goalState=[0,1,2,3,4,5,6,7,8]

problem = EightPuzzle(startState,goalState)
problem.displayState()
problem.up()
problem.displayState()
problem.down()
problem.displayState()
problem.left()
problem.displayState()
problem.right()
problem.displayState()