# We can use non-boolean objects in if conditions and other places where a boolean would be expected. 
# Python will implicitly treat them as their corresponding boolean value:


print(bool(1)) # all numbers are treated as true, except 0
print(bool(0))
print(bool("asf")) # all strings are treated as true, except the empty string ""
print(bool(""))
# Generally empty sequences (strings, lists, and other types we've yet to see like lists and tuples)
# are "falsey" and the rest are "truthy"
print(bool(-56))