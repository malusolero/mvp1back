import datetime
from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect, request
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Item, Type, Cabinet

from schemas.cabinet import CabinetPathSchema, CabinetSchema, ListCabinetsSchema, return_cabinets
from schemas.error import ErrorSchema
from schemas.type import ListTypesSchema, TypePathSchema, TypeSchema, return_types
from schemas.item import ItemSearchSchema, ItemQuery, ItemSchema, ListItemSchema, return_items, return_item

from logger import logger

from flask_cors import CORS

info = Info(title="KOC API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Docs tags
home_tag = Tag(name="Docs", description="Select docs between: Swagger, Redoc or RapiDoc")
cabinet_tag = Tag(name="Cabinet", description="Create, List, Update and Delete 'Cabinet' entity" )
type_tag = Tag(name="Type", description="Create, List, Update and Delete 'Type' entity")
item_tag = Tag(name="Item", description="Create, List, Update and Delete 'Item' entity")

@app.get('/', tags=[home_tag])
def home():
    """ Redirects for /openapi, screen for choosing the documentation.
    """
    return redirect('/openapi')

@app.get('/cabinet', tags=[cabinet_tag], responses={"200": ListCabinetsSchema, "404": ErrorSchema})
def get_cabinets():
    """ Returns the list of cabinets present in the database
    """
    logger.debug("Getting cabinets...")
    session = Session()
    cabinets = session.query(Cabinet).all()

    if not cabinets:
        return { "cabinets": []}, 200

    else:
        logger.debug(f"%d cabinets" % len(cabinets))
        print(cabinets)
        return return_cabinets(cabinets), 200

@app.post('/cabinet', tags=[cabinet_tag], responses={"200": CabinetSchema, "409": ErrorSchema, "400": ErrorSchema})
def create_cabinet(form: CabinetSchema):
    """ Create a cabinet with the received arguments
    """

    print(f"form '{form.position}'")

    cabinet = Cabinet(position=form.position)
    try:
        session = Session()
        session.add(cabinet)
        session.commit()
        return { "cabinet": { "id": cabinet.id, "position": cabinet.position}}

    except IntegrityError as e:
        error_msg = "Cabinet with received position already exists :/"
        return {"mesage": error_msg}, 409

    except Exception as e:
        error_msg = "Error happened when trying to create a new cabinet inside database :/"
        return {"mesage": error_msg}, 400

@app.put('/cabinet/<int:cabinet_id>', tags=[cabinet_tag], responses={"200": CabinetSchema, "404": ErrorSchema})
def update_cabinet(path: CabinetPathSchema, body: CabinetSchema):
    """ Update the cabinet for given path cabinet_id
    """

    print(f"path '{path.cabinet_id}'")
    print(body)

    session = Session()
    updated = session.query(Cabinet).filter(Cabinet.id == path.cabinet_id).update({ "position": body.position})
    session.commit()

    if updated:
        return {"message": 'Cabinet updated', "id": path.cabinet_id}, 200
    else:
        error_msg = 'Cabinet not found in database'
        return {"message": error_msg}, 404

@app.delete('/cabinet/<int:cabinet_id>', tags=[cabinet_tag], responses={"200": CabinetSchema, "404": ErrorSchema})
def delete_cabinet(path: CabinetPathSchema):
    """ Delete the cabinet for given path cabinet_id
    """

    print(f"path '{path.cabinet_id}'")

    session = Session()
    updated = session.query(Cabinet).filter(Cabinet.id == path.cabinet_id).delete()
    session.commit()

    if updated:
        return {"message": 'Cabinet deleted', "id": path.cabinet_id}, 200
    else:
        error_msg = 'Cabinet not found in database'
        return {"message": error_msg}, 404

@app.get('/type', tags=[type_tag], responses={"200": ListTypesSchema, "404": ErrorSchema })
def get_types():
    """ Returns the list of types present in the database.
    """
    logger.debug("Getting types...")
    session = Session()
    types = session.query(Type).all()

    if not types:
        return { "types": []}, 200

    else:
        logger.debug(f"%d types" % len(types))
        print(types)
        return return_types(types), 200

@app.post('/type', tags=[type_tag], responses={"200": TypeSchema, "409": ErrorSchema, "400": ErrorSchema})
def create_type(form: TypeSchema):
    """ Create a new type with the received arguments
    """

    print(f"form '{form.name}'")

    type = Type(name=form.name)
    try:
        session = Session()
        session.add(type)
        session.commit()
        return { "type": { "id": type.id, "name": type.name}}

    except IntegrityError as e:
        error_msg = "Type with received name already exists :/"
        return {"mesage": error_msg}, 409

    except Exception as e:
        error_msg = "Error happened when trying to create a new type inside database :/"
        return {"mesage": error_msg}, 400

@app.put('/type/<int:type_id>', tags=[type_tag], responses={"200": TypeSchema, "404": ErrorSchema})
def update_type(path: TypePathSchema, body: TypeSchema):
    """ Update the type for given path type_id
    """

    print(f"path '{path.type_id}'")
    print(body)

    session = Session()
    updated = session.query(Type).filter(Type.id == path.type_id).update({ "name": body.name})
    session.commit()

    if updated:
        return {"message": 'Type updated', "id": path.type_id}, 200
    else:
        error_msg = 'Type not found in database'
        return {"message": error_msg}, 404

@app.delete('/type/<int:type_id>', tags=[type_tag], responses={"200": TypeSchema, "404": ErrorSchema})
def delete_type(path: TypePathSchema):
    """ Delete the type for given path type_id
    """

    print(f"path '{path.type_id}'")

    session = Session()
    updated = session.query(Type).filter(Type.id == path.type_id).delete()
    session.commit()

    if updated:
        return {"message": 'type deleted', "id": path.type_id}, 200
    else:
        error_msg = 'type not found in database'
        return {"message": error_msg}, 404


@app.get('/item', tags=[item_tag], responses={"200": ListItemSchema, "404": ErrorSchema})
def get_items(query: ItemQuery):
    """ Returns the list of items. If cabinet_id is received by parameter, then returns the items for the given cabinet_id
    """
    args = request.args
    cabinet_id = args.get('cabinet_id')
    print(cabinet_id)
    logger.debug("Getting items...")
    session = Session()
    items = session.query(Item).filter(Item.cabinet_id == cabinet_id).all() if  cabinet_id else session.query(Item).all()
    for item in items:
        print(item.name)

    if not items:
        return { "items": []}, 200

    else:
        logger.debug(f"%d items" % len(items))
        print(items)
        return return_items(items), 200

@app.post('/item', tags=[item_tag], responses={"200": ItemSchema, "409": ErrorSchema, "400": ErrorSchema})
def create_item(form: ItemSchema):
    """ Create a new item with the received arguments
    """

    print(f"form '{form.name}'")
    session = Session()
    cabinet = session.query(Cabinet).filter(Cabinet.id ==  form.cabinet_id).first()


    if( cabinet is None ): 
        return { "message": 'There is not a cabinet present in the database with the given cabinet_id'}, 400
    
    type = session.query(Type).filter(Type.id == form.type_id).first()

    if( type is None ):
        return { "message": 'There is not a type present in the database with the given type_id'}, 400

    try:
        item = Item(name=form.name, brand=form.brand, amount=form.amount, weight=form.weight,\
            expiry_date=form.expiry_date,\
            cabinet_id=form.cabinet_id, type_id=form.type_id)
        session = Session()
        session.add(item)
        session.commit()
        return return_item(item)
        
    except IntegrityError as e:
        error_msg = "Item already exists in this cabinet :/"
        return {"mesage": error_msg}, 409

    except Exception as e:
        print(e)
        error_msg = "Error happened when trying to create a new type inside database :/"
        return {"mesage": error_msg}, 400

@app.put('/item/', tags=[item_tag], responses={"200": ItemSchema, "404": ErrorSchema, "409": ErrorSchema})
def update_item(query: ItemSearchSchema, form: ItemSchema):
    """ Update the item for given item name
    """

    args = request.args
    name = args.get('name')
    print(f"path '{name}'")

    try:
        session = Session()
        updated = session.query(Item).filter(Item.name == name).update(\
            { "name": form.name, "brand": form.brand, "amount": form.amount,\
                "expiry_date": form.expiry_date,\
                    "cabinet_id": form.cabinet_id, "type_id": form.type_id})
        session.commit()

        if updated:
            return {"message": 'Item updated', "name": name}, 200
        else:
            error_msg = 'Item not found in database'
            return {"message": error_msg}, 404
    
    except IntegrityError as e:
        error_msg = "Item with this name already exists :/"
        return {"mesage": error_msg}, 409

    except Exception as e:
        error_msg = "Error happened when trying to update the item inside database :/"
        return {"mesage": error_msg}, 400


@app.delete('/item', tags=[item_tag], responses={"200": ItemSchema, "404": ErrorSchema, "409": ErrorSchema})
def delete_item(query: ItemSearchSchema):
    """ Delete the item for given item name
    """
    args = request.args
    name = args.get('name')
    print(f"path '{name}'")


    session = Session()
    updated = session.query(Item).filter(Item.name == name).delete()
    session.commit()


    if updated:
        return {"message": 'Item deleted', "name": name}, 200
    else:
        error_msg = 'Item not found in database'
        return {"message": error_msg}, 404
