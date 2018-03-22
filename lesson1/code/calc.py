
# 计算半径从1-10的圆的面积（半径大于0）

pi = 3.14
r = -3
while r < 10:
  if r > 0:
    area = pi * r * r
    print(area)
  r = r + 1
print('filish!')