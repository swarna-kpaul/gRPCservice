import grpc
import unary.unary_pb2_grpc as pb2_grpc
import unary.unary_pb2 as pb2


class UnaryClient(object):
	"""
	Client for gRPC functionality
	"""

	def __init__(self,host='localhost',port=50051):
		self.host = host
		self.server_port = port

		# instantiate a channel
		self.channel = grpc.insecure_channel(
			'{}:{}'.format(self.host, self.server_port))

		# bind the client and the server
		self.stub = pb2_grpc.UnaryStub(self.channel)

	def get_url(self, message):
		"""
		Client function to call the rpc for GetServerResponse
		"""
		message = pb2.Message(message=message)
		print(f'{message}')
		return self.stub.GetServerResponse(message)


if __name__ == '__main__':
	client = UnaryClient(host='localhost')
	result = client.get_url(message="Hello Server you there?")
	print(f'{result}')
	result = client.get_url(message="Thanks for being there?")
	print(f'{result}')