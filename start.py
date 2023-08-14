# 词库导入部分
# 读取文件内容，并将每一行存储在列表中

# 导入形容词
with open('形容词.txt', 'r', encoding='utf-8') as f:
    name_1 = [line.strip() for line in f]

# 导入名字
with open('名字.txt', 'r', encoding='utf-8') as f:
    name_2 = [line.strip() for line in f]

# 导入动词
with open('动词.txt', 'r', encoding='utf-8') as f:
    name_3 = [line.strip() for line in f]

#开始随机
import random
name = ""
#第一部分
tmp = len(name_1)
tmp = random.randrange(tmp)
name += name_1[tmp]
#第二部分
tmp = len(name_2)
tmp = random.randrange(tmp)
name += name_2[tmp]
#第三部分
tmp = len(name_3)
tmp = random.randrange(tmp)
name += name_3[tmp]
#输出
print(name)