import sys
import shipment_cli
# import vessel_cli

service = sys.argv[1]

for i in range(0, 100000) :
    if service == 'consignment' :
        print shipment_cli.get_shipment(1)
    else :
        print 'other'
        shipment_cli.get_carrier(1,'sample',200)

