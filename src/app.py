from fastapi import FastAPI
from router.public_routes.product_router import product_router
from router.public_routes.auth_router import auth_router
from router.private_routes.admin_sales_router import sales_router
from router.private_routes.admin_product_router import admin_product_router
from config.product_query import ProductQuery
from config.user_query import UserQuery
from config.transaction_query import TransactionQuery
from database.db_access import DbAccess

app = FastAPI()

DbAccess.write_to_database(ProductQuery.CREATE_PRODUCT_TABLE)
DbAccess.write_to_database(UserQuery.CREATE_USER_TABLE)
DbAccess.write_to_database(TransactionQuery.CREATE_TABLE)

app.include_router(product_router)
app.include_router(auth_router)
app.include_router(sales_router)
app.include_router(admin_product_router)
