from docusign_esign import EnvelopesApi

from example_base import ExampleBase


class GetEnvelopeStatus(ExampleBase):

    def get_envelope(self, envelopeId):
        if envelopeId is None:
                raise Exception("PROBLEM: This example software doesn't know which envelope's "
                        "information should be looked up."
                        "SOLUTION: First run the <b>Send Envelope via email</b> example to create an envelope.")

        GetEnvelopeStatus.checkToken()

        # call the getEnvelope() API
        envelopeApi = EnvelopesApi(GetEnvelopeStatus.api_client)

        return envelopeApi.get_envelope(GetEnvelopeStatus.accountID, envelopeId)