def find_max_value(list):
    max_value = max(list)
    max_position = list.index(max_value)
    print(f"the value is: {max_value}  and position is :{max_position}")


def find_min_value(list):
    min_value = min(list)
    min_position = list.index(min_value)
    print(f"the value is: {min_value}  and position is :{min_position}")


if __name__ == '__main__':
    size_of_list = int(input(f'Enter the length of list:'))
    input_list = []
    for i in range(0, size_of_list):
        ele = int(input())
        input_list.append(ele)

    find_max_value(input_list)
    find_min_value(input_list)
