
# 多行注释用三个单引号 ''' 或者三个双引号 """ 将注释括起来，但提示'''用来文档注释

"""
leetcode 20题：括号匹配是否合法，类似编辑器校验括号匹配问题。
1).     ()[]{} 匹配
2).     (([]))匹配
3).     ([)] 不匹配
4).     ]][[ 不匹配
思路：用栈来解决

1.如果括号都是相同类型，如小括号，则可以用定义一个计数器解决。遇到匹配的减一，直到为0时，通过校验
2.但如果是有不同类型括号，如小括号中括号大括号。如果定义三个计算器，如果不是连续匹配的话，虽然计数器都能最后减为0，但结果还是不合法，
因为这只能说明括号是两两组成一对，比如 ([{)]}
3.括号有效的意思是：有效的表达式的子表达式也是有效表达式，就是从内部看，相邻的必须能抵消掉
Note： 在表示问题的递归结构时，栈数据结构可以派上用场。我们无法真正地从内到外处理这个问题，因为我们对整体结构一无所知。但是，栈可以帮助我们递归地处理这种情况，即从外部到内部。

"""


def is_valid(s):
    stack = []
    mapping = {")":"(","]":"[","}":"{"}
    for c in s:
        if c not in mapping:
            stack.append(c)
        elif not stack or mapping[c] != stack.pop():
            return False
    return not stack


def is_Valid1(s):
    stack = []
    mapping = {")":"(","]":"[","}":"{"}
    for c in s:
        if c in mapping:
            # Pop the topmost element from the stack, if it is non empty
            # Otherwise assign a dummy(假) value of '#' to the top_element variable
            # python的三目运算，类  a > 1 ? "1" : "2"
            top_element = stack.pop() if stack else "#"
            if mapping[c] != top_element:
                return False
        else:
            stack.append(c)
    return not stack


if __name__ == '__main__':
    s1 = "))("
    s2 = "([{)]}"
    is_Valid1(s1)
    r2 = is_Valid1(s2)

    """
    s1 = "((())"
    r2 = is_Valid1(s1)
    r1 = is_valid(s1)
    print(r1)
    
    m1 = {"k1":"v1","k2":"v2","k3":"v3"}
    # in 是判断key在不在map里面
    print("k1" in m1)
    print("v1" in m1)
    """
