#!/bin/bash

echo "Creating user and replication slot for replication..."
psql -v ON_ERROR_STOP=1 -U $POSTGRES_USER -d $POSTGRES_DB <<-EOSQL
    CREATE USER $REPLICATOR_USER WITH REPLICATION ENCRYPTED PASSWORD '$REPLICATOR_PASSWORD';
    SELECT pg_create_physical_replication_slot('$REPLICATION_SLOT');
EOSQL