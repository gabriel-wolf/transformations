from Transformations import Trans

# create class of Trans
t = Trans("(x**3)")

# print trans test function
print(t.test())

# print out current full list to string
print(t.ListToString())

# print out current value to string
print(t.toString())

# translate t up by 1 and then print
t.translate(axis="y", val=1)
print(t.ListToString())


# reflect t over the x axis once and print
t.reflect(axis="x")
print(t.ListToString())

# reflect t over the y axis 3 times and print
t.reflect(axis="y")
print(t.ListToString())
t.reflect(axis="y")
print(t.ListToString())
t.reflect(axis="y")
print(t.ListToString())

# reflect t over the x axis once and print
t.reflect(axis="x")
print(t.ListToString())
