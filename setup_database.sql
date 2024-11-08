-- Create legal evidence table
create table if not exists legal_evidence (
    id uuid default uuid_generate_v4() primary key,
    evidence_id text unique not null,
    document_type text not null,
    content text,
    analysis text,
    classification text,
    status text,
    timestamp timestamptz default now(),
    metadata jsonb default '{}'::jsonb,
    topic text,
    findings text
);

-- Create index for faster searches
create index if not exists idx_evidence_id on legal_evidence(evidence_id);
create index if not exists idx_document_type on legal_evidence(document_type);
create index if not exists idx_timestamp on legal_evidence(timestamp);

-- Create RLS policy for secure access
alter table legal_evidence enable row level security;

create policy "Enable read access for all users"
    on legal_evidence for select
    using (true);

create policy "Enable insert access for authenticated users"
    on legal_evidence for insert
    with check (true);
