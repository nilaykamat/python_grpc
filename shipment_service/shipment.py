shipments = [
    {
        'id' : 1,
        'name' : 'Shipment 1',
        'weight' : 100
    },
    {
        'id' : 2,
        'name' : 'Shipment 2',
        'weight' : 200
    },
    {
        'id' : 3,
        'name' : 'Shipment 3',
        'weight' : 300
    },
    {
        'id' : 4,
        'name' : 'Shipment 4',
        'weight' : 400
    },
    {
        'id' : 5,
        'name' : 'Shipment 5',
        'weight' : 500
    }
]

# will retrive shipment from the list of shipments based on id
def get_shipment(shipment_id):
    for shipment in shipments:
        if shipment_id == shipment['id']:
            return shipment

# will call carrier service with shipment weight to retrive approprite carrier
def get_carrier_for_shipment(shipment):
    import grpc

    # import the generated classes
    from carrier_protos import carrier_pb2
    from carrier_protos import carrier_pb2_grpc

    # open a gRPC channel

###--------
    with open('certs/tls.crt') as f:
         trusted_certs = f.read().encode()
 # create credentials
    credentials = grpc.ssl_channel_credentials(root_certificates=trusted_certs)
    #channel = grpc.secure_channel('delivery.gship.com:443', credentials)
    channel = grpc.secure_channel('carrier:50052', credentials)


    #channel = grpc.insecure_channel('localhost:50052')

    # create a stub (client)
    stub = carrier_pb2_grpc.CarrierStub(channel)

    # create a valid request message
    carrier = carrier_pb2.GetCarrierRequest(weight = shipment.weight)

    # make the call
    response = stub.GetCarrier(carrier)

    return response
