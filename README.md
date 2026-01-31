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

[子数组最大平均数 I](https://leetcode.cn/problems/maximum-average-subarray-i/)

[无重复字符的最长子串](https://leetcode.cn/problems/longest-substring-without-repeating-characters/)

[每个字符最多出现两次的最长子字符串](https://leetcode.cn/problems/maximum-length-substring-with-two-occurrences/) 

[删掉一个元素以后全为 1 的最长子数组](https://leetcode.cn/problems/longest-subarray-of-1s-after-deleting-one-element/) 

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

[最后一块石头的重量](https://leetcode.com/problems/last-stone-weight/) —— 堆排序

[ 数组的相对排序](https://leetcode.com/problems/relative-sort-array/) —— 桶排序

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

[ 14. 最长公共前缀](https://leetcode.cn/problems/longest-common-prefix/)

[ 8. 字符串转换整数 (atoi)](https://leetcode.cn/problems/string-to-integer-atoi/)



## 总结

只是为了公司考试，只要做练手题和排序题、堆栈以及字符串，其他的没必要。主要考察的还是基本代码编写能力。以我的经验，第二题一般都是题目很长的模拟题，也不会涉及算法，最多只涉及到排序。第一题要么是栈，要么滑动窗口，要么字符串处理，也不会特别难。

如果为了接下来考虑，听说刷https://leetcode.cn/studyplan/top-100-liked/ 就可以了。

可能只是刷上面题，不一定保证能过，可以看看后面README_V2.md,  notes/的题，其实选做就可以了，不需要全部做。

好像一开始我确实不会转弯，都快列出所有类型的题目了，回头我问一下其他的人，对算法的要求到底是什么， 后面再更新吧。也希望这些对你有帮助。
