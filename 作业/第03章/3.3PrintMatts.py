# 3.3PrintMatts.py

matts_width = 11         # 奇数
a = "＋"
b = "－"
c = "｜"
d = "　"
e = matts_width // 2

# 方法 1
print("方法1：")
print("＋－－－－＋－－－－＋")
print("｜　　　　｜　　　　｜")
print("｜　　　　｜　　　　｜")
print("｜　　　　｜　　　　｜")
print("｜　　　　｜　　　　｜")
print("＋－－－－＋－－－－＋")
print("｜　　　　｜　　　　｜")
print("｜　　　　｜　　　　｜")
print("｜　　　　｜　　　　｜")
print("｜　　　　｜　　　　｜")
print("＋－－－－＋－－－－＋")

# 方法 2
print("\n\n方法2：")
for i in range(matts_width):
    if i in [0, e, matts_width-1]:
        print("{}{}{}{}{}".format(a, b*(e-1), a, b*(e-1), a))
    else:
        print("{}{}{}{}{}".format(c, d*(e-1), c, d*(e-1), c))
