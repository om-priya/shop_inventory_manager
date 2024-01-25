from flask import Flask
from flask_smorest import Api
from flask_jwt_extended import JWTManager
from router.public_routes.product_router import blp as PublicProductRouter
from router.public_routes.auth_router import blp as AuthRouter
from router.private_routes.admin_product_router import blp as AdminProductRouter
from router.private_routes.admin_sales_router import blp as AdminSalesRouter

app = Flask(__name__)

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Inventory REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
app.config["JWT_SECRET_KEY"] = "jdcjdnjndkazkmwksndoenkskxmsndennxkasmxklndojnwjiue7tdysxhsnkzmwidusbx"


jwt = JWTManager(app)

api = Api(app)
api.register_blueprint(PublicProductRouter)
api.register_blueprint(AuthRouter)
api.register_blueprint(AdminProductRouter)
api.register_blueprint(AdminSalesRouter)

app.run(debug=True, port=5000)
