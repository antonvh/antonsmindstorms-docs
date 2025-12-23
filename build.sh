#!/bin/bash

# Activate virtual environment
source .venv/bin/activate

# Build the documentation
cd docs
make html
cd ..

# Open index.html with VS Code and Live Server
open -a "Visual Studio Code" docs/build/html/index.html 2>/dev/null || echo "📄 View at: docs/build/html/index.html"

echo ""
echo "✅ Build complete!"
echo "💡 Right-click index.html in VS Code and select 'Open with Live Server'"
