from typing import List, Self
from collections import deque

class State:
    def __init__(self, stack: deque[str]):
        self.f: bool =  False
        self.gamma: deque = stack
        self.next: List[List[State]] = []

    def delta(self, symbol: str) -> List[str]:
        '''Returns next states given input symbol.'''
        output = list()


        return output
    
    def setTransition(self, input_symbol: str, pop_symbol:str, next_state: Self, push_symbol: str):
        self.next.append([self, next_state])
        pass

    def setFinal(self) -> None:
        '''Sets self.f to True if state is a final state'''
        self.f = True

    def getStackSymbol(self) -> str:
        '''Returns top of the stack'''
        return self.gamma[-1]
    
    def showStack(self) -> None:
        print(self.gamma)



