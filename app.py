from flask import Flask, request, send_file
import subprocess
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Calibre Converter API is running!"

@app.route("/convert", methods=["POST"])
def convert():
    file = request.files["file"]

    input_path = "/tmp/input"
    output_path = "/tmp/output.mobi"

    file.save(input_path)

    subprocess.run([
        "ebook-convert",
        input_path,
        output_path
    ])

    return send_file(output_path, as_attachment=True)
