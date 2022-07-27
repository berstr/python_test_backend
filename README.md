This service is to test and demo various scenarios with New Relic.

## Env Variables

    export NEW_RELIC_LICENSE_KEY=XXXX

    export NEW_RELIC_APP_NAME=python-test-backend

    export NEW_RELIC_DISTRIBUTED_TRACING_ENABLED=true
    export NEW_RELIC_INFINITE_TRACING_TRACE_OBSERVER_HOST=<Trace Observer Host>
    export NEW_RELIC_APPLICATION_LOGGING_ENABLED=true
    export NEW_RELIC_APPLICATION_LOGGING_FORWARDING_ENABLED=true

Optional:
    export PYTHON_TEST_BACKEND_PORT=XXXX
## CLI

Manual start from command line:

newrelic-admin run-program python3 python_test_backend.py