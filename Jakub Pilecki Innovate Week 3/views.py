from flask import render_template, Blueprint, request

views = Blueprint("views", __name__)

#? VIEW IN THIS ISTANCE IS A BLUEPRINT

task_list =[]
#? ^^ CREATE AN EMPTY LIST ^^
#? #####################################
@views.route("/") #? THIS IS DERECTORY 
def home():
    return render_template("index.html")

@views.route("/contact") #? THIS IS DERECTORY 
def contact():
    return render_template("contact.html")

@views.route("/about") #? THIS IS DERECTORY 
def about():
    return render_template("about.html")

@views.route("/clothes")
def clothes():
    return render_template("clothes.html")

@views.route("/music")
def music():
    return render_template("music.html")

# @views.route("/todos", methods=["GET", "POST"])
# def todos():
#     if request.method =="POST":
#         task = request.form.get("task-input")
#         task_list.append(task)
#         print(task_list)
#         return render_template("todos.html", task_list=task_list)
#     return render_template("todos.html")

@views.route("/tshirt")
def tshirt():
    return render_template("tshirt.html")

@views.route("/hoodies")
def hoodies():
    return render_template("hoodies.html")

@views.route("/caps")
def caps():
    return render_template("caps.html")

# @views.route("/cart")
# def cart():
#     return render_template("cart.html")