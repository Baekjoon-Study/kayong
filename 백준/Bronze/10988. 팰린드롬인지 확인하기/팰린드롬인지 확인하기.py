Word = input()
i, j = 0, len(Word)-1
while i < j:
    if Word[i] == Word[j]:
        i += 1
        j -= 1
    else:
        print(0)
        break
if i >= j:
    print(1)