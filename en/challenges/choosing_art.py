"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Even though the group is only for spanish speakers, english speakers
are welcome.
-----------------------------------------------------------------------
    ** PYTHON CODE CHALLENGE - CHOOSING ART **

you are selecting art for a client with special tastes. client wants
only to be shown art with favorite colors, blue(b), yellow(y) or red(r),
but only one color per art-piece. so if a piece has blue, it must not
contain yellow or red write code to help you select pieces to show
client.
All art available has been color-coded by your assistant.

art = ['1ygb','2gbw','3ybg','4mbg','5bgy','6grb','7yrg','8grm','9owy']

# output
> 'Artworks 2, 4, 8, 9 can be shown to client'
"""

art = ["1ygb", "2gbw", "3ybg", "4mbg", "5bgy", "6grb", "7yrg", "8grm", "9owy"]


def sol_1():   
    cs = "b", "y", "r"
    d = []
    for i in art:
        k = 0
        for c in i[1:]:
            if c in cs:
                k += 1
        if k < 2:
            d.append(i[0])
    return d


def sol_2():
    return {i[0] for i in art if len(set(i[1:]) & {"b", "y", "r"}) < 2}


def sol_3(): # submitted code by Udo Sero 
    favorites = {'b','y','r'}
    artsplits = {item[0]: set(item[1:]) for item in art}
    selections = [
        item[0] for item in artsplits.items()
        if len(item[1].intersection(favorites)) == 1
    ]
    return selections


def sol_4(): # submitted code by Himel Sharma
    colors = ["b","y","r"]
    chosen_ones = []
    for arts in art:
        chosen = False
        for color in colors:
            c = []
            if color in arts:
                c += colors
                c.remove(color)
                if not any([c[0] in arts, c[1] in arts]):
                    chosen = True
        if chosen:
            chosen_ones += [arts[0]]
    return chosen_ones


if __name__ == "__main__":
    data = sol_1()
    # data = sol_2()
    # data = sol_3()
    # data = sol_4()
    print(f"Artworks {', '.join(data)} can be shown to client")
