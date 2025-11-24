---
slug: github-supreme-court-data-note-technical-overview
id: github-supreme-court-data-note-technical-overview
title: supreme_court_data Overview
repo: justin-napolitano/supreme_court_data
githubUrl: https://github.com/justin-napolitano/supreme_court_data
generatedAt: '2025-11-24T18:48:22.311Z'
source: github-auto
summary: >-
  This repository handles data wrangling for the US Supreme Court project. It
  pulls structured data and oral arguments from the Oyez API, organizing it by
  case term and docket number.
tags: []
seoPrimaryKeyword: ''
seoSecondaryKeywords: []
seoOptimized: false
topicFamily: null
topicFamilyConfidence: null
kind: note
entryLayout: note
showInProjects: false
showInNotes: true
showInWriting: false
showInLogs: false
---

This repository handles data wrangling for the US Supreme Court project. It pulls structured data and oral arguments from the Oyez API, organizing it by case term and docket number. 

## Key Components:
- **Python 3** and **Jupyter Notebooks** are the primary tools.
- Scripts automate data fetching, merging, and transformation into JSON.
- Integrated with Library of Congress citation data for extra metadata.
- Automated release management keeps data up to date on GitHub.

## Quick Start:

1. Clone the repo:
    ```bash
    git clone https://github.com/justin-napolitano/supreme_court_data.git
    cd supreme_court_data
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. To fetch new data, run:
    ```bash
    python update.py
    ```

4. For GitHub releases, set your token and run:
    ```bash
    export GITHUB_TOKEN=your_token_here
    python publish.py
    ```

### Gotchas:
Make sure you’re using Python 3.7 or higher. The `GITHUB_TOKEN` is required for publishing releases.
