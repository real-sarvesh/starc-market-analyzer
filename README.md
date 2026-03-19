# 📊 S.T.A.R.C. Market-Gap Analyzer
**Division:** Applied Data Science & Predictive Analytics

## ⚡ The Mission
In a saturated e-commerce landscape, identifying "what to sell next" is a multi-billion dollar problem. This engine utilizes a **Weighted Opportunity Scoring Algorithm** to identify products with high search volume (Demand) but low average ratings (Consumer Dissatisfaction).

## 🛠️ The Tech Stack
* **Language:** Python 3.9+
* **Library:** Pandas (Data Wrangling)
* **Model:** Linear Weighted Scoring (Custom S.T.A.R.C. Logic)

## 🧬 How it Works
The system ingests raw market data and applies the following normalization:
$$Opportunity\_Score = (Search\_Volume \times 0.01) - (Avg\_Rating \times 2)$$



## 🚀 How to Run
1. Clone the repo: `git clone https://github.com/STARC-resolutions/starc-market-analyzer.git`
2. Install dependencies: `pip install pandas`
3. Execute: `python analyzer.py`
