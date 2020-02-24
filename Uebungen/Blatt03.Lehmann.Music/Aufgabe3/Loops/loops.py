#!/usr/bin/env python3
# Lehmann.Music 

n = 10

print("==== 1 =====")
i = 1
j = n
while i < j:
    print(i)
    i += 3 

""" original code
print("==== 1 =====")
# [1] convert to while loop:
for i in range(0, n, 3):
  print(i)
"""


print("==== 2 =====")
for i in range(0,int(n/2),1):
     j = n - i
     print(i,j)

""" original code
# [2] convert to for loop:
print("==== 2 =====")
i = 0
j = n
while i < j:
  print(i, j)
  i += 1
  j -= 1
"""


print("==== 3 =====")
i = n
while i > -n:
    print(i)
    i -= 1

""" original code
# [3] convert to while loop:
print("==== 3 =====")
for i in range(n, -n, -1):
  print(i)
"""

print("==== 4 =====")
for i in range(1,n+1,1):
    print(i)


""" original code
# [4] convert to for loop:
print("==== 4 =====")
i = 1
while True:
  print(i)
  i += 1
  if i > n:
    break
"""
