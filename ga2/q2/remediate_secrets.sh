# Git Security Rewrite Script (Q2)
# Usage: Run in a repo to remove .env from history

# 1. Identity
git config user.name "24f2001614"
git config user.email "24f2001614@ds.study.iitm.ac.in"

# 2. Rewrite
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch .env" \
  --prune-empty --tag-name-filter cat -- --all

# 3. Prevent
echo ".env" >> .gitignore
echo "API_KEY=your_key_here" >> .env.example
git add .gitignore .env.example
git commit -m "Secure repository: Remove secrets and add guards"
