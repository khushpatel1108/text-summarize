import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Hugging Face API URL and Authorization Header
API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {
    "Authorization": "Bearer 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"  # Replace with your correct API key
}

# Function to query Hugging Face API for summarization
def query_huggingface(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    
    if response.status_code != 200:
        return {"error": f"API request failed with status code {response.status_code}"}
    
    return response.json()

# Define routes for the web app
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    try:
        # Check if 'user_input' is in the form data
        if 'user_input' not in request.form:
            return jsonify({'error': 'Text input is required'}), 400
        
        # Get the user input and selected language from the request
        user_input = request.form['user_input']
        selected_language = request.form.get('language', 'en')
        
        # Map the language selection to language codes for translation (if necessary)
        language_map = {
            'English': 'en',
            'Kannada': 'kn',
            'Hindi': 'hi',
            'Tamil': 'ta',
            'Telugu': 'te'
        }
        selected_language_code = language_map.get(selected_language, 'en')
        
        # Send the user input to Hugging Face API for summarization
        payload = {"inputs": user_input}
        output = query_huggingface(payload)
        
        # If there's an error, return it
        if "error" in output:
            return jsonify({'error': output['error']}), 500
        
        # Get the summarized text from Hugging Face API response
        summary = output[0].get('summary_text', '')
        
        if not summary:
            return jsonify({'error': 'No summary found in the response'}), 500
        
        # Render the result template with the original text and summary
        return render_template(
            'result.html',
            user_input=user_input,
            summary=summary,
            selected_language_name=selected_language
        )
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
