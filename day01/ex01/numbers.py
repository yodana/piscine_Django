def read_file():
    file = open("numbers.txt")
    numbers = file.split(',')
    for number in numbers:
        print(number)

if __name__ == '__main__':
    read_file()