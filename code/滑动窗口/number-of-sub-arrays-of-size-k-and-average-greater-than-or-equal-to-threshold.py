from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        sum = 0.0
        ans = 0

        n = len(arr)
        if n < k:
            return 0

        ll = 0
        rr = min(ll + k, n)

        for i in range(ll, rr):
            sum += arr[i]

        if sum / k >= threshold:
            ans += 1

        while rr < n:
            ll += 1
            rr += 1

            sum -= arr[ll - 1]
            sum += arr[rr - 1]

            if sum / k >= threshold:
                ans += 1

        return ans



