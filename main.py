from ds_config import DSConfig
import docusign_esign as docusign

from send_envelope import SendEnvelope


def main():

    api_client = docusign.ApiClient("https://demo.docusign.net/restapi")
    print("\nSending and envelope...")
    result = SendEnvelope(api_client).sendEnvelope()

    print("Envelope status: %s. Envelope ID: %s".format(result.getStatus(), result.getEnvelopeId()));

    print("\nList envelopes in the account...");
    envelopesList = ListEnvelopes(api_client).list()

    print("\nDone.")

if __name__ == "__main__":
    main()
