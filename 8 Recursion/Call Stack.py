def funcThree():
    print("3: starting funcThree")
    print("3: I'm function three and I'm done running")


def funcTwo():
    print("2: starting funcTwo")
    funcThree()
    print("2: I'm function two and I'm done running")

def funcOne():
    print("1: starting funcOne")
    funcTwo()
    print("1: I'm function one and I'm done running")

funcOne()