from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        m1 = len(nums1)
        m2 = len(nums2)

        l1 = 0
        l2 = 0
        ans = []
        cnt = 0  # 计数
        while l1 < m1 and l2 < m2:
            if nums1[l1] == nums2[l2]:
                if cnt == 0:
                    ans.append(nums1[l1])
                    cnt = + 1
                else:
                    if ans[cnt - 1] != nums1[l1]:
                        ans.append(nums1[l1])
                        cnt = cnt + 1
                l1 += 1
                l2 += 1
            elif nums1[l1] < nums2[l2]:
                l1 += 1
            else:
                l2 += 1
        return ans
