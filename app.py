from flask import Flask,request,render_template
import pickle
import numpy as np

app=Flask(__name__)
with open('model.pkl','rb') as model_file:
    model=pickle.load(model_file)
                      
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
   Gend=request.form['Gender']
   if Gend=="Male":
     Gender=1
   elif Gend=='Female':
     Gender=0
   EstimatedSalary=int(request.form['EstimatedSalary'])
   Age=int(request.form['Age'])
   feature=np.array([[Gender,Age,EstimatedSalary]])
   prediction=model.predict(feature)
   return render_template('index.html',pred_res=prediction[0])

   
if __name__=='__main__':
  app.run(debug=True) 
