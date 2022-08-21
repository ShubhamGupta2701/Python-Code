from turtle import hideturtle
from Lab_evaluation import forteenPuzzle
class HillClimbing:
    def __init__(self,initial,goal):
        self.currentState = initial
        self.goalState = goal
        self.EmptyIndex = self.EmptyTileIndex()
        self.prevState = None
    
    h_value = 5
    def check(self):
        for i in range(0,16):
            if self.currentState[i] != self.goalState[i]:
                self.h_value -= 1
    while check.self.h_value == 0:
        if h_value < 5:
            def up(self):
                if self.EmptyIndex == 12 or self.EmptyIndex == 13 or self.EmptyIndex == 14 or  self.EmptyIndex == 15:
                    print("can not move")
                else:
                    self.prevState = self.currentState
                    self.currentState[self.EmptyIndex] = self.currentState[self.EmptyIndex + 4]
                    self.currentState[self.EmptyIndex+4] = 0
                    self.EmptyIndex = self.EmptyIndex+4
                    return True

            def down(self):
                if self.EmptyIndex == 0 or self.EmptyIndex == 1 or self.EmptyIndex == 2 or  self.EmptyIndex == 3:
                    print("can not move")
                else:
                    self.prevState = self.currentState
                    self.currentState[self.EmptyIndex] = self.currentState[self.EmptyIndex + 4]
                    self.currentState[self.EmptyIndex+4] = 0
                    self.EmptyIndex = self.EmptyIndex+4
                    return True

            def left(self):
                if self.EmptyIndex==0 or self.EmptyIndex==4 or self.EmptyIndex==8 or self.EmptyIndex == 12:
                    print("cannot move")
                    return False
                else:
                    self.prevState = self.currentState
                    self.currentState[self.EmptyIndex] = self.currentState[self.EmptyIndex+1]
                    self.currentState[self.EmptyIndex+1] = 0
                    self.EmptyIndex = self.EmptyIndex+1
                    return True
            
            def right(self):
                if self.EmptyIndex==2 or self.EmptyIndex==6 or self.EmptyIndex==10 or self.EmptyIndex == 14:
                    print("cannot move")
                    return False
                else:
                    self.prevState = self.currentState
                    self.currentState[self.EmptyIndex] = self.currentState[self.EmptyIndex-1]
                    self.currentState[self.EmptyIndex-1] = 0
                    self.EmptyIndex = self.EmptyIndex-1
                    return True

            def EmptyTileIndex(self):
                for i in range(0,16):
                    if self.currentState[i]==0:
                        return i

            def displayState(self):
                print("------------------------------")
                for i in range(0,16,4):
                    print(self.currentState[i],self.currentState[i+1],self.currentState[i+2],self.currentState[i+3])
                print("-----------------------------")

            def isGoalReached(self):
                return self.currentState == goalState

startState=[1,3,0,4,5,2,7,8,9,6,10,12,13,14,11,0]
goalState=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,0,0]

while HillClimbing.isGoalReached != True:
    problem = forteenPuzzle(startState,goalState)
    problem.displayState()
    problem.up()
    problem.displayState()
    problem.down()
    problem.displayState()
    problem.left()
    problem.displayState()
    problem.right()
    problem.displayState()
