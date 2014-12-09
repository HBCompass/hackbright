from flask import Flask, render_template, redirect, request, flash, g
from flask import session as session
import model
from form import SignUpForm
import api

app = Flask(__name__)

app.secret_key = '\xc1\xe2=\x1b\x8e\xdc\xfdbq\xdaKuO*}g\xfd'


@app.before_first_request
def setup_session():
    session.setdefault("logged_in", False)
    session.setdefault("user_id", None)

@app.before_request
def get_user():
    if session.get("user_id") is not None:
        g.logged_in = True
    else:
        g.logged_in = False

@app.route("/")
def index():
    user_list = model.session.query(model.User).limit(50).all()
    return render_template("user_list.html", users=user_list)

@app.route("/signup")
def sign_up():
    # Sign up form to add new user to database

    #also: need to check if input fields are valid
    #invalid entries redirect back to sign_up 
    #flash "please enter valid data for so and so"
    return render_template("sign_up.html")

# @app.route("/wtf")
# def wtf():
#     form = SignUpForm()
#     return render_template("signup.html", form=form)

# @app.route("/wtf", methods=["POST"])
# def wtf_validate():
#     print "Request:", request
#     if request.form:
#     # print "POST:", request.get("POST")
#         print "Form:", request.form
#         form = SignUpForm() #i don't know what this needs
#         form.email = request.form.get("email")
#         form.password = request.form.get("password")
#         form.age = int(request.form.get("age"))
#         form.zipcode = request.form.get("zipcode")
#         # form.gender = request.form.get("gender")
#         if form.validate():
#             return 'Form validates!' 
#     return ">:("

@app.route("/signup", methods=["POST"])
def process_signup():
    #processess signup form and redirects to ??? if successful

    #if any values are null
    #flash("please fill out all fields")
    #redirect back to /signup (GET)

    for value in request.form.values():
        if value == "": 
            flash("Please fill out all fields.")
            return redirect("/signup")

    user_check = api.get_user_by_email(request.form.get("email"))
    print "user_check", user_check
    if user_check:
        flash("Email already in use.")
        return redirect ('/signup')

    new_user = model.User()
    new_user.form_user(request.form)

    #insert that user into the database
    # model.session.add(new_user)
    # model.session.commit()

    #redirect to login page 
    flash('Thanks for singing up! Please login!')
    return redirect("/login")



@app.route("/login")
def login():
    # Login form 
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def process_login():
    #processess login form and redirects to ??? if successful
    email = request.form.get("email")
    password = request.form.get("password")
    if api.check_login(email, password): #login successful 
        flash('login successful')
        return redirect("/")
    else: #login unsuccessful 
        flash('login unsuccessful')
        return redirect("/login")

@app.route("/logout")
def logout():
    api.logout()
    flash('logout successful')
    return redirect("/login")


@app.route("/user/<int:id>")
def display_movie_ratings_by_user(id):
    # Returns user's movie ratings
    current_user = api.get_user_from_db(id)
    user_ratings = current_user.ratings #list of rating objects
    return render_template("user.html", user_ratings=user_ratings) #make this

@app.route("/ratemovie/<int:id>")
def rate_movie(id):
    #check if user logged in 
    if g.logged_in == False:
        flash("Please log in to rate a movie.")
        return redirect("/login")
    else:
        #when logged in, add or update rating for movie
        movie = api.get_movie_by_id(id)
        rating = api.get_users_rating_by_movie_id(session.get("user_id"), id)
        user = api.get_user_from_db(session.get('user_id'))
        prediction = None
        template_rating = None;
        if rating:
            template_rating = rating.rating
        else:
            prediction = user.predict_rating(movie)
        return render_template("rate_movie.html", movie=movie, template_rating=template_rating, prediction=prediction)

@app.route("/ratemovie/<int:id>", methods=["POST"])
def make_new_rating(id):
    user_id = session.get("user_id")
    rating = api.get_users_rating_by_movie_id(user_id, id)
    num_stars = request.form.get("stars")
    if rating is not None:
        rating.rating = num_stars
    else:
        rating = model.Rating()
        rating.rating = num_stars
        rating.movie_id = id
        rating.user_id = user_id
        model.session.add(rating)


    print rating
    
    model.session.commit()
    flash("Your rating has been recorded! Here are all the movies you have rated!")
    return redirect("/user/" + str(session.get("user_id")))






if __name__ == "__main__":
    app.run(debug = True)

