def collatz(number: int):
    count = 0
    while number != 1:
        count += 1
        if number % 2 == 0:
            number /= 2
        else:
            number = number * 3 + 1
    return count

if __name__ == '__main__':
    result = collatz(int(input()))
    print(result)