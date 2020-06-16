import multiprocessing
import copy
import json

from datetime import timedelta
from time import time
from playsound import playsound
from Scripts.BotFunctions import runSemlar
from Scripts.rivenmarket import Rivenmarket
from itertools import chain

headless = False
max_processes = 1


def load_weapons():
    weapons = json.load(open('data/weapons/weapons.json', 'r'))
    return list(chain.from_iterable([weapons[weapon] for weapon in weapons]))


def main():
    start_time = time()
    pool = multiprocessing.Pool(max_processes)
    weapons = load_weapons()

    rmkt = Rivenmarket(headless)
    argslist = []
    for weapon in weapons:
        print("---Scanning " + weapon + "---")
        rmkt.loadWeapon(weapon)
        filename = weapon + ".csv"
        args = [headless, copy.deepcopy(rmkt.modlist), filename]
        argslist.append(args)
    rmkt.quit()

    pool.map(runSemlar, [*argslist])

    print("---DONE---")
    playsound("sound.wav")
    time_elapsed = time() - start_time
    print("Time Elapsed " + str(timedelta(seconds=time_elapsed)).split(".")[0])


if __name__ == '__main__':
    print(load_weapons())
