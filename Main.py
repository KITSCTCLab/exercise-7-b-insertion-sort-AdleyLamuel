from typing import List

def insertionSort(array) -> List[int]:
  for i in range(1, size-1):
    v = List[i]
    j = i-1
    while j>=0 and List[j]>v:
      List[j+1] = List[j]
      j = j-1
    List[j+1] = v

# data = [9, 5, 1, 4, 3]
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(insertionSort(data))
