from flask import Flask, request
from datetime import datetime

#inititalize server
app = Flask("Nazzys first server")
counter = 0

@app.route("/hello")
def hello ():
    return "Hello"

@app.route("/get_count", methods=['GET'])
def get_count():
    return_value = dict(count=counter, time=datetime.now())
    return return_value

@app.route("/update_count", methods=['POST'])
def update_count():
    global counter 
    
    request_information = request.json

    # grab the incoming count value
    incoming_count = request_information['count']

    # update the count with the incoming count
    counter += incoming_count

    return dict(count=counter, time=datetime.now())


if __name__=="__main__":
    app.run()
