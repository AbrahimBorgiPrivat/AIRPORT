# Airport Documentation

This folder contains the standalone Airport project notes and exported project material.

The GitHub Pages site is now maintained separately in `site/` and deployed with GitHub Actions.

## Project Layout

```text
AIRPORT/
|-- docs/
|-- res/
|   |-- json/
|   `-- pbi/
`-- src/
    |-- code/
    |   |-- libraries/
    |   |-- runtime_definitions/
    |   `-- service/
    `-- workspace-serve/
```

## Main Areas

- `res/json` contains JSON source data used by the Airport ETL flows
- `res/pbi` contains Power BI images, themes, and static assets
- `src/code/runtime_definitions/api_to_client` defines the API ingestion jobs
- `src/code/runtime_definitions/json_to_client` defines JSON ingestion jobs
- `src/code/runtime_definitions/create_table_and_views` defines schema/table/view SQL jobs
- `src/code/runtime_definitions/simulations` defines the Airport simulation jobs
- `src/code/service/etl` contains the Docker-based ETL services
- `src/workspace-serve/SemanticModel` contains the PBIP/TMDL model
- `src/workspace-serve/Tabular` contains Tabular Editor scripts

## Database Note

This standalone repo still targets the same database setup as the shared workspace.
Schema and database references like `cph_airport` are intentionally unchanged.
