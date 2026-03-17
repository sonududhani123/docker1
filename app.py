from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>🚀 Azure Web App Container Running</h1>
    <p>Docker + ACR + Azure DevOps CI/CD</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
