from fastapi import APIRouter
from fastapi.responses import JSONResponse

from controller import user_controller
import sqlite3

product_router = APIRouter(prefix="/api/v1/products")


@product_router.get("/")
async def get_all_products():
    try:
        products = user_controller.show_products()
        if not products:
            return JSONResponse(status_code=404, content={"message": "No data found"})
        return JSONResponse(status_code=200, content={"data": products})
    except sqlite3.Error:
        return JSONResponse(
            status_code=500, content={"message": "something went wrong in db"}
        )
    except Exception:
        return JSONResponse(
            status_code=500, content={"message": "something went wrong"}
        )


@product_router.get("/{product_id}")
async def get_single_product(product_id):
    try:
        product = user_controller.get_product_by_id_public(product_id)
        if not product:
            JSONResponse(status_code=404, content={"message": "No data found"})
        return JSONResponse(status_code=200, content={"data": product})
    except sqlite3.Error:
        return JSONResponse(
            status_code=500, content={"message": "something went wrong in db"}
        )
    except Exception:
        return JSONResponse(
            status_code=500, content={"message": "something went wrong"}
        )
