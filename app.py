from flask import Flask, request, render_template
import os

app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template("main.html", back_file='..models/NeilArmstrong.glb')


arr = os.listdir('./flask_upload')


@app.route('/model', methods=['GET', 'POST'])
def model():
    if request.method == 'POST':
        file = request.files["uploaded_file"]
        model_path = "./flask_upload/" + file.filename
        file.save(model_path)
        z = '../flask_upload/' + arr[0]
        print(z)
    else:
        z = '..models/NeilArmstrong.glb'
        print(z)

    return render_template("main.html", back_file=z)


if __name__ == '__main__':
    app.run(debug=True)
