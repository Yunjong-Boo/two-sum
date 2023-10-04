from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    for idx, element in enumerate(nums):
        other = target - element
        if other in nums and idx != nums.index(other):
            output_list = [idx, nums.index(other)]
            break

    return sorted(output_list)


if __name__ == "__main__":
    input_list = [int(e) for e in input().split()]
    target = int(input())

    output_list = twoSum(nums=input_list, target=target)
    print(output_list)
    