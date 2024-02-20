import pandas as pd

# Sample data
data = {
    'Canoo': {
        'Industry': 'Electric Vehicle Manufacturing',
        'Size': 'Large',
        'Growth Rate': '15%',
        'Trends': 'Focus on Sustainable Mobility',
        'Key Players': 'Tesla, Rivian, Lucid Motors'
    },
    'Competitors': {
        'Competitor 1': {
            'Name': 'Tesla',
            'Market Share': '30%',
            'Products/Services': 'Electric Vehicles, Energy Storage',
            'Pricing Strategies': 'Premium Pricing',
            'Marketing Efforts': 'Strong Brand Presence, Innovative Marketing Campaigns'
        },
        'Competitor 2': {
            'Name': 'Rivian',
            'Market Share': '15%',
            'Products/Services': 'Electric Trucks, Electric SUVs',
            'Pricing Strategies': 'Competitive Pricing',
            'Marketing Efforts': 'Focus on Adventure and Sustainability'
        }
    },
    'Market Trends': {
        'Consumer Behavior': 'Shift towards Electric Vehicles',
        'Technological Advancements': 'Battery Technology, Autonomous Driving',
        'Competitive Landscape': 'Increasing Competition in Electric Vehicle Market'
    },
    'Financial Performance': {
        'Revenue': '$100 million',
        'Profit Margins': '10%',
        'Return on Investment': '15%',
        'Expense Structure': 'R&D, Marketing, Production'
    }
}

# Create DataFrame from the data dictionary
df = pd.DataFrame(data)
df.to_csv('canoo_case_study_data.csv', index=False)
