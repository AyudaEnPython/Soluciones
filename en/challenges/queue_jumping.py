"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Even though the group is only for spanish speakers, english speakers
are welcome.
-----------------------------------------------------------------------
    ** PYTHON CODE CHALLENGE - QUEUE JUMPING **

Your website shows oil(CL), nat gas(NG), gold(GC) and silver(SI) prices
in 'real-time'. In fast markets, price updates lag behind as queue
overloads and users get upset. Current code displays all updates in
order they arrived to queue.

Create new queue handler that updates latest available price for each
commodity, hopefully faster. New prices are added to end of list, and
first position is read and then removed from queue:

q = [
    'CL,105.3'
    'GC,1866.40'
    'SI,22.85'
    'CL,105.4',
    'NG,7.525',
    'CL,105.6',
    'GC,1866.80',
    'NG,7.535',
]

New queue should be reduced to:
new_q = ['CL,105.6','GC,1866.80','SI,22.85','NG,7.535']

And as each price is printed out, remove that price update:

"Crude(CL) 105.6, new_q=['GC,1866.80','SI,22.85','NG,7.535']"
"Gold(GC) 1866.80, new_q= ['SI,22.85','NG,7.535']"
"Silver(SI) 22.85, new_q=['NG,7.535']"
"Nat Gas(NG) 7.535, new_q=[]"
"""
