def set_operations(A, B):
    C = set(A).union(set(B))
    D = set(A).intersection(set(B))
    print(f'''set A = {A}, set B = {B}, \n set C = {C}, set D = {D} \n cardianality of set C = {len(C)}, cadianality of set D = {len(D)}''')


if __name__ == '__main__':

    print('Enter cardianility of input set A')
    size_of_N = int(input(f'Enter the length of list:'))
    input_list_1 = []
    for i in range(0, size_of_N):
        ele = int(input())
        input_list_1.append(ele)

    print('Enter cardianility of input set B')
    size_of_M = int(input(f'Enter the length of list:'))
    input_list_2 = []
    for i in range(0, size_of_M):
        ele = int(input())
        input_list_2.append(ele)
    set_operations(input_list_1, input_list_2)
