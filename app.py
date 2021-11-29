from flask import Flask, render_template, request
from helper import run_model, cat , prod, siz, sea


app = Flask(__name__)

@app.route("/", methods = ['POST', 'GET'])


def index():
    if request.method == 'POST':
        # do the logic of retrieving the inputs from the user in the web app
        
        c = request.form['feature 1']
        s = request.form['feature 2']
        p = request.form['feature 3']
        se = request.form['feature 4']
        
        parameter1 = cat(c)
        parameter2 = siz(s)
        parameter3 = prod(p)
        parameter4 = sea(se)
        
        
        list_features = parameter1 + parameter2 + parameter3 + parameter4
        
        prediction = run_model(list_features)
        if prediction[0] < 0:
            res = [0]
        else:
            res = prediction
        
        return render_template('main.html', results = str(int(prediction/(-1000000000000))))
    else:
        return render_template('main.html')

if __name__ == '__main__':
    
    app.run(debug=False, port=  2380)