import os
import time


def everyDay():
    while True:
        os.system("bash gh_wall.sh")
        time.sleep(10800)


if __name__ == "__main__":

    everyDay()
