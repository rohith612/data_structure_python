def test_py(n):
    for i in range(n+1):
        for j in range(i):
            print(j, end=" ") 
        print("\n")

test_py(10)