import os
import re

# The pages to generate with full SEO, Canonical, OpenGraph, and Topic-Specific JSON-LD Schema
PAGES = [
    {
        "filename": "crypto-trading-community.html",
        "slug": "crypto-trading-community",
        "title": "TradeWiz | Best Crypto Trading Community in India",
        "description": "Join India's top crypto trading community. Get daily BTC and altcoin watchlists, market cycle breakdowns, scalping setups, and expert crypto mentorship.",
        "h1": 'Join India\'s Top <span class="blue">Crypto Trading</span><br>Community',
        "sub": "Trade Bitcoin, Ethereum, and altcoins with market cycle watchlists, on-chain sentiment analysis, and risk management.",
        "faq_schema": '''  <!-- Topic-Specific FAQ Schema -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [{
      "@type": "Question",
      "name": "What crypto setups does TradeWiz provide?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "TradeWiz provides 20+ weekly crypto setups covering BTC, ETH, and high-momentum altcoins with scalping, swing, and reversal analysis."
      }
    }, {
      "@type": "Question",
      "name": "Is TradeWiz suitable for crypto pattern trading and market cycles?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes! TradeWiz provides on-chain market sentiment breakdowns, weekly cycle watchlists, and live monthly masterclasses."
      }
    }]
  }
  </script>'''
    },
    {
        "filename": "forex-trading-community.html",
        "slug": "forex-trading-community",
        "title": "TradeWiz | Best Forex Trading Community in India",
        "description": "Join India's best forex trading community. Get daily forex trade ideas, live sessions, transparent performance reports, and learn from top forex experts.",
        "h1": 'Join India\'s Best <span class="blue">Forex Trading</span><br>Community',
        "sub": "Master EURUSD, GBPUSD, and GBPJPY with institutional-grade entry, stop loss, and take profit targets.",
        "faq_schema": '''  <!-- Topic-Specific FAQ Schema -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [{
      "@type": "Question",
      "name": "Why is TradeWiz the best Forex trading community in India?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "TradeWiz provides 20+ weekly high-probability forex trade setups across EURUSD, GBPUSD, GBPJPY, and AUDUSD with exact entry, stop loss, target levels, and risk management guidance."
      }
    }, {
      "@type": "Question",
      "name": "Does TradeWiz cover live economic events like NFP and CPI?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes! TradeWiz hosts live trading masterclasses and real-time community streams during major economic releases including NFP, CPI inflation data, and FOMC rate decisions."
      }
    }]
  }
  </script>'''
    },
    {
        "filename": "swing-trading-india.html",
        "slug": "swing-trading-india",
        "title": "TradeWiz | Best Swing Trading Community in India",
        "description": "Join the best swing trading community in India. Get high-probability swing trade setups for stocks and commodities with exact entry and exit levels.",
        "h1": 'Join India\'s Best <span class="blue">Swing Trading</span><br>Community',
        "sub": "Capture explosive multi-day price moves in Indian stocks (NSE/BSE) and commodities while keeping your full-time job.",
        "faq_schema": '''  <!-- Topic-Specific FAQ Schema -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [{
      "@type": "Question",
      "name": "How does swing trading with TradeWiz work for working professionals?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Our swing trade setups focus on daily and 4-hour chart breakouts, allowing members to place orders before market open or after work without staring at screens all day."
      }
    }, {
      "@type": "Question",
      "name": "What markets are covered in TradeWiz Swing Trading?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "We cover Indian large-cap and mid-cap equity stocks, NIFTY 50 futures, Gold, and Crude Oil swing setups."
      }
    }]
  }
  </script>'''
    },
    {
        "filename": "stock-trading-community.html",
        "slug": "stock-trading-community",
        "title": "TradeWiz | Best Stocks Trading Community in India",
        "description": "Learn stock trading with India's top stock trading community. Access daily equity watchlists, market analysis, and live mentorship.",
        "h1": 'Join India\'s Top <span class="blue">Stock Trading</span><br>Community',
        "sub": "Get pre-market watchlists, stock screeners, technical analysis breakdowns, and live market commentary.",
        "faq_schema": '''  <!-- Topic-Specific FAQ Schema -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [{
      "@type": "Question",
      "name": "What stock trading tools does TradeWiz provide?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Members get pre-market watchlists, stock screening filters, technical breakdown videos, live market voice commentary, and brokerage/tax calculators."
      }
    }]
  }
  </script>'''
    },
    {
        "filename": "gold-trading-setups.html",
        "slug": "gold-trading-setups",
        "title": "TradeWiz | Gold Trading Community & Setups in India",
        "description": "Trade XAUUSD like a pro. Join our gold trading community for daily XAUUSD setups, fundamental analysis, and live order flow strategies.",
        "h1": 'Daily <span class="blue">Gold Trading</span><br>Setups & Community',
        "sub": "Master XAUUSD and XAGUSD price action with institutional order flow setups and fundamental driver analysis.",
        "faq_schema": '''  <!-- Topic-Specific FAQ Schema -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [{
      "@type": "Question",
      "name": "What makes Gold (XAUUSD) trading setups at TradeWiz unique?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Our gold trade ideas integrate order flow analysis, institutional liquidity sweeps, DXY correlation, and Federal Reserve interest rate expectations for high-probability setups."
      }
    }]
  }
  </script>'''
    },
    {
        "filename": "forex-mentorship.html",
        "slug": "forex-mentorship",
        "title": "TradeWiz | Forex Mentorship for Beginners in India",
        "description": "Start your forex trading journey. Get expert forex mentorship for beginners in India with live sessions, risk management training, and support.",
        "h1": 'Expert <span class="blue">Forex Mentorship</span><br>For Beginners',
        "sub": "Step-by-step beginner-to-pro mentorship covering chart analysis, risk control, lot sizing, and trader psychology.",
        "faq_schema": '''  <!-- Topic-Specific FAQ Schema -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [{
      "@type": "Question",
      "name": "Is TradeWiz Forex Mentorship suitable for complete beginners?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, our mentorship program starts from basic concepts like lot sizing and pip calculation up to advanced institutional order flow and trade management."
      }
    }]
  }
  </script>'''
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
    canonical_pattern = re.compile(r'<link rel="canonical" href=".*?">')
    og_url_pattern = re.compile(r'<meta property="og:url" content=".*?">')
    og_title_pattern = re.compile(r'<meta property="og:title" content=".*?">')
    og_desc_pattern = re.compile(r'<meta property="og:description" content=".*?">')
    tw_title_pattern = re.compile(r'<meta name="twitter:title" content=".*?">')
    tw_desc_pattern = re.compile(r'<meta name="twitter:description" content=".*?">')
    h1_pattern = re.compile(r'<h1 class="hero-title">.*?</h1>', re.DOTALL)

    for page in PAGES:
        html = template
        url = f"https://www.tradewiz.in/{page['slug']}"
        
        # Replace metadata, Canonical, and OpenGraph URLs
        html = title_pattern.sub(f'<title>{page["title"]}</title>', html)
        html = desc_pattern.sub(f'<meta name="description" content="{page["description"]}">', html)
        html = canonical_pattern.sub(f'<link rel="canonical" href="{url}">', html)
        html = og_url_pattern.sub(f'<meta property="og:url" content="{url}">', html)
        html = og_title_pattern.sub(f'<meta property="og:title" content="{page["title"]}">', html)
        html = og_desc_pattern.sub(f'<meta property="og:description" content="{page["description"]}">', html)
        html = tw_title_pattern.sub(f'<meta name="twitter:title" content="{page["title"]}">', html)
        html = tw_desc_pattern.sub(f'<meta name="twitter:description" content="{page["description"]}">', html)
        
        # Replace H1
        html = h1_pattern.sub(f'<h1 class="hero-title">{page["h1"]}</h1>', html)

        # Replace hreflang and canonical
        html = re.sub(r'<link rel="alternate" hreflang="en-IN" href=".*?">', f'<link rel="alternate" hreflang="en-IN" href="{url}">', html)
        html = re.sub(r'<link rel="alternate" hreflang="x-default" href=".*?">', f'<link rel="alternate" hreflang="x-default" href="{url}">', html)

        breadcrumb_schema = f'''  <!-- BreadcrumbList Schema -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [{{
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://www.tradewiz.in/"
    }},{{
      "@type": "ListItem",
      "position": 2,
      "name": "{page['slug'].replace('-', ' ').title()}",
      "item": "{url}"
    }}]
  }}
  </script>'''

        # Inject topic-specific schema & breadcrumb into head
        html = html.replace('</head>', f'{page["faq_schema"]}\n{breadcrumb_schema}\n</head>')

        with open(page["filename"], "w", encoding="utf-8") as f:
            f.write(html)
        
        print(f"Generated {page['filename']} (Canonical: {url})")

if __name__ == "__main__":
    main()
