# Creación de aplicación en Entra ID

### Prerequisitos
1. Debes contar con un dominio inquilino de Entra ID

### Creación de aplicación
- Ingrese a https://entra.microsoft.com/ con sus credenciales y que cuente con permiso de Administrador de aplicaciones
- Navega a Identity > Applications > App registrations y selecciona New registration
- Completa los siguientes atributos
  - Name: Con el nombre de la aplicación 
  - Support account types: Selecciona Accounts in this organizational directory only (Default Directory only - Single tenant)
  - Redirect URI: en el caso que cuentes con una aplación web puede usar colocar la url
- Seleccionar el boton registrar

### Creación de Client secret
- Ingresar a la aplicación creada y selecciona Certificates & secrets
- Selecciona New client secret y completa la descripción y la caducidad
- Por ultimo selecciona el boton agregar
- Guarda el campo value y Secret ID

### Configuración de permisos
- Ingresa a la aplicación creada y selecciona API permissions
- Selecciona Add a permission, luego Microsoft Graph y Application permissions
- Luego selecciona los permisos que requieres que necesites trabajar, en este caso los permisos son:
  - Application.ReadWrite.All
  - AppRoleAssignment.ReadWrite.All
  - Directory.ReadWrite.All
  - User.Read
- Agrega los permisos seleccionados
- Por ultimo selecciona Grant admin consent for Default Directory

### Configuración de .env
El archivo .env contiene las siguientes variables de entorno:
- CLIENTE_ID, es el valor que se encuentra el Application (client) ID de la aplicacion creada.
- TENANT_ID= es el valor que se encuentra en la vista Overview de Entra ID.
- CLIENT_SECRET= es el campo valor creado en Certificates & secrets.
- SECRET_ID= es el campo secretId creado en Certificates & secrets.
- USER_PRINCIPAL_NAME= es el usuario concatenado con el dominio ejemplo: user@dominio.com
- APPLICATION_NAME= es el nombre de la aplicación que creaste

### Para ejecutar el Script
- Se requiere crear un entorno:
```
python -m venv env
```
- Instalar paquetes msal y python-dotenv
```
pip install msal python-dotenv
```
- configurar el archivo .env
- Ejecutar el script