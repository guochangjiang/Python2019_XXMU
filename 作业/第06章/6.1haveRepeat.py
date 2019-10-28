# 6.1haveRepeat.py

'''
重复元素判定
编写一个函数haveRepeat()，接受列表作为参数，如果一个元素
在列表中出现了不止一次，则返回True，但不改变原列表值。
'''

def haveRepeat(ls):
    if len(ls) > len(set(ls)):
        return True
    else:
        return False

if __name__ == '__main__':
    ls_1 = [1, 2, 3, 4, 5]
    ls_2 = ['1', '2', '3', '1']
    if haveRepeat(ls_1):
        print(ls_1, "存在重复元素")
    else:
        print(ls_1, "不存在重复元素")
    if haveRepeat(ls_2):
        print(ls_2, "存在重复元素")
    else:
        print(ls_2, "不存在重复元素")