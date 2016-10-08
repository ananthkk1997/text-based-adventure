# CS 61A World Game Data:
from classes import *

# Characters:

hagrid = Character('Hagrid',
                 "Welcome to Diagon Alley! "
                  "\nTry finding all the items on your Hogwarts suppy list.")
ollivander = Character('Ollivander',
                  'Remember Mr. Potter, the wand chooses the wizard. '
                  '\nCurious.. Very Curious..')
griphook = Character('Griphook', 'Vault 713!')
diggle = Character('Dedalus Diggle', 'Delighted, Mr. Potter, just cant tell you. '
                    "\nDiggle's the name, Dedalus Diggle")
quirrell = Character ('Prof Quirrell', 'P-P-Potter. '
                        '\nC-cant t-tell you how p-pleased I am to meet you.')
bartender = Character('Tom the Bartender', 'Good Lord, is this - can this be--? '
                        '\nBless my soul. Harry Potter.. what an honor.')
borgin = Character('Borgin', 'Knockturn Alley is no place for a litle boy.'
                    '\nNow get out of my shop!')
creepy_witch = Character('Witch', 'Lost, are we little boy?')
creepy_wizard = Character('Wizard', "..He's back.. I know He's back.. ")


# Things:

book1_random = Thing('Book 1',"'Curses and Countercurses' by Professor Vindictus")
book1_history = Thing('Book 2', "'A History of Magic' by Bathilda Bagshot")
book1_care = Thing('Book 3', "'Fantastic Beasts and Where to Find Them' by Newt Scamander")
book1_defense = Thing('Book 4', "'Standard Book of Spells (Grade 1)' by Miranda Goshawk")
money1 = Money(1)
money2 = Money(2)
quill = Thing('Quill', 'a feathered writing utensil')
ink = Thing('Ink', 'a bottle of ink for quills')
parchment = Thing('Parchment', 'a roll of writing material')
telescope = Thing('Telescope', 'a collapsible brass telescope')
couldron = Thing('Couldron', 'a size 2, pewter couldron for mixing potions')
scales = Thing('Scales', 'a brass set of scales for weighing potion ingredients')
wand_1 = Thing('Wand 1', 'a flexible Beechwood wand with a Dragon Heartstring core - 9 inches.',
                "You wave the wand. Behind Mr. Ollivander, boxes of wands fly off the shelves." +
                " It doesnt feel quite right.")
wand_2 = Thing('Wand 2', 'a springy Ebony wand with a Unicorn Hair core - 8.5 inches.',
                "You wave the wand and the glass jar on the counter explodes." +
                " It doesnt feel quite right.")
wand_3 = Thing('Wand 3', 'a supple Holly wand with a Phoenix Feather core - 11 inches.',
                action = None, message = "\nYou wave the wand and feel a sudden warmth in your fingers." +
                "Red and gold sparks shoot from the end of the wand like fireworks. Mr. Ollivander says: 'Curious.. Very Curious' ")
wand_4 = Thing('Wand 4', 'a whippy Maple wand with a Phoenix Feather core - 7 inches.',
                  " It doesnt feel quite right. Mr. Ollivander snatches it away.")
nimbus_2000 = Thing('Nimbus 2000', 'the fastest racing broomstick in the world!',
                "\nSorry! You don't have enough money.' ")
hand_of_glory = Thing('Hand of Glory',
                                'a large shriveled hand.. it seems harmless',
                                action = 'The Hand latches onto your arm!'
                                        '\n\nYou struggle to break free until it finally lets go.')

#Supply List:
supply_list = [book1_care, book1_defense, book1_history, quill, parchment,
            ink, telescope, couldron]
#Keys:
try:
    skeleton_key = Key('Skeleton Key', 'A key that unlocks many doors')
except NameError as e:
    skeleton_key = Thing('Not a Skeleton Key', 'You must first implement the Key class')

#Places:
leaky_couldron = Place( 'Leaky', "A popular wizarding pub and inn hidden in London",
                        [diggle, bartender, quirrell], [money1], 'The Leaky Couldron')
flourish = Place('Flourish', "Get your spell books here!",
                    [],[book1_random, book1_defense], 'Flourish and Blotts')
diagon = Place('Diagon', 'The centre of the Wizarding World!',
                [hagrid], [nimbus_2000], 'Diagon Alley')
ollivanders = Place('Ollivanders', 'Makers of Fine Wands since 382 B.C',
                    [ollivander], [wand_1, wand_2, wand_3, wand_4],'Ollivanders Wands')
knockturn  = Place('Knockturn', 'A dark, mysterious place...',
                    [creepy_witch, creepy_wizard], [money2], 'Knockturn Alley')
scribb = Place('Scribbulus', 'Seller of writing supplies',
                [], [parchment, ink, quill], 'Scribbulus Writing Instruments')
borgin_burkes = Place('Borgin', 'An unusual antique shop',
                        [borgin], [hand_of_glory, telescope], 'Borgin and Burkes')
obscurus = Place('Obscurus', 'A wizarding book publisher',
                    [], [book1_care, book1_history], 'Obscurus Books')
wiseacre = Place("Wiseacre's", 'A miscellaneous magical equipment shop',
                    [], [scales, couldron], "Wiseacre's Wizarding Equipment" )
#Welcome:
message1_1 = """\nWelcome to the Wizarding World of Harry Potter!

This game is meant to follow the storyline of Harry Potter and the Philosopher's
Stone. Use keyboard commands to progress through the book, unlock new levels, and
complete the story!\n"""

message1_2 = """\nIntroduction:\n\nThe most evil and powerful dark wizard in history, Lord Voldemort,
murdered married couple James and Lily Potter but mysteriously disappeared after
attempting to kill their infant son, Harry. While the wizarding world celebrates
Voldemort's demise, Professor Dumbledore, Professor McGonagall and
half-giant Rubeus Hagrid, of Hogwarts School of Witchcraft and Wizardry, secretly
leave one-year-old Harry in the care of his only living relatives.. the Dursleys.
 """
message1_3 = """\nMr. and Mrs. Dursley, of number four, Privet Drive, were proud to say
that they were perfectly normal, thank you very much. They were the last
people you'd expect to be involved in anything strange, mysterious, or magical
because they just didn't hold with such 'nonsense'.\n"""

message1_4 = """\nNearly ten years had passed since the Dursleys had woken up to find
their nephew on the front step. Harry was now a thin bespeckled boy, with jet-black
hair and green eyes. His glasses were held together by sellotape because Dudley Dursley
had smashed them so many times. The thing that distinguished Harry the most was the
lightning-bolt scar on his forehead. Harry often wondered how he got it, but he
never dared to ask -- the Dursleys' first rule was to never ask questions. \n"""

message1_5 = """\nBut the Dursleys could only keep out what they called 'nonsense' for so long.
The problem was, strange things often happened around Harry and there was simply
no explanation for them -- everything from ever-shrinking clothing, teleportation,
to even talking to snakes! Harry was bound to discover the truth.\n"""

message1_6 = """\nAfter 11 years in the Muggle world, You, Harry, are now face to face with
reality. The half-giant Rubeus Hagrid comes to tell you himself:\n\nHarry, you're a wizard!\n
He hands you a letter... \n """

message1_7 = """ \nMr. H. Potter\nThe Cupboard under the Stairs\n4 Privet Drive\nLittle Whinging\nSurrey\n
\n
Headmaster: Albus Dumbledore\n(Order of Merlin, First Class, Grand Sorc., Chf. Warlock,
Supreme Mugwump, International Confed. of Wizards)\n\n
Dear Mr. Potter,\n\n
   We are pleased to inform you that you have been accepted at Hogwarts School of
Witchcraft and Wizardry. Please find enclosed a list of all necessary books and
equipment. Term begins on September 1. We await your owl by no later than July 31.\n\n
Yours sincerely,\n\nMinerva McGonagall\nDeputy Headmistress\n """
message1_8 = """\nGo with Hagrid to find your school supplies and enter the Wizarding
World!\n"""

message1_9 = """Welcome to the Leaky Couldron! Use the following commands to explore.\n\n"""

chapter1_messages = [message1_1, message1_2, message1_3, message1_4, message1_5,
                    message1_6, message1_7, message1_8, message1_9]

game_chapters = {0: chapter1_messages }
levels_unlocked = {0: 'Next'}





#Exits:
diagon.add_exits([flourish, ollivanders, knockturn, scribb, obscurus, wiseacre, leaky_couldron])
leaky_couldron.add_exits([diagon])
scribb.add_exits([diagon])
flourish.add_exits([diagon])
ollivanders.add_exits([diagon])
obscurus.add_exits([diagon])
borgin_burkes.add_exits([knockturn])
wiseacre.add_exits([diagon])
knockturn.add_exits([diagon, borgin_burkes])
# Exits:



# Locked Buildings
#fsm.locked = True

# Player:
# The Player should start at Level 1, Leaky Couldron
me = Player('Ananth', leaky_couldron)
me.supply_list = supply_list
