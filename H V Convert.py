n=250
def convertbin(n):
    ans_num = 0
    multiplier = 0
    while (n > 0):
        remainder = n % 10
        n = n//10
        ans_num = ans_num + remainder * (2**multiplier)
        multiplier += 1

    return ans_num
f=convertbin(n)
print(f)
