with open("dane1.txt") as file:
    arr1 = [line.split() for line in file]
with open("dane2.txt") as file:
    arr2 = [line.split() for line in file]
    
    counter = 0
for i in range(1000):
    if arr1[i][-1] == arr2[i][-1]:
        counter +=1
print(counter)
