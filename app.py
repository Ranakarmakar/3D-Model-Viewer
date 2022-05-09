from flask import Flask, request, render_template
import os

app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template("main.html")


@app.route('/model', methods=['GET', 'POST'])
def model():
    if request.method == 'POST':
        file = request.files["uploaded_file"]
        model_path = "./flask_upload/" + file.filename
        file.save(model_path)
        arr = os.listdir('./flask_upload')
        x = arr[0]
        y = '../flask_upload/'
        z = y + x
    else:
        z = '..models/NeilArmstrong.glb'

    return render_template("main.html", back_file=z)


if __name__ == '__main__':
    app.run(debug=True)
