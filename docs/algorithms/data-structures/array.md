# Array (数组)

1. What is an array?

   An array is a collection of items indexed by integers.

   We don't care about other restrictions (e.g. fixed length, items of the same type) here unless otherwise specified.

1. What techniques can be used to solve array problems?

   1. Binary search (二分搜索, when the array is sorted)
   1. Two pointers (双指针, when the array is sorted)
   1. It is easier to shift (旋转) from the end to avoid overwrites (覆盖)
   1. Dynamic programming (动态规划, when sub-problem spaces overlap)
   
1. What is the complexity of the basic operations on an array?

   | Operation | Time complexity | Space complexity | Notes |
   | --- | --- | --- | --- |
   | Insertion | O(n - k) | O(1) | k is the index of the inserted array. The main cost is shifting element to the right. |
   | Deletion | O(n - k) | O(1) | Same as above. |

## Problems

- LeetCode: LC

| # | Title | Difficulty | Tags | Notes |
| --- | --- | --- | --- | --- |
| LC-977 | Squares of a Sorted Array | Easy | Two pointers | The array is sorted. |
| LC-1089 | Duplicate Zeros | Easy | In-place, shift | Hard to get right at once, needs more practice. |
| LC-88 | Merge Sorted Array | Easy | Shift | Seems easy but acceptance is quite low at 40%, needs more practice. |
