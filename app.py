from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample data for crops based on soil type and climate
crop_data = {
    'sandy': {
        'tropical': ['Coconut', 'Cashew', 'Millet'],
        'temperate': ['Carrot', 'Potato', 'Peanut']
    },
    'clay': {
        'tropical': ['Rice', 'Sugarcane', 'Banana'],
        'temperate': ['Wheat', 'Barley', 'Soybean']
    },
}

# Function to recommend crops based on soil and climate
def recommend_crops(soil_type, climate):
    return crop_data.get(soil_type, {}).get(climate, 'No recommendations available')

# Function to provide soil management advice
def soil_management(soil_type):
    advice = {
        'sandy': 'Add organic matter and mulch to retain moisture.',
        'clay': 'Improve drainage and aeration with organic compost.',
    }
    return advice.get(soil_type, 'No advice available')

# Function to identify disease based on symptoms
def identify_disease(symptoms):
    disease_data = {
        'yellowing leaves': 'Nitrogen deficiency, apply nitrogen fertilizer.',
        'spots on leaves': 'Fungal infection, use fungicide.',
    }
    return disease_data.get(symptoms, 'Unknown disease')

# Function to provide general farming tips
def farming_tips():
    tips = [
        'Rotate crops to prevent soil depletion.',
        'Use drip irrigation to save water.',
        'Practice organic farming for sustainability.'
    ]
    return tips

# Route to render the HTML page
@app.route('/')
def index():
    return render_template('catalog.html')

# API endpoint to get recommendations
@app.route('/get_recommendations', methods=['POST'])
def get_recommendations():
    data = request.json
    soil_type = data.get('soil_type')
    climate = data.get('climate')
    symptoms = data.get('symptoms')

    crops = recommend_crops(soil_type, climate)
    soil_advice = soil_management(soil_type)
    disease = identify_disease(symptoms)
    tips = farming_tips()

    return jsonify({
        'crops': crops,
        'soil_advice': soil_advice,
        'disease': disease,
        'tips': tips
    })

if __name__ == "__main__":
    app.run(debug=True)
