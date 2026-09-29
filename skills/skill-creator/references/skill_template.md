# Skill Template (`SKILL.md`)

```markdown
---
name: [skill-name-lowercase-hyphenated]
description: >-
  [Clear, concise description stating WHAT the skill does and WHEN the agent should activate it.
  Use 3rd person: "Use this skill when...". Limit to <= 1024 characters.]
---

# [Skill Title]

[Brief overview of what this skill enables the agent to do.]

## When to Use

- Use when: ...
- Do NOT use when: ...

## Workflow / Procedures

1. **Step 1: Preparation & Input Gathering**
   - Identify required parameters.
   
2. **Step 2: Execution**
   - If using helper scripts:
     ```bash
     uv run ./scripts/my_script.py [subcommand] --arg value --output ./output.json
     ```

3. **Step 3: Output Processing & Verification**
   - Verify output integrity and format response.

## Reference Materials

- Link to extended documentation in `references/` if necessary.
- [Detailed Guide](references/details.md)
```
