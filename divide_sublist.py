def Divide_list(input_list, n):
    my_new_list = []
    for i in input_list:
        if i % n == 0:
            my_new_list.append(i)
        else:
            pass
    print(f' the original list is: {input_list} divident is: {n} and new list is: {my_new_list} with length: {len(my_new_list)}')


if __name__ == '__main__':
    size_of_list = int(input(f'Enter the length of list:'))
    D_number = int(input(f'Enter the N value:'))
    input_list = []
    for i in range(0, size_of_list):
        ele = int(input())
        input_list.append(ele)
    Divide_list(input_list, D_number)
