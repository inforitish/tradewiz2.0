import datetime
import os

# Base URL configuration
BASE_URL = "https://www.tradewiz.in"

# Today's ISO date string
TODAY = datetime.date.today().strftime("%Y-%m-%d")

# Page definitions with priority and change frequency
PAGES_CONFIG = [
    {"slug": "", "priority": "1.0", "changefreq": "daily"},
    {"slug": "education", "priority": "0.95", "changefreq": "daily"},
    {"slug": "forex-trading-community", "priority": "0.90", "changefreq": "daily"},
    {"slug": "swing-trading-india", "priority": "0.90", "changefreq": "daily"},
    {"slug": "stock-trading-community", "priority": "0.90", "changefreq": "daily"},
    {"slug": "gold-trading-setups", "priority": "0.90", "changefreq": "daily"},
    {"slug": "crypto-trading-community", "priority": "0.90", "changefreq": "daily"},
    {"slug": "forex-mentorship", "priority": "0.90", "changefreq": "daily"},
    {"slug": "calculator", "priority": "0.85", "changefreq": "weekly"},
    {"slug": "about", "priority": "0.80", "changefreq": "monthly"},
    {"slug": "editorial-policy", "priority": "0.80", "changefreq": "monthly"},
    {"slug": "disclaimer", "priority": "0.30", "changefreq": "monthly"},
    {"slug": "privacy", "priority": "0.30", "changefreq": "monthly"},
    {"slug": "terms", "priority": "0.30", "changefreq": "monthly"},
    {"slug": "refund", "priority": "0.30", "changefreq": "monthly"},
]

def generate_sitemap():
    sitemap_entries = ['<?xml version="1.0" encoding="UTF-8"?>']
    sitemap_entries.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

    for page in PAGES_CONFIG:
        slug = page["slug"]
        loc = f"{BASE_URL}/{slug}".rstrip("/") + ("/" if slug == "" else "")
        entry = f"""  <url>
    <loc>{loc}</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>{page['changefreq']}</changefreq>
    <priority>{page['priority']}</priority>
  </url>"""
        sitemap_entries.append(entry)

    sitemap_entries.append("</urlset>\n")
    sitemap_content = "\n".join(sitemap_entries)

    sitemap_path = os.path.join(os.path.dirname(__file__), "sitemap.xml")
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(sitemap_content)
    
    print(f"Successfully generated sitemap.xml with {len(PAGES_CONFIG)} URLs and lastmod {TODAY}.")

if __name__ == "__main__":
    generate_sitemap()
