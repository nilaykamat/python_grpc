# python_grpc
A cluster of simple python micro-services communicating using gRPC

There are 3 micro-services running
<ul>
    <li>Vessel Service</li>
    <li>Consignment Service</li>
    <li>Client Service</li>
</ul>

<h4>Vessel Service</h4>
<p>The rpc endpoint "GetVessel" in this service will take in the weight of any consignment and return the details of the Vessel which can accomodate the consignment</p>

<h4>Consignment Service</h4>
<p>The rpc endpoint "GetConsignment" in this service will take in the appropriate consignment id and return the details of that consignment</p>
<p>The rpc endpoint "GetVesselForConsignment" in this service will take in the details of a consignment to find an appropritae vessel and call the Vessel Service over gRPC to get the details of the vessel for the weight of the provided consignment</p>

<h4>Client Service</h4>
<p>This is small application built over python Flask which will communicate with Consignmnet Service to get details about Consignments and Vessels.</p>
<p>There are two endpoints for this API service</p>
<ul>
    <li>getConsignment - used to get consignment given the id</li>
    <li>getVessel - used to get vessel given consignment details</li>
</ul>
<p>This also has a small UI which will help in calling the APIs</p>