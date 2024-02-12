from fastapi import APIRouter, Depends, Path
from fastapi.responses import JSONResponse
from typing import Annotated
import sqlite3
from router.public_routes.auth_router import get_user_id_from_token

from controller.admin_product_controller import (
    show_products,
    get_product_by_id,
    delete_product,
    update_product,
)
from schema.schema import ProductSchema
from models.product import Products


admin_product_router = APIRouter(prefix="/api/v1/admin")

product_id_schema = Annotated[str, Path(pattern=r"^[A-Za-z0-9]{8}$")]


@admin_product_router.get("/products")
async def get_all_products(user_id: Annotated[str, Depends(get_user_id_from_token)]):
    try:
        products = show_products(user_id)

        if not products:
            return JSONResponse(
                status_code=404,
                content={"success": False, "message": "Product Not Found"},
            )

        return JSONResponse({"success": True, "data": products})
    except sqlite3.Error:
        return JSONResponse(
            status_code=500,
            content={"success": False, "message": "something went wrong in db"},
        )
    except Exception:
        return JSONResponse(
            status_code=500,
            content={"success": False, "message": "something went wrong"},
        )


@admin_product_router.post("/products")
async def create_product(
    user_id: Annotated[str, Depends(get_user_id_from_token)],
    product_info: ProductSchema,
):
    try:
        product_obj = product_info.model_dump()
        product_obj["user_id"] = user_id

        new_product = Products(product_obj)
        new_product.save_product()
        return JSONResponse(
            status_code=201, content={"success": True, "message": "New product created"}
        )
    except sqlite3.Error:
        return JSONResponse(
            status_code=500,
            content={"success": False, "message": "something went wrong in db"},
        )
    except Exception:
        return JSONResponse(
            status_code=500,
            content={"success": False, "message": "something went wrong"},
        )


@admin_product_router.get("/products/{product_id}")
async def get_single_product(
    product_id: product_id_schema,
    user_id: Annotated[str, Depends(get_user_id_from_token)],
):
    try:
        product = get_product_by_id(product_id, user_id)

        if not product:
            return JSONResponse(
                status_code=404,
                content={"success": False, "message": "Product Not Found"},
            )

        return JSONResponse(status_code=200, content={"success": True, "data": product})
    except sqlite3.Error:
        return JSONResponse(
            status_code=500,
            content={"success": False, "message": "something went wrong in db"},
        )
    except Exception:
        return JSONResponse(
            status_code=500,
            content={"success": False, "message": "something went wrong"},
        )


@admin_product_router.put("/products/{product_id}")
async def put_update_product(
    product_id: product_id_schema,
    product_info: ProductSchema,
    user_id: Annotated[str, Depends(get_user_id_from_token)],
):
    try:
        update_product(product_id, user_id, product_info.model_dump())
        return JSONResponse(
            status_code=200,
            content={
                "success": True,
                "message": "Products with Id Updated Successfully",
            },
        )
    except ValueError:
        return JSONResponse(
            status_code=404,
            content={"success": False, "message": "Product Not Found"},
        )
    except sqlite3.Error as e:
        print(e)
        return JSONResponse(
            status_code=500,
            content={"success": False, "message": "something went wrong in db"},
        )
    except Exception:
        return JSONResponse(
            status_code=500,
            content={"success": False, "message": "something went wrong"},
        )


@admin_product_router.delete("/products/{product_id}")
async def delete_product_route(
    product_id: product_id_schema,
    user_id: Annotated[str, Depends(get_user_id_from_token)],
):
    try:
        delete_product(product_id, user_id)
        return JSONResponse(
            status_code=200,
            content={"success": True, "data": "Product deleted Successfully"},
        )
    except ValueError:
        return JSONResponse(
            status_code=404,
            content={"success": False, "message": "Product Not Found"},
        )
    except sqlite3.Error:
        return JSONResponse(
            status_code=500,
            content={"success": False, "message": "something went wrong in db"},
        )
    except Exception:
        return JSONResponse(
            status_code=500,
            content={"success": False, "message": "something went wrong"},
        )
