"""
Extends the functionalities of lambda functions
"""

from botocore.exceptions import ClientError
from kinesis_fountain.base_resource import BaseResource

class Firehose(BaseResource):
    """
    Extends the functionalities of lambda functions
    """
    resource_type = "firehose"

    def __init__(self, name):
        self.name = name
        super().__init__(resource_type=self.resource_type)

    def exists(self) -> bool:
        """
        Determines whether the lambda exists
        @return: True if lambda exists
        @rtype: bool
        """
        try:
            self.client.describe_delivery_stream(DeliveryStreamName=self.name)
            return True
        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceNotFoundException":
                return False
            else:
                raise

    @property
    def resource_arn(self) -> str:
        return self.client \
            .describe_delivery_stream(
                DeliveryStreamName=self.name)["DeliveryStreamDescription"]["DeliveryStreamARN"]
