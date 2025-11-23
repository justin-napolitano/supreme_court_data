# US Supreme Court Annotated Transcripts Data Wrangling

This repository contains the data wrangling scripts and utilities for the US Supreme Court project, which collects, processes, and organizes structured data related to Supreme Court cases and their oral argument transcripts. The data is sourced primarily from the Oyez Project's public API and is updated regularly.

## Features

- Automated fetching and updating of Supreme Court case data and oral argument transcripts from the Oyez API.
- Data files structured by case term and docket number, with separate files for transcripts of multiple oral arguments.
- Integration with Library of Congress citation data for enhanced metadata.
- Scripts to merge and transform data from various sources into JSON formats for downstream use.
- Automated release management via GitHub API to maintain up-to-date dataset versions.

## Tech Stack

- Python 3
- Jupyter Notebooks (primary language for data exploration and processing)
- Requests library for HTTP API interactions
- ratelimit for API call throttling
- pandas for data manipulation

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Git

### Installation

Clone the repository:

```bash
git clone https://github.com/justin-napolitano/supreme_court_data.git
cd supreme_court_data
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### Running Update Script

The `update.py` script fetches new or missing Supreme Court cases and transcripts from the Oyez API. Run:

```bash
python update.py
```

### Publishing Releases

The `publish.py` script manages GitHub releases, keeping a maximum of 3 releases and creating a new release tagged with the current date. It requires the `GITHUB_TOKEN` environment variable to be set with a valid GitHub API token.

```bash
export GITHUB_TOKEN=your_token_here
python publish.py
```

## Project Structure

```
supreme_court_data/
├── oyez/                      # Data processing and merging scripts
│   ├── json_to_db.py          # Converts JSON data to database-ready format
│   ├── merge_scdb.py          # Merges Supreme Court Database data with master dataset
│   ├── merge_scdb_with_master.py # Extended merging with master data
│   ├── merge_python.py        # Additional merging utilities
│   ├── rename_oyez_files.py   # Renames and organizes Oyez JSON files
│   ├── loc_cited/             # Library of Congress cited case JSON files
│   └── case_summaries.json    # Sample case summaries data
├── publish.py                 # Script to manage GitHub releases
├── update.py                  # Script to fetch and update case and transcript data
├── README.md                  # This file
└── requirements.txt           # Python dependencies
```

## Future Work / Roadmap

- Enhance error handling and retry mechanisms in API fetching scripts.
- Expand data integration with additional legal databases and metadata sources.
- Develop a database backend to store and query the case and transcript data efficiently.
- Implement more comprehensive automated testing.
- Add detailed documentation and usage examples for each script.
- Improve the data update automation workflow and monitoring.

---

*Note: Some assumptions about project details and structure were made based on available code and data samples.*