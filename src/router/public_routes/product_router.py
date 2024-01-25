from fastapi import APIRouter

# from controller import user_controller
# import sqlite3
# from response_class.response_format import SuccessResponse, ErrorResponse

product_router = APIRouter(prefix="/api/v1/products")


@product_router.get("/")
async def get_all_products():
    return {"message": "All Products"}

@product_router.get("/{product_id}")
async def get_single_product(product_id):
    return {"message": f"Single Product with id is {product_id}"}


# class AllProducts(MethodView):
#     def get(self):
#         try:
#             products = user_controller.show_products()
#             if not products:
#                 abort(404, {"message": "No data found"})
#             return jsonify({"data": products})
#         except sqlite3.Error:
#             pass
#         except Exception:
#             pass



# class ProductById(MethodView):
#     def get(self, product_id):
#         try:
#             product = user_controller.get_product_by_id_public(product_id)
#             if not product:
#                 abort(404, {"message": "No data found"})
#             return jsonify({"data": product})
#         except sqlite3.Error:
#             pass
#         except Exception:
#             pass
