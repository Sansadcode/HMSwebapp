from flask import Flask, render_template, request

app = Flask(__name__)

doctors = []
patients = [] 
prescriptions = []

@app.route('/') 
def index(): 
    return render_template('index.html', doctors=doctors, patients=patients, prescriptions=prescriptions)

@app.route('/add_patient', methods=['POST'])
def add_patient():
     patient_id = request.form['patient_id']
     patient_name = request.form['patient_name']
     patients.append({'patient_name': patient_name})
     return render_template('index.html', message='Patient added successfully!', doctors=doctors, patients=patients, prescriptions=prescriptions)



@app.route('/add_doctor', methods=['POST'])
def add_doctor():
     doctor_name = request.form['doctor_name']
     specialty = request.form['specialty'] 
     doctors.append({'doctor_name': doctor_name, 'specialty': specialty})
     return render_template('index.html', message='Doctor added successfully!', doctors=doctors, patients=patients, prescriptions=prescriptions)


@app.route('/add_prescription', methods=['POST'])
def add_prescription():
     patient_id = request.form['patient_id']
     prescription = request.form['prescription']
     prescriptions.append({'patient_id': patient_id, 'prescription': prescription})
     return render_template('index.html', message='Prescription added successfully!', doctors=doctors, patients=patients, prescriptions=prescriptions)

if __name__ == '__main__': 
     app.run(debug=True, host='0.0.0.0')