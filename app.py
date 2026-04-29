from flask import Flask, render_template, request

app = Flask(__name__)

messages = [
    "Oi, meu amor 💖",
    "Eu queria te dizer uma coisa...",
    "Desde que te conheci, tudo ficou mais bonito",
    "Você é a melhor parte dos meus dias",
    "E eu só queria que você soubesse...",
    "I LOVE YOU ❤️"
]

@app.route("/", methods=["GET", "POST"])
def index():
    step = 0

    if request.method == "POST":
        step = int(request.form.get("step", 0)) + 1

    return render_template("index.html", step=step, messages=messages)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)