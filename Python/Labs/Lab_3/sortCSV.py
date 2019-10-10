import sys

def genSortKey(col, up):
    def key(x):
        return x[col] if up else -x[col]
    return key

def main():
    try:
        int(sys.argv[6])
    except:
        print("Column Error")
        return "Column Error"

    f=open(sys.argv[2],'r')
    lines=f.readlines()
    f.close()
    accum=[]
    for i in lines:
        try:
            j=i.split('\n')[0]  # first get rid of the '\n'
        except:
            print("File Error")
            return "File Error"
        k=j.split(',')        # now split on the comma
        r=[]
        try:
            for x in k:
                r = r + [float(x)]
        except:
            print("File Error")
            return "File Error"
        accum = accum + [r] # accumulate
    
    issue = False
    for i in range (0, len(accum), 1):
        if len(accum[i]) <= int(sys.argv[6]):
            issue = True
    if issue:
        print("Column Error")
        return "Column Error"
          
    if sys.argv[8] == "+":
        sortKey=genSortKey(int(sys.argv[6]),True)

    elif sys.argv[8] == "-":
        sortKey=genSortKey(int(sys.argv[6]), False)

    print(accum)
    print(sorted(accum, key=sortKey))
    sortedlines = sorted(accum, key=sortKey)

    try:
        g = open(sys.argv[4], 'w')
    except:
        print("ERROR")
    for j in range (0, len(sortedlines), 1):

        v = ""
        for i in range (0, len(sortedlines[j]), 1):
            if i == len(sortedlines[j]) - 1:
                v += str(sortedlines[j][i])

            else:
                v += str(sortedlines[j][i]) + ","
        g.write(v + "\n")
    g.close()

main()
