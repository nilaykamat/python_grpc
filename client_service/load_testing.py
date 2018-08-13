## Load testing script
## -------------------

import sys
import shipment_cli_load_test
import carrier_cli_load_test
service = sys.argv[1]

# Increase the range value to send requests
for i in range(0, 1000000) :
    if service == 'shipment' :
        print shipment_cli_load_test.get_shipment(1)
    elif service == 'carrier' :
        print carrier_cli_load_test.get_carrier(weight = 100)
    else :
        print shipment_cli_load_test.get_carrier(1,'sample',200)
