"""
Extends the functionalities of KA apps
"""

from collections import Generator
from botocore.exceptions import ClientError
from kinesis_fountain.base_resource import BaseResource
from kinesis_fountain.firehose import Firehose

class App(BaseResource):
    """
    Extends the functionalities of KA apps
    """
    resource_type = "kinesisanalytics"
    def __init__(self, name: str):
        super().__init__(resource_type=self.resource_type)
        self.name = name

    @property
    def resource_arn(self) -> str:
        """
        Gets the app's resource ARN
        :return: Resource ARN
        :rtype: str
        """

    def exists(self) -> bool:
        """
        Determines if the app exists
        :return: True if app exists
        :rtype: bool
        """
        try:
            self.client.describe_application(ApplicationName=self.name)
            return True
        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceNotFoundException":
                return False
            else:
                raise
            
    