def generate_commentary(df, role="Batter", model_name="Random Forest"):
    commentary = []
    metric_terms = {
        "Batter": ["NSE", "PWRS", "LRS", "PWRS2"],
        "Bowler": ["PWWS", "QWWS", "PWRC", "BCS", "MOR"]
    }
    for _, row in df.iterrows():
        comments = f"{row['Player']} ranked {int(row['Rank'])} among all {role.lower()}s using {model_name} model. "

        if role == "Batter":
            comments += f"They had a solid Normalized Scoring Efficiency (NSE) and Powerplay Weighted Run Score (PWRS). "
            if row['LRS'] > 0.05:
                comments += "However, they made frequent judgment errors (LRS), which slightly affected their overall standing. "
            else:
                comments += "They showed strong decision-making with minimal errors. "
        else:
            comments += f"Consistently performed across all phases with good PWWS and control (low PWRC). "
            if row['MOR'] > 0.1:
                comments += "Their maiden over contribution is noteworthy and boosted their ranking."
            else:
                comments += "Fewer maiden overs might have cost them a better rank."

        commentary.append(comments)
    return commentary


