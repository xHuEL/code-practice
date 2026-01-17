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

[存在重复元素 II](https://leetcode.cn/problems/contains-duplicate-ii/) —— [提交记录](./code/练手题/contains-duplicate-ii.py)

[拆炸弹](https://leetcode.cn/problems/defuse-the-bomb/) —— [提交记录](./code/练手题/defuse-the-bomb.py) [提交记录2](./code/练手题/defuse-the-bomb_v2.py)

[验证回文串](https://leetcode.cn/problems/valid-palindrome/) —— [提交记录](./code/valid-palindrome.py)

[有效的字母异位词](https://leetcode.cn/problems/valid-anagram/) —— [提交记录](./code/valid-anagram.py)

[反转字符串中的元音字母](https://leetcode.cn/problems/reverse-vowels-of-a-string/) —— [提交记录](./code/reverse-vowels-of-a-string.py)

[数字转换为十六进制数](https://leetcode.cn/problems/convert-a-number-to-hexadecimal/) —— [提交记录](./code/convert-a-number-to-hexadecimal.py)

[两个数组的交集](https://leetcode.cn/problems/intersection-of-two-arrays/) —— [提交记录](./code/intersection-of-two-arrays.py)

***

2026.01.17更新



## 滑动窗口

###### 一、题型1：定长滑动窗口

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

###### 一、题型1: 回溯

[子集](https://leetcode.cn/problems/subsets/) —— [提交记录]()

[电话号码的字母组合](https://leetcode.cn/problems/letter-combinations-of-a-phone-number/)

[全排列](https://leetcode.cn/problems/permutations/)

[组合总和](https://leetcode.cn/problems/combination-sum/)

[单词搜索](https://leetcode.cn/problems/word-search/)

[分割回文串](https://leetcode.cn/problems/palindrome-partitioning/)

[岛屿数量](https://leetcode.cn/problems/number-of-islands/)

[括号生成](https://leetcode.cn/problems/generate-parentheses/)



***



###### 二、题型2: 二叉树

```tex
二叉树遍历总结
一、核心遍历方式
根据访问根节点的时机不同，可以分为以下几类：


1. 深度优先遍历
(1) 先序遍历

- 顺序：根 → 左 → 右
- 特点：优先访问根节点，然后深入左子树，最后右子树
- 常见应用：复制树、生成前缀表达式、序列化二叉树

(2) 中序遍历

- 顺序：左 → 根 → 右
- 特点：对于二叉搜索树，中序遍历的结果是一个升序序列
- 常见应用：获取二叉搜索树的有序序列、生成中缀表达式

(3) 后序遍历

- 顺序：左 → 右 → 根
- 特点：优先处理子节点，最后处理根
- 常见应用：删除树、计算表达式树的值、求解二叉树高度

2. 广度优先遍历
   (1) 层次遍历

- 顺序：按层从上到下、从左到右依次访问
- 特点：使用队列实现
- 常见应用：查找最短路径、按层打印树结构、求树宽度
```

```python
# 代码很重要,需要记住
# Python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 先序遍历
def preorder_traversal(root):
    result = []
    
    def dfs(node):
        if not node:
            return
        result.append(node.val)  # 访问根节点
        dfs(node.left)           # 遍历左子树
        dfs(node.right)          # 遍历右子树
    
    dfs(root)
    return result

# 中序遍历
def inorder_traversal(root):
    result = []
    
    def dfs(node):
        if not node:
            return
        dfs(node.left)           # 遍历左子树
        result.append(node.val)  # 访问根节点
        dfs(node.right)          # 遍历右子树
    
    dfs(root)
    return result

# 后序遍历
def postorder_traversal(root):
    result = []
    
    def dfs(node):
        if not node:
            return
        dfs(node.left)           # 遍历左子树
        dfs(node.right)          # 遍历右子树
        result.append(node.val)  # 访问根节点
    
    dfs(root)
    return result
```

```tex
图遍历举例：
   A
   / \
  B   C
 / \   \
D   E   F

- **先序遍历**：A → B → D → E → C → F
- **中序遍历**：D → B → E → A → C → F
- **后序遍历**：D → E → B → F → C → A
- **层次遍历**：A → B → C → D → E → F

一、先序遍历：
步骤1: 访问根节点 A
       ↓
       ①A
       / \
      B   C
     / \   \
    D   E   F

步骤2: 进入左子树，访问 B
       ①A
       / \
     ②B   C
     / \   \
    D   E   F

步骤3: 进入左子树，访问 D
       ①A
       / \
     ②B   C
     / \   \
   ③D  E   F

步骤4: 返回上一层，进入右子树，访问 E
       ①A
       / \
     ②B   C
     / \   \
   ③D ④E   F

步骤5: 返回根节点，进入右子树，访问 C
       ①A
       / \
     ②B  ⑤C
     / \   \
   ③D ④E   F

步骤6: 进入右子树，访问 F
       ①A
       / \
     ②B  ⑤C
     / \   \
   ③D ④E  ⑥F
   
二、中序遍历：
步骤1: 从根节点A开始，先到最左边的D
       ↓ 先到A的左子树
        A
       / \
      B   C
     / \   \
    D   E   F
       ↓ 再到B的左子树
        A
       / \
      B   C
     / \   \
    D   E   F
       ↓ D是叶子节点，访问D
        A
       / \
      B   C
     / \   \
   ①D  E   F

步骤2: 返回到B，访问B
        A
       / \
     ②B   C
     / \   \
   ①D  E   F

步骤3: 进入B的右子树，访问E
        A
       / \
     ②B   C
     / \   \
   ①D ③E   F

步骤4: 返回到A，访问A
       ④A
       / \
     ②B   C
     / \   \
   ①D ③E   F

步骤5: 进入A的右子树C，C没有左子树，直接访问C
       ④A
       / \
     ②B  ⑤C
     / \   \
   ①D ③E   F

步骤6: 进入C的右子树，访问F
       ④A
       / \
     ②B  ⑤C
     / \   \
   ①D ③E  ⑥F
   
三、后序遍历：
步骤1: 从根节点A开始，先到最左边的D
       ↓ 先到A的左子树
        A
       / \
      B   C
     / \   \
    D   E   F
       ↓ 再到B的左子树
        A
       / \
      B   C
     / \   \
    D   E   F
       ↓ D是叶子节点，访问D
        A
       / \
      B   C
     / \   \
   ①D  E   F

步骤2: 访问B的右子树E
        A
       / \
      B   C
     / \   \
   ①D ②E   F

步骤3: 访问B（左右子树都已访问）
        A
       / \
     ③B   C
     / \   \
   ①D ②E   F

步骤4: 访问C的右子树F
        A
       / \
     ③B   C
     / \   \
   ①D ②E  ④F

步骤5: 访问C（左右子树都已访问）
        A
       / \
     ③B  ⑤C
     / \   \
   ①D ②E  ④F

步骤6: 最后访问根节点A
       ⑥A
       / \
     ③B  ⑤C
     / \   \
   ①D ②E  ④F
```

***

【基础篇】

[二叉树的最大深度](https://leetcode.cn/problems/maximum-depth-of-binary-tree/)  —— [提交记录](./code/maximum-depth-of-binary-tree.py)  后序遍历

[翻转二叉树](https://leetcode.cn/problems/invert-binary-tree/) —— [提交记录](./code/invert-binary-tree.py) 后序遍历

[对称二叉树](https://leetcode.cn/problems/symmetric-tree/)

[路径总和](https://leetcode.cn/problems/path-sum/)

[二叉树的直径](https://leetcode.cn/problems/diameter-of-binary-tree/)

[二叉树展开为链表](https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/)

[从前序与中序遍历序列构造二叉树](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

[从中序与后序遍历序列构造二叉树](https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)

[二叉树剪枝](https://leetcode.cn/problems/binary-tree-pruning/)

***

【提升篇】

***



###### 三、题型3: 分治与递归

###### 四、题型4:  其他递归应用

###### 五、详细总结

[跳转地址](./notes/递归.md)



## 排序

[跳转地址](./notes/排序.md)

## 字符串

[跳转地址](notes/字符串.md)







## 刷题记录

![提交记录](./notes/pic/提交记录.png)
