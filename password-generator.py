Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
... import string
... total = string.ascii_letters + string.digits + string.punctuation
... length = 16
... password = "".join(random.sample(total, length))
