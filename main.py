from random import randint
from threading import Thread
import threading
import time

time_one = time.perf_counter()

lock = threading.Lock()


lts_one = [0 for i in range(0, 10)]
lts_two = [0 for j in range(0, 10)]


def ball(team):
    lock.acquire()

    lts_players = [[i + 1] for i in range(0, 10)]
    for a in lts_players:
        a.append(randint(0, 10) / 10)
    player = lts_players[randint(0, 9)]
    print("Игрок {} команды {} получил мяч".format(player[0], team+1))
    lock.release()
    return player


def football_team(thread):
    player = ball(thread)
    team = thread
    res = 0
    if 0 <= player[1] <= 0.30:
        print("Команда {}, игрок {} промазал ".format(team+1, player[0]))
    if 0.30 < player[1] <= 0.75:
        if randint(0, 1):
            print("Команда {}, игрок {} забил гол ".format(team+1, player[0]))
            res += 1
        else:
            print("Команда {}, игрок {} промазал ".format(team+1, player[0]))
    if 0.75 < player[1] <= 1:
        print("Команда {}, игрок {} забил год ".format(team+1, player[0]))
        res += 1
    if team == 0:
        lts_one[player[0]-1] += res
    else:
        lts_two[player[0]-1] += res


while True:

    th_1 = Thread(target=football_team, args=(0, ))
    th_2 = Thread(target=football_team, args=(1, ))
    th_1.start()
    th_2.start()
    th_1.join()
    th_2.join()

    time_two = time.perf_counter()
    if time_two - time_one >= 15:
        break

pl_1 = lts_one.index(max(lts_one))+1
pl_2 = lts_two.index(max(lts_two))+1
print("Лучший игрок из первой команды {} забил голов {}".format(pl_1, lts_one[pl_1-1]))
print("Лучший игрок из второй команды {} забил голов {}".format(pl_2, lts_two[pl_2-1]))