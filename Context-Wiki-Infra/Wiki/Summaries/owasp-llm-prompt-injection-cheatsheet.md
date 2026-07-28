---
type: Summary
title: "OWASP LLM Prompt Injection Prevention Cheat Sheet"
description: "Prompt injection is a vulnerability in Large Language Model (LLM) applications that allows attackers to manipulate the model's behavior by injecting malicious input that changes its intended"
resource: "https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html"
source_file: "Raw/12_ai_in_saas/owasp-llm-prompt-injection-cheatsheet.md"
tags: [ai-in-saas, summary]
timestamp: "2026-07-28T00:00:00Z"
---

# OWASP LLM Prompt Injection Prevention Cheat Sheet

Extractive digest of the immutable capture in
`Raw/12_ai_in_saas/owasp-llm-prompt-injection-cheatsheet.md`
(retrieved 2026-07-28).
Lead text and headings are quoted verbatim from
the source; read the capture for the full text.

Source: <https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html>

## Opening

> Prompt injection is a vulnerability in Large Language Model (LLM) applications that allows attackers to manipulate the model's behavior by injecting malicious input that changes its intended output. Unlike traditional injection attacks, prompt injection exploits the common design of most LLMs where ...
> A typical vulnerable LLM integration concatenates user input directly with system instructions:
> def process_user_query(user_input, system_prompt):
> full_prompt = system_prompt + "\n\nUser: " + user_input

## Contents of the source document

- LLM Prompt Injection Prevention Cheat Sheet¶
  - Introduction¶
  - Anatomy of Prompt Injection Vulnerabilities¶
  - Common Attack Types¶
    - Direct Prompt Injection¶
    - Remote/Indirect Prompt Injection¶
    - Encoding and Obfuscation Techniques¶
    - Typoglycemia-Based Attacks¶
    - Best-of-N (BoN) Jailbreaking¶
    - HTML and Markdown Injection¶
    - Jailbreaking Techniques¶
    - Multi-Turn and Persistent Attacks¶
    - System Prompt Extraction¶
    - Data Exfiltration¶
    - Multimodal Injection¶
    - RAG Poisoning (Retrieval Attacks)¶
    - Agent-Specific Attacks¶
  - Primary Defenses¶

## Related pages

[[HTTP]] · [[Incident Response]] · [[Least Privilege]] · [[Monitoring and Alerting]] · [[OWASP]] · [[Prompt Injection]] · [[Rate Limiting]] · [[Retrieval-Augmented Generation]] · [[Security Testing]]
