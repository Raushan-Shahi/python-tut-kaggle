

print(bool(1)) # all numbers are treated as true, except 0
print(bool(0))
print(bool("asf")) # all strings are treated as true, except the empty string ""
print(bool(""))
# Generally empty sequences (strings, lists, and other types we've yet to see like lists and tuples)
# are "falsey" and the rest are "truthy"
print(bool(-56))




# We can use non-boolean objects in if conditions and other places where a boolean would be expected. 
# Python will implicitly treat them as their corresponding boolean value:


if 0:                           #0 is a false statement so if condition will be skipped 
    print(0)
elif "spam":                    #"spam" is a true boolean so it will be executed 
    print("spam")