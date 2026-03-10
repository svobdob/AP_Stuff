## factorial

sum = 1
times = int(input("Which numbers factorial do you want to find \n"))

for i in range(1, times + 1):
    sum *= i

print(sum)

## multiplying

sum = 1
times = int(input("How many numbers do we multiply \n"))

for i in range(times):
    num = int(input("Zadejte číslo: "))
    sum *= num

print(sum)