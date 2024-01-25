from flask_smorest import Blueprint
from flask.views import MethodView
from flask_jwt_extended import jwt_required, get_jwt
from controller.helper.check_admin import check_admin
from controller.admin_product_controller import (
    show_products,
    get_product_by_id,
    delete_product,
    update_product,
)
from flask import jsonify
from schema.schema import ProductSchema, ProductIdSchema
from products.product import Products

blp = Blueprint("Admin_Products", __name__, url_prefix="/api/v1/admin")


@blp.route("/products")
class AdminProducts(MethodView):
    @jwt_required()
    @check_admin
    def get(self):
        try:
            jwt = get_jwt()
            user_id = jwt.get("sub").get("user_id")

            products = show_products(user_id)

            if not products:
                raise Exception

            return jsonify({"data": products})
        except Exception:
            pass

    @blp.arguments(ProductSchema)
    @jwt_required()
    @check_admin
    def post(self, product_obj):
        try:
            jwt = get_jwt()
            user_id = jwt.get("sub").get("user_id")
            product_obj["user_id"] = user_id

            new_product = Products(product_obj)
            new_product.save_product()

            return jsonify({"data": "New product created"})
        except Exception:
            pass


@blp.route("/products/<string:product_id>")
class AdminProductsById(MethodView):
    @jwt_required()
    @check_admin
    def get(self, product_id):
        try:
            jwt = get_jwt()
            user_id = jwt.get("sub").get("user_id")

            product = get_product_by_id(product_id, user_id)

            return jsonify({"data": product})
        except Exception:
            pass

    @blp.arguments(ProductSchema)
    @blp.arguments(ProductIdSchema)
    @jwt_required()
    @check_admin
    def put(self, product_updated_data, product_id_obj):
        try:
            jwt = get_jwt()
            user_id = jwt.get("sub").get("user_id")
            product_id = product_id_obj["product_id"]
            update_product(product_id, user_id, product_updated_data)
            return {"code": 200, "message": "Products with Id Updated Successfully"}
        except Exception:
            pass

    @jwt_required()
    @check_admin
    def delete(self, product_id):
        try:
            jwt = get_jwt()
            user_id = jwt.get("sub").get("user_id")

            delete_product(product_id, user_id)

            return jsonify({"data": "Product deleted Successfully"})
        except Exception:
            pass
