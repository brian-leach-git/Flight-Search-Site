from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def index():

    if request.method == 'POST':

        email = request.form['email']
        # if email is not in list of emails
            # add to list of emails and add to DynamoDB

        # send welcome email to new address?

    return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True)
