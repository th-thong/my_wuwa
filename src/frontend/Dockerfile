# --- Stage 1: Base ---
FROM node:18-alpine AS base

RUN apk add --no-cache libc6-compat
WORKDIR /frontend

RUN corepack enable

# --- Stage 2: Deps ---
FROM base AS deps
WORKDIR /frontend

COPY package.json pnpm-lock.yaml* ./
RUN pnpm i --frozen-lockfile

# --- Stage 3: Builder  ---
FROM base AS builder
WORKDIR /frontend

COPY --from=deps /frontend/node_modules ./node_modules
COPY . .

RUN pnpm run build

# --- Stage 4: Runner ---
FROM base AS runner
WORKDIR /frontend

ENV NODE_ENV=production
ENV NEXT_TELEMETRY_DISABLED=1

RUN addgroup --system --gid 1001 nodejs
RUN adduser --system --uid 1001 nextjs

COPY --from=builder /frontend/public ./public
COPY --from=builder --chown=nextjs:nodejs /frontend/.next/standalone ./
COPY --from=builder --chown=nextjs:nodejs /frontend/.next/static ./.next/static


USER nextjs

EXPOSE 3000
ENV PORT=3000

CMD ["node", "server.js"]
