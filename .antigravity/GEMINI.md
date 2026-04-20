# 🚀 CODING_RULES.md

## 🧠 Purpose
This document defines strict coding standards for all projects.
These rules apply to both human-written and AI-generated code (Codex, GPT, etc.).

Rule: If code violates this file → it must be rejected or rewritten.

---

## 1. ⚙️ Core Principles
- Keep it simple (KISS)
- Avoid unnecessary features (YAGNI)
- Prefer readability over cleverness
- Write code for humans first, machines second
- Every line of code must have a clear purpose

---

## 2. 🤖 AI Code Generation Rules
- ALWAYS explain logic before writing code
- NEVER generate large files blindly
- ASK before making architectural decisions
- DO NOT assume missing requirements
- START with minimal working solution (MVP)
- AVOID over-engineering

Critical Rule:
AI is treated as a junior developer. All output must be reviewed.

---

## 3. 🏗️ Structure & Architecture
- Follow separation of concerns
- Define responsibility by Action/Domain. Service files must not exceed 300 lines. If a service handles more than 5 distinct business operations, split it into sub-services (e.g., user_auth_service.py, user_profile_service.py).
- Business logic MUST reside in the /services (backend) or /hooks or /logic (frontend) directories. Route handlers and UI components are strictly for I/O: validation, calling services, and returning/rendering data.
- Keep functions small (≤ 40 lines)

### Recommended Structure
- components/ → UI only
- services/ → business logic
- utils/ → helper functions
- types/ → types/interfaces
- api/ → API calls or routes

---

## 4. 🏷️ Naming Conventions
- Use clear, descriptive names
- Avoid unnecessary abbreviations

### Standards
- Variables → camelCase
- Functions → camelCase (use verbs: getUser, calculateTotal)
- Classes → PascalCase
- Constants → UPPER_CASE

### Examples
BAD:
- data, temp, x

GOOD:
- userList, orderTotal, isAuthenticated

---

## 5. 🧹 Code Quality Rules
- Follow DRY (Don’t Repeat Yourself)
- Remove unused variables and dead code
- Avoid hardcoded values → use config/env
- Handle all edge cases
- Prefer early returns over deep nesting

---

## 6. 📝 Comments & Documentation
- Comment WHY, not WHAT
- Avoid obvious comments
- Use docstrings for functions
- Keep comments concise

Example:

BAD:
// increment i
i++

GOOD:
// retry API call if rate limit is hit

---

## 7. 🎨 Formatting & Style
- Use consistent indentation (2 or 4 spaces)
- Max line length: 80–100 characters
- Maintain spacing between logical blocks
- Use auto-formatters (Prettier, Black)

Rule:
Consistency > personal preference

---

## 8. ⚠️ Error Handling
- Never ignore errors
- Use proper try/catch blocks
- Return meaningful error messages
- Fail fast and visibly

---

## 9. 🧪 Testing Mindset
- Write testable code
- Avoid tight coupling
- Validate inputs strictly
- Focus on critical logic testing

---

## 10. 🔁 Git & Version Control
- Use conventional commits (feat:, fix:, docs:, etc.)
- Keep PRs under 400 lines of diff when possible

---

## 11. ⚡ Performance Rules
- Avoid premature optimization
- Optimize only when necessary
- Measure before improving

---

## 12. 🔐 Security Basics
- Never expose secrets
- Use environment variables
- Validate and sanitize all inputs
- Follow least privilege principle

---

## 13. 🧑‍💻 Personal Rule (Non-Negotiable)
- If I do not understand the code → I will NOT accept it
- AI-generated code must be reviewed manually
- Blind trust in generated code is prohibited

---

## 14. 🧠 AI Behavior Mode (Advanced)
AI must:
- Act like a senior engineer
- Challenge bad decisions
- Suggest simpler alternatives
- Explain trade-offs
- Teach, not just generate code

---

## ✅ Final Rule
Code quality is not optional.

If it’s not clean, understandable, and maintainable → it’s not done.