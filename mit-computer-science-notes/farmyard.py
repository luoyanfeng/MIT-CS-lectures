# 先确定鸡的数量，再来找猪的数量
def solve(numLegs, numHeads):
    for numChickens in range(0, numHeads + 1):
        numPigs = numHeads - numChickens
        totLegs = 4 * numPigs + 2 * numChickens
        if totLegs <= numLegs:
            return [numPigs, numChickens]
    return [None, None]


def barnYard():
    heads = int(input("enter number of heads"))
    legs = int(input("enter number of legs"))
    pigs, chickens = solve(legs, heads)
    # 无解的情况
    if pigs is None:
        print("there is no solution")
    else:
        print("number of pigs", pigs)
        print("number of chichens", chickens)


# 嵌套循环，先确定蜘蛛和鸡的数量
def solve1(numLegs, numHeads):
    for numSpiders in range(0, numHeads + 1):
        for numChickens in range(0, numHeads - numSpiders + 1):
            numPigs = numHeads - numChickens - numSpiders
            totLegs = 4 * numPigs + 2 * numChickens + 8 * numSpiders
            if totLegs == numLegs:
                return [numPigs, numChickens, numSpiders]
    return [None, None, None]


def barnYard1():
    heads = int(input("enter number of heads"))
    legs = int(input("enter number of legs"))
    pigs, chickens, spiders = solve1(legs, heads)
    if pigs is None:
        print("there is no solution")
    else:
        print("number of pigs", pigs)
        print("number of chichens", chickens)
        print("number of spiders", spiders)


def solve2(numLegs, numHeads):
    solutionFound = False
    for numSpiders in range(0, numHeads + 1):
        for numChickens in range(0, numHeads - numSpiders + 1):
            numPigs = numHeads - numChickens - numSpiders
            totLegs = 4 * numPigs + 2 * numChickens + 8 * numSpiders
            if totLegs == numLegs:
                print("number of pigs", numPigs)
                print("number of chickens", numChickens)
                print("number of spiders", numSpiders)
                solutionFound = True
    if not solutionFound:
        print("there is no solution")


def isPalindrome(string):
    if len(string) <= 1:
        return True
    else:
        return string[0] == string[-1] and isPalindrome(string[1:-1])


def isPalindrome1(string, indent):
    print(indent, string)
    if len(string) <= 1:
        print(indent)
        return True
    else:
        ans = string[
            0] == string[-1] and isPalindrome1(string[1:-1], indent + indent)
        print(indent, ans)
        return ans


def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)


# run test
print(fib(5))
