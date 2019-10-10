def sqrt(a,b):
    esti = a/2
    while abs(a - esti*esti) > b:
        esti = (esti + a/esti)/2
    return esti

print(sqrt(int(input("Square Root Number")), float(input("Accuracy"))))