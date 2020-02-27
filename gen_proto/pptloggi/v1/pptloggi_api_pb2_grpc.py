# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from pptloggi.v1 import pptloggi_api_pb2 as pptloggi_dot_v1_dot_pptloggi__api__pb2


class PptloggiAPIStub(object):
  """Handles the loggi-web and PPTL hardware requests.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.TurnOnDisplay = channel.unary_unary(
        '/loggi.pptloggi.v1.PptloggiAPI/TurnOnDisplay',
        request_serializer=pptloggi_dot_v1_dot_pptloggi__api__pb2.TurnOnDisplayRequest.SerializeToString,
        response_deserializer=pptloggi_dot_v1_dot_pptloggi__api__pb2.TurnOnDisplayResponse.FromString,
        )
    self.TurnOffDisplay = channel.unary_unary(
        '/loggi.pptloggi.v1.PptloggiAPI/TurnOffDisplay',
        request_serializer=pptloggi_dot_v1_dot_pptloggi__api__pb2.TurnOffDisplayRequest.SerializeToString,
        response_deserializer=pptloggi_dot_v1_dot_pptloggi__api__pb2.TurnOffDisplayResponse.FromString,
        )
    self.PressedButton = channel.unary_unary(
        '/loggi.pptloggi.v1.PptloggiAPI/PressedButton',
        request_serializer=pptloggi_dot_v1_dot_pptloggi__api__pb2.PressedButtonRequest.SerializeToString,
        response_deserializer=pptloggi_dot_v1_dot_pptloggi__api__pb2.PressedButtonResponse.FromString,
        )


class PptloggiAPIServicer(object):
  """Handles the loggi-web and PPTL hardware requests.
  """

  def TurnOnDisplay(self, request, context):
    """Request to turn on a display.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def TurnOffDisplay(self, request, context):
    """Request to turn off a display.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PressedButton(self, request, context):
    """Request triggered on a push button event.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PptloggiAPIServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'TurnOnDisplay': grpc.unary_unary_rpc_method_handler(
          servicer.TurnOnDisplay,
          request_deserializer=pptloggi_dot_v1_dot_pptloggi__api__pb2.TurnOnDisplayRequest.FromString,
          response_serializer=pptloggi_dot_v1_dot_pptloggi__api__pb2.TurnOnDisplayResponse.SerializeToString,
      ),
      'TurnOffDisplay': grpc.unary_unary_rpc_method_handler(
          servicer.TurnOffDisplay,
          request_deserializer=pptloggi_dot_v1_dot_pptloggi__api__pb2.TurnOffDisplayRequest.FromString,
          response_serializer=pptloggi_dot_v1_dot_pptloggi__api__pb2.TurnOffDisplayResponse.SerializeToString,
      ),
      'PressedButton': grpc.unary_unary_rpc_method_handler(
          servicer.PressedButton,
          request_deserializer=pptloggi_dot_v1_dot_pptloggi__api__pb2.PressedButtonRequest.FromString,
          response_serializer=pptloggi_dot_v1_dot_pptloggi__api__pb2.PressedButtonResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'loggi.pptloggi.v1.PptloggiAPI', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
