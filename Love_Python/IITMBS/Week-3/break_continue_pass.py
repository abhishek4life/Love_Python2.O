
### 1. `break`
#The `break` statement is used to exit the loop prematurely when a certain condition is met.

#**Example:**
for i in range(10):
    if i == 5:
        break
    print(i)

# Output: 0 1 2 3 4

#In this example, the loop breaks when `i` equals 5, so it stops executing at that point.

### 2. `continue`
#The `continue` statement is used to skip the rest of the code inside the loop for the current
# iteration and move to the next iteration.

#**Example:**

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# Output: 1 3 5 7 9

#In this example, the loop skips over even numbers and only prints odd numbers.

### 3. `pass`
#The `pass` statement is a null statement in Python and it is used as a placeholder.
# It means "do nothing" and is often used to indicate that a block of code will be written in the future.

#**Example:**
for i in range(5):
    if i == 2:
        pass
    print(i)

# Output: 0 1 2 3 4

#In this example, `pass` does nothing and the loop continues as usual.

#Each of these statements serves its unique purpose in controlling the flow of loops.
