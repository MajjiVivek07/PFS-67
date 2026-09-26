#module
# A module is a python file containing python code such as variables, functions, classes and statements and can be used in another python program
#python file ending with "".py"
#why do we need modules:
#code organization
#avoid rewriting
#reducing error
#code reusability
#team development

#types of modules
#1) built in/standard library modules
#these comes with python
#eg: math, random, sys, os, datetime, statistics
import math
print(math.sqrt(25))

import calculator 
print(calculator.add(10,20))
#if we want specific function we use
from calculator import add,sub
#if we want every function we use
from calculator import *

#user defined- modules created bt yourself

#third party modules:
#requests, django, flask, pandas, numpy
#these are developed outside python's standard library and are normally installed seperately