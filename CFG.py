from typing import List
from Production import Production

class CFG:
    def __init__(self) -> None:
        self.p: List[Production] = list()
    
    def produce(self, start_production:Production) -> str:
        """Returns the final string produced by the grammar

        Returns:
            str: final string produced by the grammar
        """        
        final_string: str = ""
        current_production: Production = start_production
        final_string += current_production.translate()
        index: int = 0

        print(f'Starting string: {final_string}')

        while index < len(final_string):
            letter = final_string[index]
            if letter.isupper():
                for production in self.p:
                    if production.isHead(final_string[index]):
                        final_string = final_string[:index] + production.translate() + final_string[index + 1:]
                        print(final_string)
                        break
                index = 0
                continue
            index += 1

        return final_string

    def main(self) -> None:
        """Main function of the class
        """        
        S: Production = Production("S", ["aCEB", "bBCB", "bCEB", "aB", "bB", "a", "b"])
        A: Production = Production("A", ["bB", "a", "b"])
        B: Production = Production("B", ["a", "b"])
        C: Production = Production("C", ["aCE", "bBC", "bCE", "a", "b"])
        E: Production = Production("E", ["a"])
        F: Production = Production("F", ["b"])
        
        self.p.append(S)
        self.p.append(A)
        self.p.append(B)
        self.p.append(C)
        self.p.append(E)
        self.p.append(F)
        
        result = self.produce(start_production=S)
        print(f'Final string: {result}')


def main() -> None:
    cfg: CFG = CFG()
    cfg.main()

if __name__ == "__main__":
    main()