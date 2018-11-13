number_of_inputs = int(input())
inputs_list = []
db_dict = {}

for i in range(number_of_inputs):
    inputs_list.append(input())

for i in inputs_list:
    if i not in db_dict:
        db_dict[i] = 0
        print('OK')
    else:
        db_dict[i] += 1
        print(i + str(db_dict[i]))

