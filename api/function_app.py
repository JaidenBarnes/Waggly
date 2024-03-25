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
        return func.HttpResponse(status_code = 400)





@app.function_name(name="postregisterwoofer")
@app.route(route="postregisterwoofer", auth_level=func.AuthLevel.ANONYMOUS)
@app.cosmos_db_output(arg_name="WooferDocument", database_name="waggly-database", container_name="waggly_container", connection="CosmosDbConnectionSetting")

def createWoofer(req: func.HttpRequest, WooferDocument: func.Out[func.Document]) -> func.HttpResponse:
    woofer_id = str(uuid.uuid4())
    woofer_name = req.params.get('woofername')
    woofer_breed = req.params.get('wooferbreed')
    owner_firstname = req.params.get('ownerfirstname')
    owner_lastname = req.params.get('ownerlastname')
    owner_housenumber = req.params.get('ownerhousenumber')
    owner_location = req.params.get('ownerlocation')
    owner_postcode = req.params.get('ownerpostcode')
    owner_phonenumber = req.params.get('ownerphonenumber')
    owner_email = req.params.get('owneremail')


    if woofer_name and woofer_breed and owner_firstname and owner_lastname and owner_housenumber and owner_location and owner_postcode and owner_phonenumber and owner_email:
        WooferDocument.set(func.Document.from_dict({"id": woofer_id, "woofername": woofer_name, "wooferbreed": woofer_breed, "ownerfirstname": owner_firstname, "ownerlastname": owner_lastname, "ownerhousenumber": owner_housenumber, "ownerlocation": owner_location, "ownerpostcode": owner_postcode, "ownerphonenumber": owner_phonenumber, "owneremail": owner_email}))
        return func.HttpResponse(f"stored details: {woofer_id}\n{woofer_name}\n{woofer_breed}\n{owner_firstname}\n{owner_lastname}\n{owner_housenumber}\n{owner_location}\n{owner_postcode}\n{owner_phonenumber},\n{owner_email}")
    else:
        return func.HttpResponse("unable to run function you melt", status_code = 200)

