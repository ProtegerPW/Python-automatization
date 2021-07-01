def collatz(number):
    if (number % 2) == 0:
        print(number//2)
        return number//2
    else:
        print(3 * number + 1)
        return 3 * number + 1

if __name__ == '__main__':
    print("Please enter a number")
    while True:
        try:
            inputRead = int(input())
            while (inputRead != 1):
                inputRead = collatz(inputRead)
            break

        except ValueError:
            print("As I said before - please enter an integer")

    
