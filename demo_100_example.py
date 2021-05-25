# 1.两数相加
def demo_p001():
    number1 = 15.8
    number2 = 5.4
    sum = number1 + number2
    print(f'{number1}+{number2}={sum}')
    print("\033[显示方式；前景颜色；背景颜色m…\033[034")


# 2.数的阶乘
def demo_p002(number):
    result = 1
    pull_number = number
    while pull_number>0:
        result *= number
        pull_number -= 1
    print(f"{number}的阶乘是：{result} ")
    print("\033[0;36;40m=======这是P2华丽的分割线===========p002END\033[0m")

# 3.计算圆的面积  A= R*R*3.14  math.PI
import math
def demo_p003(r):
    Arce = round(math.pi*r*r,2)
    print(f"半径为{r}圆的面积是{Arce}")

    print("\033[0;36;40m=======这是P3华丽的分割线===========P003END\033[0m")

# 4.区间内的所有一素数
def demo_p0004(s:int,e:int):
    prim = []
    status = 0
    for i in range(s,e+1):
        if i in range(1,2):
            status = 1
        for y in range(2,i):
            if i%y == 0:
                status = 0
                break
                # continue
            status = 1
        if status:
            prim.append(i)
    
    print(f'在{s}到{e}这个区间中素数有：{prim}')
    print("\033[0;36;40m=======这是P0004华丽的分割线===========p0004END\033[0m")


def demo_p004(s:int,e:int):
    prim = []
    for i in range(s,e+1):
        if is_prime(i):
            prim.append(i)
                # print(f'在{s}到{e}这个区间中：',end=' ')
                # print(f'{i}是素数',end ='\t')
                # print('')
    print(f'在{s}到{e}这个区间中素数有：{prim}')
    print("\033[0;36;40m=======P004这是华丽的分割线===========p004END\033[0m")

def is_prime(i):        
    if i in range(1,2):
        return True
    for y in range(2,i):
        if i%y == 0 :
            return False
    return True        




if __name__=="__main__":
    # demo_p001()
    # demo_p002(6)
    demo_p003(6.78)
    demo_p004(6,19)
    demo_p0004(6,19)
