import configparser
import os


def load_from_properties():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['Default']


def load_from_env():
    client_id = os.environ.get('DS_CLIENT_ID', None)
    if client_id is not None:
        return os.environ
    return None


class DSConfig:
    instance = None

    @staticmethod
    def getInstance():
        if DSConfig.instance is None:
            instance = DSConfig()

        return instance

    def __init__(self):
        self.config = load_from_env()

        if self.config is None:
            self.config = load_from_properties()

    def _client_id(self):
        return self.config['DS_CLIENT_ID']

    @staticmethod
    def client_id():
        return DSConfig.getInstance()._client_id()

    def _impersonated_user_guid(self):
        return self.config["DS_IMPERSONATED_USER_GUID"]

    @staticmethod
    def impersonated_user_guid():
        return DSConfig.getInstance()._impersonated_user_guid()

    def _target_account_id(self):
        return self.config["DS_TARGET_ACCOUNT_ID"]

    @staticmethod
    def target_account_id():
        return DSConfig.getInstance()._target_account_id()

    @staticmethod
    def oauth_redirect_uri():
        return "https://www.docusign.com"


    def _signer_email(self):
        return self.config["DS_SIGNER_1_EMAIL"]

    @staticmethod
    def signer_email():
        return DSConfig.getInstance()._signer_email()

    def _signer_name(self):
        return self.config["DS_SIGNER_1_NAME"]

    @staticmethod
    def signer_name():
        return DSConfig.getInstance()._signer_name()

    def _cc_email(self):
        return self.config["DS_CC_1_EMAIL"]

    @staticmethod
    def cc_email():
        return DSConfig.getInstance()._cc_email()

    def _cc_name(self):
        return self.config["DS_CC_1_NAME"]

    @staticmethod
    def cc_name():
        return DSConfig.getInstance()._cc_name();

    def _private_key_file(self):
        return self.config["DS_PRIVATE_KEY_FILE"]

    @staticmethod
    def private_key_file():
        return DSConfig.getInstance()._private_key_file()

    def _private_key(self):
        return self.config["DS_PRIVATE_KEY"]

    @staticmethod
    def private_key():
        return DSConfig.getInstance()._private_key()

    @staticmethod
    def authentication_url():
        return "https://account-d.docusign.com"

    @staticmethod
    def aud():
        return "account-d.docusign.com"

    @staticmethod
    def api():
        return "restapi/v2"

    @staticmethod
    def permission_scopes():
        return "signature impersonation"

    @staticmethod
    def jwt_scope():
        return "signature"
