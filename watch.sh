#!/bin/bash

watchmedo shell-command -c 'if [ "${watch_event_type}" = "modified" ]; then date; py.test -v tests.py; fi' --patterns "*.py"  . --recursive -wWD
