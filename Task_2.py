# 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def PredicatCheck ():
    result = True
    for i in range(0, 8):
        number = bin(i)
        print(f'{n} =', end=" ") 
        print(f'{num} =', end=" ") 
        num = num.replace('b', '0')
        X = int(num[-3])
        Y = int(num[-2])
        Z = int(num[-1])
        print(f'{X}{Y}{Z}', end=" ") 
        result = (not(X or Y or Z)) == ((not X) and (not Y) and (not Z))
        print()
        if result is True:
            result = "Истина"
        else:
            result = "Ложь"
    return result
print(PredicatCheck())