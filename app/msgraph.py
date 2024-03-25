# Define imports
import msal
import os
import requests

class MSGraph:

    def __init__(self, client_id, client_secret, tenant_id, scopes):
       self.client_id = client_id
       self.client_secret = client_secret
       self.tenant_id = tenant_id
       self.access_token = None
       self.authority = f'https://login.microsoftonline.com/{self.tenant_id}'
       self.scopes = scopes
       
    def get_access_token(self):
        client = msal.ConfidentialClientApplication(
            client_id=self.client_id,
            client_credential=self.client_secret,
            authority=self.authority
        )
       
        result = client.acquire_token_for_client(self.scopes)

        if "access_token" in result:
            self.access_token = result["access_token"]
            return self.access_token
        else:
            raise Exception("Failed to get access token")

    def get_user_info(self, user_principal_name):
        url = f'https://graph.microsoft.com/v1.0/users/{user_principal_name}'
        headers = {
            'Authorization': f'Bearer {self.access_token}'
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Failed to get user info")
        
    def get_server_principal(self, application_name):
        url = f'https://graph.microsoft.com/v1.0/servicePrincipals?$filter=displayName eq \'{application_name}\''
        headers = {
            'Authorization': f'Bearer {self.access_token}'
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Failed to get server principal")
        
    def set_user_asigned_app_role(self, resource_id, principal_id, app_role_id):
        url = f'https://graph.microsoft.com/v1.0/servicePrincipals/{resource_id}/appRoleAssignedTo'
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }

        data = {
            'appRoleId': app_role_id,
            'resourceId': resource_id,
            'principalId': principal_id
        }

        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 201:
            return True
        else:
            raise Exception("Failed to set user asigned app role")