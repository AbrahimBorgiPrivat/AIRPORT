# Airport

Standalone Airport simulation, ETL, and reporting project extracted from the shared `DATA PROJECTS` workspace.

The repository includes:

- API ingestion services for airport and flight data
- JSON-to-database ingestion for aircraft model reference data
- SQL-driven table and view creation jobs
- Airport simulation services for passports and flight tickets
- Power BI and Tabular Editor assets
- Shared Python libraries required by the Airport services

## Structure

```text
AIRPORT/
|-- docs/
|-- res/
|-- src/
|   |-- code/
|   |   |-- libraries/
|   |   |-- runtime_definitions/
|   |   `-- service/
|   `-- workspace-serve/
`-- .gitignore
```

## Quick Start

Install the shared Python dependencies:

```powershell
pip install -r src\code\libraries\requirements.txt
```

Run a service from its folder, for example:

```powershell
cd src\code\service\etl\service_api_to_client
docker compose up --build
```

The standalone repo now uses direct local paths:

- `res/json`
- `src/code/runtime_definitions/api_to_client`
- `src/code/runtime_definitions/json_to_client`
- `src/code/runtime_definitions/create_table_and_views`
- `src/code/runtime_definitions/simulations`

## Database

This repo still targets the same Airport database setup as the shared workspace, including the `cph_airport` schema and existing environment variable pattern.

## Power BI And Tabular

- PBIP and semantic model files live in `src/workspace-serve/SemanticModel`
- Tabular automation scripts live in `src/workspace-serve/Tabular`
- The helper C# project lives in `src/workspace-serve/TabularEditorCLITool`

See `docs/README.md` for the compact project map.
