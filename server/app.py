from flask import Flask, jsonify
from flask_migrate import Migrate
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  
    
 
    from .models import db, jwt, init_app
    init_app(app)
    migrate = Migrate(app, db)
    
  
    from .controllers.auth_controller import auth_bp
    from .controllers.guest_controller import guest_bp
    from .controllers.episode_controller import episode_bp
    from .controllers.appearance_controller import appearance_bp
    
    app.register_blueprint(auth_bp, url_prefix='/api')
    app.register_blueprint(guest_bp, url_prefix='/api')
    app.register_blueprint(episode_bp, url_prefix='/api')
    app.register_blueprint(appearance_bp, url_prefix='/api')
    
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)