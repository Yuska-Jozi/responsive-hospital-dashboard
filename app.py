from flask import Flask, render_template, jsonify

app = Flask(__name__)

KPIs = [
  {
    'area': 'Registration',
    'kpi': 'Average Wait Time',
    'uom': 'min',
    'target': 5.0,
    'actual': 9.5,
    'indicator': 'Too High',
    '': 'Details'
  },
  {
    'area': 'Registration',
    'kpi': 'Readmission Rate',
    'uom': '%',
    'target': 2.0,
    'actual': 1.3,
    'indicator': 'In Spec',
    '': 'Details'
  },
  {
    'area': 'Registration',
    'kpi': 'User Rating',
    'uom': 'star',
    'target': 5.0,
    'actual': 3.5,
    'indicator': 'Average',
    '': 'Details'
  },
  {
    'area': 'Admissions',
    'kpi': 'Cumulative Admissions Today',
    'uom': 'patient',
    'target': 'n/a',
    'actual': 7,
    'indicator': '-',
    '': 'Details'
  },
  {
    'area': 'ICU',
    'kpi': 'ICU Admissions Today',
    'uom': 'patient',
    'target': 'n/a',
    'actual': 0,
    'indicator': '-',
    '': 'Details'
  },
  {
    'area': 'Wards',
    'kpi': 'Occupied Beds vs Capacity',
    'uom': '%',
    'target': '<=85',
    'actual': 34,
    'indicator': 'In Spec',
    '': 'Details'
  },
  {
    'area': 'Wards',
    'kpi': 'Average Length of Stay',
    'uom': 'day',
    'target': '<=4.0',
    'actual': 4.5,
    'indicator': 'Too High',
    '': 'Details'
  },
  {
    'area': 'Wards',
    'kpi': 'Patient to Nurse Ratio',
    'uom': 'patient',
    'target': '6.0 - 10.0',
    'actual': 5.5,
    'indicator': 'Too Low',
    '': 'Details'
  },
  {
    'area': 'Dispensary',
    'kpi': 'Prescription Fill Time',
    'uom': 'min',
    'target': '<=5.0',
    'actual': 3.5,
    'indicator': 'In Spec',
    '': 'Details'
  },
  {
    'area': 'Dispensary',
    'kpi': 'Inventory Cover',
    'uom': '%',
    'target': 95,
    'actual': 78,
    'indicator': 'Too Low',
    '': 'Details'
  },
  {
    'area': 'Ambulances',
    'kpi': 'Mean Response Time',
    'uom': 'min',
    'target': '<=45',
    'actual': 76,
    'indicator': 'Too High',
    '': 'Details'
  },
  {
    'area': 'Staff',
    'kpi': 'Attendance',
    'uom': '%',
    'target': '>=95',
    'actual': 94,
    'indicator': 'Too Low',
    '': 'Details'
  }
]

@app.route('/')
def home():
    return render_template('index.html', kpis=KPIs)

@app.route('/api/kpis')
def list_kpis():
  return jsonify(KPIs)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)