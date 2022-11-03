
def ReverseSum(n):
    if (len(str(n))) > 5:
        last = 0
        while(n > 0):
            a = n % 10
            last = last*10 + a
            n = n // 10
        return last
    else:
        return False


if __name__ == "__main__":
    n = 1234644
    print(ReverseSum(n))
