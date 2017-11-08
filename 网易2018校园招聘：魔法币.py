'''
[编程题] 魔法币
时间限制：1秒
空间限制：32768K
小易准备去魔法王国采购魔法神器,购买魔法神器需要使用魔法币,但是小易现在一枚魔法币都没有,
但是小易有两台魔法机器可以通过投入x(x可以为0)个魔法币产生更多的魔法币。
魔法机器1:如果投入x个魔法币,魔法机器会将其变为2x+1个魔法币
魔法机器2:如果投入x个魔法币,魔法机器会将其变为2x+2个魔法币
小易采购魔法神器总共需要n个魔法币,所以小易只能通过两台魔法机器产生恰好n个魔法币,
小易需要你帮他设计一个投入方案使他最后恰好拥有n个魔法币。 
输入描述:
输入包括一行,包括一个正整数n(1 ≤ n ≤ 10^9),表示小易需要的魔法币数量。


输出描述:
输出一个字符串,每个字符表示该次小易选取投入的魔法机器。其中只包含字符'1'和'2'。

输入例子1:
10

输出例子1:
122
'''

'''
解题思路：使用目标值逆推方案
  对目标值进行判断，如果目标值为单数，则用魔法机器1进行逆推，如果为双数，则用魔法机器2逆推，每次逆推获取新的目标值，
  对新目标值重复以上操作，直至目标值为0
'''

'''
代码运行结果：
答案正确:恭喜！您提交的程序通过了所有的测试用例
'''

n = int(input())
result = ''
while n:
    if n % 2:
        n = (n - 1) // 2
        result = '1' + result
    else:
        n = (n - 2) // 2
        result = '2' + result
print(result)
