"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Even though the group is only for spanish speakers, english speakers are
welcome.
------------------------------------------------------------------------------

Write code to add up/report total number of weapons by type collected &
destroyed by UN Weapons inspectors at 3 locations.

i_1 = ["AK 40, pistols 32, grenades 50, machinguns 7, tankmines 3"]
i_2 = ["handguns 30, handgrenades 40, AK-47/M/74 63, machinegun 15, mines 7"]
i_3 = ["minen 4, machinen-guns 4, AK-47 34, pistolen 15, grenade 50"]

Your printed output should lokk something like this:

    +-----------------------------------------------------------+
    | Total number of reported and destroyed weapons:           |
    | Assault rifles - 137, Machine Guns - 26, Hand Guns - 77,  |
    | Grenades - 140, Mines - 14                                |
    +-----------------------------------------------------------+

"""
i_1 = ["AK 40, pistols 32, grenades 50, machinguns 7, tankmines 3"]
i_2 = ["handguns 30, handgrenades 40, AK-47/M/74 63, machinegun 15, mines 7"]
i_3 = ["minen 4, machinen-guns 4, AK-47 34, pistolen 15, grenade 50"]

inventory = [
    i.split(" ") for j in [i.split(", ") for i in i_1 + i_2 + i_3] for i in j
]
report = {w: 0 for w in ("AK", "pistol", "handgu", "gren", "machin", "mine")}

print(inventory)
for weapon, stock in inventory:
    for tag in report:
        if tag in weapon:
            report[tag] += int(stock)

print(
    "Total number of reported and destroyed weapons:\n"
    f"Assault rifles - {report['AK']}\nMachine Guns - {report['machin']}\n"
    f"Hand Guns - {report['handgu']+report['pistol']}\n"
    f"Grenades - {report['gren']}\nMines - {report['mine']}"
)
