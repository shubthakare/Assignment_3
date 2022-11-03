
def digitSum(n):
    sum = 0
    while (n != 0):
        sum = sum + int(n % 10)
        n = int(n/10)
    return sum


if __name__ == "__main__":
    n = 10234
    print(digitSum(n))
