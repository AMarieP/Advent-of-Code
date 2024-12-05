# --- Day 5: Print Queue ---
# Satisfied with their search on Ceres, the squadron of scholars 
# suggests subsequently scanning the stationery stacks of sub-basement 17.

# The North Pole printing department is busier than ever this close to Christmas, 
# and while The Historians continue their search of this historically significant 
# facility, an Elf operating a very familiar printer beckons you over.

# The Elf must recognize you, because they waste no time explaining that the new sleigh
#  launch safety manual updates won't print correctly. Failure to update the safety 
#  manuals would be dire indeed, so you offer your services.



#Searches unsorted list from back to front, returns index and target

import re
def frontAndBackSearch(array, target):
    
    #Get the front and back indexes
    front = 0
    back = len(array) -1

    while front <= back:
        if array[front] == target:
            return target, front
        elif array[back] == target:
            return target, back
    
    return "Target does not exist"

def isPosition(frontIndex, backIndex):
    if frontIndex < backIndex:
        return True
    if frontIndex == backIndex:
        return "Error"
    if frontIndex > backIndex:
        return False

def getIntFromRules(rule):
    ruleInt = int(rule.split('|'))
    front = ruleInt[0]
    back = ruleInt[1]
    return front, back


def validateIndex(rules, pages):
    for rule in rules:
        thisRule = getIntFromRules(rule)
        frontIndex = frontAndBackSearch(pages, thisRule[0])
        backIndex = frontAndBackSearch(pages, thisRule[1])
        isFollowRule = isPosition(frontIndex, backIndex)
        if isFollowRule:
            print(thisRule, "Is Correct")
        elif isFollowRule == "Error":
            print("Error with this one")
        else:
            (thisRule, "Is Incorrect")


    
        


