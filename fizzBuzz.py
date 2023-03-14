ileMod3 = 0
ileMod5 = 0
ileMod35 = 0

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        ileMod35 += 1
        ileMod3 += 1
        ileMod5 += 1
        print("FizzBuzz")
    elif i % 3 == 0:
        ileMod3 += 1
        print("Fizz")
    elif i % 5 == 0:
        ileMod5 += 1
        print("Buzz")
    else:
        print(i)

print(f"Liczb podzielnych przez 3 jest: {ileMod3}")
print(f"Liczb podzielnych przez 5 jest: {ileMod5}")
print(f"Liczb podzielnych przez 3 i 5 jest: {ileMod35}")
