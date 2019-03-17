from sympy import sin, cos, tan, asin, acos, atan, symbols, solve, sympify, pprint, pretty
from sympy import pi, Eq, Function, exp, simplify, solveset, S
from sympy.parsing.sympy_parser import parse_expr
from sympy.abc import x, theta
from sympy.solvers import solve
from sympy import Symbol
from sympy.geometry import *
from sympy.parsing.sympy_parser import parse_expr

# plotting imports
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox


# transformations class
class Trans():
    # instantiate variables
    x = Symbol('x')
    x, y, z, t = symbols('x y z t')
    k, m, n = symbols('k m n', integer=True)
    f, g, h = symbols('f g h', cls=Function)
    
    # init ran on creation
    def __init__(self, expression):
        self.f = expression
        self.flist = [self.f]
        self.fig, self.ax = plt.subplots()
        plt.subplots_adjust(bottom=0.2)
        self.t = np.arange(-15.0, 15.0, 0.001)
        self.s = self.t ** 2
        
    # test method to test that creation worked
    def test(self):
        return "Testing class: \nClass Creation Successful"

    # convert string to sympy format
    def tosymp(self, expr):
        return parse_expr(expr)

    # plot function using matplotlib
    def plot(self):
        self.l, = plt.plot(self.t, self.s, lw=2)
        self.axbox = plt.axes([0.1, 0.05, 0.8, 0.075])
        # convert x to self.t
        xt = self.flist[len(self.flist)-1]
        xt = xt.replace("x","(self.t)")
        ydata = eval(xt)
        self.l.set_ydata(ydata)
        self.ax.set_ylim(np.min(ydata), np.max(ydata))
        plt.draw()
        plt.show()


    # get full list in string format 
    def ListToString(self, header=True):
        if header == True:
            retString = "\nFull list of values: \n"
        else:
            retString = ""
        for i in range(len(self.flist)):
            if (i+1 != len(self.flist)):
                retString = retString + (str((i + 1)) + ". " + str(self.tosymp(self.flist[i]))) + "\n"
            else:
                retString = retString + (str((i + 1)) + ". " + str(self.tosymp(self.flist[i])))
        return retString

    # get only final value in string format
    def toString(self):
        return ("\nCurrent value: \n" + str(self.tosymp(self.flist[len(self.flist) - 1])))

    # return copy of entire list
    def getList(self):
        return self.flist

    # get final value in list
    def getFinal(self):
        return self.flist[len(self.flist)-1]

    # get first value in list
    def getInitial(self):
        return self.flist[0]

    # gte value at index
    def getIndex(self, index=0):
        return self.flist[index]

    # set list 
    def setList(self, newList=["0"]):
        self.flist = newList

    # set index of list
    def setIndex(self, index=0, value=1):
        self.flist[index] = value

    # translate by value
    def translate(self, axis="x", val=1):
        vertorhor = "vertically"
        if axis == "x":
            vertorhor = "horizontally"
        else:
            vertorhor = "vertically"
        print("\nTranslating " + str(vertorhor) + " by " + str(val) + "...")
        curr = self.flist[len(self.flist)-1]
        # if x then hor
        if (axis == "x"):
            toadd = curr
            symptoadd = self.tosymp(toadd)
            print(symptoadd.args)
            symptoadd = symptoadd.replace(x,val+x)
            self.flist.append(str(symptoadd))
        # else if y then vert
        else:
            toadd = curr
            symptoadd = self.tosymp(toadd)
            symptoadd = symptoadd + val
            self.flist.append(str(symptoadd))
        
    # reflect over x or y axis
    def reflect(self, axis="x"):
        print("\nReflecting over the " + str(axis) + "-axis...")
        curr = self.flist[len(self.flist)-1]
        # if x then flip over x axis
        if (axis == "x"):
            toadd = curr
            symptoadd = self.tosymp(toadd)
            symptoadd = symptoadd * (-1)
            self.flist.append(str(symptoadd))
        # else if y flip over y axis 
        else:
            toadd = curr
            symptoadd = self.tosymp(toadd)
            symptoadd = symptoadd.replace(x,-1*x)
            self.flist.append(str(symptoadd))
            

        
