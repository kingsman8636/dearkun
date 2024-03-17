from flask import Flask, render_template, request

app = Flask(__name__)

# List to store responses
responses = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/proposal")
def proposal():
    return render_template("proposal.html")

@app.route("/reply", methods=["GET", "POST"])
def reply():
    if request.method == "POST":
        response = request.form["response"]
        responses.append(response)  # Save response to the list
        return render_template("confirmation.html")
    else:
        return render_template("reply.html")

@app.route("/responses")
def show_responses():
    return render_template("responses.html", responses=responses)

if __name__ == "__main__":
    app.run(debug=True)
