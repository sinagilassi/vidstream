from sigiTest.core.core_fun1 import cFun1_1
from sigiTest.core import cFun2_2


def dFun1_1():
    return "dFun1_1" + cFun1_1() + " - " + cFun2_2()


def dFun1_2():
    return "dFun1_2"
