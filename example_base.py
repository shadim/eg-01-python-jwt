from ds_config import DSConfig


class ExampleBase:
    accountID = None
    api_client = None
    _token = None

    def __init__(self, api_client):
        ExampleBase.api_client = api_client

    def checkToken(self):
        if ExampleBase._token is None:#TODO:
            self.updateToken()

    def updateToken(self):
        client = ExampleBase.api_client

        client.configure_jwt_authorization_flow(DSConfig.private_key_file(),
                                                                DSConfig.aud(),
                                                                DSConfig.client_id(),
                                                                DSConfig.impersonated_user_guid(), 3600)
        account = self.get_account_info(client)
        client.host = account['base_uri']
        ExampleBase.accountID = account['account_id']
        ExampleBase._token = "DummyToken"

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
