from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import ItemSchema,ItemUpdateSchema
from sqlalchemy.exc import SQLAlchemyError
from flask_jwt_extended import jwt_required,get_jwt
from db import db
from models import ItemModel

blp = Blueprint("items",__name__,description="items blueprint")

@blp.route("/items")
class Items(MethodView):

    @blp.response(200, ItemSchema(many=True))
    def get(self):
        return ItemModel.query.all()
    

    @jwt_required()
    @blp.arguments(ItemSchema)
    @blp.response(201, ItemSchema)
    def post(self,item_data):
        item = ItemModel(**item_data)

        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the item.")

        return item
        

@blp.route("/item/<string:id>")
class itemList(MethodView):

    @jwt_required()
    @blp.response(200, ItemSchema)
    def get(self,id):
        item = ItemModel.query.get_or_404(id)
        return item
    
    @jwt_required()
    def delete(self,id):

        jwt = get_jwt()
        if not jwt.get("is_admin"):
           abort(401, message="Admin privilege required.")
        item = ItemModel.query.get_or_404(id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "item deleted"}, 200
    
    @jwt_required()    
    @blp.arguments(ItemUpdateSchema)
    @blp.response(201, ItemSchema)
    def put(self, item_data, id):
        item = ItemModel.query.get(id)
        if item:
            item.name = item_data["name"]
            item.price = item_data["price"]
        else:
            item = ItemModel(id = id,**item_data)
        
        db.session.add(item)
        db.session.commit()

        return item
        

