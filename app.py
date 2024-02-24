from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Set up OpenAI API key
api_key = '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'
openai.api_key = api_key

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    if 'symptoms' in request.form:
        symptoms = request.form['symptoms']

        # Ensure the symptoms are not empty before making an API request
        if symptoms:
            information = get_medical_information(symptoms)
            return render_template('result.html', diagnosis=symptoms, information=information)
        else:
            return render_template('result.html', diagnosis="No symptoms entered.", information="")
    else:
        return render_template('result.html', diagnosis="No symptoms entered.", information="")

def get_medical_information(symptoms):
    prompt = f"I am experiencing the following symptoms: {symptoms}. What could be the possible diagnosis?"
    
    response = openai.Completion.create(
        engine="curie",
        prompt=prompt,
        max_tokens=200
    )

    diagnosis = response.choices[0].text.strip()
    return diagnosis

if __name__ == '__main__':
    app.run(debug=True)
