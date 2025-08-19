#!/bin/bash

echo "🚀 Updating GitHub Pages branch..."

# Ensure we're on main branch
git checkout main

# Create or update gh-pages branch
if git show-ref --verify --quiet refs/remotes/origin/gh-pages; then
    echo "📋 Updating existing gh-pages branch..."
    git checkout gh-pages
    git pull origin gh-pages
else
    echo "🆕 Creating new gh-pages branch..."
    git checkout -b gh-pages
fi

# Remove all files except .git
git rm -rf . || true

# Copy static website files from main branch
git checkout main -- index.html README.md LICENSE QUICKSTART.md README-gh-pages.md CNAME .gitignore

# Add and commit changes
git add .
git commit -m "Update static website content" || echo "No changes to commit"

# Push to origin
git push origin gh-pages

echo "✅ GitHub Pages branch updated successfully!"
echo "🌐 Your website will be available at: https://robinali34.github.io/leetcode-anki-web/"
echo "📝 Note: It may take a few minutes for changes to appear on GitHub Pages."

# Return to main branch
git checkout main 