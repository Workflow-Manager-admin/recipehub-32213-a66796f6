#!/bin/bash
cd /home/kavia/workspace/code-generation/recipehub-32213-a66796f6/frontend_web_workspace/frontend_web
npm run lint 
$ESLINT_EXIT_CODE
npm run build
BUILD_EXIT_CODE=$?
if [ $ESLINT_EXIT_CODE -ne 0 ] || [ $BUILD_EXIT_CODE -ne 0 ]; then
  exit 1
fi

