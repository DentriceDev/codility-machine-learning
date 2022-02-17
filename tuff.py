from itertools import combinations_with_replacement
import functools

list1 = combinations_with_replacement([0, 1, 2, 3, 4, 5, 6, 7, 8, 9],5)
g = 0
lst = []
def solution(N):
  x = [int(a) for a in str(N)]
  sum1 = 0
  for i in x:
    sum1 = sum1 + i

  for i in list(list1):
      lst.append(list(i))#convert tuple list

  for i in range(0, 10):
    lst.pop(0)
      
  for i in list(lst):
    g = sum(i)
    if(g == (sum1*2)):
      res = functools.reduce(lambda sub, ele: sub * 10 + ele, i) # Converting tuple to integer
      break

  return res

#test run
print(solution(99))
