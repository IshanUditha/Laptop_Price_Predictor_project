from flask import Flask,render_template, request
import pickle
import numpy as np

app = Flask(__name__)

def prediction(lst):
    file_name ="notebooks/Laptop_price_predictor.pickle"
    with open(file_name,"rb") as file:
        model = pickle.load(file)
    p_value = model.predict([lst])
    return p_value



@app.route('/',methods =["POST","GET"])
def index():
    pred = 0
    if request.method == "POST":
        ram = request.form["ram"]
        weight = request.form["weight"]
        company = request.form["company"]
        type_name = request.form["type_name"]
        OpSys = request.form["OpSys"]
        Cpu_name = request.form["Cpu_name"]
        Gpu_name = request.form["Gpu_name"]
        Memory_value = request.form["Memory_value"]
        TouchScreen = request.form.getlist("TouchScreen")
        ips = request.form.getlist("ips")
        print(TouchScreen)

        f_list =[]
        f_list.append(len(TouchScreen))
        f_list.append(len(ips))
        
        company_list =['Acer', 'Apple', 'Asus','Dell', 'HP', 'Lenovo', 'MSI','Other', 'Toshiba'] 
        type_name_list =['2 in 1 Convertible','Gaming', 'Netbook', 'Notebook','Ultrabook', 'Workstation']
        OpSys_list =['Linux','Mac', 'Other', 'Windows']
        Cpu_name_list = ['AMD','Intel Core i3', 'Intel Core i5','Intel Core i7', 'Other']
        Gpu_name_list = ['AMD','Intel', 'Nvidia']
        Memory_value_list =['HDD','Other', 'SSD']


        def lit(list_,value):
            for item in list_:
                if item == value:
                    f_list.append(1)
                else:
                    f_list.append(0)
        
        lit(company_list,company)
        lit(type_name_list,type_name)
        lit(OpSys_list,OpSys)
        lit(Cpu_name_list,Cpu_name)
        lit(Gpu_name_list,Gpu_name)
        lit(Memory_value_list,Memory_value)

        f_list.append(int(ram))
        f_list.append(float(weight))

        #print(f_list)

        pred = prediction(f_list)*351
        pred =np.round(pred[0])

        #print(pred)

    return render_template("index.html",pred_value =pred)

if __name__ == "__main__":
    app.run(debug=True)