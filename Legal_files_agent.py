import json
import os
import requests
from datetime import datetime
from supabase import create_client, Client
from typing import Dict, Any

class LiverpoolLegalAgent:
    def __init__(self):
        # OpenRouter setup
        self.api_key = "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"
        self.api_base = "https://openrouter.ai/api/v1"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "HTTP-Referer": "https://github.com/Legalgit2024/liverpool-news-gallery",
            "Content-Type": "application/json"
        }
        
        # Supabase setup
        self.supabase_url = "https://gzlsscfspnymadqtozhv.supabase.co"
        self.supabase_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imd6bHNzY2ZzcG55bWFkcXRvemh2Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjkxMTAzNjIsImV4cCI6MjA0NDY4NjM2Mn0.-IczsQ1LgwoPmXoi0hQblr1RA4JU9lyBOGxTpMB9SGU"
        self.supabase: Client = create_client(self.supabase_url, self.supabase_key)
        
        self.legal_log = []

    def query_openrouter(self, messages):
        """Send request to OpenRouter API"""
        response = requests.post(
            f"{self.api_base}/chat/completions",
            headers=self.headers,
            json={
                "model": "anthropic/claude-3.5-sonnet:beta",
                "messages": messages
            }
        )
        return response.json()

    def store_evidence(self, evidence_data: Dict[str, Any]) -> str:
        """Store legal evidence in Supabase"""
        try:
            # Add timestamp and unique identifier
            evidence_data["timestamp"] = datetime.now().isoformat()
            evidence_data["evidence_id"] = f"EV-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
            
            # Store in Supabase
            result = self.supabase.table("legal_evidence").insert(evidence_data).execute()
            
            return evidence_data["evidence_id"]
        except Exception as e:
            print(f"Error storing evidence: {e}")
            return None

    def analyze_legal_document(self, document_text: str) -> Dict[str, Any]:
        """Analyze legal documents and store as evidence"""
        messages = [{
            "role": "user",
            "content": f"""Analyze this legal document related to Liverpool FC:
            {document_text}
            
            Please provide:
            1. Legal implications
            2. Key terms and conditions
            3. Compliance requirements
            4. Risk assessment
            5. Recommended actions
            6. Legal precedents
            7. Evidence classification"""
        }]

        response = self.query_openrouter(messages)
        analysis = response['choices'][0]['message']['content']

        # Prepare evidence data
        evidence_data = {
            "document_type": "legal_analysis",
            "content": document_text,
            "analysis": analysis,
            "classification": "confidential",
            "status": "active"
        }
        
        # Store in Supabase
        evidence_id = self.store_evidence(evidence_data)
        
        return {"evidence_id": evidence_id, "analysis": analysis}

    def review_compliance(self, topic: str) -> Dict[str, Any]:
        """Review compliance and store findings"""
        messages = [{
            "role": "user",
            "content": f"""Review compliance requirements for Liverpool FC regarding:
            {topic}
            
            Please provide:
            1. Regulatory requirements
            2. Current compliance status
            3. Required documentation
            4. Compliance deadlines
            5. Potential risks
            6. Mitigation strategies
            7. Evidence requirements"""
        }]

        response = self.query_openrouter(messages)
        review = response['choices'][0]['message']['content']
        
        # Store compliance review as evidence
        evidence_data = {
            "document_type": "compliance_review",
            "topic": topic,
            "findings": review,
            "status": "active"
        }
        
        evidence_id = self.store_evidence(evidence_data)
        
        return {"evidence_id": evidence_id, "review": review}

    def analyze_contract(self, contract_text: str) -> Dict[str, Any]:
        """Analyze contracts and store as legal evidence"""
        messages = [{
            "role": "user",
            "content": f"""Analyze this contract/agreement:
            {contract_text}
            
            Please provide:
            1. Key terms analysis
            2. Obligations and rights
            3. Risk factors
            4. Termination conditions
            5. Legal implications
            6. Recommended modifications
            7. Evidence preservation requirements"""
        }]

        response = self.query_openrouter(messages)
        analysis = response['choices'][0]['message']['content']
        
        # Store contract analysis as evidence
        evidence_data = {
            "document_type": "contract_analysis",
            "content": contract_text,
            "analysis": analysis,
            "status": "active"
        }
        
        evidence_id = self.store_evidence(evidence_data)
        
        return {"evidence_id": evidence_id, "analysis": analysis}

    def retrieve_evidence(self, evidence_id: str) -> Dict[str, Any]:
        """Retrieve stored evidence from Supabase"""
        try:
            result = self.supabase.table("legal_evidence").select("*").eq("evidence_id", evidence_id).execute()
            return result.data[0] if result.data else None
        except Exception as e:
            print(f"Error retrieving evidence: {e}")
            return None

    def export_evidence_report(self, evidence_id: str, format: str = "json") -> str:
        """Export evidence in specified format"""
        evidence = self.retrieve_evidence(evidence_id)
        if not evidence:
            return None
            
        if format == "json":
            return json.dumps(evidence, indent=2)
        elif format == "txt":
            return f"""
Evidence Report
ID: {evidence['evidence_id']}
Type: {evidence['document_type']}
Timestamp: {evidence['timestamp']}
Status: {evidence['status']}
Content: {evidence['content']}
Analysis: {evidence['analysis']}
            """
        return None

def main():
    agent = LiverpoolLegalAgent()
    
    # Example usage with test document
    test_document = """
    This is a test legal document for Liverpool FC regarding player transfer agreements.
    The document outlines terms and conditions for player transfers, including:
    1. Transfer fee structure
    2. Payment schedules
    3. Performance bonuses
    4. Image rights
    """
    
    # Analyze document and store as evidence
    result = agent.analyze_legal_document(test_document)
    print(f"Evidence ID: {result['evidence_id']}")
    print("\nAnalysis:")
    print(result['analysis'])
    
    # Export evidence report
    report = agent.export_evidence_report(result['evidence_id'], format="txt")
    print("\nEvidence Report:")
    print(report)

if __name__ == "__main__":
    main()
