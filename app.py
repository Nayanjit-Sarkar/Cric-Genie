from flask import Flask, request, jsonify, make_response
from flask_cors import CORS, cross_origin       
from datetime import datetime, timedelta
from get_prediction import *
import pickle
import pandas as pd

app = Flask(__name__)
CORS(app)


@app.route("/", methods=['GET'])

def Home():
    return jsonify({'response':"This is a Dream 11 prediction model"})

@app.route("/predict", methods = ["POST"])
@cross_origin()
def predict():
    if request.method == "POST":
        data = request.get_json()
        print(data)
    df = pd.read_csv("Frontend_data.csv")
    # Get match ID

    team = data['team1']
    date_str = data['date']
    date = datetime.fromisoformat(date_str[:-1])
    new_date = (date + timedelta(days=1)).strftime('%Y-%m-%d')

    # filter the DataFrame based on the input values
    result = df.query("Date == @new_date and (Team == @team or Opponent == @team)")
    match_id = result.iloc[0]['Match_Id']
    print(match_id)
    df_n = dataframe(match_id)
    print(df_n.columns)
    pred = model_pred('XGBoost', df_n )
    print(pred)
    merg_df = data_merge(pred, df_n)
    players = player_selction(merg_df)
    # response = make_response())
    # response.headers.add('Access-Control-Allow-Origin', '*')
    
    return jsonify(list(players))
    # get the match ID from the result
    

if __name__ == "__main__":
    app.run(debug=True)
