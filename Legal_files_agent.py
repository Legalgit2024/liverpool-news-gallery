import anthropic
import json
import os
from datetime import datetime
from supabase import create_client, Client
from typing import Dict, Any

class LiverpoolLegalAgent:
    def __init__(self):
        # Claude API setup
        self.claude = anthropic.Client(
            api_key="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"
        )
        self.model = "claude-3-opus-20240229"
        
        # Supabase setup for persistent storage
        supabase_url = "https://your-supabase-project.supabase.co"
        supabase_key = os.getenv("SUPABASE_KEY", "your-supabase-key")
        self.supabase: Client = create_client(supabase_url, supabase_key)
        
        self.legal_log = []

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
        prompt = f"""Analyze this legal document related to Liverpool FC:
        {document_text}
        
        Please provide:
        1. Legal implications
        2. Key terms and conditions
        3. Compliance requirements
        4. Risk assessment
        5. Recommended actions
        6. Legal precedents
        7. Evidence classification
        """

        response = self.claude.messages.create(
            model=self.model,
            max_tokens=2000,
            messages=[{
                "role": "user",
                "content": prompt
            }]
        )

        # Prepare evidence data
        evidence_data = {
            "document_type": "legal_analysis",
            "content": document_text,
            "analysis": response.content,
            "classification": "confidential",
            "status": "active"
        }
        
        # Store in Supabase
        evidence_id = self.store_evidence(evidence_data)
        
        return {"evidence_id": evidence_id, "analysis": response.content}

    def review_compliance(self, topic: str) -> Dict[str, Any]:
        """Review compliance and store findings"""
        prompt = f"""Review compliance requirements for Liverpool FC regarding:
        {topic}
        
        Please provide:
        1. Regulatory requirements
        2. Current compliance status
        3. Required documentation
        4. Compliance deadlines
        5. Potential risks
        6. Mitigation strategies
        7. Evidence requirements
        """

        response = self.claude.messages.create(
            model=self.model,
            max_tokens=1000,
            messages=[{
                "role": "user",
                "content": prompt
            }]
        )
        
        # Store compliance review as evidence
        evidence_data = {
            "document_type": "compliance_review",
            "topic": topic,
            "findings": response.content,
            "status": "active"
        }
        
        evidence_id = self.store_evidence(evidence_data)
        
        return {"evidence_id": evidence_id, "review": response.content}

    def analyze_contract(self, contract_text: str) -> Dict[str, Any]:
        """Analyze contracts and store as legal evidence"""
        prompt = f"""Analyze this contract/agreement:
        {contract_text}
        
        Please provide:
        1. Key terms analysis
        2. Obligations and rights
        3. Risk factors
        4. Termination conditions
        5. Legal implications
        6. Recommended modifications
        7. Evidence preservation requirements
        """

        response = self.claude.messages.create(
            model=self.model,
            max_tokens=1500,
            messages=[{
                "role": "user",
                "content": prompt
            }]
        )
        
        # Store contract analysis as evidence
        evidence_data = {
            "document_type": "contract_analysis",
            "content": contract_text,
            "analysis": response.content,
            "status": "active"
        }
        
        evidence_id = self.store_evidence(evidence_data)
        
        return {"evidence_id": evidence_id, "analysis": response.content}

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
    
    # Example usage
    contract_text = """
    [Example contract text for demonstration]
    """
    
    # Analyze contract and store as evidence
    result = agent.analyze_contract(contract_text)
    print(f"Evidence ID: {result['evidence_id']}")
    
    # Export evidence report
    report = agent.export_evidence_report(result['evidence_id'], format="txt")
    print("\nEvidence Report:")
    print(report)

if __name__ == "__main__":
    main()
