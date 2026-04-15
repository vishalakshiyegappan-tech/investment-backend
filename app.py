from flask import Flask, request, jsonify
from flask_cors import CORS 
from db_connection import get_db_connection
from investment_logic import select_plans

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Investment API is running!" 

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    name = data.get("name")
    age = data.get("age")
    income_source = data.get("income_source")
    income_amount = data.get("income_amount")
    investment_percentage = data.get("investment_percentage")
    investment_duration = data.get("investment_duration")
    risk_level = data.get("risk_level")

    # monthly investment
    monthly_investment = (income_amount * investment_percentage) / 100

    # select 3 plans
    results = select_plans(risk_level, monthly_investment, investment_duration)

    # save user_input to DB
    #conn = get_db_connection()
    #cursor = conn.cursor()
    #
    #query = """
    #    INSERT INTO user_inputs (name, age, income_source, income_amount, investment_percentage, investment_duration, risk_level)
    #    VALUES (%s,%s,%s,%s,%s,%s,%s)
    #"""
    #
    #cursor.execute(query, (name, age, income_source, income_amount, investment_percentage, investment_duration, risk_level))
    #conn.commit()

    return jsonify({
        "monthly_investment": monthly_investment,
        "suggestions": results
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
