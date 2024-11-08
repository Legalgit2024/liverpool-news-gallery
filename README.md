# Liverpool News Gallery Legal Files Agent

## Overview
This repository includes a legal files agent powered by Claude AI that helps gather, analyze, and manage Liverpool FC legal documentation with persistent evidence storage using Supabase.

## Features
- Automated legal document analysis
- Persistent evidence storage in Supabase
- Evidence tracking and retrieval
- Compliance review system
- Contract analysis
- Evidence report generation

## Setup
1. Install required packages:
```bash
pip install anthropic supabase-py python-dotenv
```

2. Set up environment variables:
```bash
export CLAUDE_API_KEY="your-claude-api-key"
export SUPABASE_URL="your-supabase-project-url"
export SUPABASE_KEY="your-supabase-api-key"
```

## Supabase Schema
The agent uses the following table structure in Supabase:

```sql
create table legal_evidence (
    id uuid default uuid_generate_v4() primary key,
    evidence_id text unique not null,
    document_type text not null,
    content text,
    analysis text,
    classification text,
    status text,
    timestamp timestamptz default now(),
    metadata jsonb
);
```

## Usage
```python
from Legal_files_agent import LiverpoolLegalAgent

# Initialize the agent
agent = LiverpoolLegalAgent()

# Analyze a legal document and store as evidence
result = agent.analyze_legal_document("Your legal document text")
evidence_id = result['evidence_id']

# Retrieve stored evidence
evidence = agent.retrieve_evidence(evidence_id)

# Generate evidence report
report = agent.export_evidence_report(evidence_id, format="txt")
```

## Evidence Management
- Each piece of evidence gets a unique identifier
- Evidence is stored with timestamps and classification
- Multiple export formats supported (JSON, TXT)
- Evidence can be retrieved and analyzed later

## Legal Analysis Capabilities
- Document analysis with legal implications
- Compliance review and tracking
- Contract analysis and risk assessment
- Evidence preservation and management
- Automated report generation

## Security Features
- Secure storage in Supabase
- Evidence classification system
- Audit trail with timestamps
- Access control through Supabase

## Evidence Export Formats
1. JSON Format
- Complete evidence data
- Metadata included
- Machine-readable

2. Text Format
- Human-readable reports
- Formatted for documentation
- Includes all key information

## Best Practices
1. Evidence Handling
- Always use unique evidence IDs
- Include proper classification
- Maintain chain of custody

2. Storage
- Regular backups
- Proper access control
- Evidence verification

3. Reporting
- Consistent formatting
- Complete documentation
- Clear analysis summaries
