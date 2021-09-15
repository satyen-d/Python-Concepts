def BubbleSort(L):
    for i in range(len(L)):
        for j in range(len(L)-i-1):
            if L[j]>L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
            print(L)
        print(L)
    print(L)

L = [50,52,53,51,55,54]
BubbleSort(L)
