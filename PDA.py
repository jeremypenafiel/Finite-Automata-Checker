from typing import List
from collections import deque
from State import State
from Transition import Transition

class PDA:
    def __init__(self) -> None:
        self.gamma: deque[str] = deque()
        self.transitions: List[Transition] = list()
        self.gamma.append("Z")

    def delta(self, string_input: str, initial_state: State) -> bool:
        """Accepts or rejects a string based on the transition functions and prints transitions and stack at each step

        Args:
            string_input (str): string to be accepted or rejected
            initial_state (State): initial state of the PDA

        Returns:
            bool: True if string is accepted, False otherwise
        """        

        currentState: State = initial_state
        string_input += 'e'


        '''
        Loops through the string and performs the transition function
        Breaks and rejects string if no transition can be done based on current top of stack symbol and input symbol and current state 
        '''
        for symbol in string_input:
            print("---\n")
            currentState.showStack()
            transition :Transition|None = self.search_in_transitions(currentState, symbol, currentState.getTopStackSymbol())

            # No transition found
            if transition == None:
                return False
            
            print(f'Transition function\nd({currentState.rep}, {symbol}, {currentState.getTopStackSymbol()}) = ({transition.next_state.rep}, {transition.push_symbol})')
            
            # Sets the stack of next state
            next_stack: deque[str] = self.perform_stack_operations(currentState.gamma, transition.push_symbol)
            currentState = transition.next_state
            currentState.setStack(next_stack)
        
        return True

    def perform_stack_operations(self, stack: deque[str], push_symbol: str) -> deque[str]:
        """Performs stack operations based on the push symbol

        Args:
            stack (deque[str]): stack of the state
            push_symbol (str): symbols to be pushed to the stack

        Returns:
            deque[str]: stack after performing the operations
        """        
        stack.pop()
        if push_symbol == "e":
            return stack
        
        for symbol in reversed(push_symbol):
            stack.append(symbol)

        return stack
    
    def search_in_transitions(self, current_state: State, input_symbol: str, stack_top_symbol: str) -> Transition|None:
        """Searches for a transition in the list of transitions

        Args:
            current_state (State): current state
            input_symbol (str): current input symbol
            stack_top_symbol (str): current top of stack symbol

        Returns:
            Transition|None: Transition object if found, None otherwise
        """        
        
        for transition in self.transitions:
            if transition.current_state == current_state and transition.input_symbol == input_symbol and transition.pop_symbol == stack_top_symbol:
                return transition
        return None
    
    def main(self) -> None:
        q0: State = State(self.gamma, "q0")
        q1: State = State(self.gamma, "q1")
        q2: State = State(self.gamma, "q2")
        q2.setFinal()

        self.transitions.append(Transition(q0, "0", "Z",  q0, "0Z"))
        self.transitions.append(Transition(q0, "0", "0",  q0, "00"))
        self.transitions.append(Transition(q0, "1", "0",  q1, "e"))
        self.transitions.append(Transition(q1, "1", "0",  q1, "e"))
        self.transitions.append(Transition(q1, "e", "Z",  q2, "Z"))

        result = self.delta("000111", q0)
        print(result)



if __name__ == "__main__":
    pda: PDA = PDA()
    pda.main()