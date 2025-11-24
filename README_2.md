🤖 Task 2: AI Agent Implementation - Threat Intelligence & Triage Agent

This task fulfills the requirement to develop a simple AI agent, demonstrating the ability to integrate Large Language Models (LLMs) with external tools for real-time, grounded problem-solving. This solution is conceptualized within the high-stakes environment of a Security Operations Center (SOC).

Project Deliverable

File Name

Description

Threat_intelligence.html

A single-file, self-contained web application that hosts the AI Agent. It uses JavaScript, the Gemini API, and Tailwind CSS for the front-end interface.

Agent Objective and Persona

Objective: To accelerate Level 1 (L1) SOC triage by providing analysts with instantaneous, grounded threat intelligence and recommended actions.

Persona: Tier 1 SOC Triage Agent – Professional, concise, and focused on risk mitigation.

Technical Architecture and Methodology

The agent operates on the core ReAct (Reasoning and Acting) principle, utilizing the Gemini API's capabilities to perform grounded generation.

1. Agent Core (Reasoning)

Model: Gemini 2.5 Flash

Instruction: A detailed System Instruction is utilized to enforce the SOC persona, dictating a concise, factual, and action-oriented response format.

2. External Tool (Grounding)

Tool: Google Search Integration (tools: [{"google_search": {}}])

Function: The agent uses real-time web search to ground its responses with current information, such as the latest CVE scores, active exploit techniques, or threat actor details. This ensures the advice is timely and accurate, which is essential in cybersecurity.

3. Workflow

The agent follows a rigorous workflow for every user query:

Input: Analyst submits a query (e.g., "Summarize the latest attack vector for the SolarWinds vulnerability").

Triage: The agent analyzes the input and determines that external, current data is necessary.

Action (Search): The Google Search tool is automatically invoked by the LLM.

Synthesis: The LLM processes the search results and synthesizes a direct, actionable answer.

Output: The response includes the synthesized summary, a recommended next step (e.g., "Isolate host"), and transparent Grounding Sources (citations) for verification.

Key Demonstrations

Prompt Engineering: Successful utilization of the systemInstruction to mold the LLM's behavior into a domain expert (SOC Analyst).

Tool Integration: Confirms proficiency in leveraging external services (APIs) to move beyond simple chat, turning the LLM into an "acting" entity.

UI/UX: A clean, professional user interface enhances the usability of the tool in a simulated operational environment.

Robustness: Implements exponential backoff during API calls to ensure stability against network fluctuations or rate limits.