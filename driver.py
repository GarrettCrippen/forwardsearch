import search

#Used only in project 2 part 1

search_alg=[search.forward_selection,search.backward_elimination]
while(True):
    print('Enter total number of features: ',end='')
    num = input()
    try:
        val = int(num)
    except:
        print('Error: not a number')
        break
    print('Please enter the search algorithm you would like to run.')

    for i,alg in enumerate(search_alg):
        print(f'{i+1}) {alg.__name__}')

    choice = input()
    if choice == '1' or choice =='2':
        search_alg[int(choice)-1](int(num))
    else:
        break