FROM mysql:5.7
COPY ./init.sql ./docker-entrypoint-initdb.d/init.sql
ENV MYSQL_DATABASE='mysql'
ENV MYSQL_ROOT_PASSWORD=''
ENV MYSQL_ALLOW_EMPTY_PASSWORD=yes
VOLUME [ "/data" ]