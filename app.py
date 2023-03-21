from flask import Flask, render_template, request
import pickle
import matplotlib

app = Flask(__name__)
#load the model
model=pickle.load(open("saveddmodel.sav", "rb"))

@app.route("/")
def home():
    result = ""
    return render_template("index.html", **locals())


@app.route("/predicts", methods=["POST","GET"])
def predict():
    sepal_lenght = float(request.form["sepal_length"])
    sepal_width = float(request.form["sepal_width"])
    petal_lenght = float(request.form["petal_length"])
    petal_width = float(request.form["petal_width"])
    result = model.predict([[sepal_lenght, sepal_width, petal_lenght, petal_width]])[0]
    return render_template("index.html", **locals())

if __name__ == "__main__":
    app.run(debug=True)

