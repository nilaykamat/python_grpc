vessels = [
    {
        'id' : 1,
        'max_weight' : 120
    },
    {
        'id' : 2,
        'max_weight' : 250
    },
    {
        'id' : 3,
        'max_weight' : 500
    },
    {
        'id' : 4,
        'max_weight' : 800
    },
    {
        'id' : 5,
        'max_weight' : 1500
    }
]

def get_vessel(weight):
    for vessel in vessels:
        if weight <= vessel['max_weight']:
            return vessel