from flask import Flask
def create_app():
  app = Flask( name )
  from .routes import main
  app.reglster_blueprint(main)
  return app
