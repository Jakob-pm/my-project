import random

# initialize variables
lst = []
total_sum = 0
target_sum = 360
num_elements = 30
min_val = 3
max_val = 30

# loop until the sum of the list is equal to the target sum
while total_sum != target_sum:
    # generate a random number between min_val and max_val
    num = random.randint(min_val, max_val)
    # if adding the number to the list would make the sum greater than the target sum, generate another number
    if total_sum + num > target_sum:
        continue
    # add the number to the list and update the total sum
    lst.append(num)
    total_sum += num
    # if the list has reached its desired length but the sum is not equal to the target sum, start over
    if len(lst) == num_elements and total_sum != target_sum:
        lst = []
        total_sum = 0

print(lst)