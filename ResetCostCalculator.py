#Last Epoch Skill Reset Calculator#
###################################
 #Cost for first skill = 25 gold#
 #Each next skill adds = 25 gold#


from sympy.solvers import solve
from sympy import Symbol

user_input = input('How many skill point you want to reset: ')
num = int(user_input)
user_input_previous = input('What is your 1 skill point reset cost at the moment: ')
baseCost = int(user_input_previous)
extraCost = 25
lastCost = 0
costList = [25]

def calculate(baseCost, num):
    if baseCost == 25:
        result = costCalculator(num, extraCost, costList)
    else:
        a = (baseCost/25)*2
        x = Symbol('x')
        y = solve(x**2+x-a)
        resetCount = int(y[1])
        print('Previously skill points you have resetted:', resetCount)
        num = num + resetCount
        print('After this process your total skill point reset will be: ', num)
        result = costCalculator(num, extraCost, costList)
    return result

def costCalculator(num, extraCost, costList):
    for z in range(num-1):
        extraCost = extraCost+25
        costList.append(extraCost)
    return costList


a = calculate(baseCost, num)
print(a)
print(sum(a))
costList.clear()
