import copy
import json
import multiprocessing
from itertools import chain

from playsound import playsound

from Scripts.BotFunctions import runSemlar
from Scripts.decorators import logtime
from Scripts.rivenmarket import Rivenmarket

headless = False
max_processes = 1


def load_weapons():
    weapons = json.load(open('data/weapons/weapons.json', 'r'))
    return list(chain.from_iterable([weapons[weapon] for weapon in weapons]))


@logtime
def main():
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
    playsound('data/sound/sound.wav')


if __name__ == '__main__':
    main()
