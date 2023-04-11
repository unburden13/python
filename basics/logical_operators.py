
# ternary operator
is_friend = True
# condition_if_true if condition else condition_if_else
can_message = "message allowed" if is_friend else "not allowed to message"

print(can_message)

is_magician = True
is_expert = False

magic_message = ""
if is_magician and is_expert:
    magic_message = "you are a master magician"
elif is_magician and not is_expert:
    magic_message = "at least you're getting there"
elif not is_magician:
    magic_message = "you need magic powers"

print(magic_message)

# '==' looks for equality of VALUE
# 'is' checks of location in memory where values are stored are the same

print(True == 1)  # True
print('' == 1)  # False
print([] == 1)  # False
print(10 == 10.0)  # True
print([] == [])  # True

#  following lines will raise a syntax error since python 3.8
#  https://docs.python.org/3.8/whatsnew/3.8.html#changes-in-python-behavior
print(True is 1)  # False --
print('' is 1)  # False
print([] is 1)  # False
print(10 is 10.0)  # False
print([] is [])  # False -except this one
