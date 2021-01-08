#!/bin/sh
gunicorn "web:create_app()" -b "0.0.0.0:${PORT}"