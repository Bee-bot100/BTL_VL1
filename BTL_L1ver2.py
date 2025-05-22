import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, sympify, lambdify, diff

def change(string):
    t = symbols('t')
    t_expr = sympify(string)
    return t_expr
def cal(Qh,Qc):
    work = Qh - Qc
    n = work/Qh
    return n,work
def d(expr):
    t = symbols('t')
    return diff(expr,t)

def P_draw(Work,time):
    t = symbols('t')
    P_expr = d(Work)
    P_func = lambdify((t), P_expr, 'numpy')
    t = np.linspace(0,time,100)
    fig = plt.figure(figsize=(5,5))
    ax = fig.add_subplot()
    if P_expr.is_constant():
        func = np.ones_like(t) * P_expr
        ax.plot(t,func)
    else:
        func = P_func
        ax.plot(t,func(t))
    ax.set_title(f"Đồ thị của công suất theo thời gian t")
    ax.set_xlabel('t(s)')
    ax.set_ylabel('P(W)')
    ax.axis('equal')
    plt.grid()
    plt.show()
    
def main():
    #input
    Qh = input("Nhập hàm Qh(t): ")
    Qc = input("Nhập hàm Qc(t): ")
    time = float(input("Nhập thời gian chu trình: "))
    #Change
    Qh_expr = change(Qh)
    Qc_expr = change(Qc)
    #Calculate
    n, W = cal(Qh_expr,Qc_expr)
    print(f"Hiệu suất: {n}",f"Công: {W}", sep= "\n")
    #Draw
    P_draw(W,time)
main()