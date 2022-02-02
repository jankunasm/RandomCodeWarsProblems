def parse(data):
    counter = 0
    amazing_list = []
    for letter in data:
        if letter == 'i':
            counter += 1
        elif letter == 'd':
            counter -= 1
        elif letter == 's':
            counter = counter ** 2
        elif letter == 'o':
            amazing_list.append(counter)
            
    return amazing_list
            

print(parse('iiidsoiio'))

