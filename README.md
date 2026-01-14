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

有时候可以通过时间复杂度来判断应该选择什么算法，比如[分割回文串](https://leetcode.cn/problems/palindrome-partitioning/description/?envType=problem-list-v2&envId=string),其中n为16，这个时候可以大概判断是使用dfs来进行递归遍历
![Alt text](./pic/image.png)

## 练手题

[最长和谐子序列](https://leetcode.cn/problems/longest-harmonious-subsequence/) —— [提交记录](./code/练手题/longest-harmonious-subsequence.py) [提交记录2](./code/练手题/longest-harmonious-subsequence_v2.py)

[存在重复元素 II](https://leetcode.cn/problems/contains-duplicate-ii/) —— [提交记录](./code/练手题/contains-duplicate-ii.py)

[拆炸弹](https://leetcode.cn/problems/defuse-the-bomb/) —— [提交记录](./code/练手题/defuse-the-bomb.py) [提交记录2](./code/练手题/defuse-the-bomb_v2.py)

[验证回文串](https://leetcode.cn/problems/valid-palindrome/)

[有效的字母异位词](https://leetcode.cn/problems/valid-anagram/)

[反转字符串中的元音字母](https://leetcode.cn/problems/reverse-vowels-of-a-string/)

[数字转换为十六进制数](https://leetcode.cn/problems/convert-a-number-to-hexadecimal/)

[两个数组的交集](https://leetcode.cn/problems/intersection-of-two-arrays/)

## 滑动窗口

[跳转地址](./notes/滑动窗口.md)

## 排序

[跳转地址](./notes/排序.md)

## 字符串

[跳转地址](notes/字符串.md)



## 刷题记录

![提交记录](./notes/pic/提交记录.png)
