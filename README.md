                  Web Application Self-deployment Instructions
                            
Working prototype:
    
    https://lively-pond-0095bf203.4.azurestaticapps.net

---

**1. Cloning the project**

On your PC, create a folder named:

    Waggly

Inside the 'Waggly' folder, create a folder named:

    src
    
In the GitHub repository, open the 'src' folder located at:
    
    https://github.com/JaidenBarnes/Waggly/tree/main/src

Right click + 'Download Linked File' for both the 'index.html' & 'styles.css' files then,

Move both files into the previously created local 'src' folder

Your local folder should now contain:
>Waggly > src > index.html & styles.css

Open Visual Studio Code and open the Waggly folder to begin the project


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

Ensure your GitHub repository is building the application under GitHub.com > [Waggly] > Actions

---
**7. Visit Web Application**

Open Azure portal at:

    https://portal.azure.com/#home
    
>Open Static Web Apps
>
>Open Waggly
>
>The overview tab contains a URL to the web application, open this link.
