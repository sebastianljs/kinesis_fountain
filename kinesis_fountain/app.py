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

    def _get_output_firehose_arns(self) -> Generator:
        output_descriptions = self.client \
            .describe_application(ApplicationName=self.name)["ApplicationDetail"] \
            .get("OutputDescriptions", [])
        return (
            desc.get("KinesisFirehoseOutputDescription", {}).get("ResourceARN")
            for desc in output_descriptions)

    @property
    def output_firehoses(self) -> Generator:
        """
        Returns a generator of firehoses associated with this app
        """
        output_firehose_names = (
            firehose_arn.split("/")[-1] for firehose_arn in self._get_output_firehose_arns()
            if firehose_arn)
        return (
            Firehose(name=output_firehose_name)
            for output_firehose_name in output_firehose_names if
            output_firehose_name)
