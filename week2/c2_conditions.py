x = input("press a button, then press return. \n")
try:
	x = float(x)
except Exception as e:
	print("you entered a non-numeric input. (%s)" % (x))
	raise e

if x == 2.5:
	print("5/2 is %.2f" % (x))
elif x % 1 == 0:
	print(f"you entered an integer. ({int(x)})")
else:
	print(f"you entered a float. ({x})")