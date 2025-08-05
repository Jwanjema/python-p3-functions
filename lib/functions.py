#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")


def greet(name):
    print(f"Hello, {name}!")


def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")


def add(num1, num2):
    print(f"The sum is: {num1 + num2}")
    return num1 + num2


add(45, 55)  # Example usage


def halve(number):
    print(f"The half is: {number / 2}")
    return number / 2
