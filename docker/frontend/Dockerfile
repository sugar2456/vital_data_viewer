FROM node:23-alpine

ENV TZ=Asia/Tokyo

RUN adduser -D -h /home/appuser appuser

WORKDIR /src
COPY --chown=appuser:appuser ./frontend/package.json .
COPY --chown=appuser:appuser ./frontend/package-lock.json .
RUN npm install
COPY --chown=appuser:appuser ./frontend .

RUN chown -R appuser:appuser /src

USER appuser

CMD ["npm", "run", "dev"]