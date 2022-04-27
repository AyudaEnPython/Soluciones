"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Even though the group is only for spanish speakers, english speakers
are welcome.
-----------------------------------------------------------------------
    ** PYTHON CODE CHALLENGE - RESCUE BIEBER IN PARIS **

Justin is resting and enjoying 'not being kidnapped' in Paris, 
but unfortunately local kidnappers grab him in the Louvre.
Just before police raid gangs hideout, a semi-coded text-message was 
intercepted from phone in hideout. Gang is known to use shifting Caesar
ciphers, with a code-key somehow indicating each letter shift

Police have no clue what to do...can you help and find Justin? 
you know the code for encrypting a regular non-shift caesar (below), 
but how to find the offsets?

Example:
secret = 'messagetoencode'
secret_offset = 0
msg = [chr((ord(v) + secret_offset - 97) % 26 + 97) for v in secret]

Clock is ticking...Can you find him?
"""
import re
from itertools import cycle
from typing import Tuple


def _f(msg: str) -> Tuple[str, str]:
    res = re.search(r'\W+', msg).start()
    return msg[0:res], msg[res+1:]


def decode(msg: str) -> str:
    code, msg = _f(msg)
    return "".join(
        chr((ord(s) - ord(k) - 97) % 26 + 97)
        for s, k in zip(msg, cycle(code))
    )


intercepted_msg = 'weshfrerot!elwiaojycqwfxbcbprrmabdhyviozepjpdgwfxbui'
print(decode(intercepted_msg))
