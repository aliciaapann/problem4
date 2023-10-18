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

    right_old_states = []
    left_old_states = []

    # new states in new PTM can be 10-100 (not more than 100 states
    #keep track of how many new states have been made
    curr_new_state = 10

    def create_right_portal(curr_new_state, old_state):
        portal = str(curr_new_state)
        wrap = str(curr_new_state + 1)
        right_portal = [
            [portal, '*', '*', 'R', portal],
            [portal, '_', '_', 'L', wrap],
            [wrap, '*', '*', 'L', wrap],
            [wrap, '_', '_', 'R', portal],
            [portal, '0', '0', '*', old_state]
        ]

        return right_portal
    
    def create_left_portal(curr_new_state, old_state):
        portal = str(curr_new_state)
        wrap = str(curr_new_state + 1)
        left_portal = [
            [portal, '*', '*', 'R', portal],
            [portal, '_', '_', 'L', wrap],
            [wrap, '*', '*', 'L', wrap],
            [wrap, '_', '_', 'R', portal],
            [portal, '0', '0', '*', old_state]
        ]

        return left_portal
        

    #If a 0 is written, check move instruction and move to next 0
    for line in lines: 
        if line[2] == '0' and line[3] == 'R':
            old_state = line[4]
            #send to portal state (right)
            line[4] = str(curr_new_state)
            lines = lines + create_right_portal(curr_new_state, old_state)
            curr_new_state += 2

        if line[2] == '0' and line[3] == 'L':
            old_state = line[4]
            #send to portal state (left)
            line[4] = str(curr_new_state)
            lines = lines + create_left_portal(curr_new_state, old_state)
            curr_new_state += 2

    # if you use the same data structure, you can use:
    printTM()
