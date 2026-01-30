import openai
import json
import os

def generate_script(trend):
    openai.api_key = os.getenv('OPENAI_API_KEY')
    
    prompt = f"""
    Create a viral TikTok mystery script about: {trend['name']}
    
    Make it:
    1. Hook in first 3 seconds
    2. Build suspense
    3. End with cliffhanger
    4. Optimized for TikTok algorithm 2026
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    with open('config/trending_topics.json', 'r') as f:
        trends = json.load(f)
    
    script = generate_script(trends[0])
    with open('content/scripts/script_1.txt', 'w') as f:
        f.write(script)
    
    print("✅ Generated viral script")
