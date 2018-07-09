from docusign_esign import EnvelopesApi, EnvelopeDefinition, Signer, CarbonCopy, SignHere, Tabs, Recipients

from ds_config import DSConfig
from ds_helper import DSHelper
from example_base import ExampleBase

ENVELOPE_1_DOCUMENT_1 = ""
DOC_2_DOCX = ""
DOC_3_PDF = ""


def createDocumentFromTemplate(id, name, fileExtension, content):
    return ""


def createSigner():
    signer = Signer()
    signer.email = DSConfig.signer_email()
    signer.name = DSConfig.signer_name()
    signer.recipient_id = "1"
    signer.routing_order = "1"
    return signer


def createCarbonCopy():
    cc = CarbonCopy()
    cc.email = DSConfig.cc_email()
    cc.name = DSConfig.cc_name()
    cc.routing_order = "2"
    cc.recipient_id = "2"
    return cc


def createSignHere(anchor_pattern, anchor_units, anchor_x_offset, anchor_y_offset):
    signHere = SignHere()
    signHere.anchor_string = anchor_pattern
    signHere.anchor_units = anchor_units
    signHere.anchor_x_offset = anchor_x_offset
    signHere.anchor_y_offset = anchor_y_offset
    return signHere


def setSignerTabs(signer1, signers):
    tabs = Tabs()
    tabs.sign_here_tabs = signers
    signer1.tabs = tabs


def createRecipients(signer1, cc1):
    recipients = Recipients()
    recipients.signers = [signer1]
    recipients.carbon_copies = [cc1]
    return recipients


class SendEnvelope(ExampleBase):
    def __init__(self, api_client):
        ExampleBase.__init__(self, api_client)

    def sendEnvelope(self):

        self.checkToken()
        envelope = self.createEnvelope()
        envelopeApi = EnvelopesApi(SendEnvelope.apiClient)
        results = envelopeApi.createEnvelope(SendEnvelope.accountID, envelope)
        return results

    def createEnvelope(self):
        envelopeDefinition = EnvelopeDefinition()
        envelopeDefinition.email_subject = "Please sign this document sent from Node SDK"

        doc1 = createDocumentFromTemplate("1", "Order acknowledgement", "html", ENVELOPE_1_DOCUMENT_1)
        doc2 = createDocumentFromTemplate("2", "Battle Plan", "docx", DSHelper.readContent(DOC_2_DOCX))
        doc3 = createDocumentFromTemplate("3", "Lorem Ipsum", "pdf", DSHelper.readContent(DOC_3_PDF))

        # The order in the docs array determines the order in the envelope
        envelopeDefinition.setDocuments([doc1, doc2, doc3])
        # create a signer recipient to sign the document, identified by name and email
        # We're setting the parameters via the object creation
        signer1 = createSigner()
        # routingOrder (lower means earlier) determines the order of deliveries
        # to the recipients. Parallel routing order is supported by using the
        # same integer as the order for two or more recipients.

        # create a cc recipient to receive a copy of the documents, identified by name and email
        # We're setting the parameters via setters
        cc1 = createCarbonCopy()
        # Create signHere fields (also known as tabs) on the documents,
        # We're using anchor (autoPlace) positioning
        #
        # The DocuSign platform seaches throughout your envelope's
        # documents for matching anchor strings. So the
        # sign_here_2 tab will be used in both document 2 and 3 since they
        # use the same anchor string for their "signer 1" tabs.
        signHere1 = createSignHere("**signature_1**", "pixels", "20", "10")
        signHere2 = createSignHere("/sn1/", "pixels", "20", "10")
        # Tabs are set per recipient / signer
        setSignerTabs(signer1, [signHere1, signHere2])
        # Add the recipients to the envelope object
        recipients = createRecipients(signer1, cc1)
        envelopeDefinition.setRecipients(recipients)
        # Request that the envelope be sent by setting |status| to "sent".
        # To request that the envelope be created as a draft, set to "created"
        envelopeDefinition.setStatus("sent")

        return envelopeDefinition

