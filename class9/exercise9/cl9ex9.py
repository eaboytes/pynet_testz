'''
Write a Python script in a different directory (not the one containing mytest).

    a. Verify that you can import mytest and call the three functions func1(), func2(), and func3().
    b. Create an object that uses MyClass. Verify that you call the hello() and not_hello() methods.
'''
import mytest
from mytest import *
func1()
func2()
func3()

obj=mytest.Myclass('10.4.4.4', 'lastuser', '4044')
obj.hello()
obj.not_hello()

