# WebCypher - Real-Time Phishing Website Detector Chrome Extension

![WebCypher Logo](webcypher_logo.png)

WebCypher is a Google Chrome extension that helps users detect phishing websites in real-time. With the increasing sophistication of online scams and phishing attacks, it is essential to have a reliable tool that can protect users from falling victim to such fraudulent activities. WebCypher is designed to analyze website URLs and alert users if they are potentially accessing a phishing website.

## Features

- Real-Time Phishing Detection: WebCypher employs advanced algorithms to analyze the URL of the website you are visiting and quickly determines if it is a phishing website.
- Instant Alerts: If a website is identified as a potential phishing site, WebCypher immediately alerts the user through a pop-up notification, providing them with the necessary information to stay safe.
- Secure Browsing Experience: By using WebCypher, users can significantly reduce the risk of falling victim to phishing attacks and safeguard their personal information, such as usernames, passwords, and credit card details.
- Lightweight and User-Friendly: WebCypher is designed to be a lightweight and unobtrusive extension that seamlessly integrates with your Chrome browser. It runs silently in the background without causing any disruptions to your browsing experience.

## Installation

To install WebCypher, follow these steps:

1. Open the Google Chrome browser.
2. Go to the Chrome Web Store.
3. Search for "WebCypher" in the search bar.
4. Click on the "Add to Chrome" button next to the WebCypher extension.
5. Confirm the installation by clicking "Add extension" in the pop-up window.
6. Once installed, WebCypher will appear as a small icon in the Chrome toolbar.

## How to Use

Using WebCypher is simple:

1. Ensure that the WebCypher extension is enabled (the icon will be visible in the Chrome toolbar).
2. Browse the internet as you normally would.
3. As you visit websites, WebCypher will automatically analyze the URLs in real-time.
4. If WebCypher detects a potential phishing website, a pop-up notification will appear, alerting you of the potential threat.
5. Exercise caution when visiting websites that trigger a warning and avoid entering sensitive information if the website is flagged as suspicious.

## Reporting False Positives

WebCypher strives to provide accurate phishing detection, but false positives may occur. If you believe a website has been incorrectly flagged as a phishing website, please report it to us through the following steps:

1. Click on the WebCypher icon in the Chrome toolbar.
2. Select the "Report False Positive" option from the drop-down menu.
3. Provide the necessary information, including the URL and a brief explanation of why you believe it is a false positive.
4. Click "Submit" to send the report to our team for review.

## Privacy and Data Security

WebCypher is committed to protecting your privacy and maintaining the security of your data. The extension does not collect or store any personal information or browsing history. All analysis and detection are performed locally on your device.

## Support and Feedback

If you encounter any issues while using WebCypher or have any suggestions for improvement, please reach out to our support team at support@webcypher.com. We appreciate your feedback and will do our best to address any concerns or inquiries promptly.

## Disclaimer

WebCypher is an extension designed to enhance your online security; however, it is important to note that no security tool is perfect. While WebCypher employs advanced techniques to detect phishing websites, it may not catch every instance or variation of a phishing attack. It is crucial to remain vigilant and exercise caution when sharing personal information online.

---

Thank you for choosing WebCypher!



# Phishing URL Detection API 

## Table of Content
  * [Introduction](#introduction)
  * [Directory Tree](#directory-tree)
  * [Result](#result)
  * [Conclusion](#conclusion)


## Introduction

The Internet has become an indispensable part of our life, However, It also has provided opportunities to anonymously perform malicious activities like Phishing. Phishers try to deceive their victims by social engineering or creating mockup websites to steal information such as account ID, username, password from individuals and organizations. Although many methods have been proposed to detect phishing websites, Phishers have evolved their methods to escape from these detection methods. One of the most successful methods for detecting these malicious activities is Machine Learning. This is because most Phishing attacks have some common characteristics which can be identified by machine learning methods. To see project click [here]("/").


## Directory Tree 
```
├── pickle
│   ├── model.pkl
├── Phishing URL Detection.ipynb
├── Procfile
├── README.md
├── app.py
├── feature.py
├── phishing.csv
├── requirements.txt


```

## Technologies Used

![](https://forthebadge.com/images/badges/made-with-python.svg)

[<img target="_blank" src="https://upload.wikimedia.org/wikipedia/commons/3/31/NumPy_logo_2020.svg" width=200>](https://numpy.org/doc/) [<img target="_blank" src="https://upload.wikimedia.org/wikipedia/commons/e/ed/Pandas_logo.svg" width=200>](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html)
[<img target="_blank" src="https://upload.wikimedia.org/wikipedia/commons/8/84/Matplotlib_icon.svg" width=100>](https://matplotlib.org/)
[<img target="_blank" src="https://scikit-learn.org/stable/_static/scikit-learn-logo-small.png" width=200>](https://scikit-learn.org/stable/) 
[<img target="_blank" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcScq-xocLctL07Jy0tpR_p9w0Q42_rK1aAkNfW6sm3ucjFKWML39aaJPgdhadyCnEiK7vw&usqp=CAU" width=200>](https://flask.palletsprojects.com/en/2.0.x/) 

## Result

Accuracy of various model used for URL detection
<br>

<br>

||ML Model|	Accuracy|  	f1_score|	Recall|	Precision|
|---|---|---|---|---|---|
0|	Gradient Boosting Classifier|	0.974|	0.977|	0.994|	0.986|
1|	CatBoost Classifier|	        0.972|	0.975|	0.994|	0.989|
2|	XGBoost Classifier| 	        0.969|	0.973|	0.993|	0.984|
3|	Multi-layer Perceptron|	        0.969|	0.973|	0.995|	0.981|
4|	Random Forest|	                0.967|	0.971|	0.993|	0.990|
5|	Support Vector Machine|	        0.964|	0.968|	0.980|	0.965|
6|	Decision Tree|      	        0.960|	0.964|	0.991|	0.993|
7|	K-Nearest Neighbors|        	0.956|	0.961|	0.991|	0.989|
8|	Logistic Regression|        	0.934|	0.941|	0.943|	0.927|
9|	Naive Bayes Classifier|     	0.605|	0.454|	0.292|	0.997|

Feature importance for Phishing URL Detection 
<br><br>
![image](https://user-images.githubusercontent.com/79131292/144603941-19044aae-7d7b-4e9a-88a8-6adfd8626f77.png)




## Conclusion
1. The final take away form this project is to explore various machine learning models, perform Exploratory Data Analysis on phishing dataset and understanding their features. 
2. Creating this notebook helped me to learn a lot about the features affecting the models to detect whether URL is safe or not, also I came to know how to tuned model and how they affect the model performance.
3. The final conclusion on the Phishing dataset is that the some feature like "HTTTPS", "AnchorURL", "WebsiteTraffic" have more importance to classify URL is phishing URL or not. 
4. Gradient Boosting Classifier currectly classify URL upto 97.4% respective classes and hence reduces the chance of malicious attachments.
