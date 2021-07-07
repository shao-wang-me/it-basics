# 给出由小写字母组成的字符串S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。
#
# 在 S 上反复执行重复项删除操作，直到无法继续删除。
#
# 在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。
#
# 示例：
#
# 输入："abbaca"
# 输出："ca"
# 解释：
# 例如，在 "abbaca" 中，我们可以删除 "bb" 由于两字母相邻且相同，这是此时唯一可以执行删除操作的重复项。之后我们得到字符串 "aaca"，其中又只有 "aa" 可以执行重复项删除操作，所以最后的字符串为 "ca"。
#
#
# 提示：
#
# 1 <= S.length <= 20000
# S 仅由小写英文字母组成。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def removeDuplicates(self, S: str) -> str:
        # 直接按原题做法的话，要scan很多次，不划算
        # 一次搞定最好
        # 能删除的部分一定是abcddcba这种形式的
        # 两个指针？
        # 两个指针差一个移动，直到两个指针的字母是一样的，把它们变成字符"0"或者其他不对的字符，然后向外扩展，若还是一样的，也变成"0"，直到不一样
        # 不一样了之后，其实两个指针还是相当于只差一个，继续向右移动，直到右指针到底
        # 另外一种就是类似用栈了
        ans = ''
        for c in S:
            ans = ans[:-1] if ans and ans[-1] == c else ans + c
        return ans


def test(S):
    for (s, ans) in S:
        solution = Solution()
        print('Answer for "' + s + '" is: "' + solution.removeDuplicates(s) + '". Expecting: "' + ans + '".')


test([('abbaca', 'ca'), ('a', 'a'), ('aa', ''), ('abcddcbaxjiswssw', 'xjis')])
