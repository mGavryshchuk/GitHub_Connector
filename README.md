# GitHub Connector

Problem Statement: Provide access to GitHub Issues to Cursor when private mode is turned on.

Solution: An API bridge, packaged as a Docker container, that exposes a minimal OpenAPI surface for listing, creating, updating, closing issues, and adding comments. The bridge securely proxies requests to the GitHub API.

## Goals
- Enable read/write access to GitHub Issues from Cursor while preserving privacy controls
- Offer a clean OpenAPI contract for CRUD on issues and comments
- Ship a single Docker image that is easy to run locally or deploy

## High-Level Architecture
See `docs/ARCHITECTURE.md` for details.

## Roadmap
See `docs/ROADMAP.md` for the task breakdown managed via GitHub Issues and Project.

## Quickstart (placeholder)
- TBD: Image name, environment variables, and example `docker run` command.

## License
TBD (e.g., MIT)
