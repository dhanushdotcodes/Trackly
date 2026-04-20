# TypeScript Safety

- Enable `strict: true` in tsconfig.
- Do not use `any`; use `unknown` when the type is uncertain.
- Handle `null` and `undefined` explicitly.
- Use type guards to narrow uncertain values.
- Use discriminated unions for complex state.
- Use `readonly` and `as const` where they improve safety.
- Prefer `interface` for public object shapes and `type` for unions/intersections.
- Do not throw strings; throw `Error` objects.
- Use exhaustiveness checks in switch statements.