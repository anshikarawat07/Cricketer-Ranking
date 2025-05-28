```markdown
# Cricket Performance Analysis Project

## Overview
This project analyzes cricket batting and bowling performances using Python and Streamlit. It processes player performance data across 50 matches to generate key statistics and interactive visualizations.

---

## Features
- Load and analyze batting and bowling data from CSV files.
- Calculate strike rate, total runs, wickets, and economy rate.
- Phase-wise performance: Powerplay, Middle overs, Death overs.
- Interactive visualizations for batting strike rates and bowling economy rates.
- User-friendly web app built with Streamlit.

---

## Project Structure
```

cricket\_analysis\_project/
├── data/
│   ├── batting\_performance.csv
│   └── bowling\_performance.csv
├── analysis.py
├── visualization.py
├── utils.py
├── app.py
├── requirements.txt
└── README.md

````

---

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/cricket_analysis_project.git
````

2. Change directory:

   ```bash
   cd cricket_analysis_project
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Place the data files `batting_performance.csv` and `bowling_performance.csv` inside the `data/` folder.

5. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

---

## CSV File Formats

### Batting Performance CSV (`batting_performance.csv`)

| Column          | Description                                       |
| --------------- | ------------------------------------------------- |
| Match           | Match number (1 to 50)                            |
| Player          | Player name (e.g., Batter\_1)                     |
| Runs            | Total runs scored                                 |
| Balls Faced     | Number of balls faced                             |
| PP Runs         | Runs scored during Powerplay                      |
| Middle Runs     | Runs scored during Middle overs                   |
| Death Runs      | Runs scored during Death overs                    |
| Missed Catches  | Number of catches missed                          |
| Wrong Decisions | Number of wrong umpire decisions affecting player |

### Bowling Performance CSV (`bowling_performance.csv`)

| Column         | Description                       |
| -------------- | --------------------------------- |
| Match          | Match number (1 to 50)            |
| Player         | Player name (e.g., Bowler\_1)     |
| PP Wickets     | Wickets taken during Powerplay    |
| Middle Wickets | Wickets taken during Middle overs |
| Death Wickets  | Wickets taken during Death overs  |
| PP Runs        | Runs conceded during Powerplay    |
| Middle Runs    | Runs conceded during Middle overs |
| Death Runs     | Runs conceded during Death overs  |

---

