source novamed-env/bin/activate

# NovaMed — A LangGraph based AI Agents Built on One Drug's Journey
Same fictional company, same drug-batch journey, same 11 chapters — three implementations. This repo exists to answer one question concretely: when should you reach for LangGraph vs. Google ADK vs. Microsoft Agent Framework, and what does that choice actually cost in code?

Every example below is a subsystem of **NovaMed(A fictiosious drug manufacturer)**: an agentic system that
takes a drug batch from raw-material intake through formulation, quality
control, regulatory documentation, and market-facing drug information, with
a human pharmacist able to intervene at any critical checkpoint.

## The Drug Manufacturing Journey — where each agent fits

```
RAW MATERIAL INTAKE  →  FORMULATION  →  QUALITY CONTROL
Ch.1 Batch Tracker       Ch.1 Batch        Ch.3 Batch Release Agent
Ch.7 Inventory Agent     Tracker           (purity + dosage variance)
                                                 │
                                     ┌───────────┴───────────┐
                                   PASS                     FAIL
                                     │                       │
                          REGULATORY REVIEW          DEVIATION HANDLING
                          Ch.4 Supervisor →           Ch.8 Deviation Report
                          regulatory_agent             Agent (generate →
                                     │                  QA review → revise)
                          BATCH DOCUMENTATION                │
                          Ch.4 Supervisor →           back to FORMULATION
                          documentation_agent
                                     │
                          HUMAN PHARMACIST SIGN-OFF   ← agents inform,
                                     │                   human decides
                          MARKET-FACING DRUG INFO
                          Ch.6 Drug Info & Pricing Assistant
                                     │
                          POST-MARKET SURVEILLANCE
                          Ch.10 Adverse Event Screener
                                     │
                          ONGOING COMPLIANCE
                          Ch.11 Regulatory Guidance Summarizer

R&D (Ch.5) feeds new/reformulated compounds INTO raw material intake.
SOP Assistant (Ch.2) and Plant Operations Router (Ch.9) run alongside
every stage above, supporting plant-floor operators directly.
```

## How to run this notebook

1. Run the **Setup** cell below to install dependencies.
2. Run the **Config** cell and choose `openai` or `ollama` as your provider.
   - `ollama` needs zero API key — install [Ollama](https://ollama.com/download),
     then `ollama pull llama3.2` and `ollama pull nomic-embed-text` before running.
   - `openai` needs `OPENAI_API_KEY` set as an environment variable.
3. Run cells top to bottom — each example builds on state/tools/agents from
   earlier cells, so later cells assume earlier ones have already run.


## Progress Tracker

- [ ] **01 — Batch Stage Tracker** `01_batch_stage_tracker.ipynb`
  State tracking, no LLM — the non-agentic baseline across all 3
  - [x] LangGraph
  - [x] Google ADK
  - [ ] Microsoft Agent Framework

- [ ] **02 — SOP Assistant** `02_sop_assistant.ipynb`
  Simple conversational agent with memory
  - [ ] LangGraph
  - [ ] Google ADK
  - [ ] Microsoft Agent Framework

- [ ] **03 — Batch Release Agent** `03_batch_release_agent.ipynb`
  Single tool-using agent (ReAct loop)
  - [ ] LangGraph
  - [ ] Google ADK
  - [ ] Microsoft Agent Framework

- [ ] **04 — Manufacturing Supervisor** `04_manufacturing_supervisor.ipynb`
  Multi-agent supervisor/coordinator routing
  - [ ] LangGraph
  - [ ] Google ADK
  - [ ] Microsoft Agent Framework

- [ ] **05 — Formulation R&D Pipeline** `05_formulation_rd_pipeline.ipynb`
  Fixed sequential multi-agent pipeline
  - [ ] LangGraph
  - [ ] Google ADK
  - [ ] Microsoft Agent Framework

- [ ] **06 — Drug Info & Pricing Assistant** `06_drug_info_pricing_assistant.ipynb`
  RAG + per-user/session memory
  - [ ] LangGraph
  - [ ] Google ADK
  - [ ] Microsoft Agent Framework

- [ ] **07 — Raw Material Inventory Agent** `07_raw_material_inventory_agent.ipynb`
  Read/write tool agent
  - [ ] LangGraph
  - [ ] Google ADK
  - [ ] Microsoft Agent Framework

- [ ] **08 — Batch Deviation Report Agent** `08_batch_deviation_report_agent.ipynb`
  Reflection loop (draft → review → revise)
  - [ ] LangGraph
  - [ ] Google ADK
  - [ ] Microsoft Agent Framework

- [ ] **09 — Plant Operations Router** `09_plant_operations_router.ipynb`
  Router composing earlier agents
  - [ ] LangGraph
  - [ ] Google ADK
  - [ ] Microsoft Agent Framework

- [ ] **10 — Adverse Event Screener** `10_adverse_event_screener.ipynb`
  Batch reflection loop across a dataset
  - [ ] LangGraph
  - [ ] Google ADK
  - [ ] Microsoft Agent Framework

- [ ] **11 — Regulatory Guidance Summarizer** `11_regulatory_guidance_summarizer.ipynb`
  Single-shot document summarization
  - [ ] LangGraph
  - [ ] Google ADK
  - [ ] Microsoft Agent Framework