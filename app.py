from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

model=pickle.load(open('model.pkl','rb'))


@app.route('/')
def blank():
    return render_template('index.html')

@app.route('/index.html')
def index():
    return render_template('index.html')


    
@app.route('/detect.html')
def detect():
    return render_template('detect.html')





@app.route('/predict',methods=['POST','GET'])
def predict():
    float_features=[float(x) for x in request.form.values()]
    final=[np.array(float_features)]
    print(float_features)
    print(final)
    prediction=model.predict(final)
    print(prediction)
    

    if prediction[0]==0:
        return render_template('detect.html',pred='The child is adequately nourished!')
    elif prediction[0]==1:
        return render_template('detect.html',pred='The child is moderately malnourished!')
    else:
        return render_template('detect.html',pred='The child is severely malnourished!')

if __name__ == '__main__':
    app.run(debug=True)