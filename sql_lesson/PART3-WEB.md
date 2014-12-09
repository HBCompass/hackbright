Going Online
============
A database is the last piece of technology we need before going online. In this segment, we'll take our database online, turning it into a web application using flask, our preferred web framework.

A State of Being
----------------
A database introduces an important concept to our programs. Until now, our programs have had no long-term memory. That is to say, if you ran our calculator from earlier, quit it, then ran it again, it would run exactly the same as if it were run for the first time: two plus two will always be four. 

The database changes all that. When we run our database-backed program, asking it for a student's grades will give different results over time as you add more data. This is called 'state', when the program reacts to input and responds differently. On top of that, the state is preserved when our program quits and restarts. This is called 'persistence'. Both of these things are provided by the database. 

It is of interest to note that our program is written as if it is stateless. Our database-backed application is fundamentally identical to our calculator in terms of program structure. We will abuse this fact as much as we can when writing web applications, as it makes our lives easier.

But First, A Detour Into VirtualEnv
-----------------------------------
Until now, we have not spent any time concerning ourselves with our 'environment'. On our machines, the appropriate version of python is already installed, we need only type the word to invoke it. Additionally, whenever we need a module, most of the time we can safely import it without question, as our machines have been prepared for these eventualities.

The thing is, even though it may seem like it, our computers are not our own. Modern unix-based operating systems are multi-user systems, which means multiple users can be logged in at the same time. In fact, every time you open a new terminal window, you're essentially logging in again, once in each terminal.

Given that there may be a multitude of users logged onto your system (over the network, most likely), we must generally be careful not to clobber other users' programs and settings. If you install python3 in a multi-user setting, you'll likely anger those who rely on python2.7.

In practice, the only other 'user' you need to worry about angering is your operating system. It relies on certain software packages to be installed to operate correctly. Currently, both linux and OSX are dependent on very specific versions of python. On top of that, it relies on very specific versions of certain modules, so we can't just go upgrading and installing things willy-nilly. (In python, installing certain modules sometimes forces an upgrade of others.)

Enter the virtual environment. Essentially, a virtualenv is a python sandbox. It gives you, the user, a way to cordon off whichever version of python you want to use along with whatever modules you need. This virtual environment is specific to you, and there's no need to ask permission of the operating system (or the super user) to install new modules.

Here are the steps to using virtual environments:

1. Figure out how to create an environment. [Here's a hint](http://lmgtfy.com/?q=create+virtual+environment)
This basically creates a copy of python and all of the essential modules and puts it in a directory of your choice. Creation of a virtual environment is _free_. This means you should make as many as you need, usually one per project. Each of your projects will have different requirements, so don't be stingy and try to use one env for all of them. The directory you put your environment in is usually named 'env' under the top level of your project.
2. Activate your environment.
Once an environment is created, you need to activate it. Unless you activate an environment, it simply sits there, sad and alone. But more importantly, unless you activate it, you'll continue to use the OS-specific versions of python and its modules.
3. Install your modules.
Even if you don't appreciate the utility of being able to cordon off your python configuration, at the very least, you'll now enjoy the ability to install modules without having to ask for permission. Once your environment is activated, you can install new python modules with impunity. Note: impunity is not the name of the python module installer, that program is actually called pip.
4. Work!
As you write and test your code, make sure to run it inside a terminal that has a virtualenv activated. It is very easy to forget this. If your program raises an ImportError when running, you're probably not inside the activated environment. When you activate an environment, it leaves a visual cue on your command prompt, make sure to check for it if things aren't going correctly.
5. Deactivate your environment
Just kidding, unless you're specifically going to activate another environment for a different project, don't worry about deactivating. Just open another window for that project.


Sipping From the Flask
======================
For us to have a web application, we must first have a web server. Writing such a thing for every web application would be pure tedium and requires more than a modicum of specific knowledge about HTTP, so we leave it to the experts. Instead, we use something called a framework. A framework forces us into writing programs in a style different from what we've written before, so we'll look at that briefly.

So far, our programs have been 'imperative'. They have been a sequence of commands to be executed, one after the other. With enough time, all of them can be traced through the source, by which I mean we, as humans, can interpret the program, one line at a time, and enumerate all the functions that are called, and draw out a map of what happens.

With Flask, we do something different. We activate the framework, which is essentially a web server. Before we run it, we create a few functions, and we install the functions as 'handlers' for specific events.

First, let's see what happens when you run the framework without setting up handlers.

Put the following lines into a file named webapp.py, then run it, making sure your virtualenv is activated.

    from flask import Flask, render_template, request

    app = Flask(__name__)

    if __name__ == "__main__":
        app.run(debug=True)

You should see the following:

    Meringue:sql_lesson chriszf$ python webapp.py 
     * Running on http://127.0.0.1:5000/

If you try to access the webapp in your browser by going to http://127.0.0.1:5000/ or its alias, http://localhost:5000/, you will get nothing but 404 errors, indicating the url is not found. Before we can respond to any urls, we must first set up our event handlers.

We can consider the act of a user accessing a url on our web server an 'event'. We create handlers that respond to those events, and install them in our framework. When the framework is running, it listens for many different kinds of events. If one does come up that it's been waiting for, it responds by invoking the handler function assigned to that event type. Whatever the handler returns is then returned back to the browser that caused the event to happen.

### Hello World Wide Web
Because that phrase isn't out of date. Ahem.

First, we'll make the standard 'hello world' program, but output the results in our browser. Between the following lines, enter the following code:
    
    app = Flask(__name__)

    # Code goes here

    @app.route("/")
    def helloworld():
        return "Hello world"

    if __name__ == "__main__":
        app.run(debug=True)

If your app is still running in your terminal, kill it and restart it, then access http://localhost:5000/ in your browser. Tadaa, we're done.

### We're Not Done
Let's look at our hello world handler a little more closely.

    @app.route("/")
    def helloworld():
        return "Hello world"

There are three parts here: the url pattern decorator, the name of the handler, and the response of the handler.

The most mysterious part is the pattern 'decorator', the first line. Decorators follow this format:

    @decorator_name
    def my_function():
        ...

A decorator 'decorates' a function. For now, we can consider a decorator to be an annotation, adding metadata to a function. In this case, our metadata indicates that this function is a url handler, and further more, it responds to the url "/".

The name of the handler is mostly irrelevant for now. In flask, the return type of url handlers is a string. This fact will be important in a second.

### Output to the Browser
In all our previous programs, we could use the "print" command to output text to the screen.  For our web programs, printing to the screen doesn't make sense since the user can't see our screen - we want our output to go to the user's browser.

To talk to the user's browser, our program and the browser need to be able to speak the same language: HTTP or Hypertext Transfer Protocol (that's why we put "http://" in front of all our web requests).  Fortunatly for us, Flask knows all about how to do that.  All we have to do it make sure our functions *return* the text we want to send to the browser and let Flask handle getting it there.


### Wiring Up Our Database
Let's take a copy of our hackbright\_app.py file and put it in the same directory as our webapp.py. Take a moment to find a completed version. (There's probably a copy on your local machine, go ahead and use it, even if it's from another student. The 'find -n' command is helpful here.)

In it, we should have a function that looks like the following:

    def get_student_by_github(github):
        query = """SELECT first_name, last_name, github FROM Students WHERE github = ?"""
        DB.execute(query, (github,))
        row = DB.fetchone()
        print """\
    Student: %s %s
    Github account: %s"""%(row[0], row[1], row[2])

We'll change it now, instead of printing the output, we'll return it:

    def get_student_by_github(github):
        query = """SELECT first_name, last_name, github FROM Students WHERE github = ?"""
        DB.execute(query, (github,))
        row = DB.fetchone()
        return """\
    Student: %s %s
    Github account: %s"""%(row[0], row[1], row[2])

Since this function returns a string, we can now use it in our handler. Back in webapp.py, change the handler name from helloworld to get\_student, and change the handler body as follows:

    @app.route("/")
    def get_student():
        hackbright_app.connect_to_db()
        student_github = "chriszf" # Change this as appropriate
        return hackbright_app.get_student_by_github(student_github)

We're going to use functions out of our hackbright\_app file, so we'll need to import it at the top:

    import hackbright_app

Kill your server and restart it if it's still running, then reload your browser. You should see student data showing up.

### Request Arguments
We now have a database-backed web application, that's all there is to it.

...

Okay, fine.

We need to make it more better-er. At the very least, we need a way for it to display information for a student besides the one hardcoded. To do that, we have to collect input from the person using the browser. One mechanism for acquiring that input is called the 'request arguments'. Are they called the request arguments? Whatever.

The request arguments are a set of key/value pairs that the user can send to the web server on the other end via the url. An example url with request arguments would look like this:

    http://localhost:5000/?key1=val1&key2=val2

A question mark after a url tells the server that the remainder of the line is not part of the url. It indicates that anything that follows is a set of key/value pairs in the form of key=val, with each pair separated by an ampersand. In flask, the set of pairs gets transformed into a dictionary and placed in a special variable, request.args. If you were to print request.args from inside the handler that responds to the above url, you would see the following:

    print request.args
    => { "key1": "val1", "key2": "val2" }

We'll use this to collect the student's github username from the user. The request.args variable is a dictionary. To be safe, just in case they don't enter anything, we'll use the .get() method. Modify your get\_student handler as follows:

    @app.route("/")
    def get_student():
        hackbright_app.connect_to_db()
        student_github = request.args.get("student")
        return hackbright_app.get_student_by_github(student_github)

Now try accessing your application with the following url, changing the github account as appropriate:

    http://localhost:5000/?student=chriszf

[Jawesome.](http://en.wikipedia.org/wiki/Street_Sharks)


### Mad Libs Time
Remember mad libs? Give me a noun, an adjective, a plural noun and a verb. This next part is a _lot_ like that. First, some setup.

In our current directory, running `ls` should produce the following:

    env/
    webapp.py
    hackbright_app.py

We need to add a two more directories, one named 'static' and one named 'templates'. Do that now. Your directory should look like this:

    env/
    static/
    templates/
    webapp.py
    hackbright_app.py

Now, we make a mad lib. Remember, a mad lib is basically a template with a series of spaces for you to fill in with context free words.

    The ___noun___ ___verb___ ___adverb___.

The general procedure is to ask a friend for words to fill the template without letting them know the context they are to be used. Asking me for words and filling them in, you might get the following:

    The fish crept stealthily.

We apply the same idea to our webapp. Currently, our student information is displayed pretty terribly. We're going to make it display differently using templates. It will still look terrible, but in a different way. First we create a file in our 'templates' directory named student\_info.html, and we fill it with the string we're generating in the get\_student\_by\_github function.

    Student: %s %s
    Github account: %s

The first %s is the student's first name, the second is their last name, and the third is their github id. In Jinja, the templating system we use, our placeholders are indicated by double braces. Written with these rules, our mad lib example would look like this:

    The {{noun}} {{verb}} {{adverb}}.

In our html file, we make the following change:

    Student: {{first_name}} {{last_name}}
    Github account: {{github}}

Save your file, then we'll make changes in hackbright\_app.py, then webapp.py.

In hackbright\_app.get\_student\_by\_github, we return a string containing the formatted student data. We now have a template, so instead of returning the string, we'll return the pieces of data we need to fill our template. Modify the function so that it simply returns the row:

    def get_student_by_github(github):
        query = """SELECT first_name, last_name, github FROM Students WHERE github = ?"""
        DB.execute(query, (github,))
        row = DB.fetchone()
        return row

Moving to webapp.py, we need to collect call get\_student\_by\_github to get the row. Then we need to feed the data into the template and fill in the pieces. Once we've filled in the template, we can return the string of the filled template and let the browser render it.

    @app.route("/student")
    def get_student():
        hackbright_app.connect_to_db()
        student_github = request.args.get("student")
        row = hackbright_app.get_student_by_github(student_github)
        html = render_template("student_info.html", first_name=row[0],
                                                    last_name=row[1],
                                                    github=row[2])
        return html

Notice, before going on, that I've changed the url our handler will respond to. This is important for later.

Let's look a little closer. The magic happens on the fourth and fifth lines. First, we call get\_student\_by\_github to get a tuple representing the row of data from the database. Next, we make a call to render\_template. The first argument is the name of the template file we created earlier. After that, each keyword argument is the name of a placeholder in the template to be filled, along with the value to fill it with. Mull over the line for a second and make sure you can connect all of the argument names to the placeholders. No, seriously, mull. Mull _harder_.

This is pretty important. Once you're satisfied with the way the data gets filled in, we can now style our html. I'm going to warn you though, it's not going to be pretty. Here's how I changed my student\_info.html. Feel free to go hog wild on your own.

    <html>
    <body>
    <h1>Student: {{last_name}}, {{first_name}}</h1>
    <h2>Github: {{github}}</h2>
    <p>This student has shown extreme recalcitrance and has generally proved to be unreliable.</p>
    <p>It is my recommendation that they be put on double-secret probation for the remainder of the course.</p>
    </body>
    </html>

Behold your majesty at http://localhost:5000/student?github=chriszf

Was it majestic or did you get an error?  See if you can figure out why.  Hint: Pay close attention to how your arguments are being passed from the web browser's request through your program.


### User Input Revisited
Now we have a webapp, _done_.

OKAY FINE.

We do sort of have a webapp. It's an application where a user can enter some input and receive a response backed by a database. The last remaining issue here is that our input collection mechanism is pretty ugly. We can't ask our users to enter information via the url every time. Heck, we can't even ask our users to remember what our url is half the time. Users are pretty dumb.

The standard way to ask for data is to display a form. The user fills in the form and submits it, and our webapp takes that input and processes it as before.

Building forms (at this stage) is essentially a static process. The page displaying the form won't change dynamically with some other input, so we simply need to make an html page. Create a file in your templates directory called get\_github.html, and put the following in it.

    <html>
    <body>
    <form action="/student">
    <label for="github">Enter github id</label>
    <input type="text" name="github" />
    <input type="submit">
    </form>
    </body>
    </html>

If we tried to view this file in our browser, perhaps by going to http://localhost:5000/get\_github.html, you would get a 404. Remember that our webapp only responds to the events we specify in our webapp.py. It's not sufficient to have a template, we have to have a handler that will display the template. In your webapp.py file, before your existing handler, add the new one:

    @app.route("/")
    def get_github():
        return render_template("get_github.html")

This handler is simpler than the other one we wrote. Whenever a user browses to http://localhost:5000/, it will simply render the template get\_github.html. Load the url in your browser now.

If you're not familiar with html forms, try deleting the label tag and either of the input tags and reloading your browser to see how they behave before moving on. Make sure you understand which on-screen element is attached to which tag.

The meat of this file is the line

    <form action="/student">

This tells the browser where to send the form values when the user clicks submit. Here, it sends the form data to the first handler that we built earlier. That handler expects the student's github id in the form of a key/value pair. The value is obviously whatever the user types into the text field, but where is the key?

The key for a value that is inputted by a user is stored on the html element as the name attribute. Whew. That was a mouthful. Just look at the following line:

    <input type="text" name="student" />

This html tag displays a text field for the user to type in. The 'name' attribute on the tag specifies the key that will be used for the value when the form is submitted. If that's unclear, try entering a value then submitting the form. Inspect the url request arguments on the next page. Go back, change the name attribute, submit again and inspect the url again and see how they've changed.

If you were being observant, you would have noticed that the first time you submitted, everything _worked_. We now have a webapp, a proper one even. It's a little bit duct-taped together, but it's still complete. It displays a form to a user, collects data, processes the submitted form, then displays the result.

Furthermore, now we have a context we can use to talk about _all_ webapps ever. Every webapp is a series of page-pairs. One for displaying a form, and one for processing it. These pages all link to each other with standard 'a' tags, and all of those links give the illusion of having a single cohesive application. Sometimes multiple forms show up on the same page, and sometimes two different forms end up getting processed in the same way, but the principle still stands. If you think of webapps as a series of forms, you can decompose and reconstruct pretty much any webapp in existence. Yes, even facebook.

### What Now?
Well, our app works, but it's pretty brittle. If you leave the form empty and submit, it breaks. If you enter a user who's not in the database, it breaks. Basically if you look at it funny, it breaks. That's okay, because flask gives us a bunch of tools to make our apps significantly more robust. We're not going to worry about them here, right now we're going to focus on the general layout of our app and the integration of HTML and Python.

Here are your tasks:

1. On the get\_student handler, display a user's grades for all of their projects they've completed.
# Jinja documentation
2. On the same page, when you click on a project name, it brings you to a page listing all students and their grades for that particular project. You will need a new handler for this page.
3. From _that_ page, when clicking on a student's github account, it sends you back to the get\_student handler.
4. Make a pair of handlers that allows a user to create a new student record.
5. Make a pair of handlers that allows a user to create a new project record.
6. Make a handler that allows a user to grade a student on a given project.
7. Add links to pages that allow you to navigate the entirety of the app &mdash; you should never have to manually enter a URL to reach a particular handler.
8. Make it look pretty.

And that's it. Congratulations, achievement unlocked, 'built a webapp'. It's ugly and delicate, but it's yours. Cherish it. There. **Now** we're done.
