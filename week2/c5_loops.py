while True:
    x = input("press a button, then press return. \n")

    try:
        x = int(x)
    except Exception as e:
        print(f"You entered a non-integer input. ({x})")
        continue
        
    if x <= 0:
        print(f"You entered a non-positive integer input. ({x})")
        continue

    for i in range(x):
        print(i, end="\t")
    
    break