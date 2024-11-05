create policy "Allow anonymous delete"
    on news_galleries for delete to anon using (true);
alter table news_galleries alter column title type varchar(255);
alter table news_galleries add column status text;
-- Create the news_galleries table
create table if not exists news_galleries (
    id uuid default gen_random_uuid() primary key,
    created_at timestamp with time zone default timezone('utc'::text, now()) not null,
    data jsonb not null,
    title varchar(255),
    description text,
    status text
);

-- Create the gallery_comments table
create table if not exists gallery_comments (
    id uuid default gen_random_uuid() primary key,
    gallery_id uuid references news_galleries(id),
    card_index integer not null,
    comment text not null,
    created_at timestamp with time zone default timezone('utc'::text, now()) not null
);

-- Enable Row Level Security (RLS)
alter table news_galleries enable row level security;
alter table gallery_comments enable row level security;

-- Create policies for news_galleries
create policy if not exists "Allow anonymous read access"
    on news_galleries for select to anon using (true);

create policy if not exists "Allow anonymous insert"
    on news_galleries for insert to anon with check (true);

create policy if not exists "Allow anonymous update"
    on news_galleries for update to anon using (true);

create policy if not exists "Allow anonymous delete"
    on news_galleries for delete to anon using (true);


-- Create policies for gallery_comments
create policy if not exists "Allow anonymous read access"
    on gallery_comments for select to anon using (true);

create policy if not exists "Allow anonymous insert"
    on gallery_comments for insert to anon with check (true);

create policy if not exists "Allow anonymous update"
    on gallery_comments for update to anon using (true);

-- Create indexes
create index news_galleries_created_at_idx on news_galleries (created_at desc);
create index gallery_comments_gallery_id_idx on gallery_comments (gallery_id);
