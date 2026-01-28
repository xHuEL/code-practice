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

[反转字符串中的元音字母](https://leetcode.cn/problems/reverse-vowels-of-a-string/) —— [提交记录](./code/练手题/reverse-vowels-of-a-string.py)

[数字转换为十六进制数](https://leetcode.cn/problems/convert-a-number-to-hexadecimal/) —— [提交记录](./code/练手题/convert-a-number-to-hexadecimal.py)

[两个数组的交集](https://leetcode.cn/problems/intersection-of-two-arrays/) —— [提交记录](./code/练手题/intersection-of-two-arrays.py)

***

## 链表

[删除排序链表中的重复元素](https://leetcode.cn/problems/remove-duplicates-from-sorted-list/) 

[移除链表元素](https://leetcode.cn/problems/remove-linked-list-elements/)

[环形链表](https://leetcode.cn/problems/linked-list-cycle/)

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

[重新排列日志文件](https://leetcode.com/problems/reorder-data-in-log-files/) —— 自定义排序

[最后一块石头的重量](https://leetcode.com/problems/last-stone-weight/) —— 堆排序

[ 数组的相对排序](https://leetcode.com/problems/relative-sort-array/) —— 桶排序

## 字符串

[344. 反转字符串](https://leetcode.cn/problems/reverse-string/)

[125. 验证回文串](https://leetcode.cn/problems/valid-palindrome/)

[ 14. 最长公共前缀](https://leetcode.cn/problems/longest-common-prefix/)

[ 8. 字符串转换整数 (atoi)](https://leetcode.cn/problems/string-to-integer-atoi/)



## 总结

只是为了公司考试，只要做练手题和排序题、堆栈以及字符串，其他的没必要。主要考察的还是基本代码编写能力。以我的经验，第二题一般都是题目很长的模拟题，也不会涉及算法，最多只涉及到排序。第一题要么是栈，要么滑动窗口，要么字符串处理，也不会特别难。

如果为了接下来考虑，听说刷https://leetcode.cn/studyplan/top-100-liked/ 就可以了。

可能只是刷上面题，不一定保证能过，可以看看后面README_V2.md,  notes/的题，其实选做就可以了，不需要全部做。

好像一开始我确实不会转弯，都快列出所有类型的题目了，回头我问一下其他的人，对算法的要求到底是什么， 后面再更新吧。也希望这些对你有帮助。
