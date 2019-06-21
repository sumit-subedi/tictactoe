import random
def checkresult(list):
    for i in (0,3,6):

        if(list[i]==list[i+1]==list[i+2]==1 or list[i]==list[i+1]==list[i+2]==2):

            return 1

    for i in (0,1,2):

        if(list[i]==list[i+3]==list[i+6]==1 or list[i]==list[i+3]==list[i+6]==2 ):
            return 1
    if(list[0]==list[4]==list[8]==1 or list[0]==list[4]==list[8]==2 ):
        return 1
    if (list[2] == list[4] == list[6] == 1 or list[2] == list[4] == list[6] == 2 ):
        return 1
    return 0

def nextpos(list):

    #checks to do own game
    for i in (0,3,6):
        if(list[i]==list[i+1]==2 and list[i+2]==0):
            return i+2
        if(list[i]==list[i+2]==2 and list[i+1]==0 ):
            return i+1
        if(list[i+1]==list[i+2]==2 and list[i]==0):
            return i


    for i in (0,1,2):
        if (list[i] == list[i + 3] ==  2 and list[i+6]==0):
            return i + 6
        if (list[i] == list[i + 6] ==  2 and list[i+3]==0):
            return i + 3
        if (list[i + 3] == list[i + 6] ==  2 and list[i]==0):
            return i
    if (list[0]==list[4]==2 and list[8]==0):
        return 8
    if (list[0] == list[8] == 2 and list[4]==0):
        return 4
    if (list[8] == list[4] == 2 and list[0]==0):
        return 0
    if (list[2] == list[4] == 2 and list[6]==0):
        return 6
    if (list[2] == list[6] == 2 and list[4] == 0):
        return 4
    if (list[4] == list[6] == 2 and list[2] == 0):
        return 2
    #checks to interrupt the users game
    for i in (0,3,6):
        if(list[i]==list[i+1]==1  and list[i+2]==0):
            return i+2
        if(list[i]==list[i+2]==1  and list[i+1]==0 ):
            return i+1
        if(list[i+1]==list[i+2]==1  and list[i]==0):
            return i
    for i in (0,1,2):
        if (list[i] == list[i + 3] == 1  and list[i+6]==0):
            return i + 6
        if (list[i] == list[i + 6] == 1 and list[i+3]==0):
            return i + 3
        if (list[i + 3] == list[i + 6] == 1 and list[i]==0):
            return i
    if (list[0]==list[4]==1 and list[8]==0):
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

    for j  in range(50):
        i=random.randint(0,8)
        if(list[i]==0):
            return i