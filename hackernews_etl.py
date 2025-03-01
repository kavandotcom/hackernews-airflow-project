import requests
import pandas as pd

def run_hackernews_etl():
    base_url = "https://hacker-news.firebaseio.com/v0"
    top_stories_url = f"{base_url}/topstories.json"

    response = requests.get(top_stories_url)
    
    # Print API response
    print("API Response Status:", response.status_code)
    
    if response.status_code == 200:
        top_story_ids = response.json()[:50]  # Fetch top 50 stories
        print("Top Story IDs:", top_story_ids)
    else:
        print("Failed to fetch data")
        return

    stories = []
    for story_id in top_story_ids:
        story_url = f"{base_url}/item/{story_id}.json"
        story_data = requests.get(story_url).json()
        
        stories.append({
            "title": story_data.get("title", "N/A"),
            "score": story_data.get("score", 0),
            "url": story_data.get("url", "N/A"),
            "time": pd.to_datetime(story_data.get("time", 0), unit='s')
        })

    # Print extracted data
    print("Extracted Stories:", stories)

    df = pd.DataFrame(stories)
    df.to_csv("hackernews_top_stories.csv", index=False)
    print("Hacker News ETL process completed. Data saved to hackernews_top_stories.csv")

# Run the function
run_hackernews_etl()
