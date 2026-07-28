---
type: Concept
title: "Retrieval-Augmented Generation"
description: "Answering from your own data by retrieving it and putting it in the prompt - and the cheaper things to try first."
wikipedia: "https://en.wikipedia.org/wiki/Retrieval-augmented_generation"
tags: [ai-in-saas, architectures, storage-and-databases]
timestamp: "2026-07-28T00:00:00Z"
---

# Retrieval-Augmented Generation

A model knows what was in its training data. It does not
know your customer's invoices, your changelog, or the
policy document uploaded this morning. RAG is the
unglamorous fix: **find the relevant text yourself, put
it in the prompt, and ask the question against it.**

Retrieval, prompt assembly, generation. The retrieval
half is ordinary search engineering, and it is where
almost all the quality lives.

## Try these before building an index

1. **Pass the record the user is looking at.** In an
   [[AI Assistant Panel]] scoped to invoice 4471, the
   right context is invoice 4471. No index required, and
   it beats semantic search on the question actually
   being asked.
2. **Use the search you already have.** PostgreSQL
   full-text search over your documents answers keyword
   questions well and costs one `tsvector` column.
3. **Put the whole thing in the prompt.** A handbook that
   fits in the context window does not need chunking, and
   with prompt caching the repeated read is cheap
   ([[Caching]]).

Reach for embeddings when the corpus is too big to send,
and the questions are paraphrases rather than keywords.

## The pipeline

**Ingest** — split documents into chunks of a few hundred
tokens with a little overlap, keeping natural boundaries
(headings, paragraphs). Store the text, the source, and
the `tenant_id`.

**Embed** — turn each chunk into a vector with an
embedding model; store it beside the text.

**Retrieve** — embed the question, take the nearest
chunks by cosine distance, optionally re-rank.

**Generate** — put those chunks in the prompt with their
sources, and instruct the model to answer only from them
and to say so when they do not contain the answer.

**Cite** — render the sources as links. Citations are
what makes the answer checkable, and checkability is what
makes it trustworthy.

## Use the database you already run

[[pgvector]] adds a `vector` column, distance operators
and indexes (HNSW, IVFFlat) to [[PostgreSQL]]. For any
corpus a small SaaS has, this is the right answer: one
database to back up, one to secure, and — decisively —
the vector search and the tenant filter happen in the
same query.

```sql
SELECT chunk, source
  FROM doc_chunks
 WHERE tenant_id = $1                -- not optional
 ORDER BY embedding <=> $2
 LIMIT 5;
```

A dedicated vector database is a second datastore to
operate, replicate and keep in sync, bought before you
have the scale that justifies it
([[Anti-Patterns|premature scaling]]).

## Permissions are the whole ball game

Two rules, both easy to get wrong:

- **Filter by tenant in the query, not in the prompt.**
  The `WHERE tenant_id` clause above is the control.
  Asking the model nicely is not ([[Multi-Tenant SaaS]]).
- **Retrieve only what this user may read.** An index
  built from every document in the tenant will happily
  surface the HR folder to an intern. Store the same
  access metadata your app uses and filter on it
  ([[Authorization]]).

The failure is quiet: no error, no alert, just an answer
containing something the reader should never have seen.

## Watch out for

- **The index goes stale.** Re-embed on write, or run a
  reconciliation job. Answers from deleted documents are
  worse than no answers.
- **Changing the embedding model means reindexing
  everything.** Vectors from different models are not
  comparable. Record which model produced each vector.
- **Chunking is the biggest quality lever.** Too small
  loses context, too large dilutes relevance. Tune it
  against real questions before touching anything else.
- **Hybrid beats pure vector** for names, error codes and
  identifiers — combine full-text and vector scores.
- **Retrieved text is untrusted input**, written by
  users, carrying whatever they typed
  ([[Prompt Injection]]).
- **More chunks is not better.** Every chunk is input
  tokens; five good ones beat fifty
  ([[Usage Quotas and Metering]]).
- **Evaluate.** Keep twenty real questions with known
  good answers and re-run them after every change to
  chunking, retrieval or model.

## Related

[[AI Assistant Panel]] · [[LLM API Integration]] ·
[[pgvector]] · [[PostgreSQL]] · [[Multi-Tenant SaaS]] ·
[[Authorization]] · [[Prompt Injection]] · [[Caching]] ·
[[Tool Calling]] · [[Usage Quotas and Metering]]

## Sources

- [[pgvector-readme]] · [[anthropic-context-windows]] ·
  [[anthropic-prompt-caching]] · [[owasp-llm-top-ten]] ·
  [[postgresql-tutorial-start]] ·
  [[azure-multitenant-storage-data]]
