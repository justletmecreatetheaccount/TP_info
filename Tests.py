text = "a.b ?$$"
r = ""
for c in text:
    if c.isalpha():
        r += c
print (r)