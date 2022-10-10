import itertools


def sub_sequence(str):
    combs = []
    for i in range(1, len(str)+1):
        combs.append(list(itertools.combinations(str, i)))
        a = []
        for c in combs:
            for t in c:
                a.append("".join(t))
        return a


stri = input()
b = sub_sequence(stri)
print(b)
