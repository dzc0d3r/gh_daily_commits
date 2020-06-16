import os
import time


def everyDay():
    while True:
        os.system("bash /home/m4dc0d3r/Documents/SCRIPTS/commit-every-day/gh_wall.sh")
        time.sleep(10800)


if __name__ == "__main__":

    everyDay()
