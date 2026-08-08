import os
import re

# Comprehensive Page Configurations with dedicated SEO Content Hubs
PAGES = [
    {
        "filename": "crypto-trading-community.html",
        "slug": "crypto-trading-community",
        "title": "TradeWiz | Best Crypto Trading Community in India",
        "description": "Join India's top crypto trading community. Get daily BTC and altcoin watchlists, market cycle breakdowns, scalping setups, and expert crypto mentorship.",
        "h1": 'Join India\'s Best <span class="blue">Crypto Trading</span><br>Community',
        "sub": "Trade Bitcoin, Ethereum, and altcoins with market cycle watchlists, on-chain sentiment analysis, and disciplined risk management.",
        "hub_section": '''
  <section class="section" style="padding: 60px 0; border-top: 1px solid rgba(255,255,255,0.08); background: rgba(0,0,0,0.2);">
    <div class="container" style="max-width: 1000px; margin: 0 auto; padding: 0 20px;">
      <h2 style="font-size: 2rem; font-weight: 700; margin-bottom: 24px; color: #fff;">
        Educational Hub: <span class="blue">Mastering Crypto Trading in India</span>
      </h2>
      <p style="color: #94a3b8; font-size: 1.05rem; line-height: 1.7; margin-bottom: 32px;">
        Navigating cryptocurrency volatility requires a structured framework based on market cycles, liquidity sweeps, and disciplined risk management. TradeWiz provides Indian traders with comprehensive educational breakdowns covering Bitcoin (BTC), Ethereum (ETH), and high-momentum altcoins.
      </p>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px; margin-bottom: 32px;">
        <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 24px;">
          <h3 style="font-size: 1.2rem; font-weight: 600; color: #38bdf8; margin-bottom: 12px;">BTC & ETH Market Cycles</h3>
          <p style="color: #cbd5e1; font-size: 0.92rem; line-height: 1.6;">
            Learn how Bitcoin dominance (BTC.D) and Ethereum liquidity dictate capital flow into large-cap and mid-cap altcoins across different stages of the macro market cycle.
          </p>
        </div>
        <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 24px;">
          <h3 style="font-size: 1.2rem; font-weight: 600; color: #34d399; margin-bottom: 12px;">On-Chain Liquidity & Order Flow</h3>
          <p style="color: #cbd5e1; font-size: 0.92rem; line-height: 1.6;">
            Understand exchange inflows, funding rates, open interest spikes, and liquidation heatmaps to avoid trap breakouts and identify genuine accumulation zones.
          </p>
        </div>
        <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 24px;">
          <h3 style="font-size: 1.2rem; font-weight: 600; color: #fbbf24; margin-bottom: 12px;">Strict Crypto Risk Allocation</h3>
          <p style="color: #cbd5e1; font-size: 0.92rem; line-height: 1.6;">
            Protect your capital using disciplined position sizing, trailing stop-losses, and pre-calculated invalidation levels designed specifically for 24/7 crypto markets.
          </p>
        </div>
      </div>
    </div>
  </section>
''',
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
        "text": "TradeWiz provides 20+ weekly educational crypto setups covering BTC, ETH, and high-momentum altcoins with scalping, swing, and reversal analysis."
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
        "hub_section": '''
  <section class="section" style="padding: 60px 0; border-top: 1px solid rgba(255,255,255,0.08); background: rgba(0,0,0,0.2);">
    <div class="container" style="max-width: 1000px; margin: 0 auto; padding: 0 20px;">
      <h2 style="font-size: 2rem; font-weight: 700; margin-bottom: 24px; color: #fff;">
        Educational Hub: <span class="blue">Forex Trading for Indian Traders</span>
      </h2>
      <p style="color: #94a3b8; font-size: 1.05rem; line-height: 1.7; margin-bottom: 32px;">
        Currency trading offers deep 24-hour liquidity, but mastering it requires understanding global macroeconomic drivers, interest rate differentials, and key session overlaps tailored to Indian Standard Time (IST).
      </p>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px; margin-bottom: 32px;">
        <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 24px;">
          <h3 style="font-size: 1.2rem; font-weight: 600; color: #38bdf8; margin-bottom: 12px;">London & NY Session Timing (IST)</h3>
          <p style="color: #cbd5e1; font-size: 0.92rem; line-height: 1.6;">
            Learn how the London open (1:30 PM IST) and New York overlap (6:00 PM – 9:30 PM IST) create the highest volatility and cleanest institutional order flow moves.
          </p>
        </div>
        <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 24px;">
          <h3 style="font-size: 1.2rem; font-weight: 600; color: #34d399; margin-bottom: 12px;">Major Currency Pair Dynamics</h3>
          <p style="color: #cbd5e1; font-size: 0.92rem; line-height: 1.6;">
            Master price action across EUR/USD, GBP/USD, and GBP/JPY with institutional supply/demand zones, fair value gaps (FVG), and liquidity sweep confirmation.
          </p>
        </div>
        <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 24px;">
          <h3 style="font-size: 1.2rem; font-weight: 600; color: #fbbf24; margin-bottom: 12px;">Lot Sizing & Currency Risk</h3>
          <p style="color: #cbd5e1; font-size: 0.92rem; line-height: 1.6;">
            Calculate exact micro (0.01), mini (0.10), and standard (1.0) lot sizes in INR to ensure your account risk never exceeds 1% per currency setup.
          </p>
        </div>
      </div>
    </div>
  </section>
''',
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
        "hub_section": '''
  <section class="section" style="padding: 60px 0; border-top: 1px solid rgba(255,255,255,0.08); background: rgba(0,0,0,0.2);">
    <div class="container" style="max-width: 1000px; margin: 0 auto; padding: 0 20px;">
      <h2 style="font-size: 2rem; font-weight: 700; margin-bottom: 24px; color: #fff;">
        Educational Hub: <span class="blue">Swing Trading Framework for Working Professionals</span>
      </h2>
      <p style="color: #94a3b8; font-size: 1.05rem; line-height: 1.7; margin-bottom: 32px;">
        Swing trading is the most sustainable trading methodology for Indian working professionals. By analyzing 4-hour and daily timeframe charts, you can capture 5% to 20% price expansions over days or weeks without staring at live market screens all day.
      </p>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px; margin-bottom: 32px;">
        <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 24px;">
          <h3 style="font-size: 1.2rem; font-weight: 600; color: #38bdf8; margin-bottom: 12px;">Multi-Day Breakout Setups</h3>
          <p style="color: #cbd5e1; font-size: 0.92rem; line-height: 1.6;">
            Learn how to identify institutional base building, stage-2 breakouts, and volume dry-ups across high-momentum NSE/BSE equity stocks.
          </p>
        </div>
        <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 24px;">
          <h3 style="font-size: 1.2rem; font-weight: 600; color: #34d399; margin-bottom: 12px;">Pre-Market & Weekend Planning</h3>
          <p style="color: #cbd5e1; font-size: 0.92rem; line-height: 1.6;">
            Perform thorough top-down technical analysis on weekends and place GTT/bracket orders with your broker before market open at 9:15 AM IST.
          </p>
        </div>
        <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 24px;">
          <h3 style="font-size: 1.2rem; font-weight: 600; color: #fbbf24; margin-bottom: 12px;">Trailing Stop-Loss Systems</h3>
          <p style="color: #cbd5e1; font-size: 0.92rem; line-height: 1.6;">
            Ride massive market trends by trailing your stop-loss beneath key 20-day exponential moving averages (EMA) and prior swing lows.
          </p>
        </div>
      </div>
    </div>
  </section>
''',
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
        "h1": 'Join India\'s Best <span class="blue">Stocks Trading</span><br>Community',
        "sub": "Get pre-market watchlists, stock screeners, technical analysis breakdowns, and live market commentary.",
        "hub_section": '''
  <section class="section" style="padding: 60px 0; border-top: 1px solid rgba(255,255,255,0.08); background: rgba(0,0,0,0.2);">
    <div class="container" style="max-width: 1000px; margin: 0 auto; padding: 0 20px;">
      <h2 style="font-size: 2rem; font-weight: 700; margin-bottom: 24px; color: #fff;">
        Educational Hub: <span class="blue">Indian Stock Market (NSE / BSE) Technical Analysis</span>
      </h2>
      <p style="color: #94a3b8; font-size: 1.05rem; line-height: 1.7; margin-bottom: 32px;">
        Trading Indian equities successfully requires understanding NIFTY 50 and BANK NIFTY market structure, sector rotation dynamics, and institutional volume patterns across NSE cash and derivative segments.
      </p>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px; margin-bottom: 32px;">
        <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 24px;">
          <h3 style="font-size: 1.2rem; font-weight: 600; color: #38bdf8; margin-bottom: 12px;">NIFTY 50 & Sector Rotations</h3>
          <p style="color: #cbd5e1; font-size: 0.92rem; line-height: 1.6;">
            Learn how institutional capital rotates between Banking, IT, Auto, Pharma, and FMCG sectors to identify the strongest leading stocks in the market.
          </p>
        </div>
        <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 24px;">
          <h3 style="font-size: 1.2rem; font-weight: 600; color: #34d399; margin-bottom: 12px;">Technical Stock Screening</h3>
          <p style="color: #cbd5e1; font-size: 0.92rem; line-height: 1.6;">
            Master price action filters, 52-week high momentum scanners, and consolidation breakout setups across 1500+ NSE listed stocks.
          </p>
        </div>
        <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 24px;">
          <h3 style="font-size: 1.2rem; font-weight: 600; color: #fbbf24; margin-bottom: 12px;">Brokerage & Capital Management</h3>
          <p style="color: #cbd5e1; font-size: 0.92rem; line-height: 1.6;">
            Understand STT, exchange turnover fees, and brokerage impact using precision calculators to maintain positive trading expectancy.
          </p>
        </div>
      </div>
    </div>
  </section>
''',
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
    }, {
      "@type": "Question",
      "name": "Why is TradeWiz the best stocks trading community in India?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "TradeWiz offers daily NSE/BSE equity watchlists, pre-market technical breakdowns, and comprehensive risk management training for Indian stock traders."
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
        "hub_section": '''
  <section class="section" style="padding: 60px 0; border-top: 1px solid rgba(255,255,255,0.08); background: rgba(0,0,0,0.2);">
    <div class="container" style="max-width: 1000px; margin: 0 auto; padding: 0 20px;">
      <h2 style="font-size: 2rem; font-weight: 700; margin-bottom: 24px; color: #fff;">
        Educational Hub: <span class="blue">Gold (XAU/USD) Order Flow & Macro Analysis</span>
      </h2>
      <p style="color: #94a3b8; font-size: 1.05rem; line-height: 1.7; margin-bottom: 32px;">
        Gold is one of the most volatile and liquid instruments in global financial markets. Trading XAUUSD successfully demands an understanding of real bond yields, US Dollar Index (DXY) inverse correlation, and institutional liquidity pool sweeps.
      </p>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px; margin-bottom: 32px;">
        <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 24px;">
          <h3 style="font-size: 1.2rem; font-weight: 600; color: #38bdf8; margin-bottom: 12px;">Institutional Order Flow Sweeps</h3>
          <p style="color: #cbd5e1; font-size: 0.92rem; line-height: 1.6;">
            Learn how market makers engineer liquidity around equal highs and equal lows before initiating explosive multi-hundred pip directional moves.
          </p>
        </div>
        <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 24px;">
          <h3 style="font-size: 1.2rem; font-weight: 600; color: #34d399; margin-bottom: 12px;">DXY & Macro Rate Drivers</h3>
          <p style="color: #cbd5e1; font-size: 0.92rem; line-height: 1.6;">
            Understand the relationship between US Federal Reserve interest rate policy, CPI inflation prints, and bullion demand across global trading sessions.
          </p>
        </div>
        <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 24px;">
          <h3 style="font-size: 1.2rem; font-weight: 600; color: #fbbf24; margin-bottom: 12px;">Gold Scalping & Volatility Control</h3>
          <p style="color: #cbd5e1; font-size: 0.92rem; line-height: 1.6;">
            Manage gold's fast point moves with strict position sizing and precise invalidation zones during high-impact London and New York overlaps.
          </p>
        </div>
      </div>
    </div>
  </section>
''',
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
    }, {
      "@type": "Question",
      "name": "Where to find daily gold trading setups in India?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "TradeWiz provides institutional XAUUSD gold trading setups, order flow analysis, and DXY correlation insights tailored for Indian traders."
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
        "hub_section": '''
  <section class="section" style="padding: 60px 0; border-top: 1px solid rgba(255,255,255,0.08); background: rgba(0,0,0,0.2);">
    <div class="container" style="max-width: 1000px; margin: 0 auto; padding: 0 20px;">
      <h2 style="font-size: 2rem; font-weight: 700; margin-bottom: 24px; color: #fff;">
        Educational Hub: <span class="blue">Structured Forex Mentorship Roadmap</span>
      </h2>
      <p style="color: #94a3b8; font-size: 1.05rem; line-height: 1.7; margin-bottom: 32px;">
        Going from a beginner to a consistently profitable trader requires more than random internet videos. TradeWiz offers a structured, step-by-step curriculum built around technical price action, risk management, and trading psychology.
      </p>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px; margin-bottom: 32px;">
        <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 24px;">
          <h3 style="font-size: 1.2rem; font-weight: 600; color: #38bdf8; margin-bottom: 12px;">Phase 1: Market Foundations</h3>
          <p style="color: #cbd5e1; font-size: 0.92rem; line-height: 1.6;">
            Learn market structure, candlestick reading, support/resistance, pip calculation, and position sizing formulas.
          </p>
        </div>
        <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 24px;">
          <h3 style="font-size: 1.2rem; font-weight: 600; color: #34d399; margin-bottom: 12px;">Phase 2: Institutional Setups</h3>
          <p style="color: #cbd5e1; font-size: 0.92rem; line-height: 1.6;">
            Master supply/demand zones, fair value gaps, liquidity sweeps, and multi-timeframe top-down confirmation.
          </p>
        </div>
        <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 24px;">
          <h3 style="font-size: 1.2rem; font-weight: 600; color: #fbbf24; margin-bottom: 12px;">Phase 3: Psychology & Journaling</h3>
          <p style="color: #cbd5e1; font-size: 0.92rem; line-height: 1.6;">
            Develop unbreakable trading discipline, eliminate revenge trading, and track performance with professional journaling tools.
          </p>
        </div>
      </div>
    </div>
  </section>
''',
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
    }, {
      "@type": "Question",
      "name": "Where to learn forex trading in India for beginners?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "TradeWiz provides step-by-step forex mentorship, live market breakdowns, lot sizing calculators, and supportive community learning for Indian beginners."
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

        # Inject dedicated hub content right before footer
        if "hub_section" in page:
            html = html.replace('<footer', f'{page["hub_section"]}\n<footer')

        with open(page["filename"], "w", encoding="utf-8") as f:
            f.write(html)
        
        print(f"Generated {page['filename']} with dedicated SEO Content Hub (Canonical: {url})")

if __name__ == "__main__":
    main()
