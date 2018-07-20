import sys
import consignment_cli
# import vessel_cli

service = sys.argv[1]

for i in range(0, 1000) :
	if service == 'consignment' :
		print consignment_cli.get_consignment(1)
	else :
		print 'other'
		consignment_cli.get_vessel(1,'sample',200)
