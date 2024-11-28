from flask import Flask, render_template, url_for
import os
app = Flask(__name__)


@app.route("/about")
def about():
    return render_template('about.html', title ='About')

@app.route("/contact")
def contact():
    return render_template('contact.html', title='Contact')

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/projects")
def projects_page():
    return render_template('projects.html', title='Projects')

@app.route("/projects/predicting-heart-disease")
def predicting_heart_disease():
    return render_template('projects/predicting_heart_disease.html',title='Predicting Heart Disease')

@app.route("/projects/hate-speech-detection")
def hate_speech_detection():
    return render_template('projects/hate_speech_detection.html',title='Hate Speech Detection')

@app.route("/projects/ai-ethics-essay")
def ai_ethics_essay():
    return render_template('projects/ai_ethics_essay.html', title='AI Ethics: The Graham AI Ethical Framework')




if __name__ == "__main__":
    # Use PORT provided by Render or default to 5000 for local testing
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)