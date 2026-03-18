num = int(input("Введіть число: "))

if num <= 1:
    print("Це не просте число")
else:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print("Це просте число")
    else:
        print("Це не просте число")
