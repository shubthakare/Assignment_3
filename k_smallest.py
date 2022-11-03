

def kthSmallest(input_list, K):
    input_list.sort()
    return input_list[K-1]


if __name__ == '__main__':
    size_of_list = int(input(f'Enter the length of list:'))
    Kth_index = int(input(f'Enter the K value:'))
    input_list = []
    for i in range(0, size_of_list):
        ele = int(input())
        input_list.append(ele)

    print(f"the kth smallest no is: {kthSmallest(input_list, Kth_index)}")
