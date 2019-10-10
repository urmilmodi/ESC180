FIN="datain"
try:
    f = open(FIN, 'r')
except:
    print("ERR: file", FIN, "is not present or can't be opened")
lines = f.readlines()
f.close()
for line in lines:
    print(line)
for line in lines:
    print(line.split('\n')[0])



try:
    g = open('dataout', 'w')
except:
    print("ERROR")

g.write("This is content")
g.write("This is more content")

g.write('\n')
g.write("This is content\n")
g.write("This is more content\n")
g.close()