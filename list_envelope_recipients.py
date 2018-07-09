from docusign_esign import EnvelopesApi

from example_base import ExampleBase


class ListEnvelopeRecipients(ExampleBase):

    def list(self, envelope_id):
        if envelope_id is None:
            raise Exception("PROBLEM: This example software doesn't know which envelope's "
                            "information should be looked up."
                            "SOLUTION: First run the <b>Send Envelope via email</b> example to create an envelope.")

        ListEnvelopeRecipients.checkToken()

        envelopeApi = EnvelopesApi(ListEnvelopeRecipients.api_client)

        return envelopeApi.list_recipients(ListEnvelopeRecipients.accountID, envelope_id)