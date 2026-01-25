## 基础
最基础的知识: 如何计算复杂度(时间复杂度，空间复杂度），这个关系到写代码的时候，如何在取选择最优的算法或者判断你选择的算法是否满足题目的要求。<br>
举几个直观例子<br>

1.   <b> 对于单次循环而言</b>

```
for (int i = 0; i < n; i++) 
```
这个时间复杂度为O(n), 如果其中n为100,0000，那么cpu执行的时间差不多就是1s

2. <b>对于多次循环而言</b>

```
for (int i = 0; i < n; i++) {
    for (int j = i; j < n; j++) {
    }
}

```
这个时间复杂度为O(n^2), 如果为100,000那么整个时间就会变成100,000 * 100,000，远远超过1s，这个时间肯定是不满足题目要求的，如果n < 2000，那么就可以采用O(n ^ 2)的算法

3. <b> 对于递归而言</b>

   简单来说，时间复杂度为o(2^n), 所以这种题目一般要求n都比较小

有时候可以通过时间复杂度来判断应该选择什么算法，比如[分割回文串](https://leetcode.cn/problems/palindrome-partitioning/description/?envType=problem-list-v2&envId=string),其中n为16，这个时候可以大概判断是使用dfs来进行递归遍历，后续再补
![Alt text](./pic/image.png)



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

2026.01.18更新

[2. 两数相加](https://leetcode.cn/problems/add-two-numbers/) —— [提交记录](./code/练手题/add-two-numbers.py)

```python
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        tail = None
        catch = 0  # 是否进位
        while l1 is not None or l2 is not None:
            newNode = ListNode(catch)
            if l1 is not None:
                newNode.val += l1.val
                l1 = l1.next

            if l2 is not None:
                newNode.val += l2.val
                l2 = l2.next

            catch = int(newNode.val / 10) # 首先计算出进位符
            newNode.val = int(newNode.val % 10) # 然后计算出去掉进位，最后的结果

            if head is None:
                head = newNode # 如果链表的起始位置未保存，记得保存一下
                tail = newNode # 相当于链表就一个节点
            else:
                tail.next = newNode # 在尾结点之后添加一个节点
                tail = newNode # 将添加的节点设置为尾节点

        if catch > 0:
            newNode = ListNode(catch)
            tail.next = newNode

        return head
# 这道题其实是大数加法的变形,有时候大数加法是两个str相加，这道题目就涉及到链表的操作。
# 其实还是挺难的，关键还是了解链表操作，链表关键的head和tail，还有边界条件。

```

![image-20260120235847441](./pic/双数加法.png)

[26. 删除有序数组中的重复项](https://leetcode.cn/problems/remove-duplicates-from-sorted-array/)

```python
def removeDuplicates(self, nums: List[int]) -> int:
    n = len(nums)
    ll = 0
    for i in range(1, n):
        if nums[i] == nums[i - 1]:
           continue
        else:
           nums[ll + 1] = nums[i]
           ll += 1
    return ll
# 从第一位开始，比较它跟前一位是不是相同，如果不相同那么将它移动到位置L，同时位置L记得要加1
# 这是一道模拟题，其实也可以开一个新的列表，这样更好理解
```



[20. 有效的括号](https://leetcode.cn/problems/valid-parentheses/) —— [提交记录](./code/练手题/valid-parentheses.py)

```python
## 堆栈的基本用法
    def isValid(self, s: str) -> bool:
        n = len(s)
        stk = ['0' for i in range(n)]

        top = 0
        for i in range(n):
            if s[i] == '[' or s[i] == '(' or s[i] == '{':   # 
                stk[top] = s[i]
                top += 1
            else:
                ss = stk[top - 1]
                flag = False
                if s[i] == ']' and ss == '[':
                    flag = True
                elif s[i] == '}' and ss == '{':
                    flag = True
                elif s[i] == ')' and ss == '(':
                    flag = True

                if not flag:
                    return False
                top = top - 1
        if top == 0:
            return True
        return False

```



[70. 爬楼梯](https://leetcode.cn/problems/climbing-stairs/)

```python
# 首先可以想到使用递归来实现，很容易想到递归实现：
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        if n == 2:
            return 1
    
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

# 观察上面的公式，其实是一个斐波那契数列，可以使用递推方式来实现
    def climbStairs(self, n: int) -> int:
        f = [0 for _ in range(n)]
        f[1] = 1
        f[2] = 1

        for i in range(3, n + 1):
            f[i] = f[i - 1] + f[i - 2]

        return f[n]
```

[三数之和](https://leetcode.cn/problems/3sum/)

[验证二叉搜索树](https://leetcode.cn/problems/validate-binary-search-tree/)

***

## 链表

[反转链表](https://leetcode.cn/problems/reverse-linked-list/) —— [提交记录](./code/链表/reverse-linked-list.py)

```python
# 反转逻辑，使用堆栈来实现
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 堆栈
        stack = []
        while head is not None:
            stack.append(head)
            head = head.next

        def addNode(node):
            nonlocal head, tail
            if head is None:
                head = node
                tail = node
            else:
                tail.next = node
                tail = node

        head = None
        tail = None
        while len(stack) > 0:
            cur = stack[-1]
            cur.next = None
            stack.pop()

            addNode(cur)

        return head
```



[合并两个有序链表](https://leetcode.cn/problems/merge-two-sorted-lists/) —— [提交记录](./code/链表/merge-two-sorted-lists.py)

```python
# 排序链表合并操作，归并排序中间的一个简单流程
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def addNode(node: ListNode):
            nonlocal head, tail
            if head is None:
                head = node
                tail = node
            else:
                tail.next = node
                tail = node

        head : Optional[ListNode] = None
        tail : Optional[ListNode] = None
        while list1 is not None or list2 is not None:
            if list1 is None:
                addNode(list2)
                list2 = list2.next
            elif list2 is None:
                addNode(list1)
                list1 = list1.next
            else:
                if list1.val > list2.val:
                    addNode(list2)
                    list2 = list2.next
                else:
                    addNode(list1)
                    list1 = list1.next
        return head
```



[删除排序链表中的重复元素](https://leetcode.cn/problems/remove-duplicates-from-sorted-list/) —— 

[移除链表元素](https://leetcode.cn/problems/remove-linked-list-elements/)

[环形链表](https://leetcode.cn/problems/linked-list-cycle/)

[ 环形链表 II](https://leetcode.cn/problems/linked-list-cycle-ii/)

[相交链表](https://leetcode.cn/problems/intersection-of-two-linked-lists/)

[删除链表的倒数第N个节点](https://leetcode.cn/problems/remove-nth-node-from-end-of-list/)

[链表的中间结点](https://leetcode.cn/problems/middle-of-the-linked-list/)

[两两交换链表中的节点](https://leetcode.cn/problems/swap-nodes-in-pairs/)

[奇偶链表](https://leetcode.cn/problems/odd-even-linked-list/)

[分隔链表](https://leetcode.cn/problems/partition-list/)

[ 旋转链表](https://leetcode.cn/problems/rotate-list/)

[复制带随机指针的链表](https://leetcode.cn/problems/copy-list-with-random-pointer/)

[反转链表 II](https://leetcode.cn/problems/reverse-linked-list-ii/)

[重排链表](https://leetcode.cn/problems/reorder-list/)

[排序链表](https://leetcode.cn/problems/sort-list/)

[回文链表](https://leetcode.cn/problems/palindrome-linked-list/)

[K个一组翻转链表](https://leetcode.cn/problems/reverse-nodes-in-k-group/)

[合并K个升序链表](https://leetcode.cn/problems/merge-k-sorted-lists/)



## 滑动窗口

###### 一、题型1：定长滑动窗口

必看：[前置知识](./notes/滑动窗口.md)

***

【基础版】

[定长子串中元音的最大数目](https://leetcode.cn/problems/maximum-number-of-vowels-in-a-substring-of-given-length/) 

[子数组最大平均数 I](https://leetcode.cn/problems/maximum-average-subarray-i/)

[大小为 K 且平均值大于等于阈值的子数组数目](https://leetcode.cn/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/)

[半径为 k 的子数组平均值](https://leetcode.cn/problems/k-radius-subarray-averages/)

[得到 K 个黑块的最少涂色次数](https://leetcode.cn/problems/minimum-recolors-to-get-k-consecutive-black-blocks/)

[几乎唯一子数组的最大和](https://leetcode.cn/problems/maximum-sum-of-almost-unique-subarray/)

[长度为 K 子数组中的最大和](https://leetcode.cn/problems/maximum-sum-of-distinct-subarrays-with-length-k/) 

[可获得的最大点数](https://leetcode.cn/problems/maximum-points-you-can-obtain-from-cards/) 

***

【进阶版 - 不急着做】

[使库存平衡的最少丢弃次数](https://leetcode.cn/problems/minimum-discards-to-balance-inventory/)

[爱生气的书店老板](https://leetcode.cn/problems/grumpy-bookstore-owner/)

[重新安排会议得到最多空余时间 I](https://leetcode.cn/problems/reschedule-meetings-for-maximum-free-time-i/) 

###### 二、题型2：不定长滑动窗口

不定长滑动窗口主要分为三类：求最长子数组，求最短子数组，求子数组个数。

***

【基础版】

[无重复字符的最长子串](https://leetcode.cn/problems/longest-substring-without-repeating-characters/)

[每个字符最多出现两次的最长子字符串](https://leetcode.cn/problems/maximum-length-substring-with-two-occurrences/) 

[删掉一个元素以后全为 1 的最长子数组](https://leetcode.cn/problems/longest-subarray-of-1s-after-deleting-one-element/) 

[使数组平衡的最少移除数目](https://leetcode.cn/problems/minimum-removals-to-balance-array/) 

[尽可能使字符串相等](https://leetcode.cn/problems/get-equal-substrings-within-budget/) 

[水果成篮](https://leetcode.cn/problems/fruit-into-baskets/) 

[删除子数组的最大得分](https://leetcode.cn/problems/maximum-erasure-value/) 

[最多 K 个重复元素的最长子数组](https://leetcode.cn/problems/length-of-longest-subarray-with-at-most-k-frequency/) 

[考试的最大困扰度](https://leetcode.cn/problems/maximize-the-confusion-of-an-exam/) 

[最大连续 1 的个数 III](https://leetcode.cn/problems/max-consecutive-ones-iii/) 

[将 x 减到 0 的最小操作数](https://leetcode.cn/problems/minimum-operations-to-reduce-x-to-zero/) 

[最长半重复子数组](https://leetcode.cn/problems/longest-semi-repeating-subarray/)

***

【进阶版 —— 不急着做】

###### 三、题型3：分组循环

###### 四、题型4：单序列双指针



## 递归

必看： [前置知识](./notes/递归.md)

***

###### 一、题型1: 回溯

[子集](https://leetcode.cn/problems/subsets/) —— [提交记录](./code/递归/subsets.py)

[电话号码的字母组合](https://leetcode.cn/problems/letter-combinations-of-a-phone-number/) —— [提交记录](./code/递归/letter-combinations-of-a-phone-number.py)

[全排列](https://leetcode.cn/problems/permutations/)

[组合总和](https://leetcode.cn/problems/combination-sum/)

[单词搜索](https://leetcode.cn/problems/word-search/)

[组合](https://leetcode.cn/problems/combinations/)

[分割回文串](https://leetcode.cn/problems/palindrome-partitioning/)

[岛屿数量](https://leetcode.cn/problems/number-of-islands/)

[括号生成](https://leetcode.cn/problems/generate-parentheses/)

[全排列 II](https://leetcode.cn/problems/permutations-ii/)

[组合总和 II](https://leetcode.cn/problems/combination-sum-ii/)

***



###### 二、题型2: 二叉树

必看： [前置知识](./notes/递归.md)

***

【基础篇】

[二叉树的中序遍历](https://leetcode.cn/problems/binary-tree-inorder-traversal/)

[二叉树的前序遍历](https://leetcode.cn/problems/binary-tree-preorder-traversal/)

[二叉树的后序遍历](https://leetcode.cn/problems/binary-tree-postorder-traversal/)

[二叉树的层序遍历](https://leetcode.cn/problems/binary-tree-level-order-traversal/)

[二叉树的锯齿形层序遍历](https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal/)

[二叉树的最大深度](https://leetcode.cn/problems/maximum-depth-of-binary-tree/)  —— [提交记录](./code/递归/maximum-depth-of-binary-tree.py)  后序遍历

[翻转二叉树](https://leetcode.cn/problems/invert-binary-tree/) —— [提交记录](./code/递归/invert-binary-tree.py) 后序遍历

[对称二叉树](https://leetcode.cn/problems/symmetric-tree/) —— [提交记录](./code/递归/symmetric-tree.py)

[路径总和](https://leetcode.cn/problems/path-sum/) —— [提交记录](./code/递归/path-sum.py)

[二叉树的直径](https://leetcode.cn/problems/diameter-of-binary-tree/) —— [提交记录](./code/递归/diameter-of-binary-tree.py)

[二叉树展开为链表](https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/) —— [提交记录](./code/递归/flatten-binary-tree-to-linked-list.py)

[从前序与中序遍历序列构造二叉树](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) —— [提交记录](./code/递归/construct-binary-tree-from-preorder-and-inorder-traversal.py)

[从中序与后序遍历序列构造二叉树](https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/) —— [提交记录](./code/递归/construct-binary-tree-from-inorder-and-postorder-traversal.py)

[二叉树剪枝](https://leetcode.cn/problems/binary-tree-pruning/) —— [提交记录](./code/递归/binary-tree-pruning.py)

***

【提升篇】

***



###### 三、题型3: 分治与递归

###### 四、题型4:  其他递归应用

###### 五、详细总结

[跳转地址](./notes/递归.md)



## 排序

###### 一、题型1：归并排序

[合并两个有序数组](https://leetcode.cn/problems/merge-sorted-array/)

[合并两个有序链表](https://leetcode.cn/problems/merge-two-sorted-lists/)

[ 合并K个升序链表](https://leetcode.cn/problems/merge-k-sorted-lists/)

[ 排序链表](https://leetcode.cn/problems/sort-list/)

[翻转对](https://leetcode.cn/problems/reverse-pairs/)

[ 区间和的个数](https://leetcode.cn/problems/count-of-range-sum/)

###### 二、题型2：自定义排序

[重新排列日志文件](https://leetcode.com/problems/reorder-data-in-log-files/)

[ 根据数字二进制下1的数目排序](https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/)

[ 自定义字符串排序](https://leetcode.com/problems/custom-sort-string/)

[ 根据身高重建队列](https://leetcode.com/problems/queue-reconstruction-by-height/)

[最大数](https://leetcode.com/problems/largest-number/)

[ 合并区间](https://leetcode.com/problems/merge-intervals/)

###### 三、题型3：快速排序

[多数元素](https://leetcode.com/problems/majority-element/)

[ 颜色分类](https://leetcode.com/problems/sort-colors/)

[数组中的第K个最大元素](https://leetcode.com/problems/kth-largest-element-in-an-array/)

[排序数组](https://leetcode.com/problems/sort-an-array/)

[ 最接近原点的K个点](https://leetcode.com/problems/k-closest-points-to-origin/)

[ 摆动排序 II](https://leetcode.com/problems/wiggle-sort-ii/)

###### 四、题型4：堆排序/优先队列

[最后一块石头的重量](https://leetcode.com/problems/last-stone-weight/)

[ 数据流中的第K大元素](https://leetcode.com/problems/kth-largest-element-in-a-stream/)

[ 前K个高频元素](https://leetcode.com/problems/top-k-frequent-elements/)

[有序矩阵中第K小的元素](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/)

[ 数据流的中位数](https://leetcode.com/problems/find-median-from-data-stream/)

[ 滑动窗口最大值](https://leetcode.com/problems/sliding-window-maximum/)

###### 五、题型5：桶排序

[ 数组的相对排序](https://leetcode.com/problems/relative-sort-array/)

[有效的字母异位词](https://leetcode.com/problems/valid-anagram/)

[H指数](https://leetcode.com/problems/h-index/)

[根据字符出现频率排序](https://leetcode.com/problems/sort-characters-by-frequency/)

[最大间距](https://leetcode.com/problems/maximum-gap/)

[ 存在重复元素 III](https://leetcode.com/problems/contains-duplicate-iii/)

###### 六、题型6：拓扑排序

[课程表](https://leetcode.com/problems/course-schedule/)

[ 课程表 II](https://leetcode.com/problems/course-schedule-ii/)

[ 火星词典](https://leetcode.com/problems/alien-dictionary/)

[ 最小高度树](https://leetcode.com/problems/minimum-height-trees/)

[ 矩阵中的最长递增路径](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/)

[序列重建](https://leetcode.com/problems/sequence-reconstruction/)

###### 七、详细解释

[跳转地址](./notes/排序.md)

## 二分查找

[704. 二分查找](https://leetcode.cn/problems/binary-search/)

[搜索插入位置](https://leetcode.cn/problems/search-insert-position/)

[在排序数组中查找元素的第一个和最后一个位置](https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/)

[第一个错误的版本](https://leetcode.cn/problems/first-bad-version/)

###### 题型3: 旋转数组问题

[搜索旋转排序数组](https://leetcode.cn/problems/search-in-rotated-sorted-array/)

[寻找旋转排序数组中的最小值](https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/)

###### 题型4：二维数组搜索

[搜索二维矩阵](https://leetcode.cn/problems/search-a-2d-matrix/)

[ 搜索二维矩阵 II](https://leetcode.cn/problems/search-a-2d-matrix-ii/)

###### 题型5：特殊场景

[寻找峰值](https://leetcode.cn/problems/find-peak-element/)

[寻找两个正序数组的中位数](https://leetcode.cn/problems/median-of-two-sorted-arrays/)

## 搜索

###### 一、题型1: 深度优先搜索

###### 二、题型2：宽度优先搜索

## 数据结构

###### 题型1：栈

[有效的括号](https://leetcode.cn/problems/valid-parentheses/)

[最小栈](https://leetcode.cn/problems/min-stack/)

[用队列实现栈](https://leetcode.cn/problems/implement-stack-using-queues/)

[棒球比赛](https://leetcode.cn/problems/baseball-game/)

[验证栈序列](https://leetcode.cn/problems/validate-stack-sequences/)

[简化路径](https://leetcode.cn/problems/simplify-path/)

[逆波兰表达式求值](https://leetcode.cn/problems/evaluate-reverse-polish-notation/)

[字符串解码](https://leetcode.cn/problems/decode-string/)

[柱状图中最大的矩形](https://leetcode.cn/problems/largest-rectangle-in-histogram/)

[最大矩形](https://leetcode.cn/problems/maximal-rectangle/)

[接雨水](https://leetcode.cn/problems/trapping-rain-water/)

[去除重复字母](https://leetcode.cn/problems/remove-duplicate-letters/)

###### 题型2：队列

###### 题型3：堆

###### 题型4：并查集

###### 题型3: 字典树（暂时不用）

## 图

###### 题型1：最短路

###### 题型2：最小生成树

###### 题型3：拓扑排序

## 字符串

[跳转地址](notes/字符串.md)



## 数学

