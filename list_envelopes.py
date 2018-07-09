from docusign_esign import EnvelopesApi

from example_base import ExampleBase


class ListEnvelopes(ExampleBase):

    def list(self):
        self.checkToken()

        envelopeApi = EnvelopesApi(ListEnvelopes.api_client);

        options = {}
        # $date = newDatetime();
        # $date->sub(DateInterval("P30D"))
        # options->setFromDate($date->format("Y/m/d"))
        return envelopeApi.list_status_changes(ListEnvelopes.accountID, options)
