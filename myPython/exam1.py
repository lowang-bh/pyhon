
# coding: utf-8

# ## 七月在线机器学习实训营四期第一周(Python基础)考试
# #### 考试说明:
# - 起止时间：请同学在2018年5月18日至5月20日期间完成，最晚提交时间本周日（5月20日24时之前）结束，<b>逾期不接受补考,该考试分数计入平时成绩</b>
# - 考试提交方式：请同学<font color=red><b>拷贝</b></font>该试卷后，将文件更名为同学姓名拼音-exam1（例如wangwei-exam1）后，移动至/0.Teacher/Exam/1/目录下进行作答。
# - 注意事项：为确保同学们真正了解自身对本周课程的掌握程度，<font color=red><b>请勿翻阅，移动，更改</b></font>其它同学试卷。如发现按0分处理
# - 请同学在下方同学姓名处填写自己的姓名，批改人和最终得分处不用填写

# - 同学姓名:<u></u>
# - 批改人：
# - 最终得分:

# <center><h1>####答卷开始####</h1></center>
# ***

# ### 简答题 (共十题，每题4分，共40分)

# #### 1.请谈谈Python中is 和 == 的区别(代码演示)

# is 表示同一个对象，ID相同
# == 表示内容相同
#

# In[5]:


a, b =10, 10
s1="a long string, python will not buffer it"
s2="a long string, python will not buffer it"

s3="hello"
s4="hello"
print(a==b, a is b)
# long string
print(s1==s2, s1 is s2, id(s1), id(s2))
# short string, python use buffer
print(s3==s3, s3 is s4, id(s3), id(s4))


# #### 2.什么是Python中的自省？

# python可以自动推导变量类型，不需要指定类型

# #### 3.Python中的高阶函数是指什么？

# 能够接受函数作为参数的函数

# #### 4. Python类中有哪些的成员，如何分类他们，他们各自又有哪些用途？

# 实例成员，类成员
# 实例成员在每个实例中相互独立，
# 类成员在类中共享，相当于全局，可用于单例模式，统计类中属性在所有实例中的值等

# #### 5 Python中列表，元组的相同之处及区别都有哪些？集合与字典呢？

# list与tuple：都是迭代器，支持随机访问，list可变，tuple不可变
# list与dict：list使用数组实现，dict只支持关键字访问，底层原理属于hashmap
#

# #### 6.尝试简述一下什么是Python类中的数据封装，以及封装的意义？

# 数据封装就是把类中的变量对外提供访问接口，而不是直接暴露给外面。
# 封装可以控制访问权限。
#

# #### 7.解释下Python中的局部变量，和全局变量？

# 函数内部定义的变量
# 全局变量， 在python文件中声明的变量，整个文件都可以访问

# #### 8.谈谈您对Python中闭包的理解？

# 闭包就是函数返回之后，其定义的内嵌函数仍然可以使用其中的环境进行工作
# 闭包需要满足：
# 1. 闭包函数有内嵌函数
# 2. 内嵌函数引用上一级namespace中变量
# 3. 闭包函数返回该内嵌函数

# #### 9	Python中正则表达式的*？+有什么不同？

# *？0次或多次，最少匹配
# +至少出现一次,贪婪匹配，匹配最多

# In[29]:


import re
str1 = "abcehellooo"
str2 = "hellhhoollywood "
print("-----str1----")
#o匹配多次
print(re.search(r'(hello*)', str1).groups())
#o匹配0次
print(re.search(r'(hello*?)', str1).groups())
print(re.search(r'(hello+)', str1).groups())

print("------str2-----")
#没有o,匹配0次
print(re.search(r'(hello*)', str2).groups())
#匹配0次
print(re.search(r'(hello*?)', str2).groups())
#没有o,无法匹配
print(re.search(r'(hello+)', str2))


# #### 10.Python中的模块和包是什么，如何自定义并使用？

# 一个.py文件就是一个模块， 每一个定义了__init__.py文件的目录都是一个包
# 模块的使用：import 文件名
# 包使用：定义__init__.py 并import文件名

# ### 代码题(共十题，每题6分,共60分)

# #### 1. 创建一个函数，接收一个字符串参数，判断其做为Python标识符是否合法。
#
# 具体要求：
# - 如果合法则输出 True，否则输出 False。
# - 如果该字符串与Python内置的关键字，或Bifs冲突，则打印'conflict'
# - 注:Python标识符的规则，关键字和Bifs可搜索得到

# In[108]:


import keyword
try:
    import builtins as builtin
except ImportError:
    import __builtin__ as builtin
def func(sinput):
    if not isinstance(sinput, str):
        return False
    bifs = dir(builtin)
    if sinput in keyword.kwlist or sinput in bifs:
        print('conflict')
        return False
    if str.isidentifier(sinput):
        return True
    else:
        return False
print(func("print"))


# #### 2.编写一个函数，能生成包含20个随机整数的列表，然后将前10个元素升序排列，后10个元素降序排列，并分别打印输出

# In[41]:


from random import randint
def func(start, end, numbers=20, increase_num=10):
    if increase_num>numbers:
        increase_num=numbers
    res = [randint(start, end) for x in range(numbers)]

    return sorted(res[0:increase_num]) + sorted(res[increase_num:], reverse=True)

func(1,100,20,10)


# #### 3.有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13,请使用Python代码出生成并打印该数列的前30项并求和返回

# In[51]:


from fractions import Fraction
def func(sum=30, debug=True):
    a,b=2,1
    res = 0
    for i in range(sum):
        if debug:
            print(Fraction(a,b))
        res += a/b
        a,b = a+b, a

    return res


func(30)


# #### 4. BMI编写
# 身体质量指数（BMI）是根据人的体重和身高计算得出的一个数字，BMI是可靠的身体肥胖指标，其计算公式：BMI=Weight/High2，其中体重单位为公斤，身高单位为米。
#
# - 计算公式为：$BMI=体重（kg）÷身高^2（m）$
#
# - 提示用户输入体重（kg）和身高的数字(m)(注意单位），然后计算BMI。
#
# - 根据BMI指数范围，定义当前健康状态。BMI指数在18至25之间定义为健康的标准体重,小于该范围定义为偏瘦，超过该范围定义为偏重。
#
# - 将BMI指数和其所代表状态输出
#
#
#

# In[56]:


def func(wight, hight):
    bmi = wight / hight **2
    if  18< bmi <25:
        return (bmi, '健康')
    elif bmi <18:
        return (bmi, '偏瘦')
    else:
        return (bmi, '偏胖')

func(60,1.7)


# #### 5.字符统计
# - 创建一个函数，接收字符串输入，分别统计出其中英文字母、空格、数字和其它字符的个数后打印。
# - 提示：
#   - ord('a') 能将字符 'a' 转化为 ASCII 码表上对应的数值，
#   - 例如，空格为32
#   - 数字 0-9 对应的码值为 48-57
#   - 大写字母 A-Z 对应 65-90
#   - 小写字母 a-z 对应 97-122
#   - 比122高的都是其它。

# In[60]:


def func(input_str):
    if not isinstance(input_str, str):
        print('Error, input not a string')
        return False
    res_dic = {'alpha':0, 'num':0, 'blank':0, 'other':0}
    for s in input_str:
        if 48 < ord(s) <57 :
            res_dic['num'] += 1
        elif 65<ord(s) <90 or 97 < ord(s) <122:
            res_dic['alpha'] += 1
        elif ord(s) == 32:
            res_dic['blank'] +=1
        elif ord(s) >122: # 不是else？
            res_dic['other'] +=1
    return res_dic

statics=func("hello, how are you, Mr._blank1")
for key,value in statics.items():
    print(key, value)


# #### 6.创建一个函数，可以将去除给定列表中中相邻且重复的元素(只保留一个)后，打印输出结果。
# - 说明
#   - 输入参数为 l1=[1,2,3,4,4,4,4,4,4,5,6,6,8,8,12,12,12,12,13]
#   - 操作后，保证原有整体排序不变，仅处理相邻且重复的元素
#   - 请勿使用set，否则该题不计分。

# In[79]:


def func(inputlist):
    if not isinstance(inputlist, list):
        return []
    res =[]
    lenth=len(inputlist)
    for index, item in enumerate(inputlist):
        if index < lenth -1:
            if inputlist[index+1] == item:
                pass
            else:
                res.append(item)
        else:
            res.append(item)

    return res


print(func([1,2,3,4,4,4,4,4,4,5,6,6,8,8,12,12,12,12,12]))
print(func([1,2,3,4,4,3,4,5,5,5,6,7,7,8,3,8,8,9]))


# #### 7 	创建一个函数，接收一个由整数组成的列表（需对输入列表做检查，长度最少为2,数据类型为整型），并检验后下列条件后输出：
# - 如列表是升序排列的,则输出"ASC";
# - 如列表是降序排列的,则输出"DESC";
# - 如列表无序，则输出"WRONG"。

# In[83]:


def func(inputlist):
    if not isinstance(inputlist, list):
        print('Error: not list')
        return
    if len(inputlist) <2:
        print('Error: lenth is smaller than 2')
        return
    for item in inputlist:
        if not isinstance(item, int):
            print('Error: not int item')
            return
    sum = 1
    for i in range(len(inputlist) - 1):
        if inputlist[i] >= inputlist[i+1]:
            sum += 1
        else:
            sum += 0
    if sum == len(inputlist):
        return 'DESC'
    elif sum == 1:
        return 'ASC'
    else:
        return 'WRONG'
print(func([1,2,4,5,6,7]))
print(func([1,2,9,5,6,7, 2]))
print(func([9,8,6,4,0]))


# #### 8.高阶函数综合运用
#
# l1=[1,3,6,8,10,11,17]
#
# 请仅使用map,reduce,filter对上方数组依次进行如下三次操作：
#
#
# - 剔除掉所有的偶数后打印
#
# - 对剩下的数字每个数字进行平方后打印
#
# - 对数组求和后打印

# In[90]:


#剔除掉所有的偶数后打印
l1=[1,3,6,8,10,11,17]

l2=[item for item in filter(lambda x: x%2==1, l1)]
print(l2)


# In[95]:


#对剩下的数字每个数字进行平方后打印
l3=list(map(lambda x:x**2, l2))
print(l3)


# In[94]:


#对数组求和后打印
from functools import reduce
print(reduce(lambda x,y: x+y, l1))


# #### 9.Python类设计
# 设计一个公司类，完成以下要求，<font color=red>并实例化不同对象进行验证</font>
#
# 类变量
#  - 类下公司的总个数，类下实例的名称列表
#
# 类方法
#  - 返回公司类共有多少个公司实例
#  - 返回公司类的公司实例有名称列表
#
# 实例变量
# - 公司名，简介，利润，销售额，总成本，雇员姓名，雇员列表
#
# 实例方法：
# - 招聘人才（每招一个人会有成本产生，影响该实例雇员列表，人数，总成本）
# - 解雇人员（每解雇一个人会有成本产生，影响该实例雇员列表，人数 ，总成本）
# - 公司广告推广(影响该实例总成本)
# - 交社保(按公司雇员总人数计算，影响该实例总成本)
# - 交税(按公司雇员总人数计算，影响该实例总成本)
# - 销售（按销售件数*价格计算销售额，利润按销售额*利润率进行计算利润。）
# - 获取公司雇员列表
# - 获取公司净利润
class employee(object):
    def __init__(self, name, salary=10000, base=1.0, percent=0.12):
        self._name = name
        self._salary = salary
        self._base=base
        self._percent = percent
    @property
    def coast(self):
        return self.salary(1+ self.base * 0.12)
    @property
    def social_insurance(self):
        return self.salary * self.base * self.percent
    @property
    def name(self):
        return self._name
    @property
    def salary(self):
        return self._salary
    @property
    def base(self):
        return self._base
    @property
    def percent(self):
        return self._percent
    def __str__(self):
        return self.name

class company(object):
    company_nums = 0
    instance_names_list = []

    def __init__(self, com_name, profile="no indroduction"):
        company.instance_names_list.append(com_name)
        company.company_nums +=1
        self.profile = profile
        self.sales = 0
        self.cost = 0
        self.profit = 0
        self.hire_list = []

    @classmethod
    def get_company_numbers(cls):
        return cls.company_nums
    @classmethod
    def get_instances_names(cls):
        return cls.instance_names_list

    def hire(self, name, salary, base=1.0, percent=0.12):
        new_employee = employee(name, salary, base, percent)
        self.hire_list.append(new_employee)
        self.cost += new_employee.salary

    def fire(self, name):
        try:
            indx = self.hire_list.index(name)
            member = self.hire_list.remove(indx)
            self.cost -= member.salary
        except ValueError:
            print("No employer named %s" %name)

    def advertise(self, coast):
        self.cost += coast

    def social_insurance(self):
        total = 0
        for member in self.hire_list:
            total +=  member.social_insurance
        self.cost += total

    def tax(self, tax_per_member=1000):
        total =len(self.hire_list * tax_per_member)
        self.cost +=  total

    def sale_product(self, sales_number, price, percent_of_profit=0.4):
        self.sales += price * sales_number
        self.profit += price * sales_number * percent_of_profit

    def get_profit(self):
        return  self.profit

    def get_hire_list(self):
        return self.hire_list

    def get_pure_profit(self):
        return self.profit-self.cost


c1=company("huawei", "telcom")
c2=company("Nokia", "telcom")
print(company.company_nums, company.instance_names_list)


# #### 10.结合PIL库，制作一个能生成4位随机数验证码图片的函数。
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

def rndChar():
    return chr(random.randint(65, 90))
def rndInt():
    return str(random.randint(1,9))
# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# 240 x 60:
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象:
font = ImageFont.truetype('Arial.ttf', 36)
# 创建Draw对象:
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# 输出文字:
for t in range(4):
    draw.text((60 * t + 10, 10), rndInt(), font=font, fill=rndColor2())
# 模糊:
image = image.filter(ImageFilter.BLUR)

image.show()

# ***
# <center><h1>####答卷结束####</h1></center>
#
#

# ### 本周课程意见反馈(非必答)
# 请同学围绕以下两点进行回答：
# - 自身总结：您自己在本周课程的学习，收获，技能掌握等方面进行总结，包括自身在哪些方面存在哪些不足，欠缺，困惑。作为将来回顾学习路径时的依据。
# - 课程反馈：也可以就知识点，进度，难易度，教学方式，考试方式等等进行意见反馈，督促我们进行更有效的改进，为大家提供更优质的服务。
#
