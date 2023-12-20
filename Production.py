from typing import List
import random

class Production:
    def __init__(self, head: str, body: List[str]) -> None:
        self.head: str = head
        self.body: List[str] = body
        self.weights: List[float] = list()
        self.set_weights()
    
    def set_weights(self) -> None:
        """Sets the weights of the productions
        """        
        HIGHER_WEIGHT: float = 1
        LOWER_WEIGHT: float = 0.8

        for production in self.body:
            higher_char_found: bool = False

            for letter in production:
                if letter.isupper():
                    higher_char_found = True
                    break

            if higher_char_found:
                self.weights.append(LOWER_WEIGHT)
            else:
                self.weights.append(HIGHER_WEIGHT)
            


    def translate(self) -> str:
        """Returns a randomly chosen body with a bias towards a body with all nonterminals

        Returns:
            str: body of the production
        """        

        returned_body:List[str] = random.choices(self.body, weights=self.weights, k=1)

        return returned_body[0]

    def isHead(self, symbol: str) -> bool:
        """Returns True if symbol is the head of the production, False otherwise

        Args:
            symbol (str): current symbol in string

        Returns:
            bool: True if symbol is the head of the production, False otherwise
        """        
        return self.head == symbol
    

def main() ->None:
    S: Production = Production("S", ["aXa"])
    X: Production = Production("X", ["aaXaa", "b"])

    print(S.translate())
    print(X.translate())


if __name__ == "__main__":
    main()