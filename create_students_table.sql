-- Run this in Supabase: Dashboard > SQL Editor > New query

create table if not exists students (
    id bigint generated always as identity primary key,
    name text not null,
    age integer not null,
    grade text not null
);
