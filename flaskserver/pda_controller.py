from PDA import PDA


class PDAController:

    def __init__(self):
        self.pda = PDA()
        self.input_string: str = ""
        self.states: list[str] = list()
        self.final_states: list[str] = list()
        self.rules: list[str] = list()

    def handle_data(self, request_form: dict[str, str]) -> dict[str, list[str]]:
        keys_to_remove: list[str] = list()
        mutable_dict: dict = request_form.to_dict()

        for key in request_form:
            # print(key)
            if key == "InputString":
                self.input_string = request_form[key]
                keys_to_remove.append(key)
            elif key[0:5] == 'State':
                self.states.append(request_form[key])
                keys_to_remove.append(key)
        
        for key in keys_to_remove:
            del mutable_dict[key]

        keys_to_remove.clear()

        for key in mutable_dict:
            if key[0:10] == 'FinalState':
                for state in self.states:
                    if key[10] in state:
                        self.final_states.append(state)
                        keys_to_remove.append(key)
        print(mutable_dict)
        for key in keys_to_remove:
            del mutable_dict[key]
        
        for index in range(0, len(mutable_dict), 5):
            self.rules.append(list(mutable_dict.values())[index:index+5])


        return_dict: dict[str, list[str]] = dict()
        return_dict['input_string'] = self.input_string
        return_dict['states'] = self.states
        return_dict['final_states'] = self.final_states
        return_dict['rules'] = self.rules

        return return_dict

     
    def init_pda(self, data: dict[str, list[str]]) -> bool:

        for state in data['states']:
            self.pda.add_state(state)
        
        for final_state in data['final_states']:
            self.pda.set_final_state(final_state)
        
        for rule in data['rules']:
            state = self.pda.states[rule[0]]
            state.setTransition(rule[1], rule[2], self.pda.states[rule[3]], rule[4])

        result = self.pda.delta(data['input_string'], self.pda.states[data['states'][0]])
        return result
        