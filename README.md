##################################################
# Run Ms Raffin's Super Linter against code base #
##################################################
name: Ms Raffin's Super Linter

on: [push, pull_request]

permissions:
  contents: read
  statuses: write

jobs:
  run-linters:
    name: Ms Raffin's Super Linter
    runs-on: ubuntu-latest
    steps:
      - name: Check out Git repository 🚦
        uses: actions/checkout@v4
        with:
          # Super-Linter requires full git history to accurately determine 
          # modified code deltas across multiple structural branches
          fetch-depth: 0

      - name: Run GitHub Super Linter 🚀
        uses: super-linter/super-linter@v7
        env:
          VALIDATE_ALL_CODEBASE: true
          # FIX: Change to standard workspace root '.' so it safely maps rules internally
          LINTER_RULES_PATH: .
          VALIDATE_CLANG_FORMAT: false
          VALIDATE_JAVASCRIPT_STANDARD: false
          VALIDATE_GOOGLE_JAVA_FORMAT: false
          VALIDATE_PYTHON_FLAKE8: true
          VALIDATE_GITLEAKS: false
          VALIDATE_JSON: false
          VALIDATE_JSCPD: false
          DEFAULT_BRANCH: main
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
