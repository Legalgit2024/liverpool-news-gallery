import anthropic
import json
import os
from datetime import datetime

class LiverpoolResearchAgent:
    def __init__(self):
        self.claude = anthropic.Client(
            api_key="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"
        )
        self.model = "claude-3-opus-20240229"
        self.research_log = []

    def research_topic(self, topic):
        """Perform research on a Liverpool-related topic"""
        prompt = f"""Research the following Liverpool FC topic: {topic}
        Please provide:
        1. Historical context
        2. Key facts and figures
        3. Recent developments
        4. Notable quotes
        5. Sources for verification
        """

        response = self.claude.messages.create(
            model=self.model,
            max_tokens=2000,
            messages=[{
                "role": "user",
                "content": prompt
            }]
        )

        # Log the research
        research_entry = {
            "timestamp": datetime.now().isoformat(),
            "topic": topic,
            "findings": response.content,
        }
        self.research_log.append(research_entry)
        
        return response.content

    def save_research(self, filename="research_findings.json"):
        """Save research findings to a JSON file"""
        with open(filename, 'w') as f:
            json.dump(self.research_log, f, indent=2)

    def analyze_news_article(self, article_text):
        """Analyze a news article for key information"""
        prompt = f"""Analyze this Liverpool FC news article:
        {article_text}
        
        Please provide:
        1. Main points
        2. Impact on the team/club
        3. Reliability assessment
        4. Related historical context
        """

        response = self.claude.messages.create(
            model=self.model,
            max_tokens=1000,
            messages=[{
                "role": "user",
                "content": prompt
            }]
        )
        
        return response.content

def main():
    agent = LiverpoolResearchAgent()
    
    # Example usage
    research_topic = "Liverpool FC's 2024 season performance"
    findings = agent.research_topic(research_topic)
    print(f"Research findings for {research_topic}:")
    print(findings)
    
    # Save research
    agent.save_research()

if __name__ == "__main__":
    main()
