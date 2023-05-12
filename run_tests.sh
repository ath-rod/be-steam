export PGPASSWORD='postgres'

do_connect () {
  psql \
  -U postgres \
  --host 0.0.0.0
}

##
# Terminate every transaction
# to proceed consistently.
do_connect \
<<SQL
SELECT pg_terminate_backend(pid)
FROM pg_stat_activity
WHERE datname='modular_test';
COMMIT;
SQL

##
# Drop databases
do_connect \
<<SQL
DROP DATABASE IF EXISTS modular_test;
COMMIT;
SQL

##
# Recreate databases
do_connect \
<<SQL
CREATE DATABASE modular_test;
COMMIT;
SQL

##
# Execute alembic migrations

export ENV='test'
alembic -c alembic_test.ini upgrade head

##
# Execute Testing Suite
python -m pytest --capture tee-sys
