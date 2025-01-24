from flask import Flask, render_template_string, request
import os

app = Flask(__name__)

# HTML para la página
html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Selector de Aplicaciones</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            background-color: #1e1e1e;
            color: white;
        }
        .button-container {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
            max-width: 600px;
            margin: 50px auto;
        }
        button {
            background-color: #3298dc;
            color: white;
            border: none;
            padding: 15px;
            font-size: 16px;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background-color: #2675a9;
        }
    </style>
</head>
<body>
    <h1>Selector de Aplicaciones</h1>
    <div class="button-container">
        {% for app_name in apps %}
        <form method="POST">
            <button type="submit" name="app" value="{{ app_name }}">{{ app_name }}</button>
        </form>
        {% endfor %}
    </div>
</body>
</html>
"""

# Nombres de los archivos .py a ejecutar
aplicaciones = [
    "mario.py", "app2.py", "app3.py",
    "app4.py", "app5.py", "app6.py",
    "app7.py", "app8.py", "app9.py"
]


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        app_name = request.form.get("app")
        if app_name in aplicaciones:
            try:
                os.system(f"python {app_name}")
            except Exception as e:
                return f"<p>Error al ejecutar {app_name}: {e}</p>"
            return f"<p>Ejecutando {app_name}...</p>"
    return render_template_string(html, apps=aplicaciones)


if __name__ == "__main__":
    app.run(debug=True)
