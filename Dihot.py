import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

def function(x):
    return x**2 - 2*x*(4/9) + 16/81

def Swann_algorythm(x0, t, ismax):
    delta = 0
    power = 1
    if ismax == 0:
        coeff = 1
    else:
        coeff = -1
    if (function(x0 - t)*coeff >= function(x0)*coeff) and (function(x0)*coeff <= function(x0 + t)*coeff):
        return x0 - t, x0 + t
    
    if (function(x0 - t)*coeff <= function(x0)*coeff) and (function(x0)*coeff >= function(x0 + t)*coeff):
        raise ValueError("Функция не унимодальная, попробуйте выбрать другую начальную точку")
    
    if (function(x0 - t)*coeff >= function(x0)*coeff) and (function(x0)*coeff >= function(x0 + t)*coeff):
        delta = t
        a = x0
        x = x0 + t
    
    if (function(x0 - t)*coeff <= function(x0)*coeff) and (function(x0)*coeff <= function(x0 + t)*coeff):
        delta = -t
        b = x0
        x = x0 - t

    while (function(x)*coeff < function(x0)*coeff):
        power *= 2 
        x0 = x
        x = power*delta

        if (function(x)*coeff < function(x0)*coeff):
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

def dichotomy_method(f, a, b, epsilon, l, ismax):
    length = abs(b-a)
    k = 0
    points = [[a,b]]
    if ismax == 0:
        coeff = 1
    else:
        coeff = -1
    while length > l:
        y = (a + b - epsilon) / 2
        z = (a + b + epsilon) / 2

        if f(y)*coeff <= f(z)*coeff:
            b = z
        else:
            a = y
        
        length = abs(b-a)
        k+=1
        points.append([a,b])
    return (a + b) / 2, k, points, a, b

def golden_ratio_method(f, a, b, l, ismax):
    if ismax == 0:
        coeff = 1
    else:
        coeff = -1
    delta = abs(b-a)
    k = 0
    golden_ratio = (3 - math.sqrt(5)) / 2
    points = [[a,b]]

    while delta > l:
        y = a + golden_ratio * (b - a)
        z = a + b - y

        if f(y)*coeff <= f(z)*coeff:
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
ismax = int(input("Введите 1 если ищется максимум функции и 0 для поиска минимума: "))
if ismax != 0 and ismax != 1:
    raise ValueError("Введённое значение может быть только 0 или 1")
a, b = Swann_algorythm(x0, t, ismax)
print(a,b)
result_dih, k, points, an, bn = dichotomy_method(function, a, b, 1e-3, 0.1, ismax)
drawplot(result_dih, k, points)
print("Отрезки для метода дихотомии:")
for i in range(k):
    print("a{0} = {1}".format(i, points[i][0]))
    print("b{0} = {1}".format(i, points[i][1]))
    print("l{0} = {1}".format(i, points[i][1] - points[i][0]))
    print('\n')
print(f"Решение уравнения методом дихотомии: x = {result_dih}, f(x) = {function(result_dih)}, k = {k-1}")

result_gold, k, points, an, bn = golden_ratio_method(function, a, b, 0.1, ismax)
drawplot(result_gold, k, points)
print("Отрезки для метода золотого сечения:")
for i in range(k):
    print("a{0} = {1}".format(i, points[i][0]))
    print("b{0} = {1}".format(i, points[i][1]))
    print("l{0} = {1}".format(i, points[i][1] - points[i][0]))
    print('\n')
print(f"Решение уравнения методом золотого сечения: x = {result_gold}, f(x) = {function(result_gold)}, k = {k-1}")