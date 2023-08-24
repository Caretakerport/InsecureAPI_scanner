from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def check_insecure_api(api_endpoint):
    vulnerabilities = []

    response = requests.get(api_endpoint)

    # Check for status code vulnerabilities
    if response.status_code != 200:
        vulnerabilities.append(f"API endpoint {api_endpoint} returned status code {response.status_code}")

    # Add more vulnerability checks here

    return vulnerabilities

@app.route("/", methods=["GET", "POST"])
def index():
    vulnerabilities = []

    if request.method == "POST":
        target_api = request.form.get("target_api")
        vulnerabilities = check_insecure_api(target_api)

    return render_template("index.html", vulnerabilities=vulnerabilities)

if __name__ == "__main__":
    app.run(debug=True)
