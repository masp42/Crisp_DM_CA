# Importing libraries
import pandas as pd
from flask import Blueprint, request
import numpy as np
from joblib import load
import json

# Loading the extracted model after training.
model = load('models/heart_disease.joblib')

# Backend route declaration with /main prefix, i.e. to call http://127.0.0:5000/main/api/run_model (locally).
bp1 = Blueprint('main', __name__, url_prefix='/main')

# Backend route responsible for collecting the information sent by the frontend.


@bp1.route('/api/run_model', methods=['POST'])
def run_model():
    # Collection of request values ​​and creation of DataFrame
    form_hd_df = pd.DataFrame(request.form, index=[0])
    # Extraction of only table values, without their indices
    records_hd = form_hd_df.to_records(index=False)
    results_hd = list(records_hd[0])
    # Conversion needed to make the prediction
    results_hd_as_numpy_array = np.asarray(results_hd)
    results_hd_reshaped = results_hd_as_numpy_array.reshape(1, -1)
    predicted = model.predict(results_hd_reshaped)

    # Function return converting to String
    return {
        'pred': json.dumps(int(predicted[0]))
    }
