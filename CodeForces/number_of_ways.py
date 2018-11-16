from itertools import combinations


def generate(seq):
    count = 0
    for i, j in combinations(range(1, len(seq)), 2):
        if len(set(list(map(sum, [seq[:i], seq[i:j], seq[j:]])))) == 1:
            count += 1
    return count


n = int(input())
print(generate(list(map(int, input().split()))))
