import docusign_esign as docusign

from list_envelopes import ListEnvelopes
from send_envelope import SendEnvelope


def main():

    api_client = docusign.ApiClient("https://demo.docusign.net/restapi")
    print("\nSending an envelope...")
    result = SendEnvelope(api_client).send_envelope()

    print("Envelope status: %s. Envelope ID: %s".format(result.getStatus(), result.getEnvelopeId()));

    print("\nList envelopes in the account...")
    envelopesList = ListEnvelopes(api_client).list()
    #TODO: print the first 2 envelopes like c#, java and php
    print("\nDone.")


if __name__ == "__main__":
    main()
