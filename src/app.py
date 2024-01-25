from fastapi import FastAPI
from router.public_routes.product_router import product_router
from router.public_routes.auth_router import auth_router
from router.private_routes.admin_sales_router import sales_router
from router.private_routes.admin_product_router import admin_product_router

app = FastAPI()

app.include_router(product_router)
app.include_router(auth_router)
app.include_router(sales_router)
app.include_router(admin_product_router)


@app.get("/")
async def server_check():
    return {"message": "Server is running"}
