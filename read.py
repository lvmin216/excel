import sys
f=open("hui.txt")
try:
    all_the_text=f.read()
finally:
    f.close()
