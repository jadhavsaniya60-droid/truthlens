print("Welcome to TruthLens 🔍")

news = input("Enter a news headline: ")

if "shocking" in news.lower() or "breaking" in news.lower():
    print("⚠ This might be Fake News!")
else:
    print("✅ This looks more Real.")
