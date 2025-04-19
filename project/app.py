from flask import Flask, request, jsonify
import joblib
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load the model
model = joblib.load('trackers_model.joblib')

trackers = ['google_tag', 'amazon_cloudfront', 'cloudflare', 'googleapis.com', 'gstatic', 'google_analytics', 'outbrain', 'google_fonts', 'facebook', 'youtube', 'google', 'google_syndication', 'amazon_adsystem', 'doubleclick', 'amazon_web_services', 'appnexus', 'jsdelivr', 'criteo', 'google_users', 'adobe_audience_manager', 'bing_ads', 'onetrust', 'twitter', 'google_adservices', 'reddit', 'google_photos', 'amazon_cdn', 'usercentrics', 'cloudflare_insights', 'scorecard_research_beacon', 'didomi', 'at_internet', 'qualtrics', 'cloudinary', 'forter']

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from POST request
    data = request.get_json()
    
    # Convert to numpy array
    features = np.array(data['features']).reshape(1, -1)
    
    # Predict
    prediction = model.predict(features)

    res = [trackers[i] for i,val in enumerate(prediction[0]) if val == 1] 
    print(res)
    
    # Return prediction
    return jsonify({'trackers': res})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)