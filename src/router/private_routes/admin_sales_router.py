from flask_smorest import Blueprint
from flask.views import MethodView
from flask_jwt_extended import jwt_required, get_jwt
from controller.helper.check_admin import check_admin
from schema.schema import GetSalesSchema
from transactions.transaction import Transaction
from flask import jsonify

blp = Blueprint(
    "Sales", __name__, url_prefix="/api/v1/admin", description="Operations on sales"
)


@blp.route("/sales")
class Sales(MethodView):
    @blp.arguments(GetSalesSchema)
    @jwt_required()
    @check_admin
    def get(self, sales_schema):
        try:
            jwt = get_jwt()
            jwt_sub = jwt.get("sub")
            user_id = jwt_sub.get("user_id")
            year = sales_schema["year"]

            sales_info = Transaction.get_sales(user_id, year)

            jsonify({"success": True, "data": sales_info})

        except Exception:
            pass
