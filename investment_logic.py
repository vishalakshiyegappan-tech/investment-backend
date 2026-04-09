# -------------------------------
# 15 Investment Plans (FINAL)
# -------------------------------
investment_plans = [
    # LOW RISK (1–5%)
    {"name": "Fixed Deposit (FD)", "risk": "Low", "return_rate": 0.06, "description": "Bank guaranteed return, Inflation risk- The interest earned may be lower than inflation, Reducing real value of money."},
    {"name": "Recurring Deposit (RD)", "risk": "Low", "return_rate": 0.06, "description": "Monthly deposit, Liquidity risk- Premature withdrawal may attract penalties or reduced interest."},
    {"name": "Government Bonds", "risk": "Low", "return_rate": 0.07, "description": "Very safe, government-backed but interest rate risk- Bond prices fall when market interest rate rise."},
    {"name": "Public Provident Fund", "risk": "Low", "return_rate": 0.075, "description": "Long term, Government can revise PPF interest rates periodically, Which may lower future returns."},
    {"name": "National Savings Certificate", "risk": "Low", "return_rate": 0.07, "description": "Secure postal investment, Liquidity risk- funds are locked in for full tenure with no premature withdrawal in normal cases."},

    # MEDIUM RISK (6–12%)
    {"name": "Mutual Fund – Balanced", "risk": "Medium", "return_rate": 0.10, "description": "Balanced equity-debt investment, Market risk- Returns depend on market performance and may fluctuate in volatile conditions."},
    {"name": "Mutual Fund – Large Cap", "risk": "Medium", "return_rate": 0.12, "description": "Stable large companies, Market risk- Share price fluctuations can affect returns in economic downturns."},
    {"name": "Corporate Bond Fund", "risk": "Medium", "return_rate": 0.08, "description": "Better returns than FD, Credit risk- Corporate defaults may impact returns."},
    {"name": "Gold SIP", "risk": "Medium", "return_rate": 0.09, "description": "Hedge against inflation, Price volatility risk- Gold prices can fluctuate due to global market conditions."},
    {"name": "Silver SIP", "risk": "Medium", "return_rate": 0.10, "description": "Industrial and investment metal, Market volatility risk- Silver prices can be highly unstable."},

    # HIGH RISK (12–25%)
    {"name": "Equity Mutual Fund (High Growth)", "risk": "High", "return_rate": 0.15, "description": "High growth potential, Market volatility risk- High exposure to stock market fluctuations."},
    {"name": "Small Cap Fund", "risk": "High", "return_rate": 0.20, "description": "Very high growth opportunity, Business risk- Small companies may face instability and failure."},
    {"name": "Crypto SIP", "risk": "High", "return_rate": 0.25, "description": "Very high return potential, Extreme volatility risk- Prices can change drastically within short periods."},
    {"name": "Nifty Index Fund", "risk": "High", "return_rate": 0.14, "description": "Market index based investment, Market crash risk- Index performance directly affects returns."},
    {"name": "Real Estate Crowdfunding", "risk": "High", "return_rate": 0.18, "description": "Property-backed returns, Liquidity risk- Funds may be locked and not easily withdrawable."}
]

# -------------------------------
# SIP RETURN FORMULA
# -------------------------------

def calculate_sip(m, r, n):
    monthly_rate = r / 12
    return m * (((1 + monthly_rate) ** (n * 12) - 1) / monthly_rate) * (1 + monthly_rate)

# -------------------------------
# SELECT PLANS (BASED ON INPUT)
# -------------------------------
def select_plans(risk_level, monthly_investment, duration):

    filtered = []

    for plan in investment_plans:
        if risk_level.lower() == plan["risk"].lower():
            expected = calculate_sip(monthly_investment, plan["return_rate"], duration)
            filtered.append({
                "name": plan["name"],
                "risk": plan["risk"],
                "expected_return": round(expected, 2),
                "description": plan["description"]
            })

    return sorted(filtered, key=lambda x: x["expected_return"], reverse=True)[:3]