import jsgf
from os import listdir
from os.path import isfile, join

mypath = "./grammar/"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

grammars = []

for grammarFile in onlyfiles:
    grammar = jsgf.parse_grammar_file(mypath + grammarFile)
    grammars.append(grammar)
        

def get_dialog_act(rule):
    slots = []
    get_slots(rule.expansion, slots)
    return {'act': rule.grammar.name, 'slots': slots}

def get_slots(expansion, slots):
    if expansion.tag != '':
        slots.append((expansion.tag, expansion.current_match))
        return

    for child in expansion.children:
        get_slots(child, slots)

    if not expansion.children and isinstance(expansion, jsgf.NamedRuleRef):
        get_slots(expansion.referenced_rule.expansion, slots)

def nlu(utterance):
    matched = None
    for grammar in grammars:
        matched = grammar.find_matching_rules(utterance)
        if matched:
            break

    if matched:
        return get_dialog_act(matched[0])
    else:
        return {'act': 'null', 'slots': []}
    
def preprocess(text):
    text = text.lower()
    text = text.replace("ą","a")
    text = text.replace("ę","e")
    text = text.replace("ó","o")
    text = text.replace("ł","l")
    text = text.replace("ć","c")
    text = text.replace("ń","n")
    text = text.replace("ś","s")
    text = text.replace("ą","a")
    text = text.replace("ż","z")
    text = text.replace("ź","z")
    text = text.replace("ą","a")
    text = text.replace(".","")
    text = text.replace("?","")
    text = text.replace("!","")
    text = text.replace(":"," ")
    
    
    return text

    
def ajn(text):
    frame = nlu(preprocess(text))
    return frame
