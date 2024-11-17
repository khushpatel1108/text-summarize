from flask import Flask, render_template, request, jsonify
from transformers import T5Tokenizer, T5ForConditionalGeneration
from deep_translator import GoogleTranslator

app = Flask(__name__)

# Load the model and tokenizer
model_name = "t5-small"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

# Define the summarization function
def summarize_with_t5(text, language='en'):
    if language != 'en':
        # Translate text to English if it's not already in English
        text = GoogleTranslator(source=language, target='en').translate(text)
    inputs = tokenizer(text, return_tensors="pt", max_length=512, truncation=True)
    outputs = model.generate(inputs.input_ids, max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)
    summary = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # Translate back if the language is not English
    if language != 'en':
        summary = GoogleTranslator(source='en', target=language).translate(summary)
    
    return summary

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
        
        # Map the language selection to language codes for translation
        language_map = {
            'English': 'en',
            'Kannada': 'kn',
            'Hindi': 'hi',
            'Tamil': 'ta',
            'Telugu': 'te'
        }
        selected_language_code = language_map.get(selected_language, 'en')
        
        # Perform summarization
        summary = summarize_with_t5(user_input, language=selected_language_code)
        
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
