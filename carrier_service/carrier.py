carriers = [
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

# function will go through the list of carriers and will return the one with weight which can accomodate shipment
def get_carrier(weight):
    for carrier in carriers:
        if weight <= carrier['max_weight']:
            return carrier
