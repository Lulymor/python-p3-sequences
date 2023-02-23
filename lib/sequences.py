#!/usr/bin/env python3

def print_fibonacci(length):
    fib = [0, 1] # first numbers of the sequence
    i = 2 # the next number 
    while i < length: 
        fib.append(fib[i-1] + fib[i-2]) #append 
        i +=1
    print(fib[0:length])
