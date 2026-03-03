## 练手题

[最长和谐子序列](https://leetcode.cn/problems/longest-harmonious-subsequence/) —— [提交记录](./code/练手题/longest-harmonious-subsequence.py) [提交记录2](./code/练手题/longest-harmonious-subsequence_v2.py)

> ```python
> # 方法1：
> # 首先使用dict来存储所有数字的个数
> for i in range(n):
>     if maps.__contains__(nums[i]):
>        maps[nums[i]] = maps[nums[i]] + 1
>     else:
>        maps[nums[i]] = 1
> # 再遍历所有的数字，并找到比它大1的数字的个数，
> 
> ```



[存在重复元素 II](https://leetcode.cn/problems/contains-duplicate-ii/) —— [提交记录](./code/练手题/contains-duplicate-ii.py)

```python
   # 维护一个map,map存每个数字所在的位置
   def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        maps = {}

        for i in range(n):
            if maps.__contains__(nums[i]):
                j = maps[nums[i]] # 如何当前数字出现过，那么就判断两个位置是不是小于等于
                if i - j <= k:
                    return True
                else:
                    maps[nums[i]] = i
            else:
                maps[nums[i]] = i

        return False
    
    #方法二：
    # 做了后面的题目，可以想到使用滑动窗口来实现，待补充
```



[拆炸弹](https://leetcode.cn/problems/defuse-the-bomb/) —— [提交记录](./code/练手题/defuse-the-bomb.py) [提交记录2](./code/练手题/defuse-the-bomb_v2.py)

```python
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)

        ans = [0 for _ in range(n)]
        for i in range(n):
            if k > 0:
                sum1 = 0
                for j in range(i + 1, i + 1 + k):
                    sum1 += code[j]
                ans[i] = sum1
            else:
                sum1 = 0
                for j in range(i - 1, i - 1 + k):
                    newj = (j + n) % n
                    sum1 += code[newj]
                ans[i] = sum1
```



[验证回文串](https://leetcode.cn/problems/valid-palindrome/) —— [提交记录](./code/练手题/valid-palindrome.py)

```python
class Solution:
    def isOK(self, c):
        if '0' <= c <= '9':
            return True

        if 'a' <= c <= 'z':
            return True
        return False

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()  ## 规划化
        n = len(s)

        # 双指针
        ll = 0
        rr = n - 1
        while ll < rr: 
            if not self.isOK(s[ll]):  ## 判断是否是0-9，a-z的字符
                ll = ll + 1
                continue

            if not self.isOK(s[rr]): ## 判断是否是0-9，a-z的字符
                rr = rr - 1
                continue

            if s[ll] != s[rr]:
                return False
            
            ll = ll + 1 
            rr = rr - 1

        return True
```

[有效的字母异位词](https://leetcode.cn/problems/valid-anagram/) —— [提交记录](./code/练手题/valid-anagram.py)

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 异位词，使用python的counter, 后面会用到
        counter = Counter()
        for c in s:
            counter[c] += 1

        for c in t:
            if counter[c] == 0:
                return False
            counter[c] -= 1
            if counter[c] == 0:
                del counter[c]
        
        if len(counter) != 0:
            return False
        return True
# 从这一题能学到Counter，没想到counter还可以通过del来实现
```



[反转字符串中的元音字母](https://leetcode.cn/problems/reverse-vowels-of-a-string/) —— [提交记录](./code/练手题/reverse-vowels-of-a-string.py)

```python
class Solution:
    def isYuan(self, c): # 判断是否是元音
        str = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        if c in str:
            return True
        return False

    def reverseVowels(self, s: str) -> str: # 主要是考察双指针
        n = len(s)

        ll = 0
        rr = n - 1
        ans = ['0' for _ in range(n)]

        while ll <= rr:
            if not self.isYuan(s[ll]):
                ans[ll] = s[ll]
                ll += 1
                continue

            if not self.isYuan(s[rr]):
                ans[rr] = s[rr]
                rr -= 1
                continue

            ans[ll], ans[rr] = s[rr], s[ll]            
            ll += 1
            rr -= 1
        return ''.join(ans)

```



[数字转换为十六进制数](https://leetcode.cn/problems/convert-a-number-to-hexadecimal/) —— [提交记录](./code/练手题/convert-a-number-to-hexadecimal.py)

```python
class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        maps = '0123456789abcdef'
        if num < 0:
            num += 2 ** 32 ## 主要是为了处理补码，记住就行了，没什么技巧。 负数的补码要加上2^32

        ans = ''
        while num > 0:
            inx = int(num % 16)
            c = maps[inx]
            ans += c
            num = int(num / 16)
        return ans[::-1]
```



[两个数组的交集](https://leetcode.cn/problems/intersection-of-two-arrays/) —— [提交记录](./code/练手题/intersection-of-two-arrays.py)

```python
## 其中的一种解法，排序然后通过双指针求出交集，主要是训练编码能力。也可以使用dict来求解，更简单
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        
        m1 = len(nums1)
        m2 = len(nums2)
        
        l1 = 0
        l2 = 0
        ans = []
        cnt = 0 # 计数
        while l1 < m1 and l2 < m2:
            if nums1[l1] == nums2[l2]:
                if cnt == 0:
                    ans.append(nums1[l1])
                    cnt =  + 1
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
```



***

## 链表

[删除排序链表中的重复元素](https://leetcode.cn/problems/remove-duplicates-from-sorted-list/)  —— [提交记录](./code/链表/remove-duplicates-from-sorted-list.py)

```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head

        def delNode():
            prev.next = cur.next

        while cur is not None:
            if prev is not None:
                if cur.val == prev.val:
                    delNode()
                else:
                    prev = cur
            else:
                prev = cur
            cur = cur.next
        return head
```

[移除链表元素](https://leetcode.cn/problems/remove-linked-list-elements/) —— [提交记录](./code/链表/remove-linked-list-elements.py)

```python
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        cur = head
        prev = None

        def delNode(node: ListNode):
            nonlocal prev, head
            if prev is not None:
                prev.next = node.next
            else:
                head = node.next

        while cur is not None:
            if cur.val == val:
                delNode(cur)
            else:
                prev = cur
            cur = cur.next
        return head

```



[环形链表](https://leetcode.cn/problems/linked-list-cycle/) —— [提交记录](./code/链表/linked-list-cycle.py)

```python
## 很经典的题目，一定要记住，快慢指针。
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 快慢指针
        if head is None:
            return False

        slow = head
        if slow is None:
            return False

        fast = slow.next
        if fast is None:
            return False
            
        while True:
            if fast == slow:
                return True
        
            slow = slow.next
            fast = fast.next
            if fast is None:
                return False
            
            fast = fast.next
            if fast is None:
                return False
```



[ 环形链表 II](https://leetcode.cn/problems/linked-list-cycle-ii/)

[相交链表](https://leetcode.cn/problems/intersection-of-two-linked-lists/)

## 滑动窗口

[定长子串中元音的最大数目](https://leetcode.cn/problems/maximum-number-of-vowels-in-a-substring-of-given-length/) 

```python
class Solution:
    def isyuan(self, c):
        ss = ['a', 'e', 'i', 'o', 'u']
        for cc in ss:
            if cc == c:
                return True
        return False

    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)

        ll = 0
        rr = min(n, ll + k)
        cnt = 0
        for i in range(ll, rr):
            if self.isyuan(s[i]):
                cnt += 1
        
        ans = cnt
        while rr < n:
            ll += 1
            rr += 1

            cnt -= self.isyuan(s[ll - 1])
            cnt += self.isyuan(s[rr - 1])

            if cnt > ans:
                ans = cnt
        
        return ans
            
```



[子数组最大平均数 I](https://leetcode.cn/problems/maximum-average-subarray-i/)

```python
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum = 0.0

        n = len(nums)
        ll = 0
        rr = min(ll + k, n)
        ans = 0.0

        for i in range(ll, rr):
            sum += nums[i]
            ans = sum

        while rr < n:
            ll += 1
            rr += 1

            sum -= nums[ll - 1]
            sum += nums[rr - 1]

            if ans < sum:
                ans = sum

        return ans / k

```



[无重复字符的最长子串](https://leetcode.cn/problems/longest-substring-without-repeating-characters/)

```python
# 对于单字符串而言，一般思路就是遍历整个字符串，然后使用中间变量来维持状态
# 本题思路：找到每个字符左边最近字符的位置a，然后计算当前位置b和左边最近字符的位置a的差值t
# 最后比较每个字符的差值t，找到最大值

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 每个字符的最后出现的位置，位置为str的索引下标。 比如abc，其中字符a的索引位置为-1， b的索引位置为1， c的索引位置为2
        indices_map = {}
        # 最长非重复子串的长度
        max_len = 0
        # 以当前字符为结尾的最长非重复子串的长度
        cur_len = 0

        for index, c in enumerate(s):
            if not indices_map.__contains__(c):
                cur_len = cur_len + 1
            else:
                cur_len = min(index - indices_map[c], cur_len + 1)

            if cur_len > max_len:
                max_len = cur_len
            indices_map[c] = index

        return max_len

```



[每个字符最多出现两次的最长子字符串](https://leetcode.cn/problems/maximum-length-substring-with-two-occurrences/) 

```python
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)

        # 跟踪窗口中每个字符的出现次数
        maps = defaultdict(int)
        left = 0
        ans = 0

        for right in range(n):
            c = s[right]
            maps[c] += 1

            # 如果当前字符出现超过2次，移动左指针直到它降为2次
            while maps[c] > 2:
                maps[s[left]] -= 1
                left += 1

            # 更新最大长度
            ans = max(ans, right - left + 1)

        return ans
```



[删掉一个元素以后全为 1 的最长子数组](https://leetcode.cn/problems/longest-subarray-of-1s-after-deleting-one-element/) 

```
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        delete_cnt = 0
        first = 0
        second = 0

        ans = 0

        for i in range(n):
            second = i

            if nums[i] == 0:
                delete_cnt += 1

            while delete_cnt > 1:
                if nums[first] == 0:
                    delete_cnt -= 1
                first += 1

            ans = max(ans, second - first)
        return ans


```



# 排序

[合并两个有序数组](https://leetcode.cn/problems/merge-sorted-array/) —— 归并排序

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        first = m - 1 ## 从后往前遍历，主要是为了保证
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
```



[重新排列日志文件](https://leetcode.com/problems/reorder-data-in-log-files/) —— 自定义排序

[最后一块石头的重量](https://leetcode.cn/problems/last-stone-weight/) —— 堆排序

```python
import heapq
from heapq import heappop, heappush
from typing import List


# 最大堆是一个可以自动维护最大值的数据结构
# 将最大堆中的最大值pop出来之后，最大堆会自动将剩余的最大值放在队列的前面
# 注意：最大堆只是维护最大值，最大堆是不知道第二大的数
# 在python中heapy来实现最大堆
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        arr = [-stone for stone in stones]
        heapq.heapify(arr)

        while len(arr) > 1:
            x = heappop(arr)
            y = heappop(arr)

            if x < y:
                heappush(arr, x - y)
            elif x > y:
                heappush(arr, y - x)
        return -arr[0] if arr else 0

```



[ 数组的相对排序](https://leetcode.cn/problems/relative-sort-array/) —— 桶排序

## 字符串

[344. 反转字符串](https://leetcode.cn/problems/reverse-string/)

```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def swap(a, b):
            temp = s[a]
            s[a] = s[b]
            s[b] = temp

        L = 0
        R = len(s) - 1

        while L < R:
            swap(L, R)
            L += 1
            R -= 1
```



[125. 验证回文串](https://leetcode.cn/problems/valid-palindrome/)

```python
class Solution:
    def isOK(self, c):
        if '0' <= c <= '9':
            return True

        if 'a' <= c <= 'z':
            return True
        return False

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        n = len(s)

        # 双指针
        ll = 0
        rr = n - 1
        while ll < rr:
            if not self.isOK(s[ll]):
                ll = ll + 1
                continue

            if not self.isOK(s[rr]):
                rr = rr - 1
                continue

            if s[ll] != s[rr]:
                return False
            
            ll = ll + 1
            rr = rr - 1

        return True
```



[ 14. 最长公共前缀](https://leetcode.cn/problems/longest-common-prefix/)

```python
class Solution:
    def find_longest_prefix(self, str1, str2) -> int:
        str_len1 = len(str1)
        str_len2 = len(str2)

        result = 0
        for i in range(min(str_len1, str_len2)):
            if str1[i] != str2[i]:
                break
            result += 1
        return result


    def longestCommonPrefix(self, strs: List[str]) -> str:
        list_len = len(strs)
        result = sys.maxsize

        if list_len == 0:
            return strs[0]

        for i in range(list_len):
            result = min(self.find_longest_prefix(strs[0], strs[i]), result)

        return strs[0][0:result]

```



[ 8. 字符串转换整数 (atoi)](https://leetcode.cn/problems/string-to-integer-atoi/)

```python
class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)

        ans = 0
        i = 0
        while i < n and s[i] == ' ':
            i += 1
            # print(i)

        sign = True
        if i < n and s[i] == '-':
            sign = False
            i += 1
        elif i < n and s[i] == '+':
            sign = True
            i += 1

        while i < n and '0' <= s[i] <= '9':
            ans = ans * 10 + int(s[i])
            i += 1
        
        if sign:
            if ans > 2**31 - 1:
                return 2**31 - 1
            return ans
        else:
            if ans > 2**31:
                return -2**31
            return -ans
```



## 数据结构



## 总结

只是为了公司考试，只要做练手题和排序题、堆栈以及字符串，其他的没必要。主要考察的还是基本代码编写能力。以我的经验，第二题一般都是题目很长的模拟题，也不会涉及算法，最多只涉及到排序。第一题要么是栈，要么滑动窗口，要么字符串处理，也不会特别难。

如果为了接下来考虑，听说刷https://leetcode.cn/studyplan/top-100-liked/ 就可以了。跳转地址[提交打卡](./leetcode热题打卡版.md)

可能只是刷上面题，不一定保证能过，可以看看后面README_V2.md,  notes/的题，其实选做就可以了，不需要全部做。



歇了好久。。

添加 [大模型知识目录](./大模型知识汇总)

最久的方式。

#### 碎碎念

https://www.zhihu.com/question/41221042/answer/293139603
