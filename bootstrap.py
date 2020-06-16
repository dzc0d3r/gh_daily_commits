import os
def everyDay():
    while True:
        os.system("bash commit.sh")
        #time.sleep(28800)
        print("Success !!")
        break
if __name__ == "__main__":
    everyDay()

