from typing import List, Self
from collections import deque
from State import State

class PDA:
    def __init__(self) -> None:
        self.q: List[State] = list()
        self.gamma: deque[str] = deque()
        self.gamma.append("Z")

    def delta(self, input: str) -> bool:
        # TODO: 

        isAccepted: bool = False
        currentState: State = self.q[0]
        # currentState.showStack()
        print(input)
        for symbol in input:
            next_states: List[State] = currentState.delta(symbol)
            for state in next_states:
                print("State Stack:\n")
                state.showStack()
                print("\n")



                    
        return isAccepted
    
    def main(self) -> None:
        q0: State = State(self.gamma)
        q1: State = State(self.gamma)
        q0.showStack()
        q0.setTransition("0", q0, pop_symbol="Z", push_symbol="0Z")
        q0.showStack()

        # q0.setTransition("0", q0, pop_symbol="0" , push_symbol="00")

        self.q.append(q0)
        self.q.append(q1)


        # isAccepted: bool = self.delta("0")

    def push_to_stack(self, symbol: str, state: State) -> None:
        self.gamma.append(symbol)

if __name__ == "__main__":
    pda: PDA = PDA()
    pda.main()