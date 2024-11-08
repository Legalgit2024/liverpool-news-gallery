# Liverpool News Gallery Research Agent

## Overview
This repository includes a research agent powered by Claude AI that helps gather and analyze Liverpool FC news and information.

## Features
- Automated research on Liverpool FC topics
- News article analysis
- Historical context gathering
- Research logging and storage
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
from research_agent import LiverpoolResearchAgent

# Initialize the agent
agent = LiverpoolResearchAgent()

# Research a topic
findings = agent.research_topic("Liverpool FC's 2024 season performance")

# Analyze a news article
analysis = agent.analyze_news_article("Your article text here")

# Save research findings
agent.save_research()
```

## Research Capabilities
- Historical context analysis
- Key facts and figures compilation
- Recent developments tracking
- Quote collection
- Source verification

## Output
Research findings are saved in JSON format with:
- Timestamp
- Topic
- Detailed findings
- Analysis results
