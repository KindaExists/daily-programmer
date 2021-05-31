
"""
[hard] challenge #2

Source / Reddit Post - https://www.reddit.com/r/dailyprogrammer/comments/pjsdx/difficult_challenge_2/
"""
from time import time

#! This is actually very easy, but i'm trying to make it really short
#! without using repetitive "if" statements

#! Will continue writing this later

t = 0
laps = []
def start(): print('START'); start = time(); laps.clear(); return start

def lap(start):
    new_t = get_TS(time(), sum((*laps, start)))
    laps.append(new_t)
    print(f'+{new_t}')
    return start

def stop(start):
    final_t = round(sum((*laps, get_TS(time(), start))), 3)
    print(final_t)
    with open('hard/2/log.txt', 'a') as f:
        f.write(f'Time: {final_t} | Laps: {[lap for lap in laps]}\n')
        f.close()

def get_TS(end, start): return round(end-start, 3)

if __name__ == "__main__":
    while True:
        print('1 | Start\n2 | Lap\n3 | Stop')
        user_in = input('> ')

        timer = {'1':lambda:start(), '2':lambda:lap(t), '3':lambda:stop(t)}
        if user_in not in timer.keys(): break
        else: t = timer[user_in]();