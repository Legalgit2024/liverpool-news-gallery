# Liverpool News Gallery Legal Files Agent

## Overview
This repository includes a legal files agent powered by Claude AI that helps gather, analyze, and manage Liverpool FC news and legal documentation.

## Features
- Automated legal document analysis
- News article processing
- Historical context gathering
- Legal research logging and storage
- JSON output for easy integration

## Setup
1. Install required packages:
```bash
pip install anthropic
```

2. Set up your Claude API key:
```bash
export CLAUDE_API_KEY="your-api-key"
```

## Usage
```python
from Legal_files_agent import LiverpoolResearchAgent

# Initialize the agent
agent = LiverpoolResearchAgent()

# Research a topic
findings = agent.research_topic("Liverpool FC's 2024 legal documentation")

# Analyze a news article
analysis = agent.analyze_news_article("Your article text here")

# Save research findings
agent.save_research()
```

## Legal Research Capabilities
- Legal document analysis
- Historical context review
- Key facts and figures compilation
- Recent developments tracking
- Source verification
- Legal compliance checking

## Output
Research findings are saved in JSON format with:
- Timestamp
- Topic
- Legal analysis
- Document references
- Compliance notes
