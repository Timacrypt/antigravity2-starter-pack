# Antigravity 2.0 Agent Automation Protocol (AGENTS.md)

This file contains automated instructions for **Google Antigravity 2.0** and compatible AI coding agents.
When a user asks you to "install", "setup", or "import" the skills and tools from this repository, follow these precise instructions step by step.

---

## 🤖 Instructions for Antigravity 2.0

### Step 1: Identify Installation Directories
1. Global Skills Directory:
   - Path: `~/.gemini/config/skills/` (expand `~` to the user's home directory).
   - If this directory does not exist, create it.
2. Global MCP Directory:
   - Path: `~/.gemini/antigravity/mcp/notebooklm/`
   - If this directory does not exist, create it.

### Step 2: Install Skills
Copy every folder inside the `skills/` directory of this repository into the user's global skills directory (`~/.gemini/config/skills/`):
- `brainstorming/`
- `teach/`
- `grill-me/`
- `wait-what/` (Customized: Traditional Chinese zhtw, 10th-grade high school level, English technical terms)
- `handoff/`
- `to-questionnaire/`
- `writing-for-agents/`
- `docx/`
- `xlsx/`
- `pptx/`
- `pdf/`
- `skill-creator/`
- `find-skills/`

*Note: Overwrite any existing files if the user requested a fresh installation or upgrade.*

### Step 3: Install Python Dependencies
The document processing skills (`docx`, `xlsx`, `pptx`, `pdf`) require standard Python libraries.
Run the following shell command using your terminal tool:
```bash
pip install -r requirements.txt
```
*(Libraries installed: `python-docx`, `openpyxl`, `python-pptx`, `pypdf`, `pymupdf`)*

### Step 4: Install clasp (Google Apps Script CLI)
Check if Node.js (`npm`) is available in the user's system:
```bash
npm install -g @google/clasp
```
If npm is not installed or permission is denied, notify the user and provide instructions from `mcp-and-tools/clasp/README.md`.

### Step 5: Configure NotebookLM MCP
1. Copy the configuration and instruction files from `mcp-and-tools/notebooklm/` to `~/.gemini/antigravity/mcp/notebooklm/`.
2. Inform the user to run `nlm login` in their terminal to authenticate with their Google account for NotebookLM.

### Step 6: Confirmation & Summary
Once installation is complete, output a clear summary to the user in Traditional Chinese (繁體中文):
- List all 11 installed Skills with brief descriptions.
- Explain how to trigger `/wait-what` (生動白話重新解釋).
- Explain how to use Office document skills (Word, Excel, PowerPoint, PDF).
- Provide next steps for `clasp login` and `nlm login`.
