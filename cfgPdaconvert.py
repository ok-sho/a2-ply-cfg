cfgExample = {
    'S': [['a', 'S', 'b'], []], 'A':[['x'],['S']]
}

inputString = 'aabb'

def cfg_PdaConvert(cfg, startSymbol, inputString):
    #List that will hold each letter
    inputSequence = list(inputString)

    #Iterates through each symbol in the cfg
    #Set for terminals
    terminals = set()
    #For each list of productions
    for prods in cfg.values():
        #For each production
        for prod in prods:
            #For each symbol in production
            for sym in prod:
                if sym not in cfg:
                    terminals.add(sym)
    stepCount = [0]
    #pda fnc take in the cfg stack and the remaining letters of the input string
    def pda(stack, remainingInput):
        stepCount[0] += 1


        print(f"\n----------Step {stepCount[0]}:----------")
        print(f"\nStack:{stack}, Input: {remainingInput}")

        #If stack is empty and there's no more string return true
        if not stack and not remainingInput:
            return True
        #If the stack is empty but there is still string return false
        if not stack:
            return False

        #Top of the stack
        top = stack[-1]

        #Check if the top symbol is a terminal
        if top in terminals:

            #Check if the input symbol is at the top of the stack
            if remainingInput and top == remainingInput[0]:
                #Call function again this time with stack without last element and remove first symbol from the input

                return pda(stack[:-1], remainingInput[1:])

            else:
                #If it can't call again return false
                return False
        else:
            # If the top is  non-terminal try all its productions
            for production in cfg.get(top, []):
                # Handle epsilon production explicitly
                if production == [''] or production == [' ']:  # Empty means epsilon
                    new_stack = stack[:-1]
                else:
                    # Put production symbols on the stack (reversed)
                    new_stack = stack[:-1] + production[::-1]
                # Call PDA with this new stack and the same input
                if pda(new_stack, remainingInput):
                    # If any production leads to acceptance return True
                    return True
            return False

    result = pda([startSymbol], inputSequence)

    if result:
        return "String is ACCEPTED"
    else:
        return "String is REJECTED"



print("\n----------Case where grammar =  'S': [['a', 'S', 'b'], []], 'A':[['x'],['S']] and input string = aabb----------")
print(cfg_PdaConvert(cfgExample, 'S', inputString))  # True
