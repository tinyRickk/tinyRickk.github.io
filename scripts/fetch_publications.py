#!/usr/bin/env python3
"""
Fetch publications from Google Scholar and update publications.json
This script is run automatically by GitHub Actions monthly.
"""

import json
import sys
from datetime import datetime

try:
    from scholarly import scholarly
except ImportError:
    print("Installing scholarly package...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "scholarly"])
    from scholarly import scholarly

def fetch_google_scholar_papers(author_id):
    """
    Fetch papers from Google Scholar for a specific author
    author_id: Your Google Scholar user ID (from your profile URL)
    """
    try:
        # Search for the author
        author = scholarly.search_author_id(author_id)
        scholarly.fill(author, sections=['publications'])
        
        papers = []
        
        if 'publications' in author:
            for pub in author['publications']:
                try:
                    scholarly.fill(pub)
                    
                    paper = {
                        'title': pub.get('bib', {}).get('title', 'Untitled'),
                        'authors': pub.get('bib', {}).get('author', 'Unknown'),
                        'year': pub.get('bib', {}).get('pub_year', 'N/A'),
                        'venue': pub.get('bib', {}).get('venue', 'Unknown'),
                        'citation_count': pub.get('num_citations', 0),
                        'url': pub.get('pub_url', ''),
                        'type': pub.get('bib', {}).get('type', 'article'),
                    }
                    
                    # Only add papers that have essential information
                    if paper['title'] and paper['year']:
                        papers.append(paper)
                    
                except Exception as e:
                    print(f"Warning: Could not process paper: {e}")
                    continue
        
        # Sort by year (newest first)
        papers.sort(key=lambda x: str(x.get('year', '0')), reverse=True)
        
        return papers
    
    except Exception as e:
        print(f"Error fetching from Google Scholar: {e}")
        return []

def main():
    # Your Google Scholar user ID
    # Found in your scholar profile URL: https://scholar.google.com.au/citations?user=_6mZBnoAAAAJ&hl=en
    SCHOLAR_ID = "_6mZBnoAAAAJ"
    
    print(f"Fetching publications for Google Scholar ID: {SCHOLAR_ID}...")
    
    # Fetch papers
    papers = fetch_google_scholar_papers(SCHOLAR_ID)
    
    if not papers:
        print("No papers found or error occurred. Using existing data...")
        return False
    
    # Prepare data structure
    data = {
        'last_updated': datetime.now().isoformat(),
        'total_papers': len(papers),
        'papers': papers
    }
    
    # Write to JSON file
    output_file = 'data/publications.json'
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"Successfully fetched {len(papers)} papers")
    print(f"Updated: {output_file}")
    
    return True

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
