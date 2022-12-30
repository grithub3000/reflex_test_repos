import sys
import select
import time
import random
def instructions():
    print("When you see 'DRAW', press enter as quickly as possible. Pressing enter"
        " before 'DRAW' appears will result in added penalty time.")
    press_enter = input("Press enter when you're ready to play")

def attempt():
    i, o, e = "", "", ""
    time.sleep(1)
    print("Be ready...")
    i, o, e = select.select([sys.stdin], [], [], random.uniform(1, 8))
    if(i):
        print("You pressed enter too early! Your time for this attempt is 0.6 seconds.")
        return 0.6
    else:
        print("DRAW")
        start = time.time()
        press_enter = input()
        time_taken = time.time() - start
        print(round(time_taken, 3))
        return time_taken

def display_results(results):
    print("\nRESULTS")
    attempt_number = 1
    for time in results:
        print(f"{attempt_number}. {round(time, 3)}")
        attempt_number += 1
    print("Average:", round(sum(results) / len(results), 3))

def main():
    times = []
    instructions()
    for _ in range(5):
        times.append(attempt())
    display_results(times)

main()