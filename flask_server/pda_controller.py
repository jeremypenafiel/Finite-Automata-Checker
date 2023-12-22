from PDA import PDA


class PDAController:

    def __init__(self):
        self.pda = PDA()
        self.input_string: str = ""
        self.states: list[str] = list()
        self.final_states: list[str] = list()
        self.rules: list[str] = list()

    def handle_data(self, request_form):
        keys_to_remove: list[str] = list()
        mutable_dict: dict = request_form.to_dict()

        for key in request_form:
            if key == "InputString":
                self.input_string = request_form[key]
                keys_to_remove.append(key)
            elif key[0:5] == 'State':
                self.states.append(request_form[key])
                keys_to_remove.append(key)
            elif key[0:10] == 'FinalState':
                self.final_states.append(request_form[key])
                keys_to_remove.append(key)
        
        for key in keys_to_remove:
            del mutable_dict[key]
        
        for index in range(0, len(mutable_dict), 5):
            self.rules.append(list(mutable_dict.values())[index:index+5])


        print(self.input_string)
        print(self.states)
        print(self.final_states)
        print(self.rules)
 
        
        