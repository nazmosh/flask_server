from flask import Flask

#inititalize server
app = Flask("Nazzys first server")

@app.route("/hello")
def hello ():
    return "salam nazzy joooon"
if __name__=="__main__":
    app.run()
