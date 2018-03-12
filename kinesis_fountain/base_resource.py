from abc import ABCMeta, abstractmethod
import boto3

class BaseResource(metaclass=ABCMeta):
    """
    This is the abstract base class for all kinesis_fountain resources
    Attributes:
        client  The type of boto3 client to pass on to subclasses
    """
    def __init__(self, resource_type: str):
        """
        Initialize base resource class
        :param resource_type:
        :type resource_type: str
        """
        pass

