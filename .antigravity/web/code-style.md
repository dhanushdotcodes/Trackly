## Tech Stack
- Framework: Next.js 15 with App Router
- Language: TypeScript (strict mode)
- Styling: Tailwind CSS v4

## Code Style
- Use functional components only — no class components
- Prefer named exports over default exports
- Use 'interface' for object shapes, 'type' for unions/intersections
- UI Components must use explicit Interfaces for Props. Avoid using 'any' or 'Record<string, any>'. Use 'unknown' and Type Guards if a prop type is truly dynamic.
- Always add JSDoc comments to exported functions

You are an expert in Next.js App Router.

Key Principles:
- Use Server Components by default
- Push 'use client' to the leaf nodes. If a Server Component needs interactivity, wrap the interactive element in a small, dedicated Client Component. Do not place 'use client' at the top of page.tsx files.
- Implement proper loading and error states
- Use Layouts for shared UI

File Structure:
- page.tsx: Unique UI for a route
- layout.tsx: Shared UI for a segment and its children
- loading.tsx: Loading UI for a segment
- error.tsx: Error UI for a segment
- not-found.tsx: Not found UI
- route.ts: API endpoints

Server vs Client Components:
- Server Components (Default): Data fetching, backend resources, sensitive info, large dependencies
- Client Components ('use client'): Event listeners, useState/useEffect, browser APIs, custom hooks

Data Fetching:
- Fetch data in Server Components
- Use async/await directly in components
- Use fetch with caching options
- Implement Static Site Generation (SSG) by default
- Use Server Actions for mutations

Best Practices:
- Colocate components with routes when specific
- Use private folders (_folder) for internal organization
- Use route groups ((folder)) for layout organization without URL changes
- Optimize metadata for SEO