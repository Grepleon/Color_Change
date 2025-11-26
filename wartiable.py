from tkinter import *
import sys
import math
from turtle import *
from tkinter import messagebox
from tkinter import ttk
import random
import time
import datetime as d
def is_prime(n):
    s = []
    if n == 1:
        return False
    for i in range(n):
        if n % (i + 1) == 0:
            s.append(i + 1)

    if len(s) <= 2:
        return True
    else:
        return False

def prime_factors(n):
    """Возвращает список всех простых множителей числа n (с учётом кратности)"""
    i = 2
    factors = []
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 1
    if n > 1:
        factors.append(n)
    return factors

def digit_sum(n):
    return sum(int(d) for d in str(n))

def is_smith_number(n):
    if n < 4 or is_prime(n):
        return False  # Простые и 1 — не могут быть числами Смита
    original_sum = digit_sum(n)
    factors = prime_factors(n)
    factor_digits_sum = sum(digit_sum(f) for f in factors)
    return original_sum == factor_digits_sum

def is_superprime(n):
    """Проверка, является ли число суперпростым."""
    if not is_prime(n):
        return False
    # Найдём порядковый номер n среди простых
    count = 0
    current = 2
    while current <= n:
        if is_prime(current):
            count += 1
        if current == n:
            break
        current += 1
    # Проверим, является ли этот порядковый номер простым
    return is_prime(count)


def generate_parentheses(n):
    result = []
    def backtrack(current, open_count, close_count):
        if len(current) == 2 * n:
            result.append(current)
            return
        if open_count < n:
            backtrack(current + '(', open_count + 1, close_count)
        if close_count < open_count:
            backtrack(current + ')', open_count, close_count + 1)
    backtrack('', 0, 0)
    return result

def final(x):
    n = x

    combinations = generate_parentheses(n)

    #print(*combinations)
    #print(len(combinations))

    return (len(combinations))

#final(x)

def Sterl(x):
    B = 1/2.71828
def Regular_WWW():
    print('X')

def rim(x):
    rim = ''
    x22 = x
    for i in range(int(x / 1000)):
        rim += 'M'
        x22 -= 1000
    if x22 >= 900:
        rim += 'CM'
        x22 -= 900
    for i in range(int(x22 / 500)):
        rim += 'D'
        x22 -= 500
    if x22 >= 400:
        rim += 'CD'
        x22 -= 400
    for i in range(int(x22 / 100)):
        rim += 'C'
        x22 -= 100
    if x22 >= 90:
        rim += 'XC'
        x22 -= 90
    for i in range(int(x22 / 50)):
        rim += 'L'
        x22 -= 50
    if x22 >= 40:
        rim += 'CL'
        x22 -= 40
    for i in range(int(x22 / 10)):
        rim += 'X'
        x22 -= 10
    if str(x)[-1] == '1':
        rim += 'I'
    if str(x)[-1] == '2':
        rim += 'II'
    if str(x)[-1] == '3':
        rim += 'III'
    if str(x)[-1] == '4':
        rim += 'IV'
    if str(x)[-1] == '5':
        rim += 'V'
    if str(x)[-1] == '6':
        rim += 'VI'
    if str(x)[-1] == '7':
        rim += 'VII'
    if str(x)[-1] == '8':
        rim += 'VIII'
    if str(x)[-1] == '9':
        rim += 'IX'
    if str(x)[-1] == '0':
        rim += ''
    return rim
def open_see_name_fail(x):
    save = open(x, 'r+')
    data = save.readlines()



    return data[0]

def error():
    exit()
    x = 0
    x+= 'Сметана'



def bella_beling(n):
    def bell_number(n):

        bell = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

        bell[0][0] = 1

        for i in range(1, n + 1):

            bell[i][0] = bell[i - 1][i - 1]

            for j in range(1, i + 1):
                bell[i][j] = bell[i - 1][j - 1] + bell[i][j - 1]

        return bell[n][0]
    return bell_number(n)




def sign(x):
    if x >0:
        z = 1
    elif x == 0:
        z = 0
    else:
        z = -1
    return z
def maxov(x,z):
    if abs(x) >=abs(z):
        x = 0
    else:
        x = x
    return x
def mirrormax(x,z):
    if x == abs(x):
        if x >= z:
            x = -z
    else:
        if x <= z:
            x = -z
    return x
def modmax(x,z):
    if x == abs(x):
        if x >= z:
            x = z
    else:
        if x <= z:
            x = z
    return x

def dell(x):
    d = []
    for i in range(int(x)):
        if abs(x) % (x - i) == 0:
            d . append (x - i)
    return(d)
def inter(x):
    z = input(x)
    while not z.isnumeric():

        if z.isnumeric():
            return(int(z))

        else:
            #print('int!')
            z = input(x)
    return int(z)


def Rx(Z_prom):
    def min2(s1,s2):
        s = []
        for i in range(len(s1)):
            if s1[i] not in s2 or s1.count(s1[i]) != s2.count(s1[i]):
                s.append(s1[i])
        if len(s) == 0:
            s = [-1]
        return min(s)
    Rx = []  # ранжированный список
    Rx.append(min(Z_prom))
    W_prom = []
    W_prom.append(min(Z_prom))

    while len(Z_prom) != len(W_prom):
        for i in Z_prom:
            if min2(Z_prom, W_prom) == i:
                Rx.append(i)
                W_prom.append(i)
    return Rx

def Reverse(n):
    n = str(n)
    n2 = ''
    I = -1
    for i in range(len(n) - 1):
        I += 1
        i = n[i]
        n2 += n[-I - 1]
    n2 += n[0]
    return n2
