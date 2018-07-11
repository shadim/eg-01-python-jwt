import time

from ds_config import DSConfig
from ds_helper import DSHelper

TOKEN_REPLACEMENT_IN_MILLISECONDS = 10 * 60 * 1000
TOKEN_EXPIRATION_IN_SECONDS = 3600


class ExampleBase:
    """
    Example Base class
    """
    accountID = None
    api_client = None
    _token = None
    account = None
    expiresIn = 0

    def __init__(self, api_client):
        ExampleBase.api_client = api_client

    def check_token(self):
        milliseconds = int(round(time.time() * 1000))
        if ExampleBase._token is None \
                or ((milliseconds + TOKEN_REPLACEMENT_IN_MILLISECONDS) > ExampleBase.expiresIn):
            self.update_token()

    def update_token(self):
        client = ExampleBase.api_client

        private_key_file = DSHelper.create_private_key_temp_file("private-key")

        client.configure_jwt_authorization_flow(private_key_file.name,
                                                DSConfig.aud(),
                                                DSConfig.client_id(),
                                                DSConfig.impersonated_user_guid(), 3600)

        private_key_file.close()

        if ExampleBase.account is None:
            account = self.get_account_info(client)

        ExampleBase.base_uri = account['base_uri'] + '/restapi'
        ExampleBase.accountID = account['account_id']
        client.host = ExampleBase.base_uri
        ExampleBase._token = "DummyToken"
        ExampleBase.expiresIn = 1000 * (int(round(time.time())) + TOKEN_EXPIRATION_IN_SECONDS)

    def get_account_info(self, client):
        client.host = DSConfig.authentication_url()
        response = client.call_api("/oauth/userinfo", "GET", response_type="object")

        if len(response) > 1 and 200 > response[1] > 300:
            raise Exception("can not get user info: %d".format(response[1]))

        accounts = response[0]['accounts']
        target = DSConfig.target_account_id()

        if target is not None and target != "FALSE":
            for acct in accounts:
                if acct['account_id'] == target:
                    return acct

        for acct in accounts:
            if acct['is_default']:
                return acct

        return None
