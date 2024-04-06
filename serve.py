import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    files_dir = 'static/files'  # Path to the files directory relative to the static directory
    # Get the list of files in the 'files' directory
    files = os.listdir(files_dir)
    return render_template('index.html', files=files, files_dir=files_dir)

if __name__ == '__main__':
    app.run(debug=True)
