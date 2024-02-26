# from flask import Flask , render_template 

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('pro.html')

# @app.route('/myform')
# def myform():
#     return render_template('myform.html')

# @app.route('/pro')
# def pro():
#     return render_template('pro.html')

# if __name__  == '__main__':
#     app.run(debug = True)

from flask import Flask , render_template,request
import pickle
import numpy as np


model = pickle.load(open('model.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('pro.html')

@app.route('/myform')
def myform():
    return render_template('myform.html')

@app.route('/MachineLearn')
def MachineLearn():
    return render_template('MachineLearn.html')

@app.route('/About')
def About():
    return render_template('About.html')

@app.route('/pro')
def pro():
    return render_template('pro.html')

@app.route('/Predict' , methods = ['POST'])
def Predict():
    try:
        gender = request.form.get('Gender')
        if gender == 'Male':
          gender = 1
        else :
           gender = 0
    except Exception as e:
      print("An error occurred:", e)


    Married =  request.form.get('Married')
    if Married == 'Yes':
        Married = 1
    else :
        Married = 0
    Dependents = int(request.form.get('Dependents'))
    Education =  request.form.get('Education')
    if Education == 'Graduate':
        Education = 1
    else:
        Education = 0
    Self_Employed =  request.form.get('Self_Employed')
    if Self_Employed == 'Yes':
        Self_Employed = 1
    else :
        Self_Employed = 0

    ApplicantIncome = int(request.form.get('ApplicantIncome'))
    CoapplicantIncome = float(request.form.get('CoapplicantIncome'))
    LoanAmount = float(request.form.get('LoanAmount'))
    Loan_Amount_Term = float(request.form.get('Loan_Amount_Term'))
    Credit_History = float(request.form.get('Credit_History'))
    Property_Area  =  request.form.get('Property_Area')
    if Property_Area == 'Semiurban':
        Property_Area = 1
    elif Property_Area == 'Urban':
        Property_Area = 2
    # elif Property_Area == np.nan:
    #     Property_Area = 1   
    else :
        Property_Area = 0


    # Prediction
    result = model.predict(np.array([gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area]).reshape(1,11))

    if result[0] == 1:
        result = 'Congratulation Loan has Approved'
    else:
        result = 'Sorry Loan Not Approved'

    return render_template('myform.html' , predictmyvalue = result)

if __name__ == '__main__':
    app.run(debug=True)
    