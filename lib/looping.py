#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    counter = 10
    while counter > 0:
        print(counter)
        counter -= 1
        print("Happy New Year!")

def square_integers(int_list):
    # code goes here!
    
    return [num ** 2 for num in int_list]
    

def fizzbuzz():
    # code goes here!
    for i in range(100):
        print(i)
        while i == 3:
            print("Fizz")
            while i == 5:
                print("Buzz")
                while i == 3 and 5:
                    print("FizzBuzz")
