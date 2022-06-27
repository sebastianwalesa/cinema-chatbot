class Dst:
    def __init__(self):
        self.messages = []
        self.checklist = {
            "ilosc": None,
            "tytul": None,
            "dzien": None,
            "godzina": None,
            "miejsce": None,
            "numer": None,
            
        }
        self.history = []
    
    def store(self, message):
        self.messages.append(message)

    def get_messages(self):
        return self.messages

    def get_next_question(self):
        for key, value in self.checklist.items():
            if value == None:
                return key
            
    def reset_if_needed(self,text):
        if text == "reset":
            for key in self.checklist.keys():
                self.checklist[key] = None

    
    
    def save_answer(self, slots):
        for slot in slots:
            if slot[0] == "numer":
                if (len(slot[1].replace(" ",""))) == 9:
                    self.checklist[slot[0]] = slot[1].replace(" ","")
            else:
                self.checklist[slot[0]] = slot[1]

        self.messages.append(slots)