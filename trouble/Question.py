class YesNoQuestion():
    def __init__(self, text, outcomes):
        self.text = text
        self.outcomes = outcomes

    def answer_to_boolean(self, answer):
        if answer.lower() == 'yes' or answer.lower() == 'y':
            return True
        if answer.lower() == 'no' or answer.lower() == 'n':
            return False
        else:
            return None

    def ask(self):
        valid = False

        while not valid:
            answer = input(self.text + ' (yes/no) > ')
            answer = self.answer_to_boolean(answer)

            if answer == None:
                print("Invalid answer")
            else:
                valid = True

        found = False
        for outcome in self.outcomes:
            if outcome.option == answer:
                found = True;
                outcome.result.ask()

        if not found:
            print ("Error: No result could be found for the option you entered.")
            raise Exception