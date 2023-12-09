from types import NoneType
from typing import List, Self
from collections import deque

class State:
    def __init__(self, stack: deque[str]):
        self.f: bool =  False
        self.gamma: deque[str] = stack
        self.next: List[List[State]] = []

    def delta(self, symbol: str) -> List[Self]:
        '''Returns next states given input symbol.'''
        
        return self.next[int(symbol)]
    
    def setTransition(self, input_symbol: str, next_state: Self, push_symbol: str, pop_symbol:str|None = None):
        '''Sets transition to the next state'''

        self.gamma.append(push_symbol)
        # self.next[int(input_symbol)] = [next_state]
        # if pop_symbol != None:
        #     self.gamma.pop()
        # if push_symbol[-1] == self.getStackSymbol() and len(push_symbol) > 1:
        #     self.gamma.append(push_symbol[-1])
        # if pop_symbol != None:
        #     next_state.gamma.pop()
        
        # if push_symbol != None and len(push_symbol) > 1:
        #     for letter in push_symbol:
        #         next_state.gamma.append(letter)

        # self.next.insert(int(input_symbol), [next_state])

    def setFinal(self) -> None:
        '''Sets self.f to True if state is a final state'''
        self.f = True

    def getStackSymbol(self) -> str:
        '''Returns top of the stack'''
        return self.gamma[-1]
    
    def showStack(self) -> None:
        for symbol in reversed(self.gamma):
            print(f'|{symbol}|\n')



