---

# Beyond the Scoreboard: A Data-Driven Approach to Cricketer Rankings

🏏 **Cricket Player Performance Analyzer using Advanced Metrics and Machine Learning**

---

## Overview

This project presents a data-driven approach to rank cricketers (both batters and bowlers) based on detailed performance metrics across multiple matches. Utilizing advanced cricket-specific metrics and machine learning models, it provides a robust framework to evaluate player contributions beyond traditional statistics.

---

## Features

* **Multi-metric Player Evaluation:** Computes nuanced batting and bowling metrics capturing scoring efficiency, powerplay impact, error rates, wicket effectiveness, bowling control, and more.
* **Machine Learning Models:** Applies Linear Regression, Decision Tree, and Random Forest regressors to model player performance and compute a Composite Performance Rating (CPR).
* **Interactive Web Interface:** Built with Streamlit for easy upload of player data, selection of models, and visualization of rankings and model performances.
* **Automated Commentary Generator:** Produces human-readable commentary insights on top players based on model outputs and key performance indicators.
* **Visualizations:** Bar charts and tables display rankings and comparative model performances for both batters and bowlers.

---

## Getting Started

### Prerequisites

* Python 3.7+
* Libraries: `streamlit`, `pandas`, `matplotlib`, `seaborn`, `scikit-learn`

Install dependencies via pip:

```bash
pip install streamlit pandas matplotlib seaborn scikit-learn
```

### Running the App

1. Clone the repository:

```bash
git clone https://github.com/yourusername/cricket-cpr-analyzer.git
cd cricket-cpr-analyzer
```

2. Prepare your data files:

* `batting_performance.csv` — Batting match-wise data
* `bowling_performance.csv` — Bowling match-wise data

Sample data files are provided in the `data/` directory.

3. Run the Streamlit app:

```bash
streamlit run app.py
```

4. Upload the batting and bowling CSV files via the sidebar, select the desired ML model, and explore rankings, commentary, and model performance.

---
![image](https://github.com/user-attachments/assets/b4fd06f6-0a4e-43d0-98e2-4bc0b5c5a4c7)

---

## Data Description

### Batting Data (`batting_performance.csv`)

| Column          | Description                         |
| --------------- | ----------------------------------- |
| Match           | Match number                        |
| Player          | Batter name                         |
| Runs            | Runs scored                         |
| Balls Faced     | Balls faced                         |
| PP Runs         | Runs scored during Powerplay        |
| Middle Runs     | Runs scored during middle overs     |
| Death Runs      | Runs scored during death overs      |
| Missed Catches  | Number of missed catches            |
| Wrong Decisions | Number of wrong decisions by batter |

### Bowling Data (`bowling_performance.csv`)

| Column                        | Description                           |
| ----------------------------- | ------------------------------------- |
| Match                         | Match number                          |
| Player                        | Bowler name                           |
| PP Wickets                    | Wickets taken during Powerplay        |
| Middle Wickets                | Wickets taken during middle overs     |
| Death Wickets                 | Wickets taken during death overs      |
| PP Runs                       | Runs conceded during Powerplay        |
| Middle Runs                   | Runs conceded during middle overs     |
| Death Runs                    | Runs conceded during death overs      |
| Boundaries                    | Boundaries conceded                   |
| Balls Bowled                  | Total balls bowled                    |
| Maiden Overs                  | Maiden overs bowled                   |
| Total Overs                   | Total overs bowled                    |
| Max Phase Runs                | Maximum runs conceded in any phase    |
| Max Weighted Wickets in Match | Maximum weighted wickets in any match |

---

## How It Works

1. **Metric Computation:** Custom cricket metrics like Normalized Scoring Efficiency (NSE), Powerplay Weighted Run Score (PWRS), Judgment Error Rate (LRS) for batters; and Powerplay Weighted Wicket Score (PWWS), Quality Weighted Wicket Score (QWWS), Powerplay Run Control (PWRC), Boundary Concession Score (BCS), Maiden Over Ratio (MOR) for bowlers are calculated.

2. **Aggregation:** Metrics are aggregated at the player level across matches.

3. **Composite Performance Rating (CPR):** The mean of selected metrics creates a baseline CPR for batters and bowlers.

4. **Model Training:** Three regression models predict CPRs based on underlying metrics, enabling comparison and validation of rankings.

5. **Visualization & Commentary:** Rankings, model performance charts, and generated commentary provide actionable insights.

---

## Project Structure

```
├── app.py                  # Streamlit web app
├── model_builder.py        # Metric computation & ML modeling
├── commentary_model.py     # Commentary generation logic
├── data/
│   ├── batting_performance.csv
│   └── bowling_performance.csv
└── README.md
```

---

## Future Enhancements

* Incorporate more advanced features like player form over time and opposition quality.
* Integrate ball-by-ball data for deeper analysis.
* Add player comparison dashboards.
* Deploy as a web service for broader user access.

---

# Enjoy exploring cricket analytics beyond the scoreboard! 🏏

---
