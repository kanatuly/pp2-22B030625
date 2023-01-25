x = 5
print(type(x))

x = "Hello World" # str("Hello World")
print(type(x))

x = 20 # int(20)
print(type(x))

x = 20.5 # float(20.5)
print(type(x))

x = 1j # complex(1j)
print(type(x))

x = ["apple", "banana", "cherry"] # list(("apple", "banana", "cherry"))

print(type(x))

x = ("apple", "banana", "cherry") # tuple(("apple", "banana", "cherry"))
print(type(x))

x = range(6)
print(type(x))

x = {"name" : "John", "age" : 36} # dict(name="John", age=36)
print(type(x))

x = {"apple", "banana", "cherry"} # set(("apple", "banana", "cherry"))
print(type(x))

x = frozenset({"apple", "banana", "cherry"}) # frozenset(("apple", "banana", "cherry"))
print(type(x))

x = True # bool(5)
print(type(x))

x = b"Hello" # bytes(5)
print(type(x))

x = bytearray(5)
print(type(x))

x = memoryview(bytes(5))
print(type(x))

x = None
print(type(x))


"""
Exercise:
The following code example would print the data type of x, what data type would that be?
"""
x = 5
print(type(x)) #int
