# pip install git+https://github.com/openai/whisper.git 
# pip install --upgrade --no-deps --force-reinstall git+https://github.com/openai/whisper.git
# pip install setuptools-rust
# pip install ffmpeg

import whisper

model = whisper.load_model('base')
result = model.transcribe(r"D:\SpeechToText\Audios\Sample1.wav")

# print(result["text"])
transcript = result["text"]


import openai

# Set your API key
openai.api_key = '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'

# Define the questions
questions = [
    "Question 1: Communication Skills:  Evaluate the representative's ability to communicate clearly, listen actively, and convey information effectively",
    "Question 2: Problem Resolution: Assess how well the representative addresses and resolves the customer's issue or inquiry. Quick and effective resolution is crucial",
    "Question 3: Empathy: Consider whether the representative demonstrates empathy towards the customer's situation, showing understanding and concern for their needs.",
    "Question 4: Product/Service Knowledge: Evaluate the representative's knowledge about the company's products or services. A well-informed representative can provide accurate and helpful information.",
    "Question 5: Professionalism: Assess the overall professionalism of the representative, including tone, courtesy, and adherence to company policies and standards.",
    "Question 6: Proactive Assistance: Evaluate if the representative takes proactive steps to offer additional assistance, such as providing relevant information or suggesting complementary products/services.",
    "Question 7: Resolution Accuracy: Verify that the solution provided aligns with the customer's needs and resolves the issue accurately.",
    "Question 8: Customer Satisfaction: Gauge the overall satisfaction of the customer by listening to their feedback and assessing their tone throughout the call.",
    "Overall Rating: How would you rate the overall quality of the call? Please choose one of the following options: Excellent, Good, Average, Weak, Poor?"
]

# Make sure all elements are strings
transcript = str(transcript)
questions = [str(q) for q in questions]

# Generate answers using the OpenAI API
answers = []
for i, question in enumerate(questions):
    # Construct a prompt for each question
    prompt = f"{transcript}\n\n{question}\nAnswer:"

    # Generate answer for the current question
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=300  # Adjust as needed
    )

    # Extract and append the answer to the list
    answers.append((question, response['choices'][0]['text']))

# Print the answers
for i, (question, answer) in enumerate(answers):
    print(f"\n{question}\n\nAnswer: {answer}\n")