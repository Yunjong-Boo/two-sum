from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    for idx, element in enumerate(nums):
        other = target - element
        if other in nums and idx != nums.index(other):
            output_list = [idx, nums.index(other)]
            break

    return sorted(output_list)
    