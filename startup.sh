#!/usr/bin/bash

export VERSION=1.0.0
export BACKEND__EXTERNAL__ROOT='/home/ubuntu/FastAPI'


# ------------------------ db ------------------------#

export POSTGRES__INTERNAL__SUPERUSER_NAME="root_user"
export POSTGRES__INTERNAL__SUPERUSER_PASSWORD="root_password"
export POSTGRES__INTERNAL__DEFAULT_DB_NAME="test_db"
export POSTGRES__EXTERNAL__PORT="15432"
export POSTGRES__EXTERNAL__DATA_PATH="${BACKEND__EXTERNAL__ROOT}/data/postgresql/data"


# ------------------------ pgadmin ------------------------#

export PGADMIN__INTERNAL__DEFAULT_EMAIL="admin@admin.com"
export PGADMIN__INTERNAL__DEFAULT_PASSWORD="root"
export PGADMIN__EXTERNAL__PORT=9081


# ------------------------ server ------------------------#
export BACKEND__INTERNAL__ROOT="/code/app"
export APP_SERVER__EXTERNAL__PORT=8080
export APP_SERVER__INTERNAL__PORT=8000