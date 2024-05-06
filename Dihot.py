import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

def function(x):
    return x**2 - 2*x*(4/9) + 16/81

def Swann_algorythm(x0,t):
    delta = 0
    power = 1
    if (function(x0 - t) >= function(x0)) and (function(x0) <= function(x0 + t)):
        return x0 - t, x0 + t
    
    if (function(x0 - t) <= function(x0)) and (function(x0) >= function(x0 + t)):
        raise ValueError("Функция не унимодальная, попробуйте выбрать другую начальную точку")
    
    if (function(x0 - t) >= function(x0)) and (function(x0) >= function(x0 + t)):
        delta = t
        a = x0
        x = x0 + t
    
    if (function(x0 - t) <= function(x0)) and (function(x0) <= function(x0 + t)):
        delta = -t
        b = x0
        x = x0 - t

    while (function(x) < function(x0)):
        power *= 2 
        x0 = x
        x = power*delta

        if (function(x) < function(x0)):
            if delta == t:
                a = x0
            else:
                b = x0
        else:
            if delta == t:
                b = x
            else:
                a = x
    return a, b

def dichotomy_method(f, a, b, epsilon, l):
    length = abs(b-a)
    k = 0
    points = [[a,b]]

    while length > l:
        y = (a + b - epsilon) / 2
        z = (a + b + epsilon) / 2

        if f(y) <= f(z):
            b = z
        else:
            a = y
        
        length = abs(b-a)
        k+=1
        points.append([a,b])
    return (a + b) / 2, k, points, a, b

def golden_ratio_method(f, a, b, l):
    
    delta = abs(b-a)
    k = 0
    golden_ratio = (3 - math.sqrt(5)) / 2
    points = [[a,b]]

    while delta > l:
        y = a + golden_ratio * (b - a)
        z = a + b - y

        if f(y) <= f(z):
            b = z
            y_new = a + b - y
            y = y_new
        else:
            a = y
            z_new = a + b - z
            z = z_new
        
        delta = abs(b-a)
        k+=1
        points.append([a,b])
    return (a + b) / 2, k, points, a, b

def drawplot(result, k, points):
    colors = ["r", "g", "b", "y", "k", "m"]
    n = len(colors)
    x = np.arange(a,b,0.01)
    y = function(x)
    plt.plot(x, y, color = 'k')
    for i in range(k):
        plt.plot([points[i][0],points[i][1]],[function(result) - 2 + i/k,function(result) - 2 + i/k], color = colors[i % n], linestyle='dashed')
        plt.plot([points[i][0],points[i][0]],[function(result) - 2 + i/k,function(points[i][0])], color = colors[i % n], linestyle='dashed', marker='o')
        plt.plot([points[i][1],points[i][1]],[function(result) - 2 + i/k,function(points[i][1])], color = colors[i % n], linestyle='dashed', marker='o')
    plt.show()

x0 = 3
t = 1
a, b = Swann_algorythm(x0,t)
result_dih, k, points, an, bn = dichotomy_method(function, a, b, 1e-3, 0.1)
drawplot(result_dih, k, points)
print(f"Решение уравнения методом дихотомии: x = {result_dih}, a = {an}, b = {bn}, f(x) = {function(result_dih)}, k = {k}")
result_gold, k, points, an, bn = golden_ratio_method(function, a, b, 0.1)
drawplot(result_gold, k, points)
print(f"Решение уравнения методом золотого сечения: x = {result_gold}, a = {an}, b = {bn}, f(x) = {function(result_gold)}, k = {k}")