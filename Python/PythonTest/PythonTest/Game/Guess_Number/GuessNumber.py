# This is a game for guess number

import random

# Customer input
print("请输入你的用户名:", end="")
CustomerNameInput = input()

print("**********Game Start**********")
print("Welcome '{0}' to enter the game".format(CustomerNameInput))

# Game main
GuessNumber = random.randrange(0, 10)
count = 0
IsSuccess = False

while IsSuccess==False:
    print("请输入你的数字:",  end="")
    CustomerNumberInput = int(input())
    
    if CustomerNumberInput > int(GuessNumber):
        count = count + 1
        print("提示：您输入的数字太大了")
    elif CustomerNumberInput < int(GuessNumber):
        count = count + 1
        print("提示：您输入的数字太小了")
    elif CustomerNumberInput == int(GuessNumber):
        count = count + 1
        print("提示：您答对了，合计:{0},分数:{1}".format(count, 100-count))
        IsSuccess = True

print("**********Game Over**********")
















