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
        self.legal_log = []

    def analyze_legal_document(self, document_text):
        """Analyze legal documents related to Liverpool FC"""
        prompt = f"""Analyze this legal document related to Liverpool FC:
        {document_text}
        
        Please provide:
        1. Legal implications
        2. Key terms and conditions
        3. Compliance requirements
        4. Risk assessment
        5. Recommended actions
        6. Legal precedents
        """

        response = self.claude.messages.create(
            model=self.model,
            max_tokens=2000,
            messages=[{
                "role": "user",
                "content": prompt
            }]
        )

        # Log the legal analysis
        legal_entry = {
            "timestamp": datetime.now().isoformat(),
            "document_type": "legal_analysis",
            "findings": response.content,
        }
        self.legal_log.append(legal_entry)
        
        return response.content

    def save_legal_analysis(self, filename="legal_findings.json"):
        """Save legal analysis to a JSON file"""
        with open(filename, 'w') as f:
            json.dump(self.legal_log, f, indent=2)

    def review_compliance(self, topic):
        """Review compliance requirements for specific topics"""
        prompt = f"""Review compliance requirements for Liverpool FC regarding:
        {topic}
        
        Please provide:
        1. Regulatory requirements
        2. Current compliance status
        3. Required documentation
        4. Compliance deadlines
        5. Potential risks
        6. Mitigation strategies
        """

        response = self.claude.messages.create(
            model=self.model,
            max_tokens=1000,
            messages=[{
                "role": "user",
                "content": prompt
            }]
        )
        
        # Log the compliance review
        compliance_entry = {
            "timestamp": datetime.now().isoformat(),
            "topic": topic,
            "compliance_review": response.content,
        }
        self.legal_log.append(compliance_entry)
        
        return response.content

    def analyze_contract(self, contract_text):
        """Analyze contracts and agreements"""
        prompt = f"""Analyze this contract/agreement:
        {contract_text}
        
        Please provide:
        1. Key terms analysis
        2. Obligations and rights
        3. Risk factors
        4. Termination conditions
        5. Legal implications
        6. Recommended modifications
        """

        response = self.claude.messages.create(
            model=self.model,
            max_tokens=1500,
            messages=[{
                "role": "user",
                "content": prompt
            }]
        )
        
        return response.content

def main():
    agent = LiverpoolResearchAgent()
    
    # Example usage
    legal_topic = "Player transfer agreement compliance"
    compliance_review = agent.review_compliance(legal_topic)
    print(f"Compliance review for {legal_topic}:")
    print(compliance_review)
    
    # Save legal analysis
    agent.save_legal_analysis()

if __name__ == "__main__":
    main()
