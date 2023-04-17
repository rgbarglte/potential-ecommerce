from flask import Flask

app = Flask(__name__)

# Configuración de la aplicación Flask
app.config['SECRET_KEY'] = 'mysecretkey'

# Registrar los controladores
from administration import views as administration_views
from frontend import views as frontend_views
from api import views as api_views

app.register_blueprint(administration_views.administration_blueprint)
app.register_blueprint(frontend_views.frontend_blueprint)
app.register_blueprint(api_views.api_blueprint)

if __name__ == '__main__':
    app.run()

