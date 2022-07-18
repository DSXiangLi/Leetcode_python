# 有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。 
# 
#  
#  例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 
# 和 "192.168@1.1" 是 无效 IP 地址。 
#  
# 
#  给定一个只包含数字的字符串 s ，用以表示一个 IP 地址，返回所有可能的有效 IP 地址，这些地址可以通过在 s 中插入 '.' 来形成。你 不能 重新
# 排序或删除 s 中的任何数字。你可以按 任何 顺序返回答案。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "25525511135"
# 输出：["255.255.11.135","255.255.111.35"]
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "0000"
# 输出：["0.0.0.0"]
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "101023"
# 输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 20 
#  s 仅由数字组成 
#  
#  Related Topics 字符串 回溯 👍 958 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []

        def backtrace(s, tmp):
            nonlocal result
            if not s and len(tmp)==4:
                result.append('.'.join(tmp))
                return
            elif not s:
                return
            elif len(tmp)==4:
                return

            for i in range(min(len(s), 3)):
                if i==0 and s[i] == '0':
                    backtrace(s[(i+1):], tmp+['0'])
                    break
                elif i==2 and int(s[:(i+1)])>255:
                    break
                else:
                    backtrace(s[(i+1):], tmp+[s[:(i+1)]])

        backtrace(s, [])
        return result



# leetcode submit region end(Prohibit modification and deletion)
