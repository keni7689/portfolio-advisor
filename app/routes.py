from flask import Blueprint, render_template, jsonify, request
from app.utils import get_indian_portfolio_recommendation

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/get_portfolio', methods=['POST'])
def get_portfolio():
    data = request.get_json()
    risk_level = data.get('risk_level', 'moderate')
    investment_amount = data.get('investment_amount', 100000)  # Default 1 Lakh INR
    
    portfolio = get_indian_portfolio_recommendation(risk_level, investment_amount)
    return jsonify(portfolio)