#!/bin/bash

echo "Running demo script..."
echo "Project directory structure:"
tree . || ls -R    # Uses 'tree' if available, else 'ls -R'

echo "Environment variables:"
env

echo "Demo script completed successfully."
