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
# 5.计算从1到N的平方和
def demo_p005(n):
    result = 0
    for i in range(1,n+1):
        result += i*i 
        if i<n:
            print(f'{i}*{i}+',end='')
        else:
            print(f'{i}*{i}',end='')
    print(f'= {result}')
    print("\033[0;36;40m=======P005华丽的分割线===========END\033[0m")

# 6.计算LIST的和
def demo_p006(data:list):
    totle = 0
    for x in data:
        totle += x
        if x==data[-1]:
            print(f'{x}',end='')
        else:
            print(f'{x}+',end='')
    print(f'={totle}') #等效 print(sum(data))
    print("\033[0;36;40m=======P006华丽的分割线===========END\033[0m")

# 7.数字范围内的所有偶数
def demo_p007(s:int,e:int):
    db =[]
    for x in range(s,e+1):
        if x%2==0:
            db.append(x)
    print(db)
    print("\033[0;36;40m=======P007华丽的分割线===========END\033[0m")

# 8.List remove multiple element
def demo_p008(data1:list,data2:list):
    print(f'数组1：{data1},  数组2：{data2}')
    for i in data2:
        data1.remove(i)
    print(f'删除多个元素后的数组：{data1}')
    print("\033[0;36;40m=======P008华丽的分割线===========END\033[0m")

def demo_p0008(data1:list,data2:list):
    data = [i for i in data1 if i not in data2]
    print(data)
    print("\033[0;36;40m=======P0008华丽的分割线===========END\033[0m")

# 9.list中去重 source list unique_list
def demo_p009(data1:list):
    db =[]
    for i in data1:
        if i not in db:
            db.append(i)
    print(f'输入的数据：{data1}')
    print(f'去重后的数据：{db}',end='\n')
    print(f'还可以用list(set(source_list))实现去重：',list(set(data1)))
    print("\033[0;36;40m=======P009华丽的分割线===========END\033[0m")


# 10.list 排序
def demo_p010(data1:list):
    print(f'source list:{data1}')
    # data=list(set(data1))
    # data.sort()
    print(f'source_list sorted and unique:{sorted(list(set(data1)))}')
    print("\033[0;36;40m=======P010华丽的分割线===========END\033[0m")

# 11.复杂列表，元素 字典、元组
def demo_p011():
    students = [
        {'sno':101,'sname':'小张','sgrade':88},
        {'sno':102,'sname':'小王','sgrade':77},
        {'sno':103,'sname':'小李','sgrade':99},
        {'sno':104,'sname':'小赵','sgrade':66},
    ]
    students_sort = sorted(students,key= lambda x:x['sgrade'],reverse=True)
    print(students)
    print(students_sort)
    print("\033[0;36;40m=======P011华丽的分割线===========END\033[0m")


if __name__=="__main__":
    # demo_p001()
    # demo_p002(6)
    demo_p003(6.78)
    demo_p004(6,19)
    demo_p0004(6,19)
    demo_p005(6)
    demo_p006([3,35,62,4,1])
    demo_p007(5,20)
    demo_p008([3,5,8,9,7,11,13,15,17],[7,11])
    demo_p0008([3,5,8,9,7,11,13,15,17],[7,11])
    demo_p009([10,20,30,40,10,20,40,50])
    demo_p010([10,20,30,40,10,20,40,50])
    demo_p011()
