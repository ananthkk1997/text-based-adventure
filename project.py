
from data import *

try:
    import readline
except ImportError:
    pass

import subprocess
subprocess.call(["printf", "'\033c'"])
###########
# Parsing #
###########


def adv_parse(line):
    tokens = line.split()
    if not tokens:
        raise SyntaxError('No command given')
    command = tokens.pop(0)
    if command in ('talk', 'go'):
        if not tokens or tokens[0] != 'to':
            raise SyntaxError('Did you mean "{}"?'.format(COMMAND_FORMATS[command]))
        return (command + '_to', ' '.join(tokens[1:]))
    elif command == 'check':
        if len(tokens) == 0:
            raise SyntaxError('Please type a correct command.')
        if tokens[0] == 'supplies':
            return ('check_supplies', '')
        elif tokens or tokens[0] == 'items':
            return ('check_items', '')
        else:
            raise SyntaxError('Did you mean "{0}" or "{1}"?'.format(COMMAND_FORMATS['check items'], COMMAND_FORMATS['check supplies']))
    elif command == 'unlock':
        return ('unlock', ' '.join(tokens))
    elif command == 'cast':
        return ('cast',' '.join(tokens))
    elif command == 'buy':
        return ('buy', ' '.join(tokens))
    #elif command == 'spells':
        #if tokens or tokens[0] != 'learned':
            #raise SyntaxError('Did you mean "{}"?'.format(COMMAND_FORMATS[command]))
    else:
        return (command, ' '.join(tokens))

##############
# Evaluation #
##############

def adv_eval(exp):
    operator, operand = exp[0], exp[1]
    if operator not in COMMAND_NUM_ARGS:
        help()
        raise SyntaxError('Invalid command: {}'.format(operator))
    elif operator in SPECIAL_FORMS:
        function = SPECIAL_FORMS[operator]
    else:
        function = getattr(me, operator)

    if COMMAND_NUM_ARGS[operator] == 0:
        function()
    else:
        function(operand)

def help():
    print('There are {} possible commands:'.format(len(COMMAND_FORMATS)))
    for usage in COMMAND_FORMATS.values():
        print('   ', usage)
    print("\nAlso, for long location names, simply type the first Key word of the desired location for command 'go to [place]'"
            "\n\nExample: 'go to Leaky' will take you to the Leaky Couldron")

def check_win_state(player):
    """Checks if the player is in a winning state."""
    if not player.has_wand:
        return False

    print()
    player_items = player.items
    for item in player.supply_list:
        if item not in player_items:
            return False
    return True

def welcome_loop(level):
    if level == 0:
        print(game_chapters[level][0])
        for i in game_chapters[level][1:]:
            line = input('hit Enter to continue>')
            if type(line) == str:
                import subprocess
                subprocess.call(["printf", "'\033c'"])
                print(i)
        levels_unlocked[level] = True
    elif levels_unlocked[level] == 'Next' and levels_unlocked[level-1] == True:
        print(game_chapters[level][0])
        for i in game_chapters[level][1:]:
            line = input('hit Enter to continue>')
            if type(line) == str:
                import subprocess
                subprocess.call(["printf", "'\033c'"])
                print(i)
        levels_unlocked[level] = True

########
# REPL #
########

def read_eval_print_loop():
    for level in levels_unlocked:
        welcome_loop(level)
    help()
    while True:
        if check_win_state(me):
            print(WIN_MESSAGE)
            return
        print()
        try:

            line = input('command> ')
            exp = adv_parse(line)
            import subprocess
            subprocess.call(["printf", "'\033c'"]) #This line cleares the screen each time
                                                   #a command is entered. Delete this lines if desired
            adv_eval(exp)
        except (KeyboardInterrupt, EOFError, SystemExit): # If you ctrl-c or ctrl-d
            print('\nGood game. Bye!')
            return
        # If the player input was badly formed or if something doesn't exist
        except SyntaxError as e:
            print('ERROR:', e)

#################
# Configuration #
#################

COMMAND_FORMATS = {
    'look': 'look',
    'go': 'go to [place]',
    'take': 'take [thing]',
    'talk': 'talk to [character]',
    'check items': 'check items',
    'help': 'help',
    'unlock': 'unlock [place]',
    'cast': 'cast [spell]',
    'check supplies': 'check supplies'
}

COMMAND_NUM_ARGS = {
    'look': 0,
    'go_to': 1,
    'take': 1,
    'talk_to': 1,
    'check_items': 0,
    'check_supplies': 0,
    'help': 0,
    'unlock': 1,
    'cast': 1

}

SPECIAL_FORMS = {
    'help': help,
}



WIN_MESSAGE = """
Congratulations! You collected all of your school supplies.
\nLevel 2 Unlocked!
"""


if __name__ == '__main__':
    read_eval_print_loop()
