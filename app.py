import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from model_builder import compute_metrics, compute_aggregates_and_cpr, train_models
from commentary_model import generate_commentary

# Streamlit page config
st.set_page_config(page_title="Cricket CPR Analyzer", layout="wide")
st.title("🏏 Cricket Player Performance Analyzer")

# Sidebar navigation
page = st.sidebar.selectbox("Choose a Page", [
    "🏏 Batter Rankings",
    "💬 Batter Commentary",
    "📊 Batter Model Performance",
    "🎯 Bowler Rankings",
    "💬 Bowler Commentary",
    "📊 Bowler Model Performance"
])

# File upload
batting_file = st.file_uploader("Upload Batting Performance CSV", type=["csv"])
bowling_file = st.file_uploader("Upload Bowling Performance CSV", type=["csv"])

if batting_file and bowling_file:
    batting = pd.read_csv(batting_file)
    bowling = pd.read_csv(bowling_file)

    # Compute metrics and CPRs
    batting, bowling = compute_metrics(batting, bowling)
    bat_df, bowl_df = compute_aggregates_and_cpr(batting, bowling)
    bat_df, bowl_df, bat_scores_df, bowl_scores_df = train_models(bat_df, bowl_df)

    model_options = ['Linear Regression', 'Decision Tree', 'Random Forest']
    selected_model = st.selectbox("Select Model", model_options)

    # Add rankings for each model
    for model_name in model_options:
        bat_df[f'{model_name}_Rank'] = bat_df[f'CPR_{model_name}'].rank(ascending=False)
        bowl_df[f'{model_name}_Rank'] = bowl_df[f'CPR_{model_name}'].rank(ascending=False)

    # 1. Batter Rankings
    if page == "🏏 Batter Rankings":
        st.subheader(f"Batter Rankings - {selected_model}")
        temp_bat = bat_df.sort_values(by=f'CPR_{selected_model}', ascending=False).reset_index(drop=True)
        temp_bat['Rank'] = temp_bat[f'{selected_model}_Rank']
        st.dataframe(temp_bat[['Rank', 'Player', f'CPR_{selected_model}']], use_container_width=True)

        # Graph
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.barplot(data=temp_bat.head(10), x='Player', y=f'CPR_{selected_model}', palette='Blues_r', ax=ax)
        plt.xticks(rotation=45)
        st.pyplot(fig)

    # 2. Batter Commentary
    elif page == "💬 Batter Commentary":
        st.subheader(f"Top 10 Batter Commentary - {selected_model}")
        temp_bat = bat_df.sort_values(by=f'CPR_{selected_model}', ascending=False).reset_index(drop=True)
        temp_bat['Rank'] = temp_bat[f'{selected_model}_Rank']
        for line in generate_commentary(temp_bat.head(10), role="Batter", model_name=selected_model):
            st.markdown(f"• {line}")

    # 3. Batter Model Performance
    elif page == "📊 Batter Model Performance":
        st.subheader("📊 Batter Model R2 Score Comparison")
        st.bar_chart(bat_scores_df.set_index("Model"))

    # 4. Bowler Rankings
    elif page == "🎯 Bowler Rankings":
        st.subheader(f"Bowler Rankings - {selected_model}")
        temp_bowl = bowl_df.sort_values(by=f'CPR_{selected_model}', ascending=False).reset_index(drop=True)
        temp_bowl['Rank'] = temp_bowl[f'{selected_model}_Rank']
        st.dataframe(temp_bowl[['Rank', 'Player', f'CPR_{selected_model}']], use_container_width=True)

        # Graph
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.barplot(data=temp_bowl.head(10), x='Player', y=f'CPR_{selected_model}', palette='Greens_r', ax=ax)
        plt.xticks(rotation=45)
        st.pyplot(fig)

    # 5. Bowler Commentary
    elif page == "💬 Bowler Commentary":
        st.subheader(f"Top 10 Bowler Commentary - {selected_model}")
        temp_bowl = bowl_df.sort_values(by=f'CPR_{selected_model}', ascending=False).reset_index(drop=True)
        temp_bowl['Rank'] = temp_bowl[f'{selected_model}_Rank']
        for line in generate_commentary(temp_bowl.head(10), role="Bowler", model_name=selected_model):
            st.markdown(f"• {line}")

    # 6. Bowler Model Performance
    elif page == "📊 Bowler Model Performance":
        st.subheader("📊 Bowler Model R2 Score Comparison")
        st.bar_chart(bowl_scores_df.set_index("Model"))