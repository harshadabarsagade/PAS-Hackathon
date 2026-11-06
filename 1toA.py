
37\. Maximum and Minimum elements

```python
arr = [4, 9, 1, 7, 3]

maximum = arr[0]
minimum = arr[0]

for i in arr:
    if i > maximum:
        maximum = i
    if i < minimum:
        minimum = i

print("Max =", maximum)
print("Min =", minimum)
```

38\. Second largest element without sorting

```python
arr = [12, 35, 1, 10, 34, 1]

first = -999999
second = -999999

for i in arr:
    if i > first:
        second = first
        first = i
    elif i > second and i != first:
        second = i

print("Second largest =", second)
```

39\. Count even and odd numbers

```python
arr = [1, 2, 3, 4, 5, 6]
even = 0
odd = 0

for i in arr:
    if i % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print("Even =", even)
print("Odd =", odd)
```

40\. Count positive, negative and zero

```python
arr = [-1, 2, 0, -3, 5, 0]

pos = 0
neg = 0
zero = 0

for i in arr:
    if i > 0:
        pos = pos + 1
    elif i < 0:
        neg = neg + 1
    else:
        zero = zero + 1

print("Positive =", pos)
print("Negative =", neg)
print("Zero =", zero)
```

41\. Reverse an array

```python
arr = [1, 2, 3, 4]

i = 0
j = len(arr) - 1

while i < j:
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

    i = i + 1
    j = j - 1

print(arr)
```

42\. Copy one array to another

```python
arr = [10, 20, 30]
arr2 = []

for i in arr:
    arr2.append(i)

print(arr2)
```

43\. Insert element at index K

```python
arr = [1, 2, 4, 5]
x = 3
k = 2

arr.insert(k, x)

print(arr)
```

44\. Delete element at index K

```python
arr = [10, 20, 30, 40]
k = 1

arr.pop(k)

print(arr)
```

45\. Frequency of each element

```python
arr = [1, 2, 2, 3, 1, 4]

for i in arr:
    count = 0

    for j in arr:
        if i == j:
            count = count + 1

    print(i, "=", count)
```

46\. Print unique elements (appearing only once)

```python
arr = [1, 2, 2, 3, 4, 4]

for i in arr:
    count = 0

    for j in arr:
        if i == j:
            count = count + 1

    if count == 1:
        print(i)
```

47\. Remove duplicates from sorted array

```python
arr = [1, 1, 2, 2, 3]
new = []

for i in arr:
    if i not in new:
        new.append(i)

print("Length =", len(new))
print("Array =", new)
```

48\. Linear Search

```python
arr = [4, 2, 7, 1]
x = 7
found = -1

for i in range(len(arr)):
    if arr[i] == x:
        found = i

print(found)
```

49\. Binary Search

```python
arr = [1, 3, 5, 7, 9]
target = 7

low = 0
high = len(arr) - 1

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == target:
        print("Index =", mid)
        break
    elif arr[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
```

50\. Bubble Sort

```python
arr = [5, 1, 4, 2, 8]

for i in range(len(arr)):
    for j in range(len(arr) - 1):
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp

print(arr)
```

51\. Selection Sort

```python
arr = [64, 25, 12, 22, 11]

for i in range(len(arr)):
    min_index = i

    for j in range(i+1, len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j

    temp = arr[i]
    arr[i] = arr[min_index]
    arr[min_index] = temp

print(arr)
```

52\. Insertion Sort

```python
arr = [12, 11, 13, 5, 6]

for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1

    while j >= 0 and arr[j] > key:
        arr[j+1] = arr[j]
        j = j - 1

    arr[j+1] = key

print(arr)
```

53\. Left Rotate Array by K positions

```python
arr = [1, 2, 3, 4, 5]
k = 2

for i in range(k):
    first = arr[0]

    for j in range(len(arr)-1):
        arr[j] = arr[j+1]

    arr[len(arr)-1] = first

print(arr)
```

54\. Right Rotate Array by K positions

```python
arr = [1, 2, 3, 4, 5]
k = 2

for i in range(k):
    last = arr[len(arr)-1]

    for j in range(len(arr)-1, 0, -1):
        arr[j] = arr[j-1]

    arr[0] = last

print(arr)
```

55\. Check if array is sorted

```python
arr = [1, 2, 2, 4, 5]
sorted = True

for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        sorted = False

if sorted:
    print("True")
else:
    print("False")
```

56\. Find missing number from 1 to N

```python
arr = [1, 2, 4, 5, 6]
n = 6

total = n * (n+1) // 2
sum = 0

for i in arr:
    sum = sum + i

print("Missing =", total - sum)
```

57\. Single number (all others appear twice)

```python
arr = [4, 1, 2, 1, 2]

for i in arr:
    count = 0

    for j in arr:
        if i == j:
            count = count + 1

    if count == 1:
        print(i)
```

58\. Majority element

```python
arr = [3, 2, 3]

for i in arr:
    count = 0

    for j in arr:
        if i == j:
            count = count + 1

    if count > len(arr)//2:
        print(i)
        break
```

59\. Separate even and odd numbers

```python
arr = [1, 2, 3, 4, 5, 6]
even = []
odd = []

for i in arr:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print(even + odd)
```

60\. Merge two sorted arrays

```python
arr1 = [1, 3, 5]
arr2 = [2, 4, 6]

arr = arr1 + arr2

for i in range(len(arr)):
    for j in range(len(arr)-1):
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp

print(arr)
```

### Section 4: Two Pointers, Subarrays & Optimization (Q61–Q80)

61\. Two Sum

```python
arr = [2, 7, 11, 15]
target = 9

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == target:
            print(i, j)
```

62\. Three Sum

```python
arr = [-1, 0, 1, 2, -1, -4]
result = []

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        for k in range(j+1, len(arr)):
            if arr[i] + arr[j] + arr[k] == 0:
                temp = sorted([arr[i], arr[j], arr[k]])

                if temp not in result:
                    result.append(temp)

print(result)
```

63\. Move all zeroes to end

```python
arr = [0, 1, 0, 3, 12]
new = []

for i in arr:
    if i != 0:
        new.append(i)

for i in arr:
    if i == 0:
        new.append(i)

print(new)
```

64\. Separate 0s and 1s

```python
arr = [0, 1, 1, 0, 1, 0]
new = []

for i in arr:
    if i == 0:
        new.append(i)

for i in arr:
    if i == 1:
        new.append(i)

print(new)
```

65\. Sort array of 0s, 1s and 2s

```python
arr = [2, 0, 2, 1, 1, 0]

for i in range(len(arr)):
    for j in range(len(arr)-1):
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp

print(arr)
```

66\. Maximum Subarray Sum

```python
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

maximum = arr[0]

for i in range(len(arr)):
    total = 0

    for j in range(i, len(arr)):
        total = total + arr[j]

        if total > maximum:
            maximum = total

print(maximum)
```

67\. Maximum Product Subarray

```python
arr = [2, 3, -2, 4]
maximum = arr[0]

for i in range(len(arr)):
    product = 1

    for j in range(i, len(arr)):
        product = product * arr[j]

        if product > maximum:
            maximum = product

print(maximum)
```

68\. Best Time to Buy and Sell Stock (Single transaction)

```python
arr = [7, 1, 5, 3, 6, 4]

minimum = arr[0]
profit = 0

for i in arr:
    if i < minimum:
        minimum = i

    if i - minimum > profit:
        profit = i - minimum

print(profit)
```

69\. Best Time to Buy and Sell Stock II

```python
arr = [7, 1, 5, 3, 6, 4]
profit = 0

for i in range(1, len(arr)):
    if arr[i] > arr[i-1]:
        profit = profit + arr[i] - arr[i-1]

print(profit)
```

70\. Find Peak Element

```python
arr = [1, 2, 3, 1]

for i in range(1, len(arr)-1):
    if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
        print("Index =", i)
```

71\. Trapping Rain Water

```python
arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
total = 0

for i in range(len(arr)):
    left = max(arr[:i+1])
    right = max(arr[i:])

    water = min(left, right) - arr[i]
    total = total + water

print(total)
```

72\. Maximum Sum Subarray of Size K

```python
arr = [2, 1, 5, 1, 3, 2]
k = 3

maximum = 0

for i in range(len(arr)-k+1):
    total = 0

    for j in range(i, i+k):
        total = total + arr[j]

    if total > maximum:
        maximum = total

print(maximum)
```

73\. First Negative Integer in Every Window

```python
arr = [12, -1, -7, 8, -15, 30, 16, 28]
k = 3

for i in range(len(arr)-k+1):
    found = False

    for j in range(i, i+k):
        if arr[j] < 0:
            print(arr[j], end=" ")
            found = True
            break

    if found == False:
        print(0, end=" ")
```

74\. Find Equilibrium Index

```python
arr = [-7, 1, 5, 2, -4, 3, 0]

for i in range(len(arr)):
    left = 0
    right = 0

    for j in range(i):
        left = left + arr[j]

    for j in range(i+1, len(arr)):
        right = right + arr[j]

    if left == right:
        print("Index =", i)
        break
```

75\. Find Leaders in an Array

```python
arr = [16, 17, 4, 3, 5, 2]
leaders = []

for i in range(len(arr)):
    leader = True

    for j in range(i+1, len(arr)):
        if arr[j] > arr[i]:
            leader = False

    if leader:
        leaders.append(arr[i])

print(leaders)
```

76\. Longest Consecutive Sequence

```python
arr = [100, 4, 200, 1, 3, 2]
arr.sort()

count = 1
maximum = 1

for i in range(1, len(arr)):
    if arr[i] == arr[i-1] + 1:
        count = count + 1
    elif arr[i] != arr[i-1]:
        count = 1

    if count > maximum:
        maximum = count

print(maximum)
```

77\. Intersection of Two Arrays

```python
arr1 = [1, 2, 2, 1]
arr2 = [2, 2]
result = []

for i in arr1:
    if i in arr2 and i not in result:
        result.append(i)

print(result)
```

78\. Product of Array Except Self

```python
arr = [1, 2, 3, 4]
result = []

for i in range(len(arr)):
    product = 1

    for j in range(len(arr)):
        if i != j:
            product = product * arr[j]

    result.append(product)

print(result)
```

79\. Subarray Sum Equals K

```python
arr = [1, 1, 1]
k = 2
count = 0

for i in range(len(arr)):
    total = 0

    for j in range(i, len(arr)):
        total = total + arr[j]

        if total == k:
            count = count + 1

print(count)
```

80\. Container With Most Water

```python
arr = [1, 8, 6, 2, 5, 4, 8, 3, 7]
maximum = 0

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        height = min(arr[i], arr[j])
        width = j - i
        area = height * width

        if area > maximum:
            maximum = area

print(maximum)
```

### Section 5: 2D Arrays & Matrices (Q81–Q100)

81\. Matrix Sum

```python
arr = [[1, 2], [3, 4]]
total = 0

for i in arr:
    for j in i:
        total = total + j

print("Sum =", total)
```

82\. Addition of Two Matrices

```python
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

result = []

for i in range(2):
    row = []

    for j in range(2):
        row.append(A[i][j] + B[i][j])

    result.append(row)

print(result)
```

83\. Multiplication of Two Matrices

```python
A = [[1, 2], [3, 4]]
B = [[1, 0], [0, 1]]

result = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        for k in range(2):
            result[i][j] = result[i][j] + A[i][k] * B[k][j]

print(result)
```

84\. Transpose of a Matrix

```python
arr = [[1, 2, 3], [4, 5, 6]]
result = []

for j in range(3):
    row = []

    for i in range(2):
        row.append(arr[i][j])

    result.append(row)

print(result)
```

85\. Main and Anti-Diagonal Sum

```python
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

main = 0
anti = 0

for i in range(3):
    main = main + arr[i][i]
    anti = anti + arr[i][2-i]

print("Main =", main)
print("Anti =", anti)
```

86\. Check Symmetric Matrix

```python
arr = [[1, 2], [2, 1]]
symmetric = True

for i in range(2):
    for j in range(2):
        if arr[i][j] != arr[j][i]:
            symmetric = False

print(symmetric)
```

87\. Check Identity Matrix

```python
arr = [[1, 0], [0, 1]]
identity = True

for i in range(2):
    for j in range(2):
        if i == j and arr[i][j] != 1:
            identity = False

        if i != j and arr[i][j] != 0:
            identity = False

print(identity)
```

88\. Row-wise and Column-wise Sum

```python
arr = [[1, 2], [3, 4]]

for i in range(2):
    total = 0

    for j in range(2):
        total = total + arr[i][j]

    print("Row sum =", total)

for j in range(2):
    total = 0

    for i in range(2):
        total = total + arr[i][j]

    print("Column sum =", total)
```

89\. Rotate Matrix 90 Degrees Clockwise

```python
arr = [[1, 2], [3, 4]]
result = []

for j in range(2):
    row = []

    for i in range(1, -1, -1):
        row.append(arr[i][j])

    result.append(row)

print(result)
```

90\. Rotate Matrix 90 Degrees Counter-Clockwise

```python
arr = [[1, 2], [3, 4]]
result = []

for j in range(1, -1, -1):
    row = []

    for i in range(2):
        row.append(arr[i][j])

    result.append(row)

print(result)
```

91\. Spiral Order Traversal

```python
arr = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

top = 0
bottom = 2
left = 0
right = 2

while top <= bottom and left <= right:

    for i in range(left, right+1):
        print(arr[top][i], end=" ")
    top = top + 1

    for i in range(top, bottom+1):
        print(arr[i][right], end=" ")
    right = right - 1

    if top <= bottom:
        for i in range(right, left-1, -1):
            print(arr[bottom][i], end=" ")
        bottom = bottom - 1

    if left <= right:
        for i in range(bottom, top-1, -1):
            print(arr[i][left], end=" ")
        left = left + 1
```

92\. Search in Sorted Matrix

```python
arr = [[1, 4, 7],
       [2, 5, 8],
       [3, 6, 9]]

target = 5

for i in range(3):
    for j in range(3):
        if arr[i][j] == target:
            print("Found at", i, j)
```

93\. Set Matrix Zeroes

```python
arr = [[1, 1, 1],
       [1, 0, 1],
       [1, 1, 1]]

rows = []
cols = []

for i in range(3):
    for j in range(3):
        if arr[i][j] == 0:
            rows.append(i)
            cols.append(j)

for i in rows:
    for j in range(3):
        arr[i][j] = 0

for j in cols:
    for i in range(3):
        arr[i][j] = 0

print(arr)
```

94\. Boundary Elements Traversal

```python
arr = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

for j in range(3):
    print(arr[0][j], end=" ")

for i in range(1, 3):
    print(arr[i][2], end=" ")

for j in range(1, -1, -1):
    print(arr[2][j], end=" ")

for i in range(1, 0, -1):
    print(arr[i][0], end=" ")
```

95\. Row with Maximum Number of 1s

```python
arr = [[0, 1, 1],
       [1, 1, 1],
       [0, 0, 1]]

maximum = 0
row = 0

for i in range(3):
    count = 0

    for j in range(3):
        if arr[i][j] == 1:
            count = count + 1

    if count > maximum:
        maximum = count
        row = i

print("Row =", row)
```

96\. Check Sparse Matrix

```python
arr = [[0, 0, 3],
       [0, 0, 0],
       [1, 0, 0]]

count = 0

for i in arr:
    for j in i:
        if j == 0:
            count = count + 1

if count > 9//2:
    print("True")
else:
    print("False")
```

97\. Anti-Diagonal Traversal (Zigzag)

```python
arr = [[1, 2],
       [3, 4]]

n = 2

for total in range(2*n-1):
    for i in range(n):
        j = total - i

        if j >= 0 and j < n:
            print(arr[i][j], end=" ")
    print()
```

98\. Saddle Point of Matrix

```python
arr = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

for i in range(3):
    minimum = arr[i][0]

    for j in range(3):
        if arr[i][j] < minimum:
            minimum = arr[i][j]

    col = 0

    for j in range(3):
        if arr[i][j] == minimum:
            col = j

    largest = True

    for k in range(3):
        if arr[k][col] > minimum:
            largest = False

    if largest:
        print(minimum)
```

99\. Valid Sudoku Board Verification

```python
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

valid = True

for i in range(9):
    row = []
    col = []

    for j in range(9):
        if board[i][j] != ".":
            if board[i][j] in row:
                valid = False
            row.append(board[i][j])

        if board[j][i] != ".":
            if board[j][i] in col:
                valid = False
            col.append(board[j][i])

for i in range(0, 9, 3):
    for j in range(0, 9, 3):
        box = []

        for r in range(i, i+3):
            for c in range(j, j+3):
                if board[r][c] != ".":
                    if board[r][c] in box:
                        valid = False
                    box.append(board[r][c])

print(valid)
```

100\. Generate N × N Spiral Matrix

```python
n = 3

arr = [[0 for j in range(n)] for i in range(n)]

top = 0
bottom = n-1
left = 0
right = n-1

num = 1

while top <= bottom and left <= right:

    for j in range(left, right+1):
        arr[top][j] = num
        num = num + 1
    top = top + 1

    for i in range(top, bottom+1):
        arr[i][right] = num
        num = num + 1
    right = right - 1

    for j in range(right, left-1, -1):
        if top <= bottom:
            arr[bottom][j] = num
            num = num + 1
    bottom = bottom - 1

    for i in range(bottom, top-1, -1):
        if left <= right:
            arr[i][left] = num
            num = num + 1
    left = left + 1

print(arr)
```

### Important concepts to practise

| Concept      | Used in questions |
| ------------ | ----------------- |
| for loop     | 36–100            |
| Nested loops | 45, 50, 62, 83    |
| List         | 36–80             |
| append()     | 42, 46, 59        |
| Indexing     | 41, 43, 44        |
| Two pointers | 53, 54, 80        |
| Matrix       | 81–100            |
| while loop   | 91, 100           |

My advice: Practise Section 3 first, then Section 4, and finally Section 5. Don't try to memorize all 65 programs at once.

One important thing: These are beginner-friendly versions, so some use simple nested loops instead of optimized algorithms. For questions with different input sizes, a few programs will need adjustments.


