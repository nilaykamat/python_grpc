consignments = [
    {
        'id' : 1,
        'name' : 'Consignment 1',
        'weight' : 100
    },
    {
        'id' : 2,
        'name' : 'Consignment 2',
        'weight' : 200
    },
    {
        'id' : 3,
        'name' : 'Consignment 3',
        'weight' : 300
    },
    {
        'id' : 4,
        'name' : 'Consignment 4',
        'weight' : 400
    },
    {
        'id' : 5,
        'name' : 'Consignment 5',
        'weight' : 500
    }
]

# will retrive consignmnet from the list of consignment based on id
def get_consignment(consignment_id):
    for consignment in consignments:
        if consignment_id == consignment['id']:
            return consignment

# will call vessel service with consignment weight to retrive approprite vessel
def get_vessel_for_consignment(consignment):
    import grpc

    # import the generated classes
    from vessel_protos import vessel_pb2
    from vessel_protos import vessel_pb2_grpc

    # open a gRPC channel

###--------
    with open('tls.crt') as f:
        trusted_certs = f.read().encode()
# create credentials
    credentials = grpc.ssl_channel_credentials(root_certificates=trusted_certs)
    channel = grpc.secure_channel('shippy.example.com:443', credentials)


    #channel = grpc.insecure_channel('localhost:50052')
    #channel = grpc.insecure_channel('vessel:50052')

    # create a stub (client)
    stub = vessel_pb2_grpc.VesselStub(channel)

    # create a valid request message
    vessel = vessel_pb2.GetVesselRequest(weight = consignment.weight)

    # make the call
    response = stub.GetVessel(vessel)

    return response
