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

        return JSONResponse({"success": True, "data": sales_info})
    except sqlite3.Error as e:
        print(e)
        return JSONResponse(
            status_code=500, content={"message": "something went wrong in db"}
        )
    except Exception as e:
        print(e)
        return JSONResponse(
            status_code=500, content={"message": "Something went wrong"}
        )
