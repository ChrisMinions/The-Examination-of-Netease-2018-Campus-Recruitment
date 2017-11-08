'''
[编程题] 重排数列
时间限制：1秒
空间限制：100768K
小易有一个长度为N的正整数数列A = {A[1], A[2], A[3]..., A[N]}。
牛博士给小易出了一个难题:
对数列A进行重新排列,使数列A满足所有的A[i] * A[i + 1](1 ≤ i ≤ N - 1)都是4的倍数。
小易现在需要判断一个数列是否可以重排之后满足牛博士的要求。 
输入描述:
输入的第一行为数列的个数t(1 ≤ t ≤ 10),
接下来每两行描述一个数列A,第一行为数列长度n(1 ≤ n ≤ 10^5)
第二行为n个正整数A[i](1 ≤ A[i] ≤ 10^9)


输出描述:
对于每个数列输出一行表示是否可以满足牛博士要求,如果可以输出Yes,否则输出No。

输入例子1:
2
3
1 10 100
4
1 2 3 4

输出例子1:
Yes
No
'''

'''
解题思路：分析问题
  把问题转为求数列中的数是2的倍数的个数（非四的倍数），4的倍数的个数和其他数的个数
  因为一个4的倍数可以和一个非2非4倍数的组组成目标数列
  两个2的倍数可以组成目标序列
  单个2的倍数必须和4的倍数组成目标数列
  所以我们先把2的倍数都放在一起，这样只需要再其后放置一个4的倍数就可以组成目标数列
  所以：如果没有2的倍数，4的倍数的数目只要大于等于总数的一半就可以组成目标数列
        如果有2的倍数，4的倍数的数目只要大于等于其他数目的个数就可以组成目标数列
'''

'''
代码运行结果：
答案正确:恭喜！您提交的程序通过了所有的测试用例
'''

t = int(input())

ns = []
arrays = []
for each in range(t):
    ns.append(int(input()))
    arrays.append([i for i in map(int, input().split())])

count = 0
results = []
while count < t:
    n = ns[count]
    array = arrays[count]
    fours = 0
    twos = 0
    others = 0
    for each in array:
        if each % 4 == 0:
            fours += 1
        elif each % 2 == 0:
            twos += 1
        else:
            others += 1

    if twos == 0:
        if fours >= n // 2:
            results.append('Yes')
        else:
            results.append('No')
    else:
        if fours >= others:
            results.append('Yes')
        else:
            results.append('No')

    count += 1

for each in results:
    print(each)
