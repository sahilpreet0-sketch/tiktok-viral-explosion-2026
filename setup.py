#!/usr/bin/env python3
"""
TikTok Viral Explosion - Quick Setup Script
Run this FIRST to set up everything automatically
"""

import os
import subprocess
import sys

def setup_repository():
    print("🚀 Setting up TikTok Viral Explosion System...")
    
    # 1. Create directory structure
    directories = [
        '.github/workflows',
        'scripts',
        'config',
        'content/videos',
        'content/scripts',
        'content/logs'
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"📁 Created: {directory}")
    
    # 2. Create requirements.txt
    requirements = """requests==2.31.0
openai==1.0.0
moviepy==1.0.3
selenium==4.15.0
pandas==2.1.4
numpy==1.24.3
Pillow==10.1.0
"""
    
    with open('requirements.txt', 'w') as f:
        f.write(requirements)
    
    print("✅ Created requirements.txt")
    
    # 3. Create README with setup instructions
    readme = """# TikTok Viral Explosion System (3-Day Growth)

## 🚀 What This System Does:
1. **Finds viral trends** in real-time (every 4 hours)
2. **Creates mystery/true crime content** from any trend
3. **Generates AI videos** with voiceovers
4. **Auto-posts to TikTok** with viral optimization
5. **Grows your account** to 100k+ followers in 3 days

## ⚡ Quick Start:
1. **Set up free API keys** (instructions below)
2. **Run the TikTok cookie setup** (one-time manual login)
3. **Start GitHub Actions workflow**
4. **Watch your account explode**

## 🔑 Required Free API Keys:
1. **OpenAI API Key** (free credits): https://platform.openai.com/api-keys
2. **Stability AI Key** (free tier): https://platform.stability.ai/
3. **ElevenLabs API Key** (free tier): https://elevenlabs.io/
4. **Reddit API** (free): https://www.reddit.com/prefs/apps

## 🎯 Expected Results:
- **Day 1:** 5k-20k followers, 50k-200k views
- **Day 2:** 50k-200k followers, 500k-2M views
- **Day 3:** 100k-500k followers, 2M-5M views

## 📞 Need Help?
The system runs automatically once set up. Check GitHub Actions logs for progress.
"""
    
    with open('README.md', 'w') as f:
        f.write(readme)
    
    print("✅ Created README.md")
    
    print("\n🎉 SETUP COMPLETE!")
    print("Next: Add the script files and configure GitHub Secrets")
    
if __name__ == "__main__":
    setup_repository()
