import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error

def compute_metrics(batting, bowling):
    # Batting Metrics
    batting['NSE'] = batting['Runs'] / (6 * batting['Balls Faced'])
    batting['PWRS'] = (3 * batting['PP Runs'] + batting['Middle Runs'] + 2 * batting['Death Runs']) / 6
    batting['LRS'] = (batting['Missed Catches'] + batting['Wrong Decisions']) / batting['Balls Faced']
    batting['PWRS2'] = (batting['PWRS'] - batting['PWRS'].min()) / (batting['PWRS'].max() - batting['PWRS'].min())

    # Bowling Metrics
    bowling['PWWS'] = (3 * bowling['PP Wickets'] + bowling['Middle Wickets'] + 2 * bowling['Death Wickets']) / 6
    bowling['Wicket_Weighted'] = 3 * bowling['PP Wickets'] + 2 * bowling['Middle Wickets'] + bowling['Death Wickets']
    bowling['QWWS'] = bowling['Wicket_Weighted'] / bowling['Max Weighted Wickets in Match']
    bowling['PWRC'] = 1 - ((3 * bowling['PP Runs'] + bowling['Middle Runs'] + 2 * bowling['Death Runs']) / (6 * bowling['Max Phase Runs']))
    bowling['BCS'] = 1 - (bowling['Boundaries'] / bowling['Balls Bowled'])
    bowling['MOR'] = bowling['Maiden Overs'] / bowling['Total Overs']

    return batting, bowling

def compute_aggregates_and_cpr(batting, bowling):
    bat_agg = batting.groupby('Player')[['NSE', 'PWRS', 'LRS', 'PWRS2']].mean().reset_index()
    bowl_agg = bowling.groupby('Player')[['PWWS', 'QWWS', 'PWRC', 'BCS', 'MOR']].mean().reset_index()

    bat_agg['CPR_Batter'] = bat_agg[['NSE', 'PWRS', 'LRS', 'PWRS2']].mean(axis=1)
    bowl_agg['CPR_Bowler'] = bowl_agg[['PWWS', 'QWWS', 'PWRC', 'BCS', 'MOR']].mean(axis=1)

    return bat_agg, bowl_agg

def train_models(bat_agg, bowl_agg):
    models = {
        'Linear Regression': LinearRegression(),
        'Decision Tree': DecisionTreeRegressor(random_state=42),
        'Random Forest': RandomForestRegressor(n_estimators=100, random_state=42)
    }

    bat_features = ['NSE', 'PWRS', 'LRS', 'PWRS2']
    bowl_features = ['PWWS', 'QWWS', 'PWRC', 'BCS', 'MOR']

    model_preds_bat, model_preds_bowl = {}, {}
    model_scores_bat, model_scores_bowl = [], []

    for name, model in models.items():
        model.fit(bat_agg[bat_features], bat_agg['CPR_Batter'])
        preds = model.predict(bat_agg[bat_features])
        bat_agg[f'CPR_{name}'] = preds
        model_preds_bat[name] = preds
        model_scores_bat.append({'Model': name, 'R2 Score': r2_score(bat_agg["CPR_Batter"], preds)})

        model.fit(bowl_agg[bowl_features], bowl_agg['CPR_Bowler'])
        preds = model.predict(bowl_agg[bowl_features])
        bowl_agg[f'CPR_{name}'] = preds
        model_preds_bowl[name] = preds
        model_scores_bowl.append({'Model': name, 'R2 Score': r2_score(bowl_agg["CPR_Bowler"], preds)})

    return bat_agg, bowl_agg, pd.DataFrame(model_scores_bat), pd.DataFrame(model_scores_bowl)

