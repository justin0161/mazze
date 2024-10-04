from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Add your OpenAI API key here
openai.api_key = "YOUR_OPENAI_API_KEY"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-response', methods=['POST'])
def get_response():
    data = request.get_json()
    prompt = data['prompt']
    
    # Generate a response from OpenAI API
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    
    return jsonify(response=response.choices[0].text.strip())

if __name__ == '__main__':
    app.run(debug=True)
