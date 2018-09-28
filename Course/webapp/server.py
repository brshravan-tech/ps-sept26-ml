from flask import Flask
from flask import request
import pickle
app = Flask(__name__)
header = open('html/header.html').read()
footer = open('html/footer.html').read()
cols = 'preg_count,glucose_concentration,diastolic_bp,triceps_skin_fold_thickness,two_hr_serum_insulin,bmi,diabetes_pedi,age'
@app.route('/', methods=['GET'])
def homepage():

    ips = "".join([x+'<br><input name='+ x +' type=text><br>' for x in cols.split(',')])
    f = header + '''
    <form action=predict method=GET>
        ''' + ips + '''
    <input value=Predict type=submit></form>''' + footer
    return f
    
@app.route('/predict')
def predict():
    f = open('diab_pred.pkl', 'rb')
    model = pickle.load(f)
    values=[ float(request.args.get(v)) for v in cols.split(',') ]
    pred = model.predict([values])
    f.close()
    
    return header + "Probably diabetic: YES" if pred[0] == 1 else "Probably diabetic: NO" + footer

app.run()