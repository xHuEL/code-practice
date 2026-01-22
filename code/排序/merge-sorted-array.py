from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        first = m - 1
        second = n - 1

        cnt = m + n - 1

        while first >= 0 or second >= 0:
            if first < 0:
                nums1[cnt] = nums2[second]
                cnt -= 1
                second -= 1

            elif second < 0:
                nums1[cnt] = nums1[first]
                cnt -= 1
                first -= 1
            elif nums1[first] > nums2[second]:
                nums1[cnt] = nums1[first]
                cnt -= 1
                first -= 1
            else:
                nums1[cnt] = nums2[second]
                cnt -= 1
                second -= 1

