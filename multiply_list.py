def multiply_list(input_list, n):
    my_new_list = []
    for i in input_list:
        my_new_list.append(i * n)
    return my_new_list


if __name__ == '__main__':
    size_of_list = int(input(f'Enter the length of list:'))
    n_number = int(input(f'Enter the N value:'))
    input_list = []
    for i in range(0, size_of_list):
        ele = int(input())
        input_list.append(ele)
    print(multiply_list(input_list, n_number))
