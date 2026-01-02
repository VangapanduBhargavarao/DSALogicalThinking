#1)
"""
****
****
****
****

rows=int(input())
for row in range(rows):
    for col in range(rows):
        print("*",end="")
    print()
"""

#### 2nd patterns
"""
*
**
***
****
*****



rows=int(input())
for row in range(1,rows+1):
    for col in range(row):
        print("*",end="")
    print()
"""

## third pattern.
"""
*****
****
***
**
*


rows=int(input())
for row in range(rows,0,-1):
    for col in range(row):
        print("*",end="")
    print()
"""

# right aligned right angle triange
"""
    *
   **
  ***
 ****
*****



rows=int(input())
for i in range(1,rows+1):
    print(" "*(rows-i),end="")
    for col in range(i):
        print("*",end="")
    print()
"""

####  full pyramid I think my best optimal solution for the patterns
"""
    *
   ***
  *****
 *******
*********



rows=int(input())
for row in range(1,rows+1):
    print(" "*(rows-row),end="")
    
    print("*"*(2*row-1),end="")
    print()
"""

#### inverted pyramid pattern

"""

*********
 *******
  *****
   ***
    *



rows=int(input())
for row in range(rows,0,-1):
    print(" "*(rows-row),end="")
    print("*"*(2*row-1),end="")
    print()
"""

#### diamond pattern

"""

   *
  ***
 *****
*******
 *****
  ***
   *



rows=int(input())
for i in range(1,rows+1):
    print(" "*(rows-i),end="")
    print("*"*(2*i-1),end="")
    print()
for i in range(rows-1,0,-1):
    print(" "*(rows-i),end="")
    print("*"*(2*i-1),end="")
    print()
"""


### Hallow square patterns
"""

*****
*   *
*   *
*   *
*****



rows=int(input())
for row in range(1,rows+1):
    for col in range(1,rows+1):
        if col==1 or row==1 or col==rows or row==rows:
            print("*",end="")
        else:
            print(" ",end="")
        
    print()
"""

### right angle hallow triangle.

"""
*
**
* *
*  *
*****



rows=int(input())
for row in range(1,rows+1):
    for col in range(1,row+1):
        if col==1 or col==row or row==rows:
            print("*",end="")
        else:
            print(" ",end="")
    print()
"""

### Hallow inverted triangle.
"""
*****
*  *
* *
**
*



rows=int(input())
for row in range(rows,0,-1):
    for col in range(1,row+1):
        if col==1 or col==row or row==rows:
            print("*",end="")
        else:
            print(" ",end="")
    print()
"""

## hallow center pyramid
"""

    *
   * *
  *   *
 *     *
*********

"""
