import math
import random
from lab3 import SerializerJson, SerializerFactory, SerializerYaml, DeserializerYaml, DeserializerJson, Json, Toml, Yaml


def hello():
    print('hello')

    def world():
        print('world')

    world()


def fib(n):
    if n == 0 or n == 1:
        return 1

    else:
        return fib(n - 1) + fib(n - 2)


t = 5
my_number = 42
my_list = [True, [False, 228], 'pamagiti', []]
my_dict = {'1': {'2': 'aaaaaaaaaaa'}, '-5': 228, 'fd': [my_list]}
my_list2 = {'Халява': 'прийди'}



my_parser = SerializerFactory.Serializer.create_serializer('json')
file = 'temp.json'


class A:
    x = 10

    def my_meth(self, a):
        return math.sin(self.x * a)

    def __str__(self):
        return 'a'

    def __repr__(self):
        return 'a'


class B:
    def __init__(self):
        self._a = 10
    #
    # @classmethod
    # def meth_cls(cls):
    #     return 'passed'


class C(A, B):
    pass


# #print(type(my_parser.Json))
#
ser = my_parser.Json()
C_ser = ser.dumps(B)
# C_ser = SerializerFactory.Serializer.create_serializer('json')
# a = C_ser.Json.dumps(C_ser,indent=2)
# print(a)
# # cser = Json.dumps(C)
# # #cser = SerializerJson.serialize.(C,file,indent=2)
# # cdes = Json.loads(C)
# #
# # print(cdes)
#

#
# class My:
#     a = 5
#
#
# class Dad:
#     def __init__(self, second_name):
#         self.second_name = second_name
#
#
# class Gender:
#     def __init__(self):
#         temp = random.randrange(0, 2, 1)
#         if temp == 0:
#             self.sex = 'Men'
#         else:
#             self.sex = 'Women'
#
#
# f = Gender()
#
#
# class Baby(Dad):
#     def __init__(self, first_name, second_name, gender):
#         Dad.__init__(self, second_name)
#         self.first_name = first_name
#         self.gender = gender
#
#     def get_full_name(self):
#         return [self.first_name, self.second_name]
#

# st = SerializerFactory.Serializer.create_serializer('toml')
uy = SerializerFactory.Serializer.create_serializer('json')
# la = SerializerFactory.Serializer.create_serializer('yaml')

# c11 = st.Toml.dumps(Baby)
# print(c11)
# c21 = st.Toml.loads(c11)
# my = c21('aaaa', 'aaa', f)
# print(111111111111111111111111111111111111111111111111111111111111111111)
# print(my.gender.sex)

#
# def add_four(a):
#     x = 2
#
#     def add_some():
#         print("x = " + str(x))
#         return a + x
#
#     return add_some()
#
#
# def make_multiplier_of(n):
#     def multiplier(x):
#         return x * n
#
#     return multiplier



# rory = uy.Json.dumps(Baby)
# rorys = uy.Json.loads(rory)
#
# c113 = la.Yaml.dumps(make_multiplier_of)
# c213 = la.Yaml.loads(c113)
# times3 = c213(3)
# print(make_multiplier_of.__closure__)
'''c113=uy.Json.dumps(my)
c213=uy.Json.loads(c113)'''

'''x=c2
print(x.a)'''
'''c1=uy.Json.dumps(My)
print(c1)
c2=la.Yaml.loads(c1)'''

'''v1=st.Toml.dumps(hello)
print(v1)'''
# c=st.Toml.dumps(my_number)

def my_dedc(func):
    def writer():
        print("hello")
        func()
    return writer

@my_dedc
def rory():
    print("nigga")

work = uy.Json.dumps(my_dedc(rory))
print(work)

# work = uy.Json.dumps(C)
# work1 = uy.Json.loads(work)
# print(work)
# print(work1)