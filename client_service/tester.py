import sys
import shipment_cli

service = sys.argv[1]

for i in range(0, 100000) :
    if service == '1' :
        print shipment_cli.get_shipment(1)
    else :
        print shipment_cli.get_carrier(1,'sample',200)

