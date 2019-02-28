##Working class system after classes didnt initially work.
##Defining all the requirements for the rooms


character = {'inventory': [], 'location': 'start room'}
dungeon = {
    'room 3': {
        'short description': 'Room with a 3 on the door',
        'long description': 'There is an ornate chair in this room',
        'contents': ['small key'],
        'exits': {'east': 'hallway lower'}
    },
    'room 2': {
        'short description': 'Room with a 2 on the door',
        'long description': 'The second room with something on the floor',
        'contents': ['crowbar'],
        'exits': {'west': 'hallway lower'}
    },
    'hallway lower': {
        'short description': 'A hallway',
        'long description': 'A fairly dingy hallyway with 6 connesting rooms',
        'contents': ['goo'],
        'exits': {'east': 'room 2', 'west': 'room 3', 'south': 'start room', 'north': 'hallway upper'}
    },
    'start room': {
        'short description': 'A dingy room',
        'long description': 'There are the roman numerals (VIII - V - XII - XVI) on the wall and a door',
        'contents': ['wet towel'],
        'exits': {'north': 'hallway lower'}
    },
    'room 4':{
        'short description': 'Room with a 4 on the door',
        'long description': 'There is a chair that you just got out of',
        'contents': ['A very flashy ornate key'],
        'exits': {'west': 'hallway upper'}
    },
    'room 5': {
        'short description': 'Room with a 5 on the door',
        'long description': 'a sloping north-south passage of barren rock',
        'contents': ['lock box'],
        'exits': {'east': 'hallway upper'}
    },
    'hallway upper': {
        'short description': 'A hallway',
        'long description': 'The hallway feels the same though it seems to be slightly damp',
        'contents': [],
        'exits': {'east': 'room 4', 'west': 'room 5', 'south': 'hallway lower'}
    },
    'room 6': {
        'short description': 'Room with ornate carvings and etching on the front',
        'long description': 'there is a crached window and a noose with a doll strung up from it....',
        'contents': [],
        'exits': {'south': 'hallway upper'}
        
}

}

### Still unable to get conditions


while True:
    room = dungeon[character['location']]
    command = input("What would you like to do: ")
    command_parts = command.split(None, 1)
    verb = command_parts[0]
    obj = command_parts[-1] # if the user only types one word, both verb and obj will be the same
    if verb in ['east', 'west', 'north', 'south', 'up', 'down', 'in', 'out']:
        if verb in room['exits']:
            character['location'] = room['exits'][verb]
            room = dungeon[character['location']]
            print ('You are in', room['long description'])
            for item in room['contents']:
                print ('There is a', item, 'here')
        else:
            print ('You cannot go that way')

    if verb == 'inventory':
        print ('You are carrying:')
        for item in character['inventory']:
            print ('   ', item)
    if verb == 'quit':
        print ('Goodbye')
        break
    if verb == 'take':
        if obj == 'all':
            if room['contents']:
                for item in room['contents'][:]: # this part: [:] makes a copy of the list so removing items works
                    print ('You pick up the', item)
                    character['inventory'].append(item)
                    room['contents'].remove(item)
            else:
               print ('There is nothing to take!')
        else:
            for item in room['contents']:
                if obj in item: # does the word in obj match any part of the text of item?
                    print ('You pick up the', item)
                    character['inventory'].append(item)
                    room['contents'].remove(item)
    if verb == 'look':
        print (room['long description'])





if room == 'start room' and command in ['North', 'Out']:
    input = key("Please put in the key")
    if key == "851216":
        character['location'] = ['hallway']
    
    else:
        print ("Invalid key")

