from flask import Flask, render_template, jsonify
from database import load_kpis_from_db

app = Flask(__name__)

@app.route('/')
def home():
  kpis = load_kpis_from_db()
  return render_template('index.html', kpis=kpis)

@app.route('/api/kpis')
def list_kpis():
  kpis = load_kpis_from_db()
  return jsonify(kpis)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)