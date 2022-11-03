if __name__ == '__main__':
    print('Enter number of circles')
    number_of_circle = int(input(f'Enter the N value:'))

    all_circle = []
    for i in range(0, number_of_circle):
        circle_info = []
        print(f'Enter Information for circle {i+1}')

        radius = float(input('Enter the radius: '))
        circle_info.append(radius)

        print('Enter x,y co-oridnates of the centre of the cirle')
        centre = []
        for i in range(0, 2):
            ele = int(input())
            centre.append(ele)
        circle_info.append(centre)

        area = 3.142 * radius
        circle_info.append(area)

        all_circle.append(circle_info)
    # print(all_circle)

    #sorted_circle_info = sort_list_of_dictionary(circle_info_list, key = 'area')
    # alternate way to sort list of dictionaries -
    sorted_circle = sorted(all_circle, key=lambda x: x[2])
    print(sorted_circle)
