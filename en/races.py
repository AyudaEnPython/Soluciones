"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Even though the group is only for spanish speakers, english
speakers are welcome.

## The Problem

The program you will develop here will do some simple analysis of race
times from a motor race. The examples below are based on Formula 1.

The program begins by prompting the user to enter the name of the race
for which are being recorded. If nothing is entered, some suitable
default name should be assumed.

The program will then prompt the user to enter lap times recorded by
drivers as they practice (in real life this data stream would obviously
be computer-generated and sent automatically when each driver crosses
the finish line). This carries on until the user ends the process at
the end of the session by just pressing "Enter".

The data is entered in a simple format, and will always be in the
correct format. The driver is identified by three letters, and the time
is a flotaing-point with tree places of decimals. The two values are
not separated (as the name is always three letters there is no need).
For exmple:

    LEC121.345
    ALO120.435

The final output should be the name of the driver (the three letter
code), followed by their statistics. The statistics should be the
number of laps driven, the time of the fastest lap, the time of the
slowest lap, and their average lap time. The examples below should make
this clear.

## Examples

The following ilustrate what should happen when the program executes
for a variety fo scenarios.

Here, the user enters the race name, but no data.

    Grand Prix Race Times
    Enter name of race: Beckett
    Enter Driver and Time [Enter to finish]:
    No data entered.

Here the times are for a single driver. Note that the user did not
enter a race name, so a default has been used.

        Laps    Fast        Slow        Mean
    CAM    5    187.719     191.829     189.374

Finally, there are several drivers, and the user does enter a race name

    Grand Prix Race Times
    Enter name of race: Leeds Beckett
    Enter Driver and Time [Enter to finish]: CAM100.229
    Enter Driver and Time [Enter to finish]: BAG99.928
    Enter Driver and Time [Enter to finish]: CAM100.817
    Enter Driver and Time [Enter to finish]: JEN105.757
    Enter Driver and Time [Enter to finish]: JEN103.276
    Enter Driver and Time [Enter to finish]: BAG98.757
    Enter Driver and Time [Enter to finish]: JEN98.726
    Enter Driver and Time [Enter to finish]:
    
    Grand Prix de Leeds beckett Timings
    ===================================

    3 drivers entered.

        Laps    Fast        Slow        Mean
    CAM    2    100.229    100.817    100.523
    BAG    2    98.757     99.928     99.343
    JEN    3    98.726     105.757    102.586
"""
from typing import List, Dict

Data = Dict[str, List[float]]


def get_drivers() -> List[str]:
    drivers = []
    while True:
        driver = input("Enter Driver and Time [Enter to finish]: ")
        if driver == "":
            break
        drivers.append(driver)
    return drivers


def statistics(data: List[str]) -> Data:
    result = {}
    for line in data:
        if line[:3] not in result:
            result[line[:3]] = []
        result[line[:3]].append(float(line[3:]))
    return {
        k: [len(v), min(v), max(v), sum(v)/len(v)] for k, v in result.items()
    }


def show(data: Data, race_name: str) -> None:
    title = f"\nGrand Prix {race_name} Timings"
    print(title)
    print("="*(len(title) - 1))
    if len(data) < 2:
        print("\n1 driver entered.\n")
    else:
        print(f"\n{len(data)} drivers entered.\n")
    print(f"{'Laps':>8} {'Fast':>6} {'Slow':>8} {'Mean':>8}")
    for k, v in data.items():
        print(f"{k:>3} {v[0]:>3} {v[1]:>9.3f} {v[2]:>8.3f} {v[3]:>8.3f}")


def main():
    print("Grand Prix Race Times")
    race_name = input("Enter the name of race: ")
    race_name = "Python" if race_name == "" else race_name
    drivers = get_drivers()
    if drivers == []:
        print("No data entered.")
        return
    data = statistics(drivers)
    show(data, race_name)


if __name__ == "__main__":
    main()
