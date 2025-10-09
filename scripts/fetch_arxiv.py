"""
Fetch recent arXiv papers related to LLM + Compiler + IR
Usage: python scripts/fetch_arxiv.py > new_papers.md
"""
import feedparser
import urllib.parse

query = "large language model compiler intermediate representation"
url = f"https://export.arxiv.org/api/query?search_query=all:{urllib.parse.quote(query)}&sortBy=submittedDate&max_results=10"

feed = feedparser.parse(url)

for entry in feed.entries:
    title = entry.title.strip()
    link = entry.link
    summary = entry.summary.strip().replace('\n', ' ')
    print(f"- [{title}]({link}) — {summary[:120]}...")
