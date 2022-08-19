#!/usr/bin/env python
# coding: utf-8

# In[3]:


from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model_file = open('kmeans_model.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')

@app.route('/')
def index():
    return render_template('index.html', insurance_cost=0)

@app.route('/predict', methods=['POST'])
def predict():
    '''
    Predict the insurance cost based on user inputs
    and render the result to the html page
    '''
    objek, juni, juli, agustus, september, oktober, november, desember = [x for x in request.form.values()]

    data = []
	
    # objek
    if objek == "0":
        data.append(int(objek))
    elif objek == "1":
        data.append(int(objek))
    elif objek == "2":
        data.append(int(objek))
    elif objek == "3":
        data.append(int(objek))
    elif objek == "4":
        data.append(int(objek))
    elif objek == "5":
        data.append(int(objek))
    elif objek == "6":
        data.append(int(objek))
    elif objek == "7":
        data.append(int(objek))
    elif objek == "8":
        data.append(int(objek))
    elif objek == "9":
        data.append(int(objek))
    elif objek == "10":
        data.append(int(objek))
    elif objek == "11":
        data.append(int(objek))
    elif objek == "12":
        data.append(int(objek))
    elif objek == "13":
        data.append(int(objek))
    elif objek == "14":
        data.append(int(objek))
    elif objek == "15":
        data.append(int(objek))
    elif objek == "16":
        data.append(int(objek))
    elif objek == "17":
        data.append(int(objek))
    elif objek == "18":
        data.append(int(objek))
    elif objek == "19":
        data.append(int(objek))	
    # untuk juni
    data.append(int(juni))
	# untuk juli
    data.append(int(juli))
	# untuk agustus
    data.append(int(agustus))
	# untuk september
    data.append(int(september))
	# untuk oktober
    data.append(int(oktober))
	# untuk november
    data.append(int(november))
	# untuk november
    data.append(int(desember))
        
		
    prediction = model.predict([data])
    output = round(prediction[0], 2)

    return render_template('index.html', insurance_cost=output)

if __name__ == '__main__':
    app.run(debug=True)


# In[ ]:




