class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        array_to_return = []
        for i in nums:
            count = 0
            for j in nums:
                if(i!=j):
                    if(i>j):
                        count +=1
            array_to_return.append(count)
        return array_to_return