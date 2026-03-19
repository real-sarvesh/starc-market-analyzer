import pandas as pd

# S.T.A.R.C. RESOLUTIONS - DATA SCIENCE DIVISION
# Project: Market-Gap Analyzer v1.0
# Logic: Identifies high-demand products with low-satisfaction gaps.

def run_analysis():
    print("--- STARC MARKET-GAP ANALYZER ONLINE ---")
    
    # 1. Load the data
    try:
        df = pd.read_csv('market_data.csv')
    except FileNotFoundError:
        print("[ERROR] market_data.csv not found.")
        return

    # 2. The S.T.A.R.C. Formula
    # Opportunity = (Demand * 0.8) - (Satisfaction * 0.2)
    # We normalize ratings to a 0-100 scale for comparison
    df['Opportunity_Score'] = (df['Search_Volume'] * 0.01) - (df['Avg_Rating'] * 2)

    # 3. Sort by highest opportunity
    gaps = df.sort_values(by='Opportunity_Score', ascending=False)

    print("\n[REPORT] TOP MARKET GAPS IDENTIFIED:")
    print("--------------------------------------")
    for index, row in gaps.head(3).iterrows():
        print(f"OPPORTUNITY: {row['Product_Name']}")
        print(f"CATEGORY: {row['Category']} | SCORE: {row['Opportunity_Score']:.2f}")
        print("--------------------------------------")

if __name__ == "__main__":
    run_analysis()
