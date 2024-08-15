"""Ways to convert String to Raw String
Here, we will see the various ways to use the string text to convert Python r String,
 without its meaning getting changed.

Using r before string declaration
Using double backslashes instead of a single backslash
Using repr() function
To Count occurrences of escape sequence in string"""
print(r"some\name")
s = '\name'
raw_string = repr(s)[1:-1]
print(raw_string)
