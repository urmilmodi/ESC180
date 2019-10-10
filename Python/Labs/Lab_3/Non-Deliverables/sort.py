col = int(input())
def sortKey(x):
    return x[col]

print(sorted(accum,key=sortKey))