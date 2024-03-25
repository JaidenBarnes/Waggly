import azure.functions as func
import uuid

app = func.FunctionApp()

@app.function_name(name="postregisterwalker")
@app.route(route="postregisterwalker", auth_level=func.AuthLevel.ANONYMOUS)
@app.cosmos_db_output(arg_name="WalkerDocument", database_name="waggly-database", container_name="waggly_container", connection="CosmosDbConnectionSetting")

def createWalker(req: func.HttpRequest, WalkerDocument: func.Out[func.Document]) -> func.HttpResponse:
    walker_id = str(uuid.uuid4())
    walker_firstname = req.params.get('walkerfirstname')
    walker_lastname = req.params.get('walkerlastname')
    walker_location = req.params.get('walkerlocation')
    walker_phonenumber = req.params.get('walkerphonenumber')
    walker_email = req.params.get('walkeremail')

    if walker_firstname and walker_lastname and walker_location and walker_phonenumber and walker_email:
        WalkerDocument.set(func.Document.from_dict({"id": walker_id, "walker_firstname": walker_firstname, "walker_lastname": walker_lastname, "walker_location": walker_location, "walker_phonenumber": walker_phonenumber, "walker_email": walker_email}))
        return func.HttpResponse(f"stored details: {walker_id}\n{walker_firstname}\n{walker_lastname}\n{walker_location}\n{walker_phonenumber}\n{walker_email}\n")
    else:
        return func.HttpResponse("unable to run function you melt", status_code = 200)

