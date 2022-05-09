import pandas as pd
from flask import Blueprint, request
from services.model_utils import predict_hf

bp1 = Blueprint('main', __name__, url_prefix='/main')


@bp1.route('/api/run_model', methods=['POST'])
def run_model():
    form_df = pd.DataFrame(request.form, index=[0])
    print(form_df)
    pred = predict_hf(form_df)
    print(pred)

    return {
        'data': request.form,
        'pred': pred,
        'message': 'Deu tudo certo'}
