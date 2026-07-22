# =============== original solution======================
class Solution(object):
    def moveZeroes(self, nums):
        zero = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zero.append(0)
        for i in zero:
            nums.remove(0)
        nums.extend(zero)
        return nums

"""
first problem: remove() is expensive
The cost is: 𝑂(𝑛)

second problem: you create an unnecessary list
you only need: How many zeros exist?
This is a very important programming habit: Store information, not objects.

third problem: you use extra memory
Memory: 𝑂(𝑛)
But this problem can be solved in-place.
The requirement is: Modify nums directly.

The key observation:
We don't need to move zeros.
We only need to move non-zero numbers forward.
"""
# ============= optimal idea: two pointers ==================
class Solution(object):
    def moveZeroes(self, nums):

        position = 0

        # Move all non-zero numbers forward
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[position] = nums[i]
                position += 1

        # Fill remaining positions with zeros
        while position < len(nums):
            nums[position] = 0
            position += 1