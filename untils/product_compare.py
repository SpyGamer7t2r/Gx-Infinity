import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                  " Chrome/92.0.4515.159 Safari/537.36"
}

def clean_title(title):
    return title.replace("\n", "").replace("  ", "").strip()

def search_amazon(product_name):
    try:
        url = f"https://www.amazon.in/s?k={product_name.replace(' ', '+')}"
        response = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(response.text, "html.parser")
        result = soup.select_one(".s-result-item h2 a span")
        price = soup.select_one(".s-result-item .a-price-whole")

        if result and price:
            title = clean_title(result.text)
            price_val = clean_title(price.text)
            return {"site": "Amazon", "title": title, "price": f"₹{price_val}", "url": "https://www.amazon.in" + soup.select_one(".s-result-item h2 a")["href"]}
        return None
    except Exception as e:
        return {"site": "Amazon", "error": str(e)}

def search_flipkart(product_name):
    try:
        url = f"https://www.flipkart.com/search?q={product_name.replace(' ', '+')}"
        response = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(response.text, "html.parser")
        result = soup.select_one("._4rR01T")
        price = soup.select_one("._30jeq3")

        if result and price:
            title = clean_title(result.text)
            price_val = clean_title(price.text)
            link = soup.select_one("a._1fQZEK")["href"]
            return {"site": "Flipkart", "title": title, "price": price_val, "url": "https://www.flipkart.com" + link}
        return None
    except Exception as e:
        return {"site": "Flipkart", "error": str(e)}

def compare_prices(product_name):
    results = []
    amazon_result = search_amazon(product_name)
    flipkart_result = search_flipkart(product_name)
    if amazon_result:
        results.append(amazon_result)
    if flipkart_result:
        results.append(flipkart_result)
    return results
