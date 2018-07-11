import docusign_esign as docusign

from ds_helper import DSHelper
from list_envelopes import ListEnvelopes
from send_envelope import SendEnvelope


def main():

    api_client = docusign.ApiClient()
    print("\nSending an envelope...")
    result = SendEnvelope(api_client).send_envelope()

    print("Envelope status: %s. Envelope ID: %s".format(result.status, result.envelope_id))

    print("\nList envelopes in the account...")
    envelopes_list = ListEnvelopes(api_client).list()
    envelopes = envelopes_list.envelopes
    if envelopes_list is not None and len(envelopes) > 2:
        print("Results for %d envelopes were returned. Showing the first two:"
              .format(len(envelopes_list.envelopes)))

        envelopes_list.envelopes = [envelopes[0], envelopes[1]]

    DSHelper.print_pretty_json(envelopes_list)

    print("\nDone.")


if __name__ == "__main__":
    main()
