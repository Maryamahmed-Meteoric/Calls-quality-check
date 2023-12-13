from flask import Flask, render_template, request

import os
import whisper
import openai


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Check if a file was submitted
    if 'file' not in request.files:
        return "No file provided"

    file = request.files['file']

    # Check if the file has a name and is allowed
    if file.filename == '':
        return "No selected file"
    if file:
        # Save the file to a temporary location
        audio_path = r"D:\SpeechToText\webpage\temp\temp.wav"
        file.save(audio_path)
        

        
        # Run your transcription code with the uploaded file
        model = whisper.load_model('base')
        result = model.transcribe(audio_path)
        transcript = result["text"]
        
        
        # Set your API key
        openai.api_key = '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'

        # Define the questions
        questions = [
            "Overall Rating: How would you rate the overall quality of the call? Please choose one of the following options: Excellent, Good, Average, Weak, Poor?",
            "Communication Skills:  Evaluate the representative's ability to communicate clearly, listen actively, and convey information effectively",
            "Problem Resolution: Assess how well the representative addresses and resolves the customer's issue or inquiry. Quick and effective resolution is crucial",
            "Empathy: Consider whether the representative demonstrates empathy towards the customer's situation, showing understanding and concern for their needs.",
            "Product/Service Knowledge: Evaluate the representative's knowledge about the company's products or services. A well-informed representative can provide accurate and helpful information.",
            "Professionalism: Assess the overall professionalism of the representative, including tone, courtesy, and adherence to company policies and standards.",
            "Proactive Assistance: Evaluate if the representative takes proactive steps to offer additional assistance, such as providing relevant information or suggesting complementary products/services.",
            "Resolution Accuracy: Verify that the solution provided aligns with the customer's needs and resolves the issue accurately.",
            "Customer Satisfaction: Gauge the overall satisfaction of the customer by listening to their feedback and assessing their tone throughout the call."
        ]

        # Process the transcript with OpenAI questions
        transcript = str(transcript)
        questions = [str(q) for q in questions]
        answers = []

        for i, question in enumerate(questions):
            prompt = f"{transcript}\n\n{question}\nAnswer:"
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=300
            )
            answers.append((question, response['choices'][0]['text']))
        
        os.remove(audio_path)    

        return render_template('results.html', answers=answers)

if __name__ == '__main__':
    app.run(debug=True)
    

