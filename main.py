a = int(input('введите число: '))
def prime(a):
    k = 0
    for i in range(a):
        if a % (i+1) == 0:
            k += 1
    if k > 2:
         return False
    else:
         return True


if __name__ == "__main__":
    a = int(input('введите число: '))
    print(prime(a))