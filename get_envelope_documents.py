from docusign_esign import EnvelopesApi
from os.path import normpath, join

from ds_helper import DSHelper
from example_base import ExampleBase


class GetEnvelopeDocuments(ExampleBase):

    def download(self, envelope_id):
        if (envelope_id is None):
            raise Exception(
                "PROBLEM: This example software doesn't know which envelope's"
                "information should be looked up."
                "SOLUTION: First run the <b> Send Envelope via email </b> example to create an envelope.")

        GetEnvelopeDocuments.checkToken()
        # The workflow will be multiple API requests:
        #  1) list the envelope's documents
        #  2) Loop to get each document
        envelopeApi = EnvelopesApi(GetEnvelopeDocuments.api_client)
        docDownloadDirPath = DSHelper.ensureDirExistance("downloaded_documents")
        documents = envelopeApi.list_documents(ExampleBase.accountID, envelope_id)
        DSHelper.printPrettyJSON(documents)

        envelopeDocuments = documents.envelope_documents
        print "Download files path: %s".format(docDownloadDirPath)
        for doc in envelopeDocuments:
            docName = "%s__$s".format(envelope_id, doc.name)
            hasPDFsuffix = docName.upper().endswith(".PDF")

            if ("content" == doc.type or "summary" == doc.type) and not hasPDFsuffix:
                docName += ".pdf"

            docBytes = envelopeApi.get_document(ExampleBase.accountID, doc.document_id, envelope_id)
            filePath = normpath(join(docDownloadDirPath, docName))
            DSHelper.writeByteArrayToFile(filePath, docBytes)

            print "\nWrote document id %s to %s".format(doc.document_id, docName)
