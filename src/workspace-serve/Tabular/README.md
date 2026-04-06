# Airport Tabular Automation

This folder contains the Tabular Editor scripts for the standalone Airport reporting project.

## Structure

```text
src/workspace-serve/
|-- SemanticModel/
|   |-- Airport Passenger Flight Insights (Power BI Demo).pbip
|   |-- Airport Passenger Flight Insights (Power BI Demo).Report/
|   `-- Airport Passenger Flight Insights (Power BI Demo).SemanticModel/
|-- Tabular/
|   |-- Measures/
|   |   |-- KPI/
|   |   `-- VISUALS/
|   |-- Tables/
|   `-- run_tabular_scripts.ps1
`-- TabularEditorCLITool/
```

## Requirements

- `.NET 8 SDK`
- `Tabular Editor 2`
- Built helper DLL in `src/workspace-serve/TabularEditorCLITool/bin/Release/netstandard2.0/TabularEditorCLITool.dll`

## Build

```powershell
cd "src\workspace-serve\TabularEditorCLITool"
dotnet build -c Release
```

## Run

```powershell
& "C:\Program Files (x86)\Tabular Editor\TabularEditor.exe" `
  ".\src\workspace-serve\SemanticModel\Airport Passenger Flight Insights (Power BI Demo).SemanticModel\definition\model.tmdl" `
  -S ".\src\workspace-serve\Tabular\Measures\KPI\KPI_MEASURES.csx" -D
```

Or run the bundled script sequence:

```powershell
.\src\workspace-serve\Tabular\run_tabular_scripts.ps1
```

## Notes

- KPI measures read DAX from `src/workspace-serve/Tabular/Measures/KPI/MEASURES`
- Visual measures read DAX from `src/workspace-serve/Tabular/Measures/VISUALS/MEASURES`
- Calculated table scripts live under `src/workspace-serve/Tabular/Tables`
