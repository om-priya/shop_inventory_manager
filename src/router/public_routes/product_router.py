from flask_smorest import Blueprint, abort
from flask.views import MethodView
from flask import jsonify
from controller import user_controller
import sqlite3
from response_class.response_format import SuccessResponse, ErrorResponse
from flask_jwt_extended import get_jwt

blp = Blueprint(
    "Fetch-Products",
    __name__,
    url_prefix="/api/v1/products",
    description="Fetching Products for Users/Client",
)


@blp.route("/")
class AllProducts(MethodView):
    def get(self):
        try:
            products = user_controller.show_products()
            if not products:
                abort(404, {"message": "No data found"})
            return jsonify({"data": products})
        except sqlite3.Error:
            pass
        except Exception:
            pass


@blp.route("/<string:product_id>")
class ProductById(MethodView):
    def get(self, product_id):
        try:
            product = user_controller.get_product_by_id_public(product_id)
            if not product:
                abort(404, {"message": "No data found"})
            return jsonify({"data": product})
        except sqlite3.Error:
            pass
        except Exception:
            pass
