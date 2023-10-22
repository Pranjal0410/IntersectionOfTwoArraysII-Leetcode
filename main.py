from collections import Counter

class Solution:
    @staticmethod
    def intersect(nums1, nums2):
        count1, count2 = Counter(nums1), Counter(nums2)
        result = []

        for num, freq in count1.items():
            if num in count2:
                result.extend([num] * min(freq, count2[num]))

        return result   
