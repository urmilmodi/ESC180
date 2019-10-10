def factorial():
    value = int(input("Factorial Number: ")) ##Input the Number
    n = 0 ## Set the While Loop
    output = 1 ## Number you output
    while (n < value): ## Run the code below if and only if the factorial isn't finished yet
        output = output * (n + 1) ## Multiply the numbers
        n = n + 1 ## Increase the While Loop Number Because you multiplied by it
    print(output) ## Print the Factorial Value

while True:
    factorial()