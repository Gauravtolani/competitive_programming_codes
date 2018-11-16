from collections import defaultdict

n = int(input())
errors_list = input().split()
errors_list_1 = input().split()
errors_list_2 = input().split()


def list_difference(a, b):
    count = defaultdict(int)

    for x in a:
        count[x] += 1

    for x in b:
        count[x] -= 1

    print(count)

    diff = []
    for x in a:
        if count[x] > 0:
           count[x] -= 1
           diff.append(x)
    return ''.join(diff)


print(list_difference(errors_list, errors_list_1))
print(list_difference(errors_list_1, errors_list_2))
