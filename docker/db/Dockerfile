FROM postgres:13

ENV POSTGRES_USER=root
ENV POSTGRES_PASSWORD=123456
ENV POSTGRES_DB=ops

COPY docker/db/postges-dump.sql /docker-entrypoint-initdb.d