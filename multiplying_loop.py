# !/usr/bin/env python3

# Created by: Wajd Mariam
# Created on: October 2019
# This program loops and multiplies all the whole


def main():
    # variables
    answer = 1
    counter = 1

    # input
    number = int(input("Enter a number to loop it and multiply its results: "))

    # process & output
    while counter <= number:
        answer = answer * counter
        counter = counter + 1
    print("The factorial of your number is {}".format(answer))


if __name__ == "__main__":
    main()
