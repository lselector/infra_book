
# A Guide to Setting Up and Maintaining a Local AI-Driven "ContextWiki" knowledge management system on a laptop, using Obsidian as the core database, OKF as standard file format, and Claude Code (or a similar LLM developer interface) as the automated AI librarian.

---

## 1. Architectural Philosophy

All data is stored strictly on your laptop's drive in plain text Markdown (`.md`) format.

System uses an ultra-flat directory structure, relying on bi-directional linking rather than subfolders to establish relationships.

## 2. Directory Structure

```text

Your-Context-Wiki/
│
├── .cursor/ or .claude/      # Configuration directories for your local AI tools
├── Inbox/                     # Quick text captures, dictations, and unorganized notes
├── Raw/                       # Immutable source files (web scrapes, transcripts, raw API data)
│
├── Wiki/                      # The Compounding Knowledge Base (Managed by the AI Librarian)
│   ├── Concepts/              # Broad topic overviews (e.g., [[Machine Learning]])
│   ├── Entities/              # Specific elements (e.g., [[OpenAI]], [[Wes Roth]])
│   └── Summaries/             # AI-generated cliff notes and metadata summaries of Raw documents
│
├── Dashboards/                # Actionable visualization layers
│   ├── Projects.md            # Kanban board or task dashboard
│   ├── Index.md               # Dynamic structural anchor for human browsing
│   └── Log.md                 # System operational changelog
│
└── claude.md                  # The AI System Rulebook (The "Employee Handbook")

```

---

## 3. Building the Wiki: From Topics to OKF Files

Creating your own context wiki is a four-stage
pipeline. Each stage feeds the next:

```text
1. Define topics & keywords
        |
2. Download content        -->  Raw/
        |
3. Convert content to .md  -->  Wiki/Summaries/
        |
4. Create OKF files        -->  Wiki/Concepts/, Wiki/Entities/
   and interlink them
```

### Step 1: Define the main topics and keywords

Decide what the wiki is about before collecting
anything.

* List the **main topics** — the big areas the wiki
  should cover (e.g., "Machine Learning", "AI Agents").
* For each topic, list **keywords and subtopics** —
  the search terms for finding content, and the likely
  names of future concept files.
* Save the plan as a simple note (e.g., `Topics.md` in
  `Dashboards/`). It serves as the checklist for the
  rest of the process.

### Step 2: Download content into the "Raw" directory

Collect source material from the internet (articles,
docs, specs, transcripts, blog posts) and store it
unmodified in `Raw/`.

* Keep original formats: `.html`, `.pdf`, `.txt`, `.md`.
* Record the source URL for each file (in the filename
  or a `Raw/sources.md` list) — you will need it later
  for the OKF `resource` field and citations.
* Never edit these files (Source Immutability) — you
  can always re-convert from them.

### Step 3: Convert content into Markdown files

Convert each raw source into clean Markdown.

* Strip navigation, ads, and boilerplate; keep the
  substance.
* Turn long prose into headings, bullets, and tables.
* Replace images with short text descriptions.
* Place cleaned summaries into `Wiki/Summaries/`.

Tools that help: `pandoc` (html/pdf → md),
readability extractors, or the AI Librarian itself.

### Step 4: Create OKF files and interlink them

Reshape the Markdown into OKF concept files — see
[d1_okf.md](d1_okf.md) for the format and
[d2_docs2okf.md](d2_docs2okf.md) for a detailed
conversion tutorial.

1. **One file = one concept.** Each file describes a
   single thing, saved flat into `Wiki/Concepts/` or
   `Wiki/Entities/`.
2. **Add YAML frontmatter** with at least `type`, plus
   `title`, `description`, `resource` (the source URL
   from Step 2), and `tags`.
3. **Structure the body** with headings like
   `# Schema`, `# Examples`, `# Citations`.
4. **Interlink** related concepts with wiki links
   (`[[Entity Name]]`) so the files form a navigable
   graph (see Section 5).
5. **Update `Dashboards/Index.md`** so both humans and
   agents can start broad and drill down.
6. **Commit to Git** — the wiki is now versioned,
   diffable, and recoverable.

When adding new material later, run it through the
same pipeline: `Raw/` → Markdown → OKF.

---

## 4. Configuring the AI Librarian (`claude.md`)

Create a file named `claude.md` in the root of your vault. This acts as the immutable system prompt and behavioral rulebook for your local AI tool (Claude Code / Cursor). Whenever the AI operates within this directory, it must parse and follow these instructions.

```markdown
# AI Librarian System Instructions

You are the automated curator of this local-first Context-Wiki. Your primary objective is to maintain order, process data from the Inbox and Raw directories, build out the Wiki network, and keep everything cross-linked without user intervention.

## Core Directives
1. **Source Immutability:** Never modify or delete files inside the `Raw/` directory. They are legal source truths.
2. **Flat Hierarchy Enforcement:** When creating new knowledge notes, always save them directly into `Wiki/Concepts/` or `Wiki/Entities/`. Never create nested subfolders.
3. **Bi-Directional Linking:** Every time you create or modify a file, you must actively link relevant keywords to their respective pages using wiki syntax: `[[Entity Name]]` or `[[Concept Name]]`.
4. **The Ripple Update Routine:** When parsing a new document, determine if it alters existing knowledge. If a new note mentions an existing entity, open that entity's file and update its context or add a cross-reference back to the new data.

## Processing Pipeline
* **Step 1:** Scan the `Inbox/` and `Raw/` directory for raw texts or newly scraped web dumps.
* **Step 2:** Generate an optimized summary file and place it into `Wiki/Summaries/`.
* **Step 3:** Extract any unique concepts or actors mentioned in the document. Check if they exist in `Wiki/Concepts/` or `Wiki/Entities/`. If they do not, create them using flat structures. If they do, append the new context.
* **Step 4:** Clear processed items out of the `Inbox/` once completely parsed and filed.

```

---

## 5. Document Interlinking Mechanics

Relationships are established organically through links, turning your text files into an interactive graph.

### Syntax Rules

* Use standard wiki links: `[[OpenAI]]`.
* To link a text string to a page with a different name, use the pipe operator: `[[OpenAI|The parent entity of ChatGPT]]`.

### Example of a Connected Note (`Wiki/Entities/Andre Karpathy.md`)

```markdown
# Andre Karpathy

## Background
* Co-founder of [[OpenAI]]
* Former Director of AI at [[Tesla]]

## Key Contributions
* Popularized the idea of an **LLM Wiki**, which serves as the core inspiration for this local [[Context-Wiki]] architecture.
* Advocated for using [[Obsidian]] as an integrated development environment (IDE) for personal thoughts.

## Related Logs
* [[Wiki/Summaries/Karpathy-Stream-Notes-2026-04]]

```

---

## 6. Daily Maintenance and Ingestion

A wiki stays useful only if it is easy to grow and
easy to prune. The two core maintenance operations
are **adding** documents and **removing** them.

### Adding New Documents

New material always goes through the same pipeline
described in Section 3: `Raw/` → Markdown → OKF.

Step by step:

1. **Capture the source.** Save the new document
   (web page, PDF, transcript, note) unmodified into
   `Raw/` — or drop a quick note into `Inbox/` for
   later processing. Record the source URL.
2. **Summarize.** Create a cleaned Markdown summary
   in `Wiki/Summaries/`.
3. **Create or update concept files.** For each new
   concept or entity mentioned:
   - If a file already exists in `Wiki/Concepts/` or
     `Wiki/Entities/`, **append** the new context
     there — do not create a duplicate.
   - If not, create a new OKF file (frontmatter with
     `type`, `title`, `description`, `resource`,
     `tags` — see [d1_okf.md](d1_okf.md)).
4. **Interlink (Ripple Update).** Add `[[wiki links]]`
   from the new file to related existing pages, and
   open those pages to add links back. This keeps the
   graph bi-directional.
5. **Update the dashboards.** Add the new concept to
   `Dashboards/Index.md` and add a dated entry to
   `Dashboards/Log.md`.
6. **Commit to Git** with a short message, e.g.
   `git commit -m "add: Anthropic workspace paper"`.

#### Manual Ingestion via AI CLI

Using Claude Code Desktop or terminal-based AI utilities initialized in your vault's root directory, you can push manual instructions:

```bash
# Ingesting a web source or research paper
claude code "Please read the text block or URL from the clipboard, save it to Raw/Anthropic-Workspace-Paper.md, and run your Ripple Update Routine."

```

### Removing Documents

Remove a document when it is obsolete, duplicated,
wrong, or out of scope. Because files are heavily
interlinked, deletion is more than `rm` — you must
also heal the graph.

Step by step:

1. **Find all references first.** Search the vault
   for links pointing to the file:

   ```bash
   grep -rn "Old Concept Name" Wiki/ Dashboards/
   ```

   (In Obsidian, check the *Backlinks* pane.)
2. **Heal or redirect the links.** In each referring
   file, either delete the link, replace it with a
   link to a better page (e.g. the concept that
   superseded it), or rewrite the sentence.
   Never leave dangling `[[links]]` on purpose.
3. **Merge before deleting (if needed).** If the file
   still contains unique, valuable content, move that
   content into the surviving concept file first.
4. **Delete the Wiki file(s).** Remove the concept
   file and its related summary from
   `Wiki/Summaries/` if the source is gone too.
5. **Keep `Raw/` intact.** Source files in `Raw/` are
   immutable — normally leave them in place even when
   the derived Wiki pages are deleted, so the wiki
   can be rebuilt. Only remove a `Raw/` file when the
   source itself must be purged (e.g. copyright or
   privacy), and note the reason in the log.
6. **Update the dashboards.** Remove the entry from
   `Dashboards/Index.md` and record the removal (what
   and why) in `Dashboards/Log.md`.
7. **Commit to Git**, e.g.
   `git commit -m "remove: obsolete XYZ concept"` —
   the content stays recoverable in history.

You can also delegate the whole routine to the AI
Librarian:

```bash
claude code "Remove Wiki/Concepts/Old-Topic.md: first find all backlinks, redirect or delete them, update Index.md and Log.md, then delete the file."
```

### Context-Aware Querying and Search

Because the database is flat and written in clear markdown text, your local LLM can read, index, and reason across the context instantly without needing a slow vector database. You can query the system natively:

```bash
claude code "Based on my video logs and the trending topics in Raw/Analytics, what AI topics have I underrepresented in the last 90 days?"

```

### Recovering from Corrupt or Hallucinated Data

1. **Traceability:** Because every AI-generated document in `Wiki/` must reference source text, tracing bad data is straightforward. If an AI hallucination occurs, run a keyword search to locate the file, then follow the *Removing Documents* steps above.
2. **Git Version Control (Recommended):** Run `git init` in your Context-Wiki root directory. If the AI introduces formatting errors or corrupts links during an automated update loop, simply execute a `git revert` or `git checkout` to restore the knowledge base to its last clean state.

---

## See also

* [d1_okf.md](d1_okf.md) — the Open Knowledge Format:
  definition, frontmatter fields, and examples.
* [d2_docs2okf.md](d2_docs2okf.md) — converting a single
  document into an OKF concept file.
