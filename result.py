import random


def checkresult(list):
    #5. right now it seems like some cases are not accounted for (UPDATE: I think I figured it out. If I click on another option, after I lost, it says I won. Further testing might be required)
    ##  which goes to show you that manually trying to check every case makes things very difficult
    ##  this is when algorithms can work miracles. Not only can they make your program run faster,
    ##  they can make your code easier to read. I'd have to think harder on how to solve the problem of tic tac toe
    ##  inorder to give you any hints though :/
    ##  I can actually see this being a difficult problem to solve. It's kind of like the longest road/path problem.
    ##  and in this case I'd say that keeping it simple is better. So if you want to continue writing every case down, I'd agree.
    ##  but think on it for a bit and see if you can come with a better solution then checking each possible case
    for i in (0, 3, 6):
        # 6. Comment! You might come back to this code in a few weeks and have NO IDEA what is going on
        ##  you don't have to comment every line but you MUST try to
        ##  comment anything that is obtuse or tricky like this.
        if(list[i] == list[i + 1] == list[i + 2] == 1 or list[i] == list[i + 1] == list[i + 2] == 2):

            return 1

    for i in (0, 1, 2):

        if(list[i] == list[i + 3] == list[i + 6] == 1 or list[i] == list[i + 3] == list[i + 6] == 2):
            return 1
    if(list[0] == list[4] == list[8] == 1 or list[0] == list[4] == list[8] == 2):
        return 1
    if (list[2] == list[4] == list[6] == 1 or list[2] == list[4] == list[6] == 2):
        return 1
    return 0


def nextpos(list):

    #checks to do own game
    for i in (0, 3, 6):
        if(list[i] == list[i + 1] == 2 and list[i + 2] == 0):
            return i + 2
        if(list[i] == list[i + 2] == 2 and list[i + 1] == 0):
            return i + 1
        if(list[i + 1] == list[i + 2] == 2 and list[i] == 0):
            return i

    for i in (0, 1, 2):
        if (list[i] == list[i + 3] == 2 and list[i + 6] == 0):
            return i + 6
        if (list[i] == list[i + 6] == 2 and list[i + 3] == 0):
            return i + 3
        if (list[i + 3] == list[i + 6] == 2 and list[i] == 0):
            return i
    if (list[0] == list[4] == 2 and list[8] == 0):
        return 8
    if (list[0] == list[8] == 2 and list[4] == 0):
        return 4
    if (list[8] == list[4] == 2 and list[0] == 0):
        return 0
    if (list[2] == list[4] == 2 and list[6] == 0):
        return 6
    if (list[2] == list[6] == 2 and list[4] == 0):
        return 4
    if (list[4] == list[6] == 2 and list[2] == 0):
        return 2
    #checks to interrupt the users game
    for i in (0, 3, 6):
        if(list[i] == list[i + 1] == 1 and list[i + 2] == 0):
            return i + 2
        if(list[i] == list[i + 2] == 1 and list[i + 1] == 0):
            return i + 1
        if(list[i + 1] == list[i + 2] == 1  and list[i] == 0):
            return i
    for i in (0, 1, 2):
        if (list[i] == list[i + 3] == 1 and list[i + 6] == 0):
            return i + 6
        if (list[i] == list[i + 6] == 1 and list[i + 3] == 0):
            return i + 3
        if (list[i + 3] == list[i + 6] == 1 and list[i] == 0):
            return i
    if (list[0] == list[4] == 1 and list[8] == 0):
        return 8
    if (list[0] == list[8] == 1 and list[4]==0):
        return 4
    if (list[8] == list[4] == 1 and list[0]==0):
        return 0
    if (list[2] == list[4] == 1 and list[6]==0):
        return 6
    if (list[2] == list[6] == 1 and list[4] == 0):
        return 4
    if (list[4] == list[6] == 1 and list[2] == 0):
        return 2

    for j in range(50):
        i = random.randint(0, 8)
        if(list[i] == 0):
            return i
