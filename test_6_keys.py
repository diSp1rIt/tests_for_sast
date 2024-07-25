import ctypes

a = input()

b = ctypes.cast(id(a), ctypes.py_object).value

eval(b)