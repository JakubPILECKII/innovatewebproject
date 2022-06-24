from flask import Flask, Blueprint

from views import views
#? WE IMPORTM VIEWS FROM VIEWS FILE

app = Flask(__name__)
#? WE INSANTIATE THE APP OBJECT 

app.register_blueprint(views)
#? WE REGISTER THE VIEWS BLUEPRINT

if __name__ == "__main__":
    #? Checking is flask app is working with global codespace
    app.run(debug=True, port=8000)
