import pandas as pd
import pulp
from pulp import value
import pickle
def dataframe(match_id):
    df0 = pd.read_csv('merged_final_encoded.csv')
    df = df0.loc[df0['Match_Id'] == match_id]
    X=df.drop(columns={'total_points','Date'},axis=1)
    return X

def model_pred(model_name, X ):
    print("Reached Here!!")
    if model_name == 'Random Forest':
        with open('rf_model.pkl', 'rb') as file:
            loaded_model = pickle.load(file)
    elif model_name == 'XGBoost':
        with open('xgb_model.pkl', 'rb') as file:
            loaded_model = pickle.load(file)
    elif model_name == 'Catboost':
        with open('catboost_model.pkl', 'rb') as file:
            loaded_model = pickle.load(file)
#     else:
#         with open('demo_model.pkl', 'rb') as file:
#             loaded_model = pickle.load(file)
    predictions = loaded_model.predict(X)
    return predictions     
def data_merge(predictions, X):
    new_df = pd.DataFrame(predictions, columns=['Points_Predicted'])
    # df = pd.read_csv('merged_final_encoded.csv')
    dfe = pd.read_csv('label_encoding.csv')
    new_df=new_df.reset_index(drop=True)
    X = X.reset_index(drop=True)
    merged_df = pd.concat([X, new_df], axis=1)

    merged_df = merged_df[['Match_Id', 'Name', 'Team', 'Position','Points_Predicted']]
    name_mapping = dfe.set_index('Name_encoded')['Name'].to_dict()
    merged_df['Name'] = merged_df['Name'].map(name_mapping)
    return merged_df

def player_selction(merged_df):
    prob = pulp.LpProblem("IPL Fantasy Team Selection", pulp.LpMaximize)
    players = list(merged_df['Name'])
    player_vars = pulp.LpVariable.dicts("Players", players, lowBound=0, upBound=1, cat='Binary')
    # Set the objective function
    prob += pulp.lpSum([player_vars[players[i]] * merged_df['Points_Predicted'].iloc[i] for i in range(len(merged_df))])

    prob += pulp.lpSum([player_vars[players[i]] for i in range(len(merged_df))]) == 11
    # Set team constraints
    for team in merged_df['Team'].unique():
        prob += pulp.lpSum([player_vars[players[i]]  for i in range(len(merged_df)) if merged_df['Position'].iloc[i] == team]) <= 7
    # Set player category constraints
    prob += pulp.lpSum([player_vars[players[i]] for i in range(len(merged_df)) if merged_df['Position'].iloc[i] == 3]) >= 1
    prob += pulp.lpSum([player_vars[players[i]] for i in range(len(merged_df)) if merged_df['Position'].iloc[i] ==  3]) <= 4
    prob += pulp.lpSum([player_vars[players[i]] for i in range(len(merged_df)) if merged_df['Position'].iloc[i] == 1]) >= 3
    prob += pulp.lpSum([player_vars[players[i]] for i in range(len(merged_df)) if merged_df['Position'].iloc[i] ==  1]) <= 6
    prob += pulp.lpSum([player_vars[players[i]] for i in range(len(merged_df)) if merged_df['Position'].iloc[i] == 0]) >= 1
    prob += pulp.lpSum([player_vars[players[i]] for i in range(len(merged_df)) if merged_df['Position'].iloc[i] == 0]) <= 4
    prob += pulp.lpSum([player_vars[players[i]] for i in range(len(merged_df)) if merged_df['Position'].iloc[i] == 2]) >= 3
    prob += pulp.lpSum([player_vars[players[i]] for i in range(len(merged_df)) if merged_df['Position'].iloc[i] ==2]) <=6
    prob.solve()
    if value(prob.objective) != None:
        playernamelist = []


        for v in prob.variables():
            if v.varValue > 0:
                a = v.name.replace("Players_", "").replace("_", " ")
                playernamelist.append(a)



    return playernamelist