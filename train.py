# # print("Hello World")
# start = input("press any key to continue...")
# started = False

# while start != '':
#     start = input("press any key to continue...")
# else:
#     press_start = input("enter start to start the game: ")
#     while press_start != 'start':
#         print("wrong command")
#         press_start = input("enter start to start the game: ")
#     else:
#         started = True
#         print("game has been started...")


# def generator(n):
#     num = 0
#     while (num < n):
#         yield num
#         num += 1
# # def generator():
#     # yield 1
#     # yield 2
#     # yield 3

# for x in generator(n=20000):
#     print(x)

# class Computer(object):
#     def __init__(self, ram, cpu, hard):
#         self.ram = ram
#         self.cpu = cpu
#         self.hard = hard
#     def value(self):
#         return self.ram + self.hard + self.cpu


# class Laptop(Computer):
#     def __init__(self, size, *args, **kwargs):
#         self.size = size
#         super(Laptop, self).__init__(*args, **kwargs)
    
#     def value(self):
#         return super(Laptop, self).value() + self.size


# pc1 = Computer(12, 2, 4)
# pc2 = Computer(13, 4, 2)
# laptop1 = Laptop(30, 20, 8, hard=6) # hard is kwargs the numbers before kwargs are args we shuold represent these in __init__
# print(pc1.value())
# print(pc2.value())
# print(laptop1.value())



# class Device:
#     count = 0
#     def __init__(self, ip, name, mac):
#         self.ip = ip
#         self.name = name
#         self.mac_address = mac
#         Device.count += 1

#     def get_status(self):
#         """return results based on ping results for self.ip"""
#         pass


# class TV(Device):
#     def turn_on(self):
#         """connect to self.ip and turn on"""
#         pass
#     def turn_off(self):
#         """connect to self.ip and turn off"""
#         pass

# class Thermo(Device):
#     def get_degree(self):
#         """connect to self.ip and return results"""
#         pass

# class SmartTV(TV):
#     def turn_on(self):
#         """turn on the smart TV with self.ip"""
#         pass



# class Student(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# stu1 = Student("mahdi", 22)
# stu2 = Student("mamad", 22)

# setattr(stu1, "grade", "high_school")
# # ya balaei ya paeini e jufteshun ye attr ezafe mikonan be class(mesle name o age)
# # stu1.grade = "high_school"

# print(getattr(stu2, "name"))
# # eyne paeinie 
# # print(stu2.name)

# delattr(stu1, "grade")
# # eyne paeinie 
# # del stu1.grade

# x = hasattr(stu2, 'age')
# y = hasattr(stu1, 'grade')
# print(x, y)





# from random import randint
# random_num = randint(0, 10)


# while True:
#     print(random_num)
#     x = int(input("Guess a number between 0 to 10: "))
#     if x == random_num:
#         print("You gussed right!")
#         break
#     elif x > 10 or x < 0:
#         print("You should guess between 0 to 10")
#     elif x != random_num:
#         print("wrong guess!")

# --------- ham balaey ham paeini --------------

# x = int(input("Guess a number between 1 to 10: "))
# while x != random_num:
#     print("Wrong guess!")
#     x = int(input("Guess another number: "))
# else:
#     print("Right guess!")


# -------- computer guesses a number ----------------

# while True:
#     print("My guess is: ", random_num)
#     print("""
# if it's right enter 'yes'
# if i should guess higher enter 'higher'
# if i should guess lower enter 'lower'
#     """)
#     user_answer = input("which one is that: ")
#     if user_answer == 'yes':
#         print("Yeaaay! i won!")
#         break
#     elif user_answer == 'higher':
#         random_num = randint(random_num, 10)
#     elif user_answer == 'lower':
#         random_num = randint(0, random_num)

# ----- create star in GUI ------------
# import turtle
# x = turtle.Pen()
# # for i in range(1, 7):
# #     x.left(135)
# #     x.forward(100)

# x.color(0, 0, 1)
# x.begin_fill()
# x.forward(120)
# x.left(90)
# x.forward(19)
# x.left(70)
# x.forward(80)
# x.right(20)
# x.forward(40)
# x.left(40)
# x.forward(70)
# x.left(45)
# x.forward(40)
# x.right(40)
# x.forward(30)
# x.left(60)
# x.forward(27)
# x.left(50)
# x.forward(10)
# x.right(10)
# x.forward(8)
# x.left(75)
# x.forward(120)
# x.end_fill()
# x.up()
# x.color(0, 0, 0)
# x.forward(30)
# x.right(45)
# x.forward(20)
# x.down()
# x.begin_fill()
# x.circle(20)
# x.end_fill()
# x.up()
# x.right(150)
# x.forward(120)
# x.down()
# x.begin_fill()
# x.circle(20)
# x.end_fill()

# import re
# x = "I work for Iran revelutionary gaurd corps"
# result = re.search('work', x)
# print(result)
# # ------------ assert -------------------
# x = "hello"
# assert x == 'goodbye', "it should be hello"

# # ----------- halghe ha --------------
# n = 2
# for _ in range(1, 10):
#     n += 1
#     print(n)


# x = ""
# y = " - "
# for _ in range(1, 11):
#     x += " * "
#     print(x, " \ ")
#     y += " - "
#     if _ >= 10:
#         print(y)


# z = 9
# while z > 0:
#     z -= 1
#     if z == 6: # be 6 ke residi boro
#         continue # boro baadio bekhun 6 o print nakun
#     print(z)


# # ------------ list haye pishrafte ----------------
 

# list1  = ['mamad', 'jafar', 'kazem']
# list2  = ['mahdi', 'reza', 'ahmad']
# final_list = [list1, list2]

# list3 = list1 # inja yani list 3 hamoon list e 1 e
# list3[0] = 'parsa' # pas inja darvaghe list1 taqir karde bara hamin to final list ham taqir ro mibinim
# print(list3)
# print(final_list)

# list4 = list2[:] # inja darvaqe ye list jadid misaze ke copy list2 e pas age taqiresh bedim hich etefaqi bara list2 nemiofte
# list4[2] = 'hamid'
# print(list4)
# print(final_list)

# # amma age elemente dakhele ye list e copy shude ke shamele list haye dg hast (final_list) o avaz konim un list ham taqir mikkone
# final_list_copy = final_list[:]
# final_list_copy[0][0] = 'mamad' # chon darvaqe in final_list_copy ham dare mostaqim be khude list1 va list2 eshare mikone na be final_list
# print (final_list_copy)
# print (final_list)

# """baraye inke taqirate final_list_copy faqat ro khudesh emal she bayad Deep copy kard"""
# import copy

# final_list_copy = copy.deepcopy(final_list) # to inja az list1 va list2 ye copy dg misaze bara final_list_copy

# final_list_copy[0][0] = 'parsa'
# print(final_list_copy)
# print(final_list)


# list1 = ['mamad', 'kazem', 'jasem']


# def list_change(lst):
#     lst[0] = 'parsa'


# list_change(list1)
# print(list1)






# # ------------- generator ha --------------

# def my_range(x):
#     while x > 0:
#         print("counting next number ... ")
#         yield x
#         x -= 1

# for i in my_range(10):
#     print(i)


# from random import randrange

# def random_gen_info(low, high):
#     while True:
#         yield randrange(low, high)

# r = random_gen_info(0, 100)
# print(next(r))
# # for x in r:
# #     print(x)

# v = [ i ** 2 for i in range(1000)] # in generator nist fek konam mesle hamoon return e(yani value o return mikone)
# print(v)

# x = ( i ** 2 for i in range(1000))  # halghe for o age injury benevisim generator mish( hamoon yield)
# print(next(x))


# <===================================================== List va Generator =====================================================>

# # --------- ye list i az tuple -------------------
"""to inja chun kollan az generator estefade kardim doone doone retuen mikone
be sharti ke halghe doovom ke list e range kami dashte bashe
"""
# x = ([(i, ii) for ii in range(10)] for i in range(9000000000000000000))
# print(x)
# [print(y) for y in x] # bekhatere in ke x kollan generatore in khat bayad for bezarim

# # ------------ eine balaeye faqat dg list nist --------------------------
"""to inja chun kollan az generator estefade kardim doone doone retuen mikone"""
# x = (((i, ii) for ii in range(9000000000000000000)) for i in range(9000000000000000000))
# print(x)
# [[print(y) for y in u] for u in x]
# # ---------- ye list comprihanshen ---------------
"""to ye in ja chun az list cumprihanshun estefade kardim avval range o be dast miare baad return mikone"""
# x = [[(i, ii) for ii in range(10)] for i in range(9000000000000000000)]
# print(x)
# [print(y) for y in x] # niaz be for nadare vali mishe guzasht

# # ----------- ye listi az generator ha ke ba 2 halghe tuple mishe --------------
"""to ye in ja chun az list cumprihanshun estefade kardim avval range o be dast miare baad return mikone"""
# x = [((i, ii) for ii in range(9000000000000000000)) for i in range(9000000000000000000)] 
# print(x)
# [[print(y) for y in u] for u in x] # age ye for mizashtim faghat generator neshun midad amma bara gereftane khuroji bayad 2 ta halghe bezarim


# ------------------ list comprehension -------------------
"""range khudesh ye generator e"""
# xyz = [i for i in range(5)]
# print(xyz)
# # ------- YA ----------
# xyz = []
# for i in range(5):
#     xyz.append(i)

# print(xyz)

# -------- generator -------

# xyz = [x for x in (i for i in range(5))] # generator o to ye list zakhire mikone
# print(xyz)

# xyz = (i for i in range(5))
# for x in xyz:
#     print(x)

# ----------------
# input_list = [5, 6, 2, 10, 15, 20, 3]

# def div_by_five(num):
#     # if num % 5 == 0:
#     #     return True
#     # else:
#     #     return False
#     return num % 5 == 0

# xyz = (i for i in input_list if div_by_five(i))

# # for x in xyz:
# #     print(x)
# # --- ya ---
# [print(i) for i in xyz]



# #  -------------- khundane khat haye ye file txt -----------------
# import time

# def calculate(file1):
#     file1.seek(0, 2)  # boro be akhare file
#     while True:
#         line = file1.readline()
#         if not line:
#             time.sleep(1) # age khate dg ei nabud 1 sanie vaysa 
#             continue # dobare check kon bebin khatti hast ya na
#         yield line


# my_file = open('text.txt')
# x = calculate(my_file)
# for line in x:
#     print(line, )
#     if line[:0] == '.': # age be noghte residi dg halghe while o edame nade
#         break

# cart = {}
# product_id = [1, 2, 3]
# cart[str(product_id)] = {
#     'id': 2
# }
# cart[str(product_id)]['name'] = 'kazem'
# # cart2[product_ids]
# # print(cart.keys())

# list1 = [1, 3, 4]
# print(list1)
# for y in cart.keys():
#     print(y)
#     [print('yes')  if u in str(list1) else print('no') for u in y]

# class Post(object):
#     pass


# x = 'post'
# # print(dir(x))
# y = x.__class__(Post)
# print(y)
# print(type(y))


# list4 = [3, 5, 20, 15, 2, 1]
# def div_by_five(num):
#     if num % 5 == 0:
#         return True
#     else:
#         return False

# x = [i for i in list4 if div_by_five(i)]

# [print(i) for i in x]

# [[print(i, ii) for ii in range(5)] for i in range(5)]


# def add(self, product, quantity=1, updated=False):
#     product_id = self.cart[str(product.id)]

#     if updated:
#         cart = self.cart[product_id]['quantity'] = quantity
#     else:
#         cart = self.cart[product_id]['quantity'] += quantity


# def sqrt(x, guess=0.1):
#     print("Your guess: ", guess, "   Result: ", guess*guess)
#     if good_enough(guess, x):
#         return guess
#     else:
#         guess = improve_guess(guess, x)
#         return sqrt(x, guess)


# def good_enough(guess, x):
#     if abs(guess*guess - x) == 0: 
#         return True
#     else:
#         return False

# def avg(a, b):
#     return (a + b) / 2.0

# def improve_guess(guess, x):
#     return avg(guess, float(x)/guess)

# sqrt(25)

# # ---------------------- high order functions -----------------------------------
# def add_wrapping_with_style(style):
#     def add_wrapping(item):
#         def wrapped_item():
#             x = item()
#             # return f"a {style} Wrapped of box of {str(item())}"
#             return f"a {style} Wrapped of box of {str(x)}"
#         return wrapped_item
#     return add_wrapping


# @add_wrapping_with_style('red')
# def new_gpu():
#     return 'a Tesla P-100 GPU'

# print(new_gpu())

# def logger(f):
#     def wrapper(n):
#         print("I'm going to call a function.")
#         v = f(n)
#         print("the function returned: ", v)
#         return v
    
#     return wrapper



# logged_fib = logger(f=fibo)
# logged_fib(4)
# from functools import wraps

# def halle(name=None):
#     def memorize(f):
#         mem = {}
#         @wraps(f)
#         def memorized_func(n):
#             if n not in mem:
#                 mem[n] = f(n) # in f hamoon fucntion e fibo e

#             return mem[n]
        
#         return memorized_func
#     return memorize

# # @memorize()  # in hamoon fibo = memorize(f=fibo)
# @halle()  # in hamoon fibo = memorize(f=fibo)
# def fibo(n):
#     if n <= 1:
#         return n
#     else:
#         return fibo(n-2) + fibo(n-1)

# print(fibo(200))
# print(fibo.__name__) # age @wraps() o nazarim esme wrapper o barmigardoone ... age bezarim esme asli function (fibo) o ro barmogardoone
# print(fibo.__doc__)
# fibo = memorize(f=fibo)  # vaghti injury minevisim bayad hatman samte chape = esme khude function bashe
# print(fibo(100))


# with open('text.txt', 'r') as f:
#     for line in f:
#         print(line)


# from contextlib import contextmanager
# import time

# @contextmanager
# def timeit():
#     start_time = int(round(time.time() * 1000))
#     yield

#     end_time = int(round(time.time() * 1000))
#     elapsed = end_time - start_time
#     print(f"code took {elapsed} ms to run...")

# def another_function():
#     time.sleep(2)


# with timeit():
#     another_function()

# # ---------- kochik tarin addade ye list o bar migardoone -----------------
# smallest = None
# for x in [3, 4, 5, 14, 6, 7, 32, 43]:
#     if smallest is None:
#         smallest = x
#     elif smallest > x:
#         smallest = x
# print(smallest)


# mem = {}
# def wrapper(x):
#     if x not in mem:
#         mem[x] = x
#         print(mem)
#     return mem[x]

# print(wrapper(3))

## ========================================= parallel ya multiprocess va halle khata ba Lock =========================================

# ------------ Multy process ------------

# import multiprocessing

# def spawn(num):
#     print(f"Spawned!{num}")



# # bara multi processing bayad hatman khat e zir o benvisim
# if __name__ == '__main__':
#     for i in range(55):
#         p = multiprocessing.Process(target=spawn, args=(i, ))
#         p.start()
#         p.join() # join tazmin mikone ke process be soorate order shude run she 

# ---------------------------------------------
# from multiprocessing import Pool
# def job(num):
#     return num * 2

# if __name__ == '__main__':
#     p = Pool(processes=20)
#     data = p.map(job, range(20))
#     p.close()
#     print(data)

# ----------------------------------------------


# from multiprocessing import Process, Lock, Value
# import time


# def add_500(total, lock):
#     for _ in range(100):
#         time.sleep(0.01)
#         with lock:
#             total.value += 5
    

# def sub_500(total, lock):
#     for _ in range(100):
#         time.sleep(0.01)
#         lock.acquire()
#         total.value -= 5
#         lock.release()
    


# if __name__ == '__main__':
#     total = Value('i', 500)
#     lock = Lock()

#     add_process = Process(target=add_500, args=(total, lock, ))
#     sub_process = Process(target=sub_500, args=(total, lock, ))


#     add_process.start()
#     sub_process.start()
#     add_process.join()
#     sub_process.join()
#     print(total.value)

# total = 500
# total = add_500(total)
# print(total)
# total = sub_500(total)
# print(total)
## --------------------- Asunchronous programming parallel ----------------------------
# import threading # thread mesle processor e amma sabok tare az value ya ... nemikhad estefade konim
# import time
# from multiprocessing import Lock, Process, Value, Queue  # vaghti az processor estefade mikonim bayad ya az Value ya az Array estefade konim

# num_threads = 5
# iteration_in_one_thread = 100

# counter = 0

# lock = Lock()
# # lock = threading.Lock()

# def f(counter, lock): # q
#     # global counter

#     for _ in range(iteration_in_one_thread):
#         with lock:
#             v = counter.value
#             time.sleep(0.01)
#             v += 1
#             counter.value = v
#             # q.put(counter.value)

# threads = []
# def run_experiment():
#     if __name__ == '__main__':  
#         global counter
#         # counter = 0
#         counter = Value('i', 0)
#         # threads = []
#         for _ in range(num_threads):
#             # t = threading.Thread(target=f)
#             # q = Queue()
#             t = Process(target=f, args=(counter, lock, )) #q
#             threads.append(t)
#             t.start()
#         for i in threads:
#             i.join()

#         # while q.empty() is False:
#         #     print(q.get())

#         print(f"calculated value: {counter.value}")
#         print(f"expected value: {num_threads * iteration_in_one_thread}")

# run_experiment()



## ------------------ functional programming ----------------
"""ham map ham filter generator hastan bara hamin bayad tabdil be list beshan ta beshe print gereft"""
## -------map--------------
"""apply single option to all elements by mapping"""
# from math import sqrt

# [print(sqrt(i)) for i in [2, 3, 4, 5]] 
# x = map(sqrt, [1, 4 ,5, 9]) # to inja kare bala ro besoorate paralel anjam mide
# print(list(x))

# def my_map(f, seq):
#     result = []
#     for elt in seq:
#         result.append( f(elt) )
#     return result

# print(my_map(sqrt, [1, 4, 9, 16]))


# def power_of_two(k):
#     return 2**k

# print(power_of_two(3))
# print(list(map(power_of_two, [1, 2, 3, 4, 5])))


# print(list(map(lambda k: 2**k, [1, 2, 3, 4, 5])))

## ------ filter ------------
"""filter some values out by passing a boolean function by filter"""
# x = filter(str.isalpha, ['x', 'y', '2', '3', 'q'])
# print(list(x))


## ------ reduce ------------
"""jame 2 addade ghabli o migire ba baadi jam mikone"""
# from functools import reduce

# # def add(x, y):
# #     return x + y

# # print(reduce(add, [1, 3, 2], 0)) # 0 addade avvalie ast ba 1 jam mishe mishe 1 baad 1 ba 2 jammishe mishe 3 baad 3 ba 3 jam mishe mishe 6

# from collections import defaultdict, Counter
# lines = [
#     "A cow is a domestic animal. A cow is a very useful animal.",
#     "A cow is a domestic animal. A cow is a very useful animal.",
#     "A cow is a domestic animal. A cow is a very useful animal.",
#     "A cow is kept in barns. Cow milk is very healty."
# ]
# def count_words(s):
#     # counts = {}
#     counts = defaultdict(int) # tahgriban hamoon balaeye (be soorate default ye meghdare 0 mide be dict: counts = {0:})
#     for word in s.split():
#         counts[word] += 1 # age counts = {} error midad chun meghdari tush nabud

#     return dict(counts)

# counts_map = list(map(count_words, lines))
# # print(counts_map)

# def reduce_counts(x, y): # 2ta dict migire ba ham merg mikone
#     # print("x:", x)
#     # print("y:", y)
#     # print("------")
#     # return {"word": 0}
#     counter = Counter()
#     # print(dict(counter))
#     counter.update(x)
#     counter.update(y)
#     # return counter
#     return dict(counter)


# print(reduce(reduce_counts, counts_map, {}))

## -------------------------- Regular expressions ---------------------------

# text = """03-02-2025 10:22Am  welcome to iran my email is huskar_assassin@yahoo.com
#             and I check it often. You should send me an email !"""

# haystack = "Date: 03-02-2025"
# needle = "Da"
# import re
# match = re.match(needle, haystack)
# # print(match.group(0))

# haystack = text
# str_prefix = ".*"
# str_username = "([a-zA-z0-9_.]*)" # vagti parantez mizarim to group() ye position barash moshakhas mkonim male in group(2)
# str_domain = "(.*\..*?)" # group(3)
# str_email = "(" + str_username + "@" + str_domain + ")"
# needle = str_prefix + "\s" + str_email + "\s"
# # print(haystack)
# # str_date = "\d{2}-\d{2}-\d{4}" # har chizi ta space
# # str_day = "\d{2}:\d{2}[aApP][mM]" # 2 ta ragham e digit
# # needle = str_date + "\s" + str_day
# # print(neelde)
# res = re.match(needle, haystack)
# if res:
#     print("Found!.")
#     print(res.group(1))
# else:
#     print("Not Found!.")




# ========================= Fahmidaaaam __iter__ bara chieeeeeeeeeeeeeeeeeeeeeee =========================
"""vaghti bekhaim vase class e moon ye halghe for tarif konim bayad function e iter o ba yield seda bezanim"""
# class Person(object):
#     def __init__(self, firstname, lastname, cart=None):
#         self.first_name = firstname
#         self.last_name = lastname
#         self.cart = cart
#         if not self.cart:
#             self.cart = {}
    
#     def __iter__(self):
#         # yield self.first_name, self.last_name
#         for item in self.cart.values():
#             item['total_price'] = item['quantity'] * item['price']
#             yield item


# x = Person("Rek'sai", "SMX", {'product': {'price': 2000, 'quantity': 2, 'title': 'food'},})
# for y in x:
#     print(y['total_price'])
#     # print(y.product.price)


"""age __iter__ nazarim bayad injuri benvisim"""
# class IterableContainer:
#     def __init__(self, data=(1,2,3,4,5)):
#         self.data = data
#     def __iter__(self):
#         # for x in self.data:
#         #     yield x
#         return IterableContainerIterator(self.data)
  

# class IterableContainerIterator:
#     def __init__(self, data):
#         self.data = data
#         self._pos = 0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         try:
#             item = self.data[self._pos]
#         except IndexError:
#             raise StopIteration
#         self._pos += 1
#         return item
  

# container = IterableContainer()

# for x in container:
#         print(x)
# ========== linked list ==============
# class Node():
#     def __init__(self, d, n=None):
#         self.data = d
#         self.next_node = n
    
#     def get_next(self):
#         return self.next_node
    
#     def set_next(self, n):
#         self.next_node = n
    
#     def get_data(self):
#         return self.data

#     def set_data(self, d):
#         self.data = d

# class LinkedList():
#     def __init__(self, r=None):
#         self.root = r
#         self.size = 0
    
#     def get_size(self):
#         return self.size

#     def add(self, d):
#         new_node = Node(d=d, n=self.root)
#         self.root = new_node
#         self.size += 1

#     def remove(self, d):
#         this_node = self.root
#         prev_node = None

#         while this_node:
#             if this_node.get_data() == d:
#                 if prev_node:
#                     prev_node.set_next(this_node.get_next())
#                 else:
#                     self.root = this_node
#                 self.size -= 1
#                 return True

#             else:
#                 prev_node = this_node
#                 this_node = this_node.get_next()

#         return False

#     def find(self, d):
#         this_node = self.root
#         while this_node:
#             if this_node.get_data() == d:
#                 return d
#             else:
#                 this_node = this_node.get_next()

#         return None

# my_list = LinkedList()
# my_list.add(5)
# my_list.add(8)
# my_list.add(12)
# print(my_list.remove(12))
# print(my_list.find(5))


# x = list()

# # print(dir(x))
# x.insert(1, 'hello')
# x.append('Hello')
# print(x)
# print(x.count('hello'))
# print(x.index('Hello'))

# purse = dict()
# names  = ['mamad', 'jasem', 'ghasem', 'mehdi', 'mehdi']
# for name in names:
# # ---------------------------
#     # if name in purse:
#     #     purse[name] += 1
#     # else:
#     #     purse[name] = 1
# # ----------- ya ------------
#     purse[name] = purse.get(name, 0) + 1
# print(purse)

# # myobject = {'1':{}, '2':{}, '3':{}, '4':{}}
# # myobject['1']['first_name'] = 'Mamad'
# # myobject['1']['last_name'] = 'Mamadian'
# # print(myobject)

# # myobject.get('5', None)

# fname = input("Enater File name: ")
# if len(fname) < 1:
#     fname = 'text.txt'

# hand = open(fname)
# dictionary = dict()

# for line in hand:
#     lin = line.rstrip()
#     # print(lin)
#     words = lin.split()
#     # print(wds)
#     for word in words:
#         # print(word)
#         # print('**', word, dictionary.get(word, -99))
#         # ---------------------------------------
#         # # if the key is not there the count is zero
#         # count = dictionary.get(word, 1)
#         # print(word, 'old', count)
#         # new_count = count + 1
#         # dictionary[word] = new_count
#         # print(word, 'new', new_count)
#         # ------------- ya ---------------------
#         """ get or/and update the dict"""
#         dictionary[word] = dictionary.get(word, 0) + 1
#         # print(word, dictionary[word])
#         # -------------------------------------
#         # if word in dictionary:
#         #     dictionary[word] += 1
#         #     # print("--------------**Exists**-------------------")
#         # else:
#         #     dictionary[word] = 1
#         #     # print("--------------**New**-------------------")
#         # # print(dictionary[word])
#         # print(word, dictionary[word])

# # print(dictionary)

# # --------------- most common word ---------------
# # largest = -1
# largest = None
# the_word = None
# for key, value in dictionary.items():
#     if largest is None:
#         largest = value
#     # print(key, value)
#     elif value > largest:
#         largest = value
#         the_word =key

# print("max word count is: ", the_word, largest)

# ============================== Tuples ===========================
"""
to tuple age az sort estefade konim faghat Key o sort mikone na Value ha ro ..
bayad az function e sorted() estefade konim...

"""

# a_dict = {'a':10, 'b':1, 'c':22}
# temp = list()
# for k, v in a_dict.items():
#     temp.append((v, k)) # bar assasse tuple ke value avvale o key dovvom to ye list mizarim

# # print(temp)
# temp = sorted(temp, reverse=True)
# print(temp)
# the_max = temp[0]
# print("The maximum number is: ", the_max)

# ------------ dakhele file ----------------------
# fhand = open('text.txt')
# count = dict()
# for line in fhand:
#     words = line.split()
#     for word in words:
#         count[word] = count.get(word, 0) +1

# ----------------------------------------
# my_list = list()
# for key, value in count.items():
#     new_tuple = (value, key)
#     my_list.append(new_tuple)
# # for key_value in count.items():
#     # my_list.append(key_value)

# my_list = sorted(my_list, reverse=True)
# for val, key in my_list[:10]:
#     print(key, val) # to inja jaye key o value o ro avaz mikonim
# print(my_list)

# ------------- ya -----------------
# x = sorted([(value, key) for key, value in count.items()], reverse=True)[:10]
# for i in x:
#     print(i)
# # idks = [_ for _ in sorted([(value, key) for key, value in count.items()], reverse=True)[:10]]
# # for idk in idks:
#     # print(idk)
# -----------------------------------------------------

# fname = input("Enater File name: ")
# if len(fname) < 1:
#     fname = 'text.txt'

# hand = open(fname)
# dictionary = dict()

# for line in hand:
#     lin = line.rstrip()
#     words = lin.split()
#     for word in words:
#         """ get or/and update the dict"""
#         dictionary[word] = dictionary.get(word, 0) + 1

# # print(dictionary)

# # x = sorted(dictionary.items(), reverse=True)
# # print(x[:10])
# temp = list()
# for k, v in dictionary.items():
#     new_tuple = (v, k)
#     # print(new_tuple)
#     temp.append(new_tuple)
# temp = sorted(temp, reverse=True)
# for v, _ in temp[:10]:
#     print(v, _)


# ======================== socket programming ===============================

# import socket
# mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysocket.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode() # encode unicode haye python o tabdil be UTF-8 mikone
# mysocket.send(cmd)


# while True:
#     data = mysocket.recv(512)
#     if (len(data) < 1):
#         break
#     print(data.decode()) # to inja UTF-8 tabdil mishe be unicode
# mysocket.close()

# ----------------------- behtar az socket urllibe ---------------------------

# from urllib import request, parse, error

# fhand = request.urlopen('http://data.pr4e.org/romeo.txt') # inja automatic encode mikone
# for line in fhand: # inja header o barnemigardoone 
#     print(line.decode().strip())

# =================== web services ===============?
# ------------------ XML ------------------------------
# import xml.etree.ElementTree as ET
# # data = """
# #     <person>
# #         <name>Rek'sai</name>
# #         <phone type="intl">
# #             09226996207
# #         </phone>
# #         <email hide="yes"/>
# #     </person>
# # """
# data = """
#     <stuff>
#         <users>
#             <user x="2">
#                 <name>Rek'sai</name>
#                 <id>004</id>
#             </user>
#             <user x="7">
#                 <name>Mamad</name>
#                 <id>009</id>
#             </user>
#         </users>
#     </stuff>
# """

# # tree = ET.fromstring(data)
# # print("Name: ", tree.find('name').text)
# # print("phone: ", tree.find('phone').text)
# # print("Attr: ", tree.find('email').get('hide'))


# tree = ET.fromstring(data)
# lst =  tree.findall('users/user')
# print("User count: ", len(lst))

# for item in lst:
#     print("Name: ", item.find('name').text)
#     print("Id: ", item.find('id').text)
#     print("Attribute: ", item.get('x'), '\n')

# ====================== Json ===========================

# -------------------- web services -----------------------------

# import json
# data = """
#     {
#         "name" : "Rek'sai",
#         "phone" : {
#             "type" : "intl",
#             "number" : "09226996207"
#         },
#         "email" : {
#             "hide" : "yes"
#         }
#     }
# """

# info = json.loads(data) # info alan ye dict e
# print("Name:" , info['name'])
# print("Hide:" , info['email']['hide'])

# -------------------------

# import json
# data = """
#     [
#         {
#         "id" : "001",
#         "name" : "Rek'sai",
#         "x" : "2",
#         "phone" : {
#             "type" : "intl",
#             "number" : "09226996207"
#             }
#         },
#         {
#         "id" : "001",
#         "name" : "Mahdi",
#         "x" : "5",
#         "phone" : {
#             "type" : "intl",
#             "number" : "09226996207"
#             }
#         }
#     ]
# """

# info = json.loads(data) # info alan ye dict e
# print("User count: ", len(info), "\n")
# for item in info:
#     print("Name: " , item['name'])
#     print("Id: " , item['id'])
#     print("Attribute: " , item['x'])


# ----------------- service Oriented Approch --------------------

# -------- Google map API --------------

# import urllib.request, urllib.parse, urllib.error
# import json

# serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

# while True:
#     address = input("Enter Location: ")
#     if len(address) < 1:
#         break
#     url = serviceurl + urllib.parse.urlencode(
#         {'address': address}
#     )
#     print("Retriving ", url)
#     uh = urllib.request.urlopen(url)
#     # headers = dict(uh.getheaders())
#     data = uh.read().decode()
#     print("Retrieve ", len(data), "Characters")

#     try:
#         js = json.loads(data)
#     except:
#         js = None

#     if not js or 'status' not in js or js['status'] != 'OK': # age js None bud YA 'status' to js nabud YA js['status'] != 'OK' bud ...
#         print('======= Failure to retrieve ========')
#         print(data)
#         continue

#     print(json.dumps(js, indent=4))

#     lat = js['results'][0]['geometry']['location']['lat']
#     lng = js['results'][0]['geometry']['location']['lng']
#     print('lat', lat, 'lng', lng)
#     location = js['results'][0]['formated_address']


# -----------------------------------------------------------

# ====================== Python Objects (OOP) =====================
# ====================== Data structurs ===========================

# class PartyAnimal(object):
#     x = 0
#     def party(self):
#         self.x += 1
#         print("So far: ", self.x)


# animals = PartyAnimal()
# animals.party()

# print(dir(PartyAnimal))

# --------------- Object life cycle -----------------------

# class PartyAnimal(object):
#     x = 0

#     def __init__(self):
#         print("I am the setter")


#     def party(self):
#         self.x += 1
#         print("So far: ", self.x)

#     def __del__(self):
#         print("Iam the Deleter ", self.x)


# animals = PartyAnimal()
# animals.party()
# animals.party()
# animals = 42
# print("animals now is : ", animals)

# -----------------------------

# class PartyAnimal(object):
#     x = 0
#     name = "" # ino mishe guzasht mishe nazasht

#     def __init__(self, z):
#         self.name = z
#         print(self.name, "sakhte shud")


#     def party(self):
#         self.x += 1
#         print(self.name, "Party count: ", self.x)

# s = PartyAnimal("Cat")
# s.party()

# d = PartyAnimal("Dog")
# d.party()
# s.party()

# --------------- Inharitance ------------------

# class PartyAnimal(object):
#     x = 0
#     name = "" # ino mishe guzasht mishe nazasht

#     def __init__(self, z):
#         self.name = z
#         print(self.name, "sakhte shud")


#     def party(self):
#         self.x += 1
#         print(self.name, "Party count: ", self.x)


# class FootballFan(PartyAnimal):
#     points = 0

#     def touchdown(self):
#         self.points = self.points + 7
#         self.party()
#         print(self.name, "Points: ", self.points)

# j = FootballFan("Jim")
# j.party()
# j.touchdown()
# j.touchdown()

# ===================== databases SQLLite ====================

# import sqlite3
# conn = sqlite3.connect('emaildb.sqlite')
# cur = conn.cursor()

# cur.execute("""
# DROP TABLE IF EXISTS Counts
# """)

# cur.execute("""
# CREATE TABLE Counts (email TEXT, count INTEGER)
# """)

# fname = input("Enter file name: ")
# if (len(fname) < 1):
#     fname = 'text.txt'
 
# fh = open(fname)
# for line in fh:
#     if not line.startswith('Lorem '):
#         continue
#     pieces = line.split()
#     email = pieces[1]

#     cur.execute('SELECT count FROM Counts WHERE email = ?', (email,)) # ? messe placeholder e
#     row  = cur.fetchone() # avvalin info ro az database begir
#     if row is None:
#         cur.execute("""INSERT INTO Counts (email, count)
#             VALUES (?, 1)""", (email,))
#     else:
#         cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email,))

#     conn.commit() # inja az ram mirize to hard

# sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

# for row in cur.execute(sqlstr):
#     print(str(row[0]), row[1])

# cur.close()

# ======================================================================
# ---------------------- final chapter everything ----------------------
# ======================================================================


# get_email = 'lordofhell225@gmail.com'
# email = get_email.split('@')[0]
# print(email)
# # if instance.__class__.objects.filter(username=set_email).exists():
# #     instance.username = set_email + '_' + str(instance.id)
# # instance.username = set_email


# ======================================================================
# ------------------------- Udemy python -------------------------------
# ======================================================================

# =============== set comprehension ================

# x = set(i*2 for i in range(4) if i%2 == 0)
# x = set(i for i in [1, 2, 3, 4] if i%2 == 0)
# x = set((a, b) for b in range(3) for a in range(4))
# print(x)

# ================ Dictionary comprehension =========

# mydict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# x = [i for i in mydict.keys()]
# y = [i for i in mydict.values()]
# z = [i for i in mydict.items()]
# # print(x, y, z)
# new = {k*2:v*2 for (k,v) in mydict.items()} # to dict comprehension avval e khat e loop bayad beine key va value hatman : bashe
# print(new)

# # -------------------------------

# mydict = {}
# for i in range(10):
#     if i%2 == 0:
#         mydict[i] = i ** 2

# print(mydict)
# # -------- ya ----------------------
# new_dict = {i:i**2 for i in range(10) if i%2 == 0}
# print(new_dict)
# # -------------------------------

# mydict = {'temp1': 10, 'temp2': 20, 'temp3': 30, 'temp4': 40}
# cel = list(map(lambda x: (float(5)/9)*(x-32), mydict.values() ))
# cel_dict = dict(zip(mydict.keys(), cel))
# print(cel_dict)
# # --------- ya--------------------------
# mydict = {'temp1': 10, 'temp2': 20, 'temp3': 30, 'temp4': 40}
# cel_dicts = {k:(float(5)/9)*(v-32) for k,v in mydict.items()}
# print(cel_dicts)

# ------------- if statemnet -------------

# mydict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

# # new_dict = {k:v for k,v in mydict.items() if v > 2}
# # new_dict = {k:v for k,v in mydict.items() if v%2 == 0}
# new_dict = {k:('even num' if v%2 == 0 else 'odd nem') for k,v in mydict.items()}
# print(new_dict)

# # ----------------------------------
# mydict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

# new_dict = {k:v for k,v in mydict.items() if v > 3 if v%2 == 0} # bejaye if e dovvom mishe and ya or guzasht
# print(new_dict)

# # ------------------ nested dictionary -------------
# mydict = {'one':{'sub_one': 10}, 'two': {'sub_two': 20}, 'three':{'sub_three': 30}, 'four': {'sub_four': 40}}

# for (external_key, external_value) in mydict.items():
#     for (internal_key, internal_value) in external_value.items():
#         # print(internal_key, internal_value)
#         external_value.update({internal_key: float(internal_value)})

# # mydict.update({external_key: external_value}) # ino to amoozesh guzashte bud nemidonam chera ... bedoone ina m javab hamoone
# print(mydict)

# ======================== Meta programming ===============================
# ========================== (decorators) ======================
""" ye function ya class ke function ya class ye dg ro mitune edit kone"""

# ----------- fucntion decorators ---------------

# def outside_func():
#     def inside_func():
#         print('I am the inside function')
#         # outside_func() # nemishe func e out o dakhele func e in seda zad

#     print('I am the outside function')
#     inside_func()


# outside_func()

# -----------------------

# def addition(a, b):
#     def add(x, y):
#         return x + y
#     sum = f"the sum of {a} and {b} is: " + str(add(a, b))
#     return sum


# print(addition(3, 5))

# -------- mesal e asli -------

# def x(function):
#     print("I am the function x")


# @x
# def y():
#     print("I am the fucntion y")

# x(y()) # avval dakhele x ejaramishe baad khude x

# -------------------------------
# def x(function):
#     print("I am the function x")
#     return function


# @x
# def y():
#     print("I am the fucntion y")

# y()
# -----------------------

# from functools import wraps

# def get_class_for(the_class=None)
#     def get_or_create_for_auth_and_anon(function):
#         @wraps(function)
#         def args_for_func(request, instance, likedislike):
#             ip_address = get_client_ip(request)
#             content_type = ContentType.objects.get_for_model(instance.__class__())
#             if request.user.is_authenticated:
#                 try:
#                     queryset = the_class.objects.get(
#                         ip_address=ip_address,
#                         content_type=content_type,
#                         object_id=instance.id
#                     )
#                 except the_class.DoesNotExist:
#                     queryset = the_class.objects.create(
#                         user=request.user,
#                         ip_address=ip_address,
#                         content_type=content_type,
#                         object_id=instance.id,
#                         likedislike=likedislike
#                     )
#             else:
#                 try:
#                     queryset = the_class.objects.get(
#                         ip_address=ip_address,
#                         content_type=content_type,
#                         object_id=instance.id
#                     )
#                 except the_class.DoesNotExist:
#                     queryset = the_class.objects.create(
#                         ip_address=ip_address,
#                         content_type=content_type,
#                         object_id=instance.id,
#                         likedislike=likedislike
#                     )
#             return queryset
#         return args_for_func
#     return get_or_create_for_auth_and_anon


# ---------------------
# def poly(a, b, c):
#     def pol(x):
#         return a*x**2 + b*x + c
#     return pol


# outer = poly(1, 2, 3)
# inner = outer(4)
# print(inner)

# --------------------

# def outer_func(a):
#     def inner_func(b):
#         return a + b
#     return inner_func

# def repeatabel(myarg, other):
#     x = outer_func(other)
#     d = x(myarg)
#     print(d)

# repeatabel(2, 5)
# repeatabel(3, 5)
# repeatabel(5, 5)

# ---------------------------

# def add_more(func):
#     func.data = 2
#     # def args(c):
#     return func




# def add(x, y):
#     return x + y + add.data
 
# add_more(add)
# c = add(5, 4)
# print(c)


# -------------------------------

# def x(a):
#     def y(b):
#         # print(type(a))
#         if type(a) is int or type(b) is not int:
#             print("not Valid input")
#         else:
#             return a + str(b)
#     return y

# def repeatable(a, b):
#     c = x(a)
#     d = c(b)
#     print(d)

# repeatable("hello ", 24)

# ------------- class decorators ---------------

# ------------------ Meta classes --------------------

# class x:
#     pass

# x.variable  = 10

# c = x()
# print(c.variable)

# ---------------------

# def meta_func():
#     print("I am the metaclass function")


# class inharit:
#     def func(self):
#         print("I am inharited method")

# my_metaobject = type('meta', (inharit,), dict(name="Mahdi", meta_function=meta_func()))
# # print(type(my_metaobject))

# b = my_metaobject()
# # print(type(b))
# b.func()
# print(b.name)

# ============================================================
# ======================= new on laptop ======================
# ============================================================


# ---------------- enumerate --------------------------
'''
ye tuple az list ya dict migire ba index esh pas mide
bara dict key ro pas nemide faghat be tedade key ha addad mizare
'''
# example = ['left', 'right', 'down', 'up']
# example2 = {'a': 'mahdi', 'b': 'mamad', 'c': 'kazem'}
# # for i in range(len(example)):
# #     print(i, example[i])

# for x, y in enumerate(example):
#     print(x, y)

# # to khat e paein list o tabdil mikone be dict baad index a ro be onvane key darnazar migire
# new_dict = dict(enumerate(example))
# print(new_dict)

# --------------------- handling errors----------------------------
"""hich vaght chizi to variable to exception zakhire nakon"""

# import sys
# import logging

# def error_handling():
#     return f"{sys.exc_info()[0]}. ({sys.exc_info()[1]}), in Line {sys.exc_info()[2].tb_lineno}"

# try:
#     a + b
# except Exception as e:
#     logging.error(error_handling())
#     # print(sys.exc_info()[0])
#     # print(sys.exc_info()[1])
#     # print(sys.exc_info()[2].tb_lineno)




# -------------- OOP ----------------

# class Singleton:
#     __instance = None
#     def __init__(self):
#         if not  Singleton.__instance:
#             print("mikhayn obj ro ijad konim")
#         else:
#             print("obj ghablan ijad shude", self.getinstance)
#     def __new__(cls):
#         if not hasattr(cls, 'instance'):
#             cls.instance = super().__new__(cls)
#         return cls.instance


# s1 = Singleton()
# print(s1)
# s2 = Singleton()
# print(s2)

# ------------------------------------------------------

# test = [10, 2, 5, 10, 1, 5, 10]

# def number_of(list, element):
#     c = 0
#     for e in list:
#         if e != element:
#             continue
#         c += 1
#     return c

# print(number_of(test, 5))

# ------------------- reverse kardane string --------------------------------

# a = 'abc'

# def reverse(string):
#     result = ""
#     for c in string:
#         result = c + result
    
#     return result

# print(reverse(a))


# =================================================================================================================

# =================================================================================
# ================================= Design patterns ===============================
# =================================================================================

# import abc

# class MyABC(metaclass=abc.ABCMeta):
#     pass

#     @abc.abstractmethod
#     def do_somthing(self, value):
#         pass

#     @abc.abstractproperty
#     def some_property(self, value):
#         pass


# -------------------------------------------------------------------------------

# -------------------- Factory Pattern ----------------------
"""
to raveshe interface faghat method a inharet mishan 
amma to abstractbase ha attribute ham inharet mishe
"""

# ---------- Factory Pattern -------------

# class ShapeInterface:
#     def draw(self): pass

# class Circle(ShapeInterface):
#     def draw(self):
#         print("Circle.draw")

# class Square(ShapeInterface):
#     def draw(self):
#         print("Square.draw")


# class ShapeFactory:
#     @staticmethod
#     def get_shape(type):
#         if type == 'circle':
#             return Circle()
#         elif type == 'square':
#             return Square()
#         assert False, "Could not find shape "


# shape = ShapeFactory()
# f = shape.get_shape('circle')
# f.draw()
# s = shape.get_shape('tringle')
# s.draw()
# print(f)

# ----------- abstract base factory pattern -------------

# # ===== abstract shape classes =====
# class Shape2DInterface:
#     def draw(self): pass

# class Shape3DInterface:
#     def build(self): pass

# # ===== concrete shape classes =====
# class Circle(Shape2DInterface):
#     def draw(self):
#         print("Circle.draw")

# class Square(Shape2DInterface):
#     def draw(self):
#         print("Square.draw")

# class Sphere(Shape3DInterface):
#     def build(self):
#         print("Sphere.build")

# class Cube(Shape3DInterface):
#     def build(self):
#         print("Cube.build")

# # ===== abstract shape factory ====
# class ShapeFactoryInterface:
#     @staticmethod
#     def get_shape(sides): pass


# # ====== concrete shape factories =====

# class Shape2DFactory(ShapeFactoryInterface):
#     @staticmethod
#     def get_shape(sides):
#         if sides == 1:
#             return Circle()
#         if sides == 4:
#             return Square()
#         assert False, "bad 2D shape creation shape not define for " + sides + "faces"

# class Shape3DFactory(ShapeFactoryInterface):
#     @staticmethod
#     def get_shape(sides):
#         if sides == 1:
#             return Sphere()
#         if sides == 6:
#             return Cube()
#         assert 0, "bad 3D shape creation: shape not define for "+ sides + "faces"



# D2shape = Shape2DFactory()
# D2shape.get_shape(1).draw()

# D3shape = Shape3DFactory()
# D3shape.get_shape(6).build()


# ----------- builder pattern -------------

# class Car:
#     def __init__(self):
#         self.__wheels = list()
#         self.__engine = None
#         self.__body = None

#     def setBody(self, body):
#         self.__body = body

#     def attachWheel(self, wheel):
#         self.__wheels.append(wheel)

#     def setEngine(self, engine):
#         self.__engine = engine

#     def specification(self):
#         print(f"body: {self.__body.shape}")
#         print(f"engine horsepower: {self.__engine.horsepower}")
#         print(f"tire size: {self.__wheels[0].size}")

    

# # ==== Car parts ====

# class Wheel:
#     size = None

# class Engine:
#     horsepower = None

# class Body:
#     shape = None

# class Director:
#     __builder = None

#     def setBuilder(self, builder):
#         self.__builder = builder

    
#     # the algorithm for assembeling car
#     def getCar(self):
#         car = Car()

#         #body
#         body = self.__builder.getBody()
#         car.setBody(body)

#         #engine
#         engine = self.__builder.getEngine()
#         car.setEngine(engine)

#         # 4 wheels
#         i = 0
#         while i < 4:
#             wheel = self.__builder.getWheel()
#             car.attachWheel(wheel)
            
#             i += 1
        
#         return car


# class BuilderInterface:
#     def getWheel(self): pass
#     def getEngine(self): pass
#     def getBody(self): pass


# class JeepBuilder(BuilderInterface):
#     def getWheel(self):
#         wheel = Wheel()
#         wheel.size = 22
#         return wheel

#     def getEngine(self):
#         engine = Engine()
#         engine.horsepower = 400
#         return engine

#     def getBody(self):
#         body = Body()
#         body.shape = "SUV"
#         return body


# class NeisanBuilder(BuilderInterface):
#     def getWheel(self):
#         wheel = Wheel()
#         wheel.size = 16
#         return wheel

#     def getEngine(self):
#         engine = Engine()
#         engine.horsepower = 100
#         return engine

#     def getBody(self):
#         body = Body()
#         body.shape = "hatchback"
#         return body



# d = Director()
# d.setBuilder(JeepBuilder())
# print(d.getCar())
# d.getCar().specification()


# ----------- prototype pattern -------------

# from copy import deepcopy

# class Car:
#     def __init__(self):
#         self.__wheels = list()
#         self.__engine = None
#         self.__body = None

#     def setBody(self, body):
#         self.__body = body

#     def attachWheel(self, wheel):
#         self.__wheels.append(wheel)

#     def setEngine(self, engine):
#         self.__engine = engine

#     def specification(self):
#         print(f"body: {self.__body.shape}")
#         print(f"engine horsepower: {self.__engine.horsepower}")
#         print(f"tire size: {self.__wheels[0].size}")

#     def clone(self):
#         return deepcopy(self)

    

# # ==== Car parts ====

# class Wheel:
#     size = None

# class Engine:
#     horsepower = None

# class Body:
#     shape = None

# class Director:
#     __builder = None

#     def setBuilder(self, builder):
#         self.__builder = builder

    
#     # the algorithm for assembeling car
#     def getCar(self):
#         car = Car()

#         #body
#         body = self.__builder.getBody()
#         car.setBody(body)

#         #engine
#         engine = self.__builder.getEngine()
#         car.setEngine(engine)

#         # 4 wheels
#         i = 0
#         while i < 4:
#             wheel = self.__builder.getWheel()
#             car.attachWheel(wheel)
            
#             i += 1
        
#         return car


# class BuilderInterface:
#     def getWheel(self): pass
#     def getEngine(self): pass
#     def getBody(self): pass


# class JeepBuilder(BuilderInterface):
#     def getWheel(self):
#         wheel = Wheel()
#         wheel.size = 22
#         return wheel

#     def getEngine(self):
#         engine = Engine()
#         engine.horsepower = 400
#         return engine

#     def getBody(self):
#         body = Body()
#         body.shape = "SUV"
#         return body


# class NeisanBuilder(BuilderInterface):
#     def getWheel(self):
#         wheel = Wheel()
#         wheel.size = 16
#         return wheel

#     def getEngine(self):
#         engine = Engine()
#         engine.horsepower = 100
#         return engine

#     def getBody(self):
#         body = Body()
#         body.shape = "hatchback"
#         return body

# d = Director()
# d.setBuilder(JeepBuilder())
# jeep = d.getCar()
# jeep.specification()
# jeep2 = jeep.clone()
# jeep2.specification()

# -------------------------------

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __str__(self):
#         print(f"{self.x}, {self.y}")

#     def move(self, x, y):
#         self.x += x
#         self.y += y

#     def clone(self, move_x, move_y):
#         obj = deepcopy(self)
#         obj.move(move_x, move_y)

#         return obj


# p0 = Point(0, 0)
# p1 = p0.clone(1, 1)
# p1.__str__()

# =================== singleton and bolg patterns ===================

# class Singleton:
#     __instance = None
#     # @classmethod
#     def __new__(cls, val=None):
#         if Singleton.__instance is None:
#             Singleton.__instance = object.__new__(cls)
#         Singleton.__instance.val = val
#         return Singleton.__instance

# x = Singleton()
# x.val = "burger"
# print(x.val)

# y = Singleton()
# y.val = "susise"
# print(y.val)
# print(x.val)
# print(x == y)

# -------------------------------

# class Borg:
#     __share_state = {}
#     def __init__(self):
#         self.__dict__ = self.__share_state


# a = Borg()
# b = Borg()

# a.val = "milkshake"
# print(b.val)

# ========================= Stractur pattern =================

# ------------------ Facad ------------------

# class Engine:
#     def __init__(self):
#         self.spin = 0

#     def start(self, spin):
#         self.spin = min(spin, 3000)

# class StarterMotor:
#     def __init__(self):
#         self.spin = 0

#     def start(self, charge):
#         # if there is enough power then spin fast
#         if (charge > 50):
#             self.spin = 2500

# class Battery:
#     def __init__(self):
#         self.charge =0

# class Car:
#     # the facad obj that deals with battery, engine, startermotor
#     def __init__(self):
#         self.battery = Battery()
#         self.starter = StarterMotor()
#         self.engine = Engine()


#     def turn_key(self):
#         self.starter.start(self.battery.charge)
#         self.engine.start(self.starter.spin)
#         if self.engine.spin > 0:
#             print("Engine started")
#         else:
#             print("Engine Not started")

#     def jump(self):
#         self.battery.charge = 100
#         print("Jumped")


# c = Car()
# c.turn_key()
# c.jump()
# c.turn_key()

# ------------- proxy -------------------

# class SubjectInterface:
#     """
#     define a common interface for REalSubject and Proxy so that a
#     proxy can be used anywhere a RealSubject is expencted
#     """

#     def request(self): pass



# class Proxy(SubjectInterface):
#     def __init__(self, real_subject):
#         self._real_subject = real_subject

#     def request(self):
#         print("proxy may be doing something, like contorlling request access")
#         self._real_subject.request()


# class RealSubject(SubjectInterface):
#     def request(self):
#         print("the real thing is dealing with the request")



# rs = RealSubject()
# rs.request()
# proxy = Proxy(rs)
# proxy.request()

# --------------------------

# class Blog:
#     def read(self):
#         print("read the blog")

#     def write(self):
#         print("write the blog")

# class Proxy:
#     def __init__(self, target):
#         self.target = target

#     def __getattr__(self, attr):
#         return getattr(self.target, attr)

# class AnonUserBlogProxy(Proxy):
#     def __init__(self, blog):
#         super().__init__(blog)

#     def write(self):
#         print("Only authorized users can write blog posts")


# blog = Blog()
# blog.write()
# proxy = AnonUserBlogProxy(blog)
# proxy.write()

# ----------------- Decorator ---------------------

# class WindowInterface:
#     def build(self): pass

# class AbstaractWindowDecorator(WindowInterface):

#     def __init__(self, window):
#         self._window = window

#     def build(self): pass

# class Window(WindowInterface):
#     def build(self):
#         print("Building window")

# class BorderDecorator(AbstaractWindowDecorator):
#     def add_border(self):
#         print("Adding border")

#     def build(self):
#         self.add_border()
#         self._window.build()


# class VerticalSBDecorator(AbstaractWindowDecorator):
#     def add_vertical_scroll_bar(self):
#         print("adding Vertiacal Scroll bar")        
    
#     def build(self):
#         self.add_vertical_scroll_bar()
#         self._window.build()

# class HorizantalSBDecorator(AbstaractWindowDecorator):
#     def add_horizantal_scroll_bar(self):
#         print("adding horizantal scroll bar")

#     def build(self):
#         self.add_horizantal_scroll_bar()
#         self._window.build()


# w = Window()
# # w.build()
# wb = BorderDecorator(w)
# # wb.build()
# vsb = VerticalSBDecorator(wb)
# # vsb.build()
# hsb = HorizantalSBDecorator(vsb)
# hsb.build()

# -------------- Adapter --------------------------------------

# # adapter source interface
# class EuropeanSocketInterface:
#     def voltage(self): pass
#     def live(self): pass
#     def neutral(self): pass
#     def earth(self): pass

# # target interface
# class USASocketInterface:
#     def voltage(self): pass
#     def live(self): pass
#     def neutral(self): pass

# #adapter
# class EuropeanSocket(EuropeanSocketInterface):
#     def voltage(self):
#         return 230

#     def live(self):
#         return 1

#     def neutral(self):
#         return -1

#     def earth(self):
#         return 0


# # Client
# class AmericanKettle:
#     __power = None

#     def __init__(self, power):
#         self.__power = power

#     def boil(self):
#         if self.__power.voltage() > 110:
#             print("Kettle on fire")
#         else:
#             if self.__power.live() == 1 and self.__power.neutral() == -1:
#                 print("Coffee time")
#             else:
#                 print("No Power...")


# class Adapter(USASocketInterface):
#     __socket = None

#     def __init__(self, socket):
#         self.__socket = socket

#     def voltage(self):
#         return 110

#     def live(self):
#         return self.__socket.live()

#     def neutral(self):
#         return self.__socket.neutral()
                

# socket = EuropeanSocket()
# kettle = AmericanKettle(socket)
# kettle.boil()
# adaptor = Adapter(socket)
# kettle = AmericanKettle(adaptor)
# kettle.boil()

# =============== Command pattern ==========

# class Screen(object):
#     def __init__(self, text=""):
#         self.text = text
#         self.clip_board = ""

#     def cut(self, start=0, end=0):
#         self.clip_board = self.text[start:end]
#         self.text = self.text[:start] + self.text[end:]

#     def paste(self, offset=0):
#         self.text = self.text[:offset] + self.clip_board + self.text[offset:]

#     def clear_clipboard(self):
#         self.clip_board = ""

#     def length(self):
#         return len(self.text)

#     def __str__(self):
#         return self.text


# # Screen command interface
# class ScreenCommand:
#     def __init__(self, screen):
#         self.screen = screen
#         self.previous_state = screen.text

#     def execute(self): pass

#     def undo(self): pass


# class CutCommand(ScreenCommand):
#     def __init__(self, screen, start=0, end=0):
#         super().__init__(screen)
#         self.start = start
#         self.end = end

#     def execute(self):
#         self.screen.cut(start=self.start, end=self.end)

#     def undo(self):
#         self.screen.clear_clipboard()
#         self.screen.text = self.previous_state


# class PaseCommand(ScreenCommand):
#     def __init__(self, screen, offset=0):
#         super().__init__(screen)
#         self.offset = offset

#     def execute(self):
#         self.screen.paste(offset=self.offset)

#     def undo(self):
#         self.screen.clear_clipboard()
#         self.screen.text = self.previous_state


# class ScreenInvoker:
#     def __init__(self):
#         self.history = list()

#     def store_and_execute(self, command):
#         command.execute()
#         self.history.append(command)

#     def undo_last(self):
#         if self.history:
#             self.history.pop().undo()



# screen = Screen("hello world")
# print(screen.__str__())
# cut = CutCommand(screen, start=5, end=11)
# client = ScreenInvoker()
# client.store_and_execute(cut)
# print(screen.__str__())
# paste = PaseCommand(screen, offset=0)
# client.store_and_execute(paste)
# print(screen.__str__())
# client.undo_last()
# print(screen.__str__())


# ================ Interpreter pattern ===========

























# ================================================================================================
# ======================================== Zero to Mastery =======================================
# ================================================================================================

# user = {
#     'name': "Golem",
#     'age': "22",
#     'can_swim': False
# }

# for item in enumerate(user.items()):
#     key, value = item
#     print(key, value)

# #  --------------- exercise ----------------

# mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]

# x = sum(u for u in mylist)
# print(x)

# g = 0
# for y in mylist:
#     g += y
# print(g)

 
# #  --------------- exercise ----------------

# picture = [
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 1, 1, 1, 0, 0],
#     [0, 1, 1, 1, 1, 1, 0],
#     [1, 1, 1, 1, 1, 1, 1],
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 0, 1, 0, 0, 0]
# ]

# for lst in picture:
#     for i in lst:
#         if not i: # yani i == 0
#             print(" ", end="")
#         else:
#             print("*", end="")
#     print('') # need a new line after new row( ya hamoon lst )

# --------------- developer fundemental ------------------

# mylist = ['a', 'b', 'c', 'b', 'm', 'n', 'n']

# temp = list()
# for x in mylist:
#     if mylist.count(x) > 1:
#         temp.append(x)
#         for y in temp:
#             if temp.count(y) > 1:
#                 temp.remove(y)

# print(temp)

# # --------------- ya ---------------------

# temp = list()
# for x in mylist:
#     if mylist.count(x) > 1:
#         if x not in temp:
#             temp.append(x)

# print(temp)

# ============= Functions ============
    
# def myFunction(parameter, default_parameter='Heh'):
#     print(f"Hello {parameter}, {default_parameter}")

# myFunction('Positional argument')
# myFunction(parameter ='Keyword argument')

# -----------------------

# def mySum(num1, num2):
#     the_sum = num1 + num2
#     return f"{num1} + {num2} = {the_sum}"

# print(mySum(1, 2))

# ---------- DocStrings -------------

# def test(a):
#     """this is a fucking test"""
#     print(a)

# print(test.__doc__)
# test("@.@")

# ------------ Clean Code -------------

# def is_even(num):
#     # if num % 2 == 0:
#     #     return True
#     # else:
#     #     return False
#     return num % 2 == 0

# print(is_even(24))

# -------- *args **kwargs -----------
##             params, *args, default params, **kwargs
# def super_func(name, *args, age=22, **kwargs):
#     for key, values in kwargs.items():
#         print(f"{key}: {values}")
#     return sum(args)

# print(super_func(1,2,3,4,5, firstName="Mehdi", lastName="Asadnejad"))

# ---------- exercise -------------

# def highest_even(li):
#     highest = None
#     for num in li:
#         if num % 2 == 0:
#             if highest is None:
#                 highest = num
#             elif num > highest:
#                 highest = num
#     return highest
#     # ---- ya -----
#     # return max(highest)


# print(highest_even([10, 2, 4, 5, 11, 8]))

# ---------------- global kwargs -------------
# total = 0

# def count():
#     global total # avval bayad to func taarifesh konim baad be unvane variable azash estefade konim
#     total += 1
#     return total

# count()
# count()
# print(count())

# ---------- nonlocal ----------------

# def outer():
#     x = "local"
#     def inner():
#         nonlocal x # variable func e parent o migire
#         x = "nonlocal" # alan local e outer shude nonlocal
#         print("inner: ", x)
#     inner()
#     print("outer: ", x) # to 3 khate bala x taghir karde

# outer()


# =================== OOP ===============

# class PlayerCharacter(object):
#     # class object attribute( ke static e)
#     membership = True
#     def __init__(self, name, age):
#         if self.membership: # bara membership chun class attribute mishe injuri nvsht: PlayerCharacter.membership
#             self.name = name 
#             self.age = age
    
#     @staticmethod # vaghti az in estefade mikonim ke nakhaim az attribute haye __init__ estefade konim
#     def run(num1, num2):
#         return num1 + num2

#     @classmethod # ba in decorator mishe bedoone taeen kardane object(instance) be class sedash zad
#     def adding(cls, num1, num2):
#         return cls('mamad', num1+num2) # in khat engar : PlayerCharacter("mamad", 23)

# player3 = PlayerCharacter.adding(2, 4)
# print(player3.age)

# player1 = PlayerCharacter("Mehdi", 22)
# print(player1.run(1, 4), player1.name, player1.membership, player1.adding(1, 3))

# ==================== Functional Programming =======================
"""
to functional programming nabayad print i dakhele function bezarim
ya new_list nabayad biroon az function bashe
behtare Data ro birun az function taarif konim mesle wizard
"""

# wizard = {
#     'name': 'Merlin',
#     'power': 50
# }

# def multiply_by2(li, data):
#     new_list = list()
#     for i in li:
#         new_list.append(i * 2)

#     return new_list, data

# print(multiply_by2([1, 2, 4], wizard))

# ================= map, filter, zip, reduce =====================
# -------------------------- map ----------------------
"""
faghat baraye function haye iterable estefade mikonim map o.
vaghti az map estefade mikonim dg niazy nist dakhele function ye iterable o (list) vasash halghe for bnvisim
chun khude map iter mikone vorodi e function o ( ke masalan ye list e) yai done done mifreste dakhele function.
amma hatman bayad dakhele ye list map o taarif konim.
khude map ye list e jadid to hafeze misaze.
"""
# def multiply_by2(li):
#     # new_list = list()
#     # for i in li:
#     #     new_list.append(i * 2)

#     # return new_list
#     return li*2

# # print(multiply_by2([1, 2, 4]))
# print(list(map(multiply_by2, [1,2,4,5])))

# ---------------------- filter --------------------------
"""
filter am mesle map ye function migire va ye iterable mesle list.
filter bar assase True va False amal mikone to inja age item i ke 
pass dade taghsim bar 2 sefr nashud True bar migardoone va un addad
ro add mikone to list e jadid.
"""
# mylist = [1,2,3,4]

# def check_odd(item):
#     return item % 2 != 0

# print(list(filter(check_odd, mylist)))

# --------------------- Zip -------------------------------
"""
2 ta iterable ya list migire va ba ham zip mikone(unaei ke ham index hastan o kenar ham to ye tuple mizare baad to ye list add mikone)
"""

# mylist = [1,2,3,4]
# your_list = [10, 20, 30]
# their_list = (5, 4, 3)

# print(list(zip(mylist, your_list, their_list)))

# ----------------- reduse -------------------------------

# from functools import reduce

# mylist = [1,2,3,4]

# def accumlator(acc, item):
#     print(acc, item)
#     return acc + item

# print(reduce(accumlator, mylist, 0))

# ============== lambda expressions =====================

# from functools import reduce

# mylist = [1, 2, 3]

# # lambda parameter_list: action(parameter)

# print(list(map(lambda item: item * 2, mylist)))
# print(list(filter(lambda item: item % 2 != 0, mylist)))
# print(reduce(lambda acc, item: acc + item , mylist))

# ================ Decorators =========================

from functools import wraps

# def my_decorator(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print("***********")
#         func(*args, **kwargs)
#         print("***********")
#     return wrapper

# @my_decorator
# def greet(name):
#     print(f"Hello {name}")

# # a = hello(greet)
# # print(a)
# greet("Mahdi")

# ----------------------------------
# from time import time

# def performance(func):
#     def wrapper(*args, **kwargs):
#         start = time()
#         f = func(*args, **kwargs)
#         end = time()
#         print(f"it took: {end - start}")
#         return f
#     return wrapper



# @performance
# def long_time():
#     for i in range(100000000):
#         i * 5

# long_time()

# ======================= Error Handling ===================================

# try:
#     age = int(input("What is your age? "))
#     print(age)
# except ValueError:
#     raise ValueError("Please Enter a number")

# ----------------------------------------------------

# while True:
#     try:
#         username = int(input("Enter an age: "))
#         print(f"Your age is {username}")
#         10/username
#     except (TypeError, ValueError):
#         print("Enter a int as first letter")
#         # continue
#     except (ZeroDivisionError):
#         print("You cannot Enter 0 as age")
#     else:
#         break
#     finally:
#         print("Thank you for your time")

# ----------------------------------------------------

# def mysum(num1, num2):
#     try:
#         result = int(num1 + num2)
#     except TypeError as err:
#         print("Enter only numbers;", err)
#     else:
#         return result

# print(mysum("1", 2))

# ---------------------------------------------------------

# while True:
#     try:
#         username = int(input("Enter an age: "))
#         print(f"Your age is {username}")
#         10/username
#     except (TypeError, ValueError):
#         print("Enter a int as first letter")
#         # continue
#     except (ZeroDivisionError):
#         print("You cannot Enter 0 as age")
#     else:
#         break
#     finally:
#         print("Thank you for your time")

# ====================== Generators =================================

# def make_list(number):
#     result = list()
#     for i in number:
#         result.append(i*2)
#     yield result

# mlist = make_list(range(100000))
# y = [x for x in mlist]
# print(y)

# ----------------------------------------------------
"""
fibonachi ba yield
"""

# def fib(num):
#     a = 0
#     b = 1
#     for _ in range(num):
#         yield a
#         temp = a
#         a = b
#         b = temp + b
#         # yield b

# for x in fib(20):
#     print(x)
