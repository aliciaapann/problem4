import fileinput

def getTMCommands(line):
    tokens = line.strip().split()
    if len(line) == 0 or line[0] == ";" or len(tokens) < 5:
        return []
    else:
        return tokens[:5]

"""
Parses TM/PTM (from stdin)
- Return: list of line in the TM.
- Each line is list of strings (length 5): [stateIn, read, write, direction, stateOut]
  (as with Morphitt syntax)
"""
def parseInput():
    lines = list(fileinput.input())
    lines = map(lambda x: x.strip(), lines)
    lines = map(getTMCommands, lines)
    lines = [line for line in lines if len(line) > 0]
    return lines

def printTM():
    for line in lines:
        formatted_line = f"{line[0]} {line[1]} {line[2]} {line[3]} {line[4]}"
        print(formatted_line)


if __name__ == '__main__':
    # read an TM via stdin. See parser.py for details on the returned object
    lines = parseInput()

    # new states in new PTM can be 10-100 (not more than 100 states)
    new_states = []
    for i in range(11,100):
        new_states.append(str(i))
    
    #keep track of how many new states have been made
    curr_new_state = 0
                            
    # Put your code here:

    # add instructions to convert 0s to Xs
    zeros_to_Xs = [
        ['0', '0', 'X', 'R', '0'],
        ['0', '*', '*', 'R', '0'],
        ['0', '_', '_', 'L', '10'],
        ['10', '*', '*', 'L', '10'],
        ['10', '_', '_', 'R', '11']
    ]

    for line in lines:
        #change start state
        if line[0] == '0':
            line[0] = new_states[curr_new_state]
        if line [4] == '0':
            line[4] = new_states[curr_new_state]

    curr_new_state += 1

        
        

    for line in lines:
        # replace all 0s with Xs in instructions
        if line[1] == '0':
            line[1] = 'X'
        if line[2] == '0':
            line[2] == 'X'


    lines = zeros_to_Xs + lines
    # if you use the same data structure, you can use:
    printTM()
