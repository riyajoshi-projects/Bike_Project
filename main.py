from flask import Flask ,render_template,request  
app=Flask(__name__)

import joblib
model=joblib.load(r"C:\Users\RIya\Desktop\6month-Data-Science\machine learning\Bike_Project\Model\bike_model.lb")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/form")
def form():
     return render_template("form.html")


@app.route("/predict",methods=['POST','GET'])
def predict():
     if request.method =='POST':

          kms_driven = float(request.form['kms_driven'])
          owner = int(request.form['owner'])
          age = float(request.form['age'])
          power = float(request.form['power'])
          brand = int(request.form['brand'])

          print("Bike Informations :-",[[kms_driven,owner,age,power,brand]])
          data =[[kms_driven,owner,age,power,brand]]
          pred = model.predict(data)


          pred = int(pred[0]) 

         
## Convert the predicted price into Indian currency format

          def indian_currency(num):
                s = str(num)
                
                if len(s) <= 3:
                    return s
                
                last_three = s[-3:]
                remaining = s[:-3]
                        
                parts = []
                while remaining:
                    parts.insert(0, remaining[-2:])
                    remaining = remaining[:-2]
            
                return ",".join(parts) + "," + last_three

          
          pred = indian_currency(pred)
          print("prediction :-",pred)


          return render_template("form.html", prediction=pred)

         
if __name__=="__main__":
    app.run(debug=True)