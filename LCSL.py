from array import *

p = "palindrome"
q = "mailroom"

i = len(p)
j = len(q)


def base_case():
    #fill an empty list of lists with "none"
    LCStuff = [["none" for k in range(8)] for l in range(10)]
    #iterate through the characters in p
    for value in p:
        #if the first char of q equals the current char of p
        if q[0] == value:
            #set that index in table to 1
            LCStuff[p.index(value)][0] = 1
            #otherwise zero
        else:
            LCStuff[p.index(value)][0] = 0
    #iterate through q
    for val in range(j):
        #if the first char of p equals the current char of q
        if(p[0] == q[val]):
            #set that box to 1
            LCStuff[0][val] = 1
            #otherwise set it to zero
        else:
            LCStuff[0][val] = 0
    return LCStuff

#Fill table based on char matching
def fillTable():
    LCSL = base_case()
    #iterate through the indexs of p and q
    for pVal in range(1, 10):
        for qVal in range(1, 8):
            #if the chars match set their respective box to 1 plus the top left box
            if(p[pVal]==q[qVal]):
                LCSL[pVal][qVal] = 1 + LCSL[pVal-1][qVal-1]
            #otherwise take the max of the three surrounding boxes
            else:
                LCSL[pVal][qVal] = max(LCSL[pVal-1][qVal], LCSL[pVal][qVal-1], LCSL[pVal-1][qVal-1])
    #write it to a file for easy viewing
    file = open("array.txt", "w+")
    for line in LCSL:
        file.write(str(line) + "\n")
    file.close()
    reTrace(LCSL)

#Function to retrace table and find the longest common substring
def reTrace(LCSL):
    current = LCSL[len(p)-1][len(q)-1]
    pVal = 9
    qVal = 7
    letters = []

    while(current!=0):

        if(p[pVal]==q[qVal]):
            current = LCSL[pVal-1][qVal-1]
            letters.append(p[pVal])
            qVal -= 1
            pVal -= 1
        elif(current==LCSL[pVal][qVal-1]):
            current = LCSL[pVal][qVal-1]
            qVal -= 1
        elif(current==LCSL[pVal-1][qVal]):
            current = LCSL[pVal-1][qVal]
            pVal -= 1
        elif(current==LCSL[pVal-1][qVal-1]):
            current = LCSL[pVal-1][qVal-1]
            pVal -= 1
            qVal -= 1

    letters.reverse()
    print(letters)
fillTable()
