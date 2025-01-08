import pandas as pd
from datetime import datetime

def get_indian_portfolio_recommendation(risk_level, investment_amount):
    # Portfolio allocations based on risk level with Indian investment options
    portfolios = {
        'conservative': {
            'Large Cap Mutual Funds': 0.30,
            'Government Bonds': 0.25,
            'Fixed Deposits': 0.20,
            'Gold': 0.15,
            'Liquid Funds': 0.10
        },
        'moderate': {
            'Large Cap Mutual Funds': 0.35,
            'Mid Cap Mutual Funds': 0.20,
            'Index Funds (Nifty 50)': 0.20,
            'Government Bonds': 0.15,
            'Gold': 0.10
        },
        'aggressive': {
            'Mid Cap Mutual Funds': 0.30,
            'Small Cap Mutual Funds': 0.25,
            'Large Cap Mutual Funds': 0.20,
            'Sectoral Funds': 0.15,
            'International Funds': 0.10
        }
    }
    
    investment_recommendations = {
        'conservative': {
            'Large Cap Mutual Funds': ['SBI Bluechip Fund', 'HDFC Top 100 Fund'],
            'Government Bonds': ['SBI PSU Bond Fund', 'HDFC Government Securities Fund'],
            'Fixed Deposits': ['Bank FDs (3-5 years)', 'Post Office Term Deposits'],
            'Gold': ['Sovereign Gold Bonds', 'Gold Mutual Funds'],
            'Liquid Funds': ['HDFC Liquid Fund', 'Axis Liquid Fund']
        },
        'moderate': {
            'Large Cap Mutual Funds': ['Axis Bluechip Fund', 'Mirae Asset Large Cap Fund'],
            'Mid Cap Mutual Funds': ['Kotak Emerging Equity Fund', 'HDFC Mid-Cap Opportunities Fund'],
            'Index Funds (Nifty 50)': ['UTI Nifty Index Fund', 'HDFC Index Fund-NIFTY 50 Plan'],
            'Government Bonds': ['SBI Magnum Gilt Fund', 'IDFC G-Sec Fund'],
            'Gold': ['Gold ETFs', 'Sovereign Gold Bonds']
        },
        'aggressive': {
            'Mid Cap Mutual Funds': ['Axis Midcap Fund', 'DSP Midcap Fund'],
            'Small Cap Mutual Funds': ['Nippon India Small Cap Fund', 'SBI Small Cap Fund'],
            'Large Cap Mutual Funds': ['Canara Robeco Bluechip Equity Fund', 'ICICI Prudential Bluechip Fund'],
            'Sectoral Funds': ['ICICI Prudential Technology Fund', 'Tata Digital India Fund'],
            'International Funds': ['Franklin India Feeder - Franklin US Opportunities Fund', 'Motilal Oswal S&P 500 Index Fund']
        }
    }
    
    selected_portfolio = portfolios.get(risk_level, portfolios['moderate'])
    recommendations = investment_recommendations.get(risk_level, investment_recommendations['moderate'])
    
    # Calculate allocations
    allocations = {}
    for category, percentage in selected_portfolio.items():
        amount = investment_amount * percentage
        allocations[category] = {
            'percentage': percentage,
            'amount': amount,
            'monthly_sip': amount * 0.05,  # Suggesting 5% of allocation as monthly SIP
            'recommended_funds': recommendations[category]
        }
    
    return {
        'risk_level': risk_level,
        'total_amount': investment_amount,
        'allocations': allocations,
        'general_advice': get_general_advice(risk_level)
    }

def get_general_advice(risk_level):
    advice = {
        'conservative': {
            'time_horizon': '3-5 years',
            'key_points': [
                'Focus on capital preservation',
                'Regular income through FDs and bonds',
                'Gold as a hedge against inflation',
                'Consider Senior Citizens Savings Scheme if applicable'
            ]
        },
        'moderate': {
            'time_horizon': '5-7 years',
            'key_points': [
                'Balanced approach between equity and debt',
                'Regular SIPs in mutual funds',
                'Index funds for long-term stable returns',
                'Consider PPF for tax-saving benefits'
            ]
        },
        'aggressive': {
            'time_horizon': '7+ years',
            'key_points': [
                'Higher exposure to equity for long-term wealth creation',
                'Systematic investment in small and mid-cap funds',
                'International diversification',
                'Consider ELSS funds for tax saving'
            ]
        }
    }
    return advice.get(risk_level, advice['moderate'])