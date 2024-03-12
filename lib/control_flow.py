#!/usr/bin/env python3

def admin_login(username, password):
    if (username == 'admin' or username == 'ADMIN') and password == '12345':
        return "Access granted"
    else:
        return "Access denied"

def hows_the_weather(temperature):
    if temperature < 40:
        return "It's brisk out there!"
    elif ((temperature > 40) and (temperature < 65)):
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"

def fizzbuzz(num):
    if num % 3 ==0 and num % 5 ==0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else: 
        return num

def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero!"

def calculator(operation, num1, num2):
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }

    if operation in operations:
        return operations[operation](num1, num2)
    else:
        print("Invalid operation!")
        return None