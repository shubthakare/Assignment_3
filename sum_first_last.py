
def ReverseSum(n):
    if (len(str(n))) > 5:
        result = 0
        last = 0
        first = 0
        rev = 0
        while(n > 0):
            a = n % 10
            if rev == 0:
                print(a)
                last = a
            elif(len(str(n)) == 1):
                print(n)
                first = n
            else:
                rev = rev*10 + a
                n = n // 10
        return first+last
    else:
        return False


def add_first_and_last(n):
    number = str(n)
    result = int(number[0]) + int(number[-1])
    return result


if __name__ == "__main__":
    n = 1234644
    # print(add_first_and_last(n))
    print(ReverseSum(n))
