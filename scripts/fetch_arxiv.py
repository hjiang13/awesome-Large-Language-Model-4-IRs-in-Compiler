"""
Fetch recent arXiv papers related to LLM + Compiler + IR
Usage: python scripts/fetch_arxiv.py
"""
import feedparser
import urllib.parse
import os

query = "large language model compiler intermediate representation"
url = f"https://export.arxiv.org/api/query?search_query=all:{urllib.parse.quote(query)}&sortBy=submittedDate&max_results=10"

feed = feedparser.parse(url)

# 获取项目根目录
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
output_file = os.path.join(project_root, "NEW_PAPERS.md")

# 写入文件
with open(output_file, 'w', encoding='utf-8') as f:
    f.write("# Recent arXiv results for LLM + Compiler + IR\n\n")
    f.write(f"*Last updated: {feed.feed.get('updated', 'Unknown')}*\n\n")
    
    if not feed.entries:
        f.write("No new papers found.\n")
    else:
        for entry in feed.entries:
            title = entry.title.strip()
            link = entry.link
            summary = entry.summary.strip().replace('\n', ' ')
            f.write(f"- [{title}]({link}) — {summary[:120]}...\n")

print(f"Successfully updated {output_file} with {len(feed.entries)} papers")
