from dotenv import load_dotenv
import os
import app.msgraph

load_dotenv()

config = {
    'client_id': f'{os.getenv('CLIENTE_ID')}',
    'client_secret': f'{os.getenv('CLIENT_SECRET')}',
    'tenant_id': f'{os.getenv('TENANT_ID')}',
    'scopes': ['https://graph.microsoft.com/.default'],
    'user_principal_name': f'{os.getenv("USER_PRINCIPAL_NAME")}',
    'application_name': f'{os.getenv("APPLICATION_NAME")}'
}

# Inicializar la clase MSGraph
ms_graph = app.msgraph.MSGraph(client_id=config['client_id'], client_secret=config['client_secret'], tenant_id=config['tenant_id'], scopes=config['scopes'])

# Obtener el token de acceso del usuario
ms_graph.get_access_token()

# Obtener información del usuario
user_info = ms_graph.get_user_info(user_principal_name=config['user_principal_name'])
principal_id = user_info['id']

# Obtener información de server principal
sp_info = ms_graph.get_server_principal(application_name=config['application_name'])
resource_id = sp_info['value'][0]['id']
app_role_id = sp_info['value'][0]['appRoles'][0]['id']

# Asignar el rol de usuario al sp
ms_graph.set_user_asigned_app_role(resource_id=resource_id, principal_id=principal_id, app_role_id=app_role_id)