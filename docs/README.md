# AIRPORT Dokumentation

Denne mappe samler projektets skriftlige materiale og fungerer som indgang til rapporten og den øvrige dokumentation.

<p>
  <a href="https://abrahimborgiprivat.github.io/AIRPORT/html/index.html"><strong>Åbn GitHub Pages-sitet</strong></a><br />
  Se den samlede projektpræsentation som et statisk website med separate sider for de vigtigste emner.
</p>

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

<table>
  <tr>
    <td align="center"><strong>Overblik</strong></td>
    <td align="center"><strong>Passagerflow</strong></td>
    <td align="center"><strong>Kapacitet</strong></td>
  </tr>
  <tr>
    <td><img src="../res/pbi/img/PBIPage1.png" alt="Power BI side 1" width="100%" /></td>
    <td><img src="../res/pbi/img/PBIPage2.png" alt="Power BI side 2" width="100%" /></td>
    <td><img src="../res/pbi/img/PBIPage3.png" alt="Power BI side 3" width="100%" /></td>
  </tr>
</table>

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
