name: Create Folder and File

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: windows-latest

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v2

      - name: Setup Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.10' # Use the appropriate Python version

      - name: Install Dependencies
        run: |
          pip install -r requirements.txt
          pip install selenium beautifulsoup4 requests

      - name: Execute Python Script
        run: python $GITHUB_WORKSPACE/scripts/web_scraper.py

      - name: Create Folder and File
        run: |
          for /f %%i in ('python scripts/web_scraper.py') do (
            md "%%~ni" 2>nul
            echo. > "%%~ni/%%~nxi.txt"
            echo "%%~ni/%%~nxi.txt"
          )

      - name: Commit and Push Changes
        run: |
          git config user.email "kabirsahu725@gmail.com"
          git config user.name "kabir325"
          git add .
          git commit -m "Generated folder and file"
          git push
