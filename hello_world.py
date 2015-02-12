#! /usr/bin/env python
from flask import Flask

app = Flask(__name__)
  
@app.route("/hello/<name>")
def hello_person(name):
    string = "<HTML><title></title><body>Hello....{}\n".format(name.title())
    #return "Hello {}!".format(name.title())
    string2 = " looking Good\n</body></HTML>"
    final = string + string2
    return final
  
@app.route("/hi/<name>")
def hi_kitten(name):
    html = """
        <h1>
            Hello {}!
        </h1>
        <p>
            Here's a picture of a kitten.
        </p>
        <img src="http://placekitten.com/g/200/300">
        <p>
           Awww...{}
        </p>
    """
    return html.format(name.title(), name.title())

@app.route("/jedi/<first_name>/<last_name>")
def print_jedi(first_name, last_name):
    full_name = first_name+" "+last_name
    jedi = last_name[0:3]+first_name[0:2]
    
    html = """
        <h1>
            Hello {}!
        </h1>
        <p>
           <h4>
           Jedi's Name is: {}
           <h4>
        </p>
    """
    return html.format(full_name, jedi) 
  
 
if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=8080)