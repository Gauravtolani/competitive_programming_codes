'''
edabit problem
https://edabit.com/challenge/cHzvB5KCWCK3oCLGL
'''
import numpy as np


def count_neigbours(the_item,input_matrix):
    alive_neighbours_count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            try:
                if((the_item[0][0] + i >= 0) and (the_item[0][1] + j)>=0):
                    if input_matrix[the_item[0][0] + i][the_item[0][1] + j] == 1:
                        alive_neighbours_count +=1
            except:
                continue
    if the_item[1] == 1:
        return alive_neighbours_count-1
    else:
        return alive_neighbours_count


def deal_alive_condition(the_item, input_matrix):
    if the_item[1] == 0:
        if count_neigbours(the_item, input_matrix) == 3:
            return 'I'
        else:
            return '_'
    else:
        if((0 <= count_neigbours(the_item,input_matrix) <= 1) or (4 <= count_neigbours(the_item, input_matrix))):
            return '_'
        else:
            return 'I'


def convoy_gol(input_matrix):
    final_str = ''
    new_array = np.array(input_matrix)
    new_list = []
    for x in np.ndenumerate(np.array(input_matrix)):
        new_list.append(deal_alive_condition(x, input_matrix))

    new_list = np.array(new_list).reshape(new_array.shape[0], new_array.shape[1])
    for i in new_list:
        final_str = final_str + (''.join(i)) + '\n'

    return final_str.strip()