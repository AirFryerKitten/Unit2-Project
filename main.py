#Jonas York
#U2 Project
#Bear and fish

from ecosystem import * 
from time import sleep
DAYS_SIMULATED = 30
RIVER_SIZE = 15
START_BEARS = 10
START_FISH = 10


def main():
  r = River(RIVER_SIZE, START_BEARS, START_FISH)
  day = 0
  done = False
  while done == False:
    print(f"\n\nDay: {day+1}")
    print(r)
    print(f"\nStarting Poplation: {r.population} animals")
    done = r.new_day()
    print(f"Ending Poplation: {r.population} animals")
    print(r)
    day += 1
    sleep(1)

  print("\nTest Done")
  print(f"\nTotal days {day+1}")
  print("\nFinal Results")
  print(r)



if __name__ == "__main__":
  main()