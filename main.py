import random
from time import sleep
import threading
memory = []
stop_reading_data = False
stop_odd_numbers = False


def reading_data():
    global memory
    global stop_reading_data
    f_1 = open('1.txt', 'r')
    str_one = f_1.read().split(',')
    for a in str_one:
        memory.append(eval(a))
    stop_reading_data = True


def odd_numbers():
    global stop_reading_data
    global memory
    global stop_odd_numbers


    while not stop_reading_data:
        pass

    print('Нечетные числа')

    for a in memory:
        if a % 2 != 0:
            print(a)
    stop_odd_numbers = True


def max_min_average():
    global stop_reading_data
    global memory
    global stop_odd_numbers

    while not stop_reading_data:
        pass

    average = 0

    #sum
    for i in memory:
        average += i

    average = average / len(memory)
    while not stop_odd_numbers:
        pass
    print("Max = ", max(memory))
    print("Min = ", min(memory))
    print("Average = ", average)


th_1 = threading.Thread(target=reading_data, )
th_2 = threading.Thread(target=odd_numbers, )
th_3 = threading.Thread(target=max_min_average, )

th_1.start()
th_2.start()
th_3.start()