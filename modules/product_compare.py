# modules/product_compare.py

import requests
from bs4 import BeautifulSoup

def compare_product_prices(query):
    results = []

    try:
        # Amazon Search
        amazon_url = f"https://www.amazon.in/s?k={query.replace(' ', '+')}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        }
        response = requests.get(amazon_url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        product = soup.find("div", {"data-component-type": "s-search-result"})
        if product:
            name = product.h2.text.strip()
            link = "https://www.amazon.in" + product.h2.a["href"]
            price_span = product.find("span", {"class": "a-price-whole"})
            price = price_span.text.strip() if price_span else "N/A"
            results.append(f"🛒 <b>Amazon:</b> ₹{price}\n🔗 {link}")
        else:
            results.append("🛒 <b>Amazon:</b> No results found.")

    except Exception as e:
        results.append(f"❌ Amazon Error: {e}")

    try:
        # Flipkart Search
        flipkart_url = f"https://www.flipkart.com/search?q={query.replace(' ', '+')}"
        response = requests.get(flipkart_url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        product = soup.find("div", {"class": "_1AtVbE"})
        if product:
            title = product.find("div", {"class": "_4rR01T"})
            price = product.find("div", {"class": "_30jeq3"})
            link_tag = product.find("a", {"class": "_1fQZEK"})
            if title and price and link_tag:
                name = title.text.strip()
                price = price.text.strip()
                link = "https://www.flipkart.com" + link_tag["href"]
                results.append(f"🏪 <b>Flipkart:</b> {price}\n🔗 {link}")
            else:
                results.append("🏪 <b>Flipkart:</b> No results found.")
        else:
            results.append("🏪 <b>Flipkart:</b> No results found.")
    except Exception as e:
        results.append(f"❌ Flipkart Error: {e}")

    return "\n\n".join(results)