# AIRPORT Dokumentation

Denne mappe samler projektets skriftlige materiale og fungerer som indgang til rapporten og den øvrige dokumentation.

## Indhold

- `Abrahim_Borgi_AIRPORT_Simulation_Project.pdf`
  den samlede projektrapport
- `README.md`
  denne oversigt over dokumentationsmaterialet

## Formål

AIRPORT er bygget som en samlet case, der viser:

- hvordan syntetiske og eksterne data kan kombineres
- hvordan en ETL-pipeline kan struktureres og genkøres
- hvordan en relationel datamodel kan understøtte analyser
- hvordan resultaterne kan formidles i Power BI

Projektet spænder derfor over både data engineering, modellering og rapportering.

## Rapportens fokus

Rapporten og den tilhørende løsning er bygget omkring tre hovedområder:

### 1. Overblik

Et samlet overblik over passagerer, fly, punctualitet, destinationer og aktivitetsniveau.

![Power BI side 1](../res/pbi/img/PBIPage1.png)

### 2. Passagerflow

Analyse af check-in, security og timing frem mod afgang.

![Power BI side 2](../res/pbi/img/PBIPage2.png)

### 3. Kapacitet

Analyse af sædeudnyttelse, belægningsgrad og forskelle på tværs af flytyper og selskaber.

![Power BI side 3](../res/pbi/img/PBIPage3.png)

## Relaterede dele af repository'et

- `site/`
  GitHub Pages-sitet med HTML-sider og genanvendelige CSS-filer
- `src/code/runtime_definitions/`
  definitioner for ingestion, simulation og SQL-jobs
- `src/code/service/etl/`
  de kørbare ETL-services
- `src/workspace-serve/SemanticModel/`
  PBIP-projekt og semantisk model
- `src/workspace-serve/Tabular/`
  Tabular Editor-scripts og DAX-assets

## Links

- [Tilbage til projektets README](../README.md)
- [Åbn PDF-rapporten](./Abrahim_Borgi_AIRPORT_Simulation_Project.pdf)
