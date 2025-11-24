---
slug: github-supreme-court-data
title: Automated Data Pipeline for US Supreme Court Case Transcripts
repo: justin-napolitano/supreme_court_data
githubUrl: https://github.com/justin-napolitano/supreme_court_data
generatedAt: '2025-11-23T09:45:18.470770Z'
source: github-auto
summary: >-
  Technical overview of an automated system collecting, processing, and organizing US Supreme Court
  oral argument transcripts and case metadata.
tags:
  - legal-data
  - data-pipeline
  - supreme-court
  - api-integration
  - automation
seoPrimaryKeyword: supreme court data
seoSecondaryKeywords:
  - oral argument transcripts
  - ozey api
  - legal metadata
seoOptimized: true
---

# US Supreme Court Data Wrangling: Technical Overview

This project focuses on collecting, processing, and organizing structured data related to United States Supreme Court cases, specifically annotated transcripts of oral arguments. The primary data source is the Oyez Project's public API, supplemented with metadata from the Library of Congress and the Supreme Court Database (SCDB).

## Motivation and Problem Statement

Access to structured, annotated data on Supreme Court oral arguments and case metadata is limited. Legal researchers, political scientists, and developers benefit from datasets that combine transcripts, audio timestamps, speaker identifications, and case metadata in a machine-readable format. This project addresses the need for an automated, maintainable pipeline to fetch, update, and organize this data efficiently.

## Architecture and Components

### Data Sources

- **Oyez API**: Provides case metadata, oral argument transcripts, and links to digitized audio.
- **Library of Congress (LOC)**: Offers citation metadata and digitized resources for historical cases.
- **Supreme Court Database (SCDB)**: Supplies structured legal provisions and case-centered data for integration.

### Core Scripts

- **update.py**: Implements rate-limited API calls to Oyez to fetch new or missing cases and their transcripts. It handles cases with multiple oral arguments by fetching each transcript separately and writing JSON files named by term and docket number.

- **publish.py**: Manages GitHub releases for the dataset. It maintains a maximum of three releases by deleting older ones and creates a new release tagged with the current date. This ensures users can access recent snapshots of the data.

- **oyez/json_to_db.py**: Contains utilities to convert raw JSON files into formats suitable for database ingestion or further processing.

- **oyez/merge_scdb.py** and **oyez/merge_scdb_with_master.py**: Merge SCDB data with Oyez and LOC metadata, enriching case records with legal provisions and citation details.

- **oyez/rename_oyez_files.py**: Processes Oyez JSON files to rename and organize them based on citation patterns, facilitating easier lookup and integration.

### Data Organization

Data files are named using the pattern `{term}.{docket}.json` for case overviews, with transcripts for multiple oral arguments appended with `-t01`, `-t02`, etc. This naming convention supports straightforward indexing and retrieval.

The dataset includes audio metadata linking to Amazon S3 storage of digitized oral argument recordings in multiple formats (mp3, ogg, m3u8).

### Automation and Rate Limiting

API calls to Oyez are rate-limited to avoid overloading the public API, using decorators from the `ratelimit` library to enforce call limits. The update process is designed to run regularly (weekly), with automation facilitated by GitHub Actions (external to this repo).

## Implementation Details

- **Rate Limiting**: The `get_http_json` function in `update.py` is decorated to allow no more than 10 calls per 10 seconds, roughly one call per second, ensuring compliance with API usage policies.

- **Data Writing**: Case data and transcripts are serialized as indented JSON files into the `oyez/cases` directory, supporting human readability and version control.

- **Release Management**: The `publish.py` script uses GitHub API calls authenticated via a token to list, delete, and create releases. It assumes the repository environment variable `GITHUB_REPOSITORY` is set.

- **Citation Handling**: Scripts in the `oyez` folder parse and normalize citation strings to generate consistent file identifiers (e.g., `usrep` + volume + page with zero-padding).

- **Data Merging**: Merging scripts combine multiple data sources by reading CSVs and JSON files, attaching metadata fields, and outputting enriched JSON nodes.

## Assumptions and Limitations

- The project assumes access to a valid GitHub token for release management.
- Some scripts reference local file paths which may require adjustment for deployment or collaboration.
- The dataset requires significant disk space (~3.5GB) for full decompression.
- The update process depends on the availability and stability of the Oyez API.

## Summary

This repository provides a practical, automated framework to maintain an up-to-date, richly annotated dataset of US Supreme Court cases and oral argument transcripts. It integrates multiple authoritative sources, enforces API usage constraints, and supports versioned releases for user access. The codebase balances data acquisition, transformation, and organization with automation to support ongoing research and application development in legal and political domains.
