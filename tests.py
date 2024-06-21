for i in range(9):
    print(f"i = {i}")
    for j in range(9):
        print(f"j = {j}")
        for k in range(9):
            print(f"k = {k}")
            if k == 1:
                break
        print("Here")