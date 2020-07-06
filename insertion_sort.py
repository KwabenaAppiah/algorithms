# Reference: https://www.tutorialspoint.com/insertion-sort-in-python-program

# Functions takes a list of numbers
def insertion_sort(nums):

    # Loops from index 1 to the last element in the list
    for j in range(1, len(nums)):
    
        # Set the current index to the var 'key'
        key = nums[j]
        
        # Update the var 'i' w/ a value that is 'j-1'
        # This should place 'i' at an index for 'j'
        i = j-1
        
        # While i is greater than or equal to zero AND the value of key is less than the value at nums[i]
        while i >= 0 and key < nums[i]:
        
            # If the loop condition is still true, the value at index i is greater than the index at i+1
            # Replace the element at index 'i+1' w/ the elment at index 'i'
            nums[i + 1] = nums[i]
            
            # Update the loop by decrementing 1 from the var 'i'
            i--

        nums[i + 1] = key

nums = [5, 2, 3, 6, 1, 3]
print("output 1: {}".format(nums))
insertion_sort(nums)
print("output 2: {}".format(nums))
