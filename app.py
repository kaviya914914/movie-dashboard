from flask import Flask
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    df = pd.read_csv("data/movies.csv")

    html = """
    <h1>Movie Dashboard</h1>
    <table border="1">
    <tr>
    <th>Title</th>
    <th>Year</th>
    <th>Rating</th>
    </tr>
    """

    for index, row in df.iterrows():
        html += f"""
        <tr>
        <td>{row['title']}</td>
        <td>{row['year']}</td>
        <td>{row['rating']}</td>
        </tr>
        """

    html += "</table>"

    return html


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)