# 開発環境用ステージ
FROM node:23-alpine AS development

ENV TZ=Asia/Tokyo

RUN adduser -D -h /home/appuser appuser

WORKDIR /src
COPY --chown=appuser:appuser ./frontend/package.json .
COPY --chown=appuser:appuser ./frontend/package-lock.json .
RUN npm install
COPY --chown=appuser:appuser ./frontend .

USER appuser

CMD ["npm", "run", "dev"]

# 本番環境用ステージ
FROM node:23-alpine AS production

ENV TZ=Asia/Tokyo

RUN adduser -D -h /home/appuser appuser

WORKDIR /src
COPY --chown=appuser:appuser ./frontend/package.json .
COPY --chown=appuser:appuser ./frontend/package-lock.json .
COPY --chown=appuser:appuser ./frontend .

RUN npm install && npm run build && npm prune --production

USER appuser

CMD ["npm", "run", "start"]