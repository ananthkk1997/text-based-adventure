# A "simple" adventure game.

from data import *

class Player(object):
    def __init__(self, name, place):
        """Create a player object."""
        self.name = name
        self.place = place
        self.has_wand = False
        self.items = []
        self.spells = {}
        self.money = 0

    def look(self):
        self.place.look()

    def go_to(self, location):
        """Go to a location if it's among the exits of player's current place.
        """
        destination_place = self.place.get_neighbor(location)
        if destination_place.locked:
            print(destination_place.name, 'is locked! Go look for a key to unlock it')
        elif destination_place == self:
            print("Can't go to ", location, "from ", self.place, ".")
            print("Try looking around to see where to go.")
        else:
            self.place = destination_place
        print("You are at " + self.place.nickname)
        self.place.look()


    def talk_to(self, person):
        """Talk to person if person is at player's current place.
        """
        if type(person) != str:
            print('Person has to be a string.')
        elif person in self.place.characters:
            print(person + " says: " + '\n\n' + self.place.characters[person].talk())
        else:
            print(person + " is not here.")

    def take(self, thing):
        """Take a thing if thing is at player's current place
        """
        if type(thing) != str:
            print('Thing should be a string.')
        elif thing in self.place.things:
            if self.place.things[thing].action == None:
                print(self.name + " takes the " + thing)
                a = self.place.things[thing]
                if isinstance(a, Money):
                    self.money += a.amount
                else:
                    self.items.append(a)
                    if 'Wand' in thing:
                        self.has_wand = True
                if self.place.things[thing].message != None:
                    print(self.place.things[thing].message)
                self.place.take(thing)
            #elif isinstance(self.place.things[thing], Good):
                #self.characters[Shopkeeper].talk()

            else:
                print(self.place.things[thing].action)



        else:
            print(thing + " is not here.")


    def check_items(self):
        """Print each item with its description and return a list of item names.

        """
        print('Your inventory:')
        if not self.items:
            print('    there is nothing.')
        else:
            for item in self.items:
                if not isinstance(item, Money):
                    print('   ', item.name, '-', item.description)

        print('Money:')
        print('    {} Galleons'.format(self.money))
        return [item.name for item in self.items]

    def check_supplies(self):
        print('\nHogwarts School of Witchcraft and Wizardry')
        print('\nFirst year students will require:\n')
        for supply in self.supply_list:
            print('    ', supply.name, ' - ', supply.description)

    def unlock(self, place):
        """If player has a key, unlock a locked neighboring place.

        >>> key = Key('SkeletonKey', 'A Key to unlock all doors.')
        >>> gbc = Place('GBC', 'You are at Golden Bear Cafe', [], [key])
        >>> fsm = Place('FSM', 'Home of the nectar of the gods', [], [])
        >>> gbc.add_exits([fsm])
        >>> fsm.locked = True
        >>> me = Player('Player', gbc)
        >>> me.unlock(fsm)
        Place must be a string
        >>> me.go_to('FSM')
        FSM is locked! Go look for a key to unlock it
        You are at GBC
        >>> me.unlock(fsm)
        Place must be a string
        >>> me.unlock('FSM')
        FSM can't be unlocked without a key!
        >>> me.take('SkeletonKey')
        Player takes the SkeletonKey
        >>> me.unlock('FSM')
        FSM is now unlocked!
        >>> me.unlock('FSM')
        FSM is already unlocked!
        >>> me.go_to('FSM')
        You are at FSM
        """
        a = place
        if type(place) != str:
            print("Place must be a string")
            return
        key = None
        for item in self.items:
            if type(item) == Key:
                key = item
        if key == None:
            print(place + " can't be unlocked without a key!")
        else:
            key.use(self.place.get_neighbor(a))

    def cast(self, spell):
        if not self.has_wand:
            print('You need a Wand to cast a spell!')
        else:
            print("Abracadabra")

    def spells_learned(self):
        for spell in self.spells:
            print('   ', spell.name, '-', spell.description)

class Character(object):
    def __init__(self, name, message):
        self.name = name
        self.message = message

    def talk(self):
        return self.message


class Thing(object):
    def __init__(self, name, description, action = None, message = None):
        self.name = name
        self.description = description
        self.action = action
        self.message = message

    def use(self, place):
        print("You can't use a {0} here".format(self.name))

class Spell(Thing):
    types = 'magical'

class Money(Thing):
    description = "wizarding currency"
    def __init__(self, amount, action = None, message = None):
        if amount == 1:
            self.name = str(amount) + ' Galleon'
        else:
            self.name = str(amount) + ' Galleons'
        self.amount = amount
        self.action = action
        self.message = message
class Key(Thing):
    def use(self, place):
        if place.locked == True:
            place.locked = False
            print(place.name + " is now unlocked!")
        else:
            print(place.name + " is already unlocked!")

class Wand(Thing):
    def __init__(self, name, description, action):
        Thing.__init__(self, name, description, action)


class Place(object):
    def __init__(self, name, description, characters, things, nickname = None):
        self.name = name
        if nickname == None:
            self.nickname = self.name
        else:
            self.nickname = nickname
        self.description = description
        self.characters = {character.name: character for character in characters}
        self.things = {thing.name: thing for thing in things}
        self.locked = False
        self.exits = {} # {'name': (exit, 'description')}

    def look(self):
        print('You are currently at ' + self.nickname + '. You take a look around and see:')
        print('\nCharacters:')
        if not self.characters:
            print('    no one in particular')
        else:
            for character in self.characters:
                print('   ', character)
        print('\nThings:')
        if not self.things:
            print('    nothing in particular')
        else:
            for thing in self.things.values():
                print('   ', thing.name, '-', thing.description)
        print('\n')
        self.check_exits()

    def get_neighbor(self, exit):
        """
        >>> sather_gate = Place('Sather Gate', 'You are at Sather Gate', [], [])
        >>> gbc = Place('GBC', 'You are at Golden Bear Cafe', [], [])
        >>> gbc.add_exits([sather_gate])
        >>> place = gbc.get_neighbor('Sather Gate')
        >>> place is sather_gate
        True
        >>> place = gbc.get_neighbor('FSM')
        Can't go to FSM from GBC.
        Try looking around to see where to go.
        >>> place is gbc
        True
        """
        if type(exit) != str:
            print('Exit has to be a string.')
            return self
        elif exit in self.exits or exit in [self.exits[i][0].nickname for i in self.exits]:
            if exit in self.exits:
                exit_place = self.exits[exit][0]
                return exit_place
            else:
                new_value = 0
                for i in self.exits:
                    if self.exits[i][0].nickname == exit:
                        new_value = i
                if new_value == 0:
                    raise SyntaxError('Please type a valid location.')
                else:
                    exit_place = self.exits[new_value][0]
                    return exit_place

        else:
            print("Can't go to {} from {}.".format(exit, self.nickname))
            print("Try looking around to see where to go.")
            return self

    def take(self, thing):
        return self.things.pop(thing)

    def check_exits(self):
        print('You can exit to:')
        for exit, description in self.exits.values():
            print('   {}'.format(exit.nickname),' - ', description)

    def add_exits(self, places):
        for place in places:
            self.exits[place.name] = (place, place.description)
