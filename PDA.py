from typing import List
from collections import deque
from State import State
from Transition import Transition

class PDA:
    def __init__(self) -> None:
        self.q: List[State] = list()
        self.gamma: deque[str] = deque()
        self.transitions: List[Transition] = list()

        self.gamma.append("Z")

    def delta(self, string_input: str, initial_state: State) -> bool:
        # TODO: 

        isAccepted: bool = False
        currentState: State = initial_state
        string_input += 'e'
        print(string_input)
        for symbol in string_input:
            print("---\n")
            currentState.showStack()
            for transition in self.transitions:
                if (transition.current_state == currentState and 
                    transition.input_symbol == symbol and 
                    transition.pop_symbol == currentState.getStackSymbol()):
                        print(f'd({currentState.rep}, {symbol}, {currentState.getStackSymbol()}) = ({transition.next_state.rep}, {transition.push_symbol})')
                        next_stack: deque[str] = self.perform_stack_operations(currentState.gamma, transition.push_symbol)
                        currentState = transition.next_state
                        currentState.setStack(next_stack)
                        break
        
        print(currentState)
        isAccepted = currentState.f
        return isAccepted

    def perform_stack_operations(self, stack: deque[str], push_symbol: str) -> deque[str]:
        stack.pop()
        if push_symbol == "e":
            return stack
        
        for symbol in reversed(push_symbol):
            stack.append(symbol)

        return stack
    
    def search_in_transitions(self, current_state: State, input_symbol: str, stack_top_symbol: str) -> Transition|None:
        for transition in self.transitions:
            if transition.current_state == current_state and transition.input_symbol == input_symbol and transition.pop_symbol == stack_top_symbol:
                return transition
        return None
    
    def main(self) -> None:
        q0: State = State(self.gamma, "q0")
        q1: State = State(self.gamma, "q1")
        q2: State = State(self.gamma, "q2")
        q2.setFinal()

        self.transitions.append(Transition(q0, q0, "0", "0Z", "Z"))
        self.transitions.append(Transition(q0, q0, "0", "00", "0"))
        self.transitions.append(Transition(q0, q1, "1", "e", "0"))
        self.transitions.append(Transition(q1, q1, "1", "e", "0"))
        self.transitions.append(Transition(q1, q2, "e", "Z", "Z"))

        result = self.delta("0011", q0)
        print(result)



if __name__ == "__main__":
    pda: PDA = PDA()
    pda.main()