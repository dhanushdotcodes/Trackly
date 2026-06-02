----
name: skill-name
description: Brief description of what the skill does in one sentence.
----

# Skill: Name of the Skill

## When to Use
Use this skill when:
- Trigger condition 1
- Trigger condition 2

Do NOT use when:
- Anti-trigger condition 1
- Anti-trigger condition 2

---

## Input
- Tech stack, parameters, architecture info, etc.
- Example inputs or user parameters required.

---

## Constraints and Guidelines

* Next.js App Router MUST be used exclusively.
* URLs MUST use `kebab-case` (e.g., `/forgot-password`).
* Private route files MUST be prefixed with `_` (e.g., `_components`, `_lib`).
* Utilities MUST be kept out of route folders.
* Special Next.js files MUST NOT be renamed (e.g., `page.tsx`, `layout.tsx`).
* Use functional components ONLY; NEVER use class components.
* Prefer named exports over default exports.
* UI Components MUST use explicit Interfaces for Props. NEVER use `any` or `Record<string, any>`.
* ALWAYS add JSDoc comments to exported functions.
* Use Server Components by default; push `use client` to the leaf nodes.
* NEVER place `'use client'` at the top of `page.tsx` files.
* Use Server Actions for all mutations.
* ALWAYS follow the Rules of Hooks strictly.
* Optimize hook dependency arrays carefully.
* Use memoization ONLY where it clearly reduces unnecessary work.
* NEVER use `bg-gradient-to-br` for gradients; ALWAYS use `bg-linear-to-br` (Tailwind v4).

### Typescript Guidelines
* TypeScript `strict: true` MUST be enabled.
* NEVER use `any`; use `unknown` and Type Guards if a type is dynamic or uncertain.
* Handle `null` and `undefined` explicitly.
* Use type guards to narrow uncertain values.
* Use discriminated unions for complex state.
* NEVER throw strings; ALWAYS throw `Error` objects.
* Use exhaustiveness checks in all `switch` statements.

### Build & Verify Commands
* Build: `bun run build`
* Test (single): `bun test <file_path>`
* Lint / typecheck: `bun run lint && bun x tsc --noEmit`
* Dev server: `bun run dev`

Always run the lint/typecheck command after a series of edits. Prefer running a single targeted test over the full suite for speed.

---

## Steps to Execute

1. Step One
   - Detail about step one.
   - Any specific sub-actions or tools to use.

2. Step Two
   - Detail about step two.

3. Step Three
   - Detail about step three.

---

## Output Format
- Expected output, files created, or structure.
- Details of how artifacts are formatted and shared.

---

## Checklist
- [ ] Requirements and scope are fulfilled
- [ ] No hardcoded configuration has been introduced
- [ ] Tests or validation steps have been executed
- [ ] Code follows project standards and rules
