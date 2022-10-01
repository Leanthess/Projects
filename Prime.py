primeList = []

try:
    nmb = int(input("Please enter a number: "))

except ValueError:
    print("Error Name -> ValueError [Please enter a number, not string]")

else:
    for i in range(2,nmb):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            primeList.append(i)

print(primeList)