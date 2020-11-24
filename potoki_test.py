import time

def main():
    print("It’s time !")

if __name__ == "__main__":
    print("press ctrl-c to stop")
    loop_forever = True
    while loop_forever:
        main()
        try:
            time.sleep(60)
        except KeyboardInterrupt:
            loop_forever = False

print("\n", "fdsfs")