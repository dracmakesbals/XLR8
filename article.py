import requests

# News API Configuration
news_api_key = '484ef554d0d84e6098ddf46ada222ab5'  # Replace with your API key
news_url = (
    f"https://newsapi.org/v2/everything?"
    f"q=market OR economy OR business&language=en&apiKey={news_api_key}"
)

# Fetch Live News Articles
response = requests.get(news_url)
articles = response.json().get('articles', [])

# Check if articles are fetched correctly
if not articles:
    print("No articles found. Check your API key or the NewsAPI service.")
else:
    print(f"Fetched {len(articles)} articles.")

# Define Economic Terms and Skills Mapping
economic_terms = [
    'GDP', 'inflation', 'recession', 'unemployment', 'stock market', 
    'interest rates', 'cryptocurrency', 'supply chain', 'startups'
]

skills_mapping = {
    'GDP': 'Macroeconomics',
    'inflation': 'Data Analysis',
    'recession': 'Risk Management',
    'unemployment': 'Career Planning',
    'stock market': 'Investment Strategies',
    'interest rates': 'Financial Planning',
    'cryptocurrency': 'Blockchain Technology',
    'supply chain': 'Operations Management',
    'startups': 'Entrepreneurship'
}

# Analyze Articles for Trends and Skills
def analyze_articles(articles, terms):
    trend_summary = {}
    
    for article in articles[:10]:  # Analyze top 10 articles
        title = article.get('title', '')
        description = article.get('description', '')
        content = f"{title} {description}".lower()
        
        for term in terms:
            if term.lower() in content:
                if term not in trend_summary:
                    trend_summary[term] = {'count': 0, 'articles': []}
                trend_summary[term]['count'] += 1
                trend_summary[term]['articles'].append(title)

    return trend_summary

# Get Trend Analysis
trends = analyze_articles(articles, economic_terms)

# Display Trends and Skills
if trends:
    print("\nMarket Trends and Required Skills:")
    for term, info in trends.items():
        print(f"\nTrend: {term.capitalize()} (Mentioned {info['count']} times)")
        print(f"Required Skill: {skills_mapping.get(term, 'General Economics')}")
        print("Example Articles:")
        for article_title in info['articles'][:2]:  # Show top 2 articles
            print(f"- {article_title}")
else:
    print("\nNo significant trends detected.")