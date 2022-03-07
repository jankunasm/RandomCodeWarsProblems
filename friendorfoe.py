# Make a program that filters a list of strings and returns a list with only your friends name in it.

# If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...

# Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

# i.e.

# friend ["Ryan", "Kieran", "Mark"] `shouldBe` ["Ryan", "Mark"]

#  My solution

def friend(x):
    newlist = []
    for string in x:
        if len(string) == 4:
            newlist.append(string)
    return newlist


print(friend(["Ryan", "Kieran", "Mark"]))


# List Comp solution

def friend(x):
    return [f for  f in x if len(f) == 4]

print(friend(["Ryan", "Kieran", "Mark"]))