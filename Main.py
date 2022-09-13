from typing import List

def insertionSort(a) -> List[int]:
  for i in range(1, len(a)-1):
    v = a[i]
    j = i-1
    while j>=0 and a[j]>v:
      a[j+1] = a[j]
      j = j-1
    a[j+1] = v

# data = [9, 5, 1, 4, 3]
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(insertionSort(data))
