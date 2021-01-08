#!/bin/sh
gunicorn "scheduler.wsgi" -b "0.0.0.0:${PORT}"