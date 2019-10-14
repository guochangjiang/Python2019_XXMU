# 4.2ChrCount.py

'''
4.2 统计不同字符个数
用户从键盘输入一行字符，编写一个程序，
统计并输出英文字符、数字、空格和其他字符的个数。
'''

chr_seq = input("请输入一行字符：")

# 方法1：ord()函数
chr_en_num = 0
chr_digit_num = 0
chr_space_num = 0
chr_other_num = 0
for c in chr_seq:
    if ord("A") <= ord(c) <= ord("Z") or ord("a") <= ord(c) <= ord("z"):
        chr_en_num += 1
    elif ord("0") <= ord(c) <= ord("9"):
        chr_digit_num += 1
    elif ord(c) == ord(" ") or ord(c) == ord("\t"):
        chr_space_num += 1
    else:
        chr_other_num += 1
print("方法1：")
print("英文字符数为{}\n数字数为{}\n空格数为{}\n其他字符个数为{}".\
    format(chr_en_num, chr_digit_num, chr_space_num, chr_other_num))

# 方法2
chr_en_num = 0
chr_digit_num = 0
chr_space_num = 0
chr_other_num = 0
for c in chr_seq:
    if "A" <= c <= "Z" or "a" <= c <= "z":
        chr_en_num += 1
    elif "0" <= c <= "9":
        chr_digit_num += 1
    elif c == " " or c == "\t":
        chr_space_num += 1
    else:
        chr_other_num += 1
print("\n方法2：")
print("英文字符数为{}\n数字数为{}\n空格数为{}\n其他字符个数为{}".\
    format(chr_en_num, chr_digit_num, chr_space_num, chr_other_num))