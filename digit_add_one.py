
def add_digit(n):
    if (len(str(n))) > 5:
        result = ''
        for i in str(n):
            result += str(int(i)+1)
        return result
    else:
        return False


if __name__ == "__main__":
    n = 1234644
    print(add_digit(n))
