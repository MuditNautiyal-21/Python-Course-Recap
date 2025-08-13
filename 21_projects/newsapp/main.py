import requests

query = input("What are you interested in today?")
api="95956013d17649e6b4207e46314f794a"

url = f"https://newsapi.org/v2/everything?q={query}&from=2025-07-09&sortBy=publishedAt&apiKey={api}"


print(url)

r =requests.get(url)

data = r.json()

articles=data["articles"]

for index, article in enumerate(articles):
    print(index + 1, article["title"], article["url"])
    print("\n==============================\n")