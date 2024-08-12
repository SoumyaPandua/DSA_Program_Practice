import array as arr

def second_max(arr, n):
  if n<2:
    return None
  
  maximum = float('-inf')
  second_maximum = float('-inf')
  for i in range(n):
    if arr[i] > maximum:
      second_maximum = maximum
      maximum = arr[i]
    elif arr[i] > second_maximum and arr[i] != maximum:
      second_maximum = arr[i]
  
  return second_maximum

arr = arr.array('i', [1,29,3,5,1,7])
print(second_max(arr, len(arr)))