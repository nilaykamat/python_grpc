import grpc

# import the generated classes
from proto import calculator_pb2
from proto import calculator_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = calculator_pb2_grpc.CalculatorStub(channel)

# create a valid request message
number = calculator_pb2.Number(value=16)
numbers = calculator_pb2.Numbers(number1=10, number2=5)
# make the call
response1 = stub.SquareRoot(number)
response2 = stub.Sum(numbers)
response3 = stub.Difference(numbers)
response4 = stub.Multiplication(numbers)
response5 = stub.Division(numbers)

print('squareroot of 16 : ' + str(response1.value))
print('sum of 10 & 5 : ' + str(response2.value))
print('difference of 10 & 5 : ' + str(response3.value))
print('multiplication of 10 & 5 : ' + str(response4.value))
print('division of 10 & 5 : ' + str(response5.value))