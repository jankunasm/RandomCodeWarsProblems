# def zero():
#     return 0
# def one():
#     return int(1)
# def two(): 
#     return int(2)
# def three():
#     return 3
# def four():
#     return 4
# def five():
#     return 5
# def six():
#     return 6
# def seven():
#     return 7
# def eight():
#     return 8
# def nine():
#     return 9

# def plus(add): 
#     return ('+')
# def minus():
#     return (-)
# def times():
#     return (*)
# def divided_by():
#     return (/)

# print(one(plus(two)))

# (seven(times(five())), 35)

# we need to make optional arguments
# one argument per operator

# thelist = []

# def one(operator = '', number = ''):
#     thelist.append(int(1))

# def two(operator = '', number = ''):
#     thelist.append(int(2))

# def plus(number):
    



# print(two(plus(one())))

def one(dictionary = {}):
    if dictionary == {}:
        return 1
    elif str(dictionary.keys()) == "dict_keys(['plus'])":
        return 1 + dictionary['plus']
    elif str(dictionary.keys()) == "dict_keys(['minus'])":
        return 1 - dictionary['minus']
    elif str(dictionary.keys()) == "dict_keys(['times'])":
        return 1 * dictionary['times']
    elif str(dictionary.keys()) == "dict_keys(['divided_by'])":
        return 1 // dictionary['divided_by']

def two(dictionary = {}):
    if dictionary == {}:
        return 2
    elif str(dictionary.keys()) == "dict_keys(['plus'])":
        return 2 + dictionary['plus']
    elif str(dictionary.keys()) == "dict_keys(['minus'])":
        return 2 - dictionary['minus']
    elif str(dictionary.keys()) == "dict_keys(['times'])":
        return 2 * dictionary['times']
    elif str(dictionary.keys()) == "dict_keys(['divided_by'])":
        return 2 // dictionary['divided_by']

def three(dictionary = {}):
    if dictionary == {}:
        return 3
    elif str(dictionary.keys()) == "dict_keys(['plus'])":
        return 3 + dictionary['plus']
    elif str(dictionary.keys()) == "dict_keys(['minus'])":
        return 3 - dictionary['minus']
    elif str(dictionary.keys()) == "dict_keys(['times'])":
        return 3 * dictionary['times']
    elif str(dictionary.keys()) == "dict_keys(['divided_by'])":
        return 3 // dictionary['divided_by']\

def four(dictionary = {}):
    if dictionary == {}:
        return 4
    elif str(dictionary.keys()) == "dict_keys(['plus'])":
        return 4 + dictionary['plus']
    elif str(dictionary.keys()) == "dict_keys(['minus'])":
        return 4 - dictionary['minus']
    elif str(dictionary.keys()) == "dict_keys(['times'])":
        return 4 * dictionary['times']
    elif str(dictionary.keys()) == "dict_keys(['divided_by'])":
        return 4 // dictionary['divided_by']

def five(dictionary = {}):
    if dictionary == {}:
        return 5
    elif str(dictionary.keys()) == "dict_keys(['plus'])":
        return 5 + dictionary['plus']
    elif str(dictionary.keys()) == "dict_keys(['minus'])":
        return 5 - dictionary['minus']
    elif str(dictionary.keys()) == "dict_keys(['times'])":
        return 5 * dictionary['times']
    elif str(dictionary.keys()) == "dict_keys(['divided_by'])":
        return 5 // dictionary['divided_by']

def six(dictionary = {}):
    if dictionary == {}:
        return 6
    elif str(dictionary.keys()) == "dict_keys(['plus'])":
        return 6 + dictionary['plus']
    elif str(dictionary.keys()) == "dict_keys(['minus'])":
        return 6 - dictionary['minus']
    elif str(dictionary.keys()) == "dict_keys(['times'])":
        return 6 * dictionary['times']
    elif str(dictionary.keys()) == "dict_keys(['divided_by'])":
        return 6 // dictionary['divided_by']

def seven(dictionary = {}):
    if dictionary == {}:
        return 7
    elif str(dictionary.keys()) == "dict_keys(['plus'])":
        return 7 + dictionary['plus']
    elif str(dictionary.keys()) == "dict_keys(['minus'])":
        return 7 - dictionary['minus']
    elif str(dictionary.keys()) == "dict_keys(['times'])":
        return 7 * dictionary['times']
    elif str(dictionary.keys()) == "dict_keys(['divided_by'])":
        return 7 // dictionary['divided_by']

def eight(dictionary = {}):
    if dictionary == {}:
        return 8
    elif str(dictionary.keys()) == "dict_keys(['plus'])":
        return 8 + dictionary['plus']
    elif str(dictionary.keys()) == "dict_keys(['minus'])":
        return 8 - dictionary['minus']
    elif str(dictionary.keys()) == "dict_keys(['times'])":
        return 8 * dictionary['times']
    elif str(dictionary.keys()) == "dict_keys(['divided_by'])":
        return 8 // dictionary['divided_by']

def nine(dictionary = {}):
    if dictionary == {}:
        return 9
    elif str(dictionary.keys()) == "dict_keys(['plus'])":
        return 9 + dictionary['plus']
    elif str(dictionary.keys()) == "dict_keys(['minus'])":
        return 9 - dictionary['minus']
    elif str(dictionary.keys()) == "dict_keys(['times'])":
        return 9 * dictionary['times']
    elif str(dictionary.keys()) == "dict_keys(['divided_by'])":
        return 9 // dictionary['divided_by']

def zero(dictionary = {}):
    if dictionary == {}:
        return 0
    elif str(dictionary.keys()) == "dict_keys(['plus'])":
        return 0 + dictionary['plus']
    elif str(dictionary.keys()) == "dict_keys(['minus'])":
        return 0 - dictionary['minus']
    elif str(dictionary.keys()) == "dict_keys(['times'])":
        return 0 * dictionary['times']
    elif str(dictionary.keys()) == "dict_keys(['divided_by'])":
        return 0 // dictionary['divided_by']

def plus(number = ''):
    return {"plus":number}

def minus(number = ''):
    return {"minus":number}

def times(number = ''):
    return {"times":number}

def divided_by(number = ''):
    return {"divided_by":number}




