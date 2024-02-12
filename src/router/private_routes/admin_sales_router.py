from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from router.public_routes.auth_router import get_user_id_from_token
from schema.schema import GetSalesSchema
import sqlite3
from schema.schema import GetSalesSchema
from models.transaction import Transaction


sales_router = APIRouter(prefix="/api/v1/admin")


@sales_router.get("/sales")
async def get_sales(
    sales_info: GetSalesSchema, user_id: Annotated[str, Depends(get_user_id_from_token)]
):
    try:
        year = sales_info.year
        sales_info = Transaction.get_sales(user_id, year)

        if not sales_info:
            return JSONResponse(
                status_code=404, content={"success": False, "message": "No Data Found"}
            )
        return JSONResponse(
            status_code=200, content={"success": True, "data": sales_info}
        )
    except sqlite3.Error as e:
        print(e)
        return JSONResponse(
            status_code=500,
            content={"success": False, "message": "something went wrong in db"},
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"success": False, "message": "Something went wrong"},
        )
