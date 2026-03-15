import sympy
import math
fc=input('请输入方程式: ').strip()#后面是把什么空白的删去
x=sympy.Symbol('x')
y=sympy.Symbol('y')
def xishu(a):
    a=a.replace(' ','').replace('^','**')
    left,right=a.split('=')#把等式分成两部分
    l=sympy.sympify(left)
    r=sympy.sympify(right)#把字符串转换成sympy的表达式,henhenzhongyao
    shi=l-r
    x=sympy.Symbol('x')
    xi=sympy.poly(shi,x).all_coeffs()#求多项式的系数,固定搭配
    cishu=len(xi)-1
    return xi,cishu
def jiyuan(fcstr):
    fcstr=fcstr.replace(' ','').replace('^','**')
    left,right=fcstr.split('=')
    expr=left+'-('+right+')'
    exstr=sympy.sympify(expr)
    ji=exstr.free_symbols#获取方程式中的未知数
    yuan=len(ji)
    return yuan
yuan=jiyuan(fc)
xi,cishu=xishu(fc)#解包获取
def shouyiyuanyici():#(手写一元一次)
        a=xi[0]
        b=xi[1]
        x=(-b/a)
        return x
def shouyiyuanyierci():#(手写一元二次)
        a=xi[0]
        b=xi[1]
        c=xi[2]
        x1=(-b+math.sqrt(b**2-4*a*c))/(2*a)
        x2=(-b-math.sqrt(b**2-4*a*c))/(2*a)
        return x1,x2
def shoueryuanyici():#(手写二元一次)
        a=xi[0]
        b=xi[1]
        c=xi[2]
        d=xi[3]
        e=xi[4]
        f=xi[5]
        y=(a*f-c*d)/(a*e-c*b)
        x=(f-e*y)/d
        return x,y
def shouyiyuansanci():#(手写一元三次)
        a=xi[0]
        b=xi[1]
        c=xi[2]
        d=xi[3]
        x1=(-b+math.sqrt(b**2-3*a*c))/(3*a)
        x2=(-b-math.sqrt(b**2-3*a*c))/(3*a)
        x3=(-b)/(3*a)
        return x1,x2,x3
def syyiyuanyici(fc):#(sympy解一元一次)
    x=sympy.Symbol('x')
    left,right=fc.split('=')
    leftexper=sympy.sympify(left.replace(' ','').replace('^','**'))
    rightexper=sympy.sympify(right.replace(' ','').replace('^','**'))
    equation=sympy.Eq(leftexper,rightexper)
    result=sympy.solve(equation,x)
    return result
def syyiyuanyierci(fc):#(sympy解一元二次)
    x=sympy.Symbol('x')
    left,right=fc.split('=')
    leftexper=sympy.sympify(left.replace(' ','').replace('^','**'))
    rightexper=sympy.sympify(right.replace(' ','').replace('^','**'))
    equation=sympy.Eq(leftexper,rightexper)
    result=sympy.solve(equation,x)
    return result
def syeryuanyici(fc):#(sympy解二元一次)
    x=sympy.Symbol('x')
    y=sympy.Symbol('y')
    left,right=fc.split('=')
    leftexper=sympy.sympify(left.replace(' ','').replace('^','**'))
    rightexper=sympy.sympify(right.replace(' ','').replace('^','**'))
    equation=sympy.Eq(leftexper,rightexper)
    x,y=sympy.solve(equation,[x,y])
    return x,y
def syyiyuansanci(fc):#(sympy解一元三次)
    x=sympy.Symbol('x')
    left,right=fc.split('=')
    leftexper=sympy.sympify(left.replace(' ','').replace('^','  **'))
    rightexper=sympy.sympify(right.replace(' ','').replace('^','**'))
    equation=sympy.Eq(leftexper,rightexper)
    x=sympy.solve(equation,x)
    return x     
if yuan==1:
    if cishu==1:
         print('手写一元一次: ',shouyiyuanyici())
         print('sympy一元一次',syyiyuanyici(fc))
    elif cishu==2:
            print('手写一元二次: ',shouyiyuanyierci())
            print('sympy一元二次',syyiyuanyierci(fc))
    elif cishu==3:
            print('手写一元三次: ',shouyiyuansanci())
            print('sympy一元三次',syyiyuansanci(fc))
if  yuan==2:
    if cishu==1:
        print('手写二元一次: ',shoueryuanyici())
        print('sympy二元一次',syeryuanyici(fc))