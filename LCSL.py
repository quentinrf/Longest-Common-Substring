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
    #set the current cell equal to the bottom right cell
    current = LCSL[len(p)-1][len(q)-1]
    #set pVal equal to last index of the p string
    pVal = 9
    #set qVal equal to last index of the q string
    qVal = 7
    #create an empty list to store the letters
    letters = []

    #while we havent reached the top left corner
    while(current!=0):
        #if the characters match we know this char is in the longest common substring
        if(p[pVal]==q[qVal]):
            current = LCSL[pVal-1][qVal-1]
            letters.append(p[pVal])
            qVal -= 1
            pVal -= 1
        #otherwise if its equal to the one to the left this is our new cell
        elif(current==LCSL[pVal][qVal-1]):
            current = LCSL[pVal][qVal-1]
            qVal -= 1
        #otherwise if its equal to the upper one this is our new cell
        elif(current==LCSL[pVal-1][qVal]):
            current = LCSL[pVal-1][qVal]
            pVal -= 1
        #otherwise if its equal to the upper left one this is our new cell
        elif(current==LCSL[pVal-1][qVal-1]):
            current = LCSL[pVal-1][qVal-1]
            pVal -= 1
            qVal -= 1
    #reverse the list of letters and print them
    letters.reverse()
    print(letters)
fillTable()
