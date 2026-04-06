# AIRPORT

Et end-to-end data- og rapporteringsprojekt, der simulerer centrale dele af en lufthavns operationelle datagrundlag og omsætter det til analyser i Power BI.

## Formål

Projektet er udviklet for at demonstrere, hvordan man kan bygge en realistisk BI-løsning, selv når der ikke er adgang til interne systemer eller rigtige passagerdata.

Løsningen samler derfor:

- syntetiske passager- og billetdata
- eksterne fly- og lufthavnsdata
- referencefiler for flymodeller
- en relationel datamodel i PostgreSQL
- en Power BI-rapport med KPI'er og interaktive dashboards

Målet er ikke kun at vise dashboards, men hele kæden fra datakilde til beslutningsstøtte.

## Hvad projektet indeholder

- Python-baserede simulationer af passagerer, billetter, check-in og security-flow
- ETL-services til API-ingestion, JSON-indlæsning og SQL-baseret tabel/view-opbygning
- runtime-definitioner til genkørbare dataloads
- PBIP-projekt, semantisk model og Tabular Editor-assets
- et statisk GitHub Pages-site bygget med HTML/CSS og deployet via GitHub Actions

## Power BI-rapport

Rapporten er opdelt i tre hovedsider:

1. `Overblik`
2. `Passagerflow`
3. `Kapacitet`

### Overblik

Første side samler de vigtigste KPI'er om passagerer, fly, punctualitet, destinationer og belastning over tid.

![Power BI side 1](res/pbi/img/PBIPage1.png)

### Passagerflow

Anden side fokuserer på check-in, security og passagerernes timing frem mod afgang.

![Power BI side 2](res/pbi/img/PBIPage2.png)

### Kapacitet

Tredje side viser, hvordan sædekapacitet og belægningsgrad udvikler sig på tværs af fly, selskaber og områder.

![Power BI side 3](res/pbi/img/PBIPage3.png)

## Projektstruktur

```text
AIRPORT/
|-- docs/
|-- res/
|   |-- json/
|   `-- pbi/
|-- site/
|   |-- assets/
|   |-- css/
|   `-- html/
|-- src/
|   |-- code/
|   |   |-- libraries/
|   |   |-- runtime_definitions/
|   |   `-- service/
|   `-- workspace-serve/
`-- README.md
```

## Centrale mapper

- `docs/` indeholder rapport og supplerende dokumentation
- `res/` indeholder referencefiler, billeder og Power BI-assets
- `site/` indeholder GitHub Pages-sitet
- `src/code/` indeholder ETL-logik, runtime-definitioner og services
- `src/workspace-serve/` indeholder Power BI-, semantic model- og Tabular-assets

## GitHub Pages

Projektets statiske site ligger i `site/`:

- `site/index.html` er Pages-entrypoint
- `site/html/` indeholder de enkelte sider
- `site/css/` indeholder genanvendelige stylesheets
- `.github/workflows/pages.yml` deployer sitet til GitHub Pages

## Rapport og dokumentation

- [Projektets PDF-rapport](docs/Abrahim_Borgi_AIRPORT_Simulation_Project.pdf)
- [Dokumentationsoversigt](docs/README.md)

## Teknologi

- Python
- Docker
- PostgreSQL
- SQL
- Power BI
- Tabular Editor 2
- GitHub Actions
- Static HTML/CSS
