FROM oven/bun:1-alpine AS base
WORKDIR /usr/src/app

# --- Dependencies ---
FROM base AS deps
COPY package.json bun.lockb ./
RUN bun install --frozen-lockfile

# --- Development ---
FROM deps AS development
COPY . .
EXPOSE 3000
CMD ["bun", "run", "dev", "--hostname", "0.0.0.0", "--port", "3000"]

# --- Build ---
FROM deps AS builder
COPY . .
RUN bun run build

# --- Production ---
FROM base AS production
COPY --from=builder /usr/src/app/.next ./.next
COPY --from=builder /usr/src/app/public ./public
COPY --from=builder /usr/src/app/package.json ./package.json
COPY --from=builder /usr/src/app/node_modules ./node_modules

EXPOSE 3000
CMD ["bun", "run", "start", "--hostname", "0.0.0.0", "--port", "3000"]
