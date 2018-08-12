## Load testing script
## -------------------

import sys
import shipment_cli
import carrier_cli2
service = sys.argv[1]

# Increase the range value to send requests
for i in range(0, 1000000) :
    if service == 'shipment' :
        print shipment_cli.get_shipment(1)
    elif service == 'carrier' :
        print carrier_cli2.get_carrier(weight = 100)
    else :
        print shipment_cli.get_carrier(1,'sample',200)
