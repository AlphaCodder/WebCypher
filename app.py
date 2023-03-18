#importing required libraries

from flask import Flask, request
import numpy as np
import warnings
import pickle
warnings.filterwarnings('ignore')
from feature import FeatureExtraction

file = open("pickle/model.pkl","rb")
gbc = pickle.load(file)
file.close()


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = request.get_json()
        url = data.get('url', '')
        obj = FeatureExtraction(url)
        x = np.array(obj.getFeaturesList()).reshape(1,30) 

        y_pred =gbc.predict(x)[0]
        #1 is safe       
        #-1 is unsafe
        y_pro_phishing = gbc.predict_proba(x)[0,0]
        y_pro_non_phishing = gbc.predict_proba(x)[0,1]
        # if(y_pred ==1 ):
        pred = "It is {0:.2f} % safe to go ".format(y_pro_phishing*100)
        x =round(y_pro_non_phishing,2)
        # print(y_pro_phishing, ' ', y_pro_non_phishing, ' ', x)

        num = x*100
        result = ""
        if x >= 0 and x <= 0.5:
            num = 100 - num
        if x > 0.5 and x <= 1:
            result = "It is {0:.2f} % safe to go ".format(num)
        elif x >= 0 and x <= 0.5:
            result = "It is {0:.2f} % unsafe to go ".format(num)
        return result
    elif request.method == "GET":
        return "Welcome to Phishing Detection API - By Kumar"
    return "Unrecognized request method"


if __name__ == "__main__":
    app.run(debug=True)