import os
import re

# The pages to generate
PAGES = [
    {
        "filename": "forex-trading-community.html",
        "title": "TradeWiz | Best Forex Trading Community in India",
        "description": "Join India's best forex trading community. Get daily forex trade ideas, live sessions, transparent performance reports, and learn from top forex experts.",
        "h1": 'Join India\'s Best <span class="blue">Forex Trading</span><br>Community'
    },
    {
        "filename": "swing-trading-india.html",
        "title": "TradeWiz | Best Swing Trading Community in India",
        "description": "Join the best swing trading community in India. Get high-probability swing trade setups for stocks and commodities with exact entry and exit levels.",
        "h1": 'Join India\'s Best <span class="blue">Swing Trading</span><br>Community'
    },
    {
        "filename": "stock-trading-community.html",
        "title": "TradeWiz | Top Stock Trading Community India",
        "description": "Learn stock trading with India's top stock trading community. Access daily equity watchlists, market analysis, and live mentorship.",
        "h1": 'Join India\'s Top <span class="blue">Stock Trading</span><br>Community'
    },
    {
        "filename": "gold-trading-setups.html",
        "title": "TradeWiz | Gold Trading Community & Setups in India",
        "description": "Trade XAUUSD like a pro. Join our gold trading community for daily XAUUSD setups, fundamental analysis, and live order flow strategies.",
        "h1": 'Daily <span class="blue">Gold Trading</span><br>Setups & Community'
    },
    {
        "filename": "forex-mentorship.html",
        "title": "TradeWiz | Forex Mentorship for Beginners in India",
        "description": "Start your forex trading journey. Get expert forex mentorship for beginners in India, complete with live sessions, risk management training, and a supportive community.",
        "h1": 'Expert <span class="blue">Forex Mentorship</span><br>For Beginners'
    }
]

def main():
    if not os.path.exists("index.html"):
        print("index.html not found.")
        return

    with open("index.html", "r", encoding="utf-8") as f:
        template = f.read()

    # Regex patterns to replace
    title_pattern = re.compile(r'<title>.*?</title>')
    desc_pattern = re.compile(r'<meta name="description" content=".*?">')
    og_title_pattern = re.compile(r'<meta property="og:title" content=".*?">')
    og_desc_pattern = re.compile(r'<meta property="og:description" content=".*?">')
    tw_title_pattern = re.compile(r'<meta name="twitter:title" content=".*?">')
    tw_desc_pattern = re.compile(r'<meta name="twitter:description" content=".*?">')
    h1_pattern = re.compile(r'<h1 class="hero-title">.*?</h1>', re.DOTALL)

    for page in PAGES:
        html = template
        
        # Replace metadata
        html = title_pattern.sub(f'<title>{page["title"]}</title>', html)
        html = desc_pattern.sub(f'<meta name="description" content="{page["description"]}">', html)
        html = og_title_pattern.sub(f'<meta property="og:title" content="{page["title"]}">', html)
        html = og_desc_pattern.sub(f'<meta property="og:description" content="{page["description"]}">', html)
        html = tw_title_pattern.sub(f'<meta name="twitter:title" content="{page["title"]}">', html)
        html = tw_desc_pattern.sub(f'<meta name="twitter:description" content="{page["description"]}">', html)
        
        # Replace H1
        html = h1_pattern.sub(f'<h1 class="hero-title">{page["h1"]}</h1>', html)

        with open(page["filename"], "w", encoding="utf-8") as f:
            f.write(html)
        
        print(f"Generated {page['filename']}")

if __name__ == "__main__":
    main()
