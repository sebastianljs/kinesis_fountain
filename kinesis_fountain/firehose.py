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

