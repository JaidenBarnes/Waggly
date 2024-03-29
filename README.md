                             Web Application Self-deployment Instructions
**1. Clone project**

Open VS Code
>Clone git repository > enter:
    
    https://github.com/JaidenBarnes/Waggly.git
>Choose project save destination into a new folder named:

    Waggly

An error will appear, 'failed to locate virtual environment', click 'create' then select:
>python 3.11

---
**2. Create Static Web App**

View tab > Command Pallette > type and select:

    Azure Static Web Apps: Create Static Web App...
(press enter) > then choose 'create':
> Static Web App name: 'Waggly'
> 
> GitHub repository name: 'Waggly'
> 
> Region: West Europe
> 
> Build preset: Custom
>
> Application code location:

    /src
> Application build ouput location:

    /src

---
!!!!!!!!!!!!!!!!!!!!!!!!
DON'T THINK THIS IS NEEDED!!! --> There is already a function_app.py file containing x2 functions,
postregisterdogwalker and postregisterwoofer, suggesting only the 'deploy to Azure Functions' is needed.

View tab > Command Pallette > type 'Azure Static Web Apps: Create HTTP Function...' > then:
>Language: Python
>
>Python Programming Model: Model V2
>
>Python Interpreter: python 3.11
>
>Function Name:

    postregisterwalker
    
>Authorisation level: ANONYMOUS

** Also, if needed, then postregisterwoofer would be needed too
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

---
**3. Create Function App**

Azure tab > Resources > click '+' > click 'Create Function App in Azure...' > enter:
>Function App Name:

    wagglyFunctions
    
>Runtime Stack: Python 3.11
>
>Resource Location: UK South

Azure tab > Resources > expand Function App > expand wagglyFunctions > right click 'Functions' > click 'Deploy to Function App'

---
**4. Create Database**

Azure tab > Resources > right click 'Azure Cosmos DB' > click 'Create Server':
>Account Name:

    wagglydbaccount
>
>Capacity Model: Serverless
>
>Resource Group: wagglyFunctions

Then,

Azure tab > Resources > right click 'Azure Cosmos DB' > right click 'wagglydbaccount (Core (SQL))' > click 'Create Database':
>Database Name:

    waggly-database

>Collection ID:

    waggly_container

>Partition Key:

    /id

---
**5. Link Functions with Database with endpoint key**

Azure tab > Expand 'Azure Cosmos DB' > right click 'wagglydbaccount (Core (SQL))' > click 'Copy Connection String'

View (menu bar) > Command Pallete > type and select:

    Azure Functions: Add New Setting...
    
>Resource: wagglyFunctions

>App Setting Name:

    CosmosDbConnectionSetting

>Value: [paste the connection string]

Then,

View (menu bar) > Command Pallete > type and select:

    Download Remote Settings...
    
>Resource: wagglyFunctions
>
>Overwrite: Yes to all
>

>Note: The connection string in 'Waggly/api/local.settings.json' has been generated and 'function_app.py''s connection settings should now be accurate.

---
**6. Deploy & Commit Changes**
    
Azure tab > Resources > Expand 'Function App' > right click 'wagglyFunctions' > choose 'Deploy to Function App...'

Then,
    
Source Control tab > type [commit message] > click commit > click sync

---
**7. Visit Web Application**

Open Azure portal at:

    https://portal.azure.com/#home
    
>Open Static Web Apps
>
>Open Waggly
>
>The overview tab contains a URL to the web application
