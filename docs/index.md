---
title: AIRPORT
description: End-to-end data- og rapporteringsprojekt med simulerede passagerdata, eksterne flydata og Power BI-rapportering.
permalink: /
---

# AIRPORT

En komplet data- og rapporteringsløsning, der simulerer centrale dele af en lufthavns operationelle datagrundlag og omsætter det til analyser i Power BI.

[Laes den fulde projektrapport (PDF)](./Abrahim_Borgi_AIRPORT_Simulation_Project.pdf)

> Projektet kombinerer syntetiske passager- og billetdata med eksterne fly- og lufthavnsdata for at skabe et realistisk analysegrundlag. Losningen er udviklet som et end-to-end forloeb fra dataindlaesning og simulering til datamodel, KPI'er og visuelle dashboards.

## Projektets formaal

Projektet er udviklet for at demonstrere, hvordan man kan bygge en realistisk data- og BI-losning under praktiske begraensninger:

- uden adgang til interne produktionssystemer
- uden adgang til faktiske passagerdata
- med behov for baade teknisk pipeline, datamodellering og forretningsrettet rapportering

Maalet er derfor ikke kun at vise visualiseringer, men at dokumentere hele kaeden:

- indsamling af data fra flere kilder
- simulering af operationelle haendelser og passageradfaerd
- strukturering af data i en relationel database
- opbygning af semantisk model og KPI'er
- formidling af indsigt i et interaktivt Power BI-produkt

## Hvad projektet loeser

I en lufthavnskontekst er der mange centrale spoergsmaal, som kraever et samlet datagrundlag:

- Hvor mange passagerer og afgange er haandteret i en given periode?
- Hvor stor en andel af flyene afgaar rettidigt?
- Hvordan bevaeger passagererne sig gennem check-in og security?
- Kommer passagererne gennem security i god tid?
- Hvor godt udnyttes flyenes saedekapacitet?
- Hvilke selskaber, destinationer og tidspunkter driver belastningen?

AIRPORT-projektet er bygget til at besvare netop den type spoergsmaal i en samlet rapportloesning.

## Loesningens arkitektur

Losningen er bygget som en modulopdelt pipeline, hvor hver del kan koeres og vedligeholdes separat.

### 1. Datakilder

Projektet samler data fra tre hovedkilder:

- Simulerede data i Python:
  passagerer, pasnumre, nationaliteter, billetkoblinger, check-in-type, check-in-tidspunkt og security-passager
- API-data:
  historiske flyafgange og metadata om lufthavne
- JSON-referencefiler:
  flymodeller med fx producent, kapacitet, rækkevidde og kodevaerdier

Det giver et miks af syntetiske og virkelighedsnaere data, som tilsammen skaber et brugbart analyseunivers.

### 2. ETL og databehandling

Repository'et indeholder fire Docker-baserede ETL-services, som driver de centrale indlaesninger:

- `service_api_to_client`
- `service_json_to_client`
- `service_create_table_views_from_sql`
- `service_simulations`

ETL-laget staar for:

- hentning af eksterne data
- indlaesning af referencefiler
- simulering af passager- og billetdata
- oprettelse af schema, tabeller og views
- upserts til PostgreSQL, saa data kan genkoeres og opdateres kontrolleret

Designet viser en praktisk og genbrugelig tilgang, hvor runtime-definitioner, Python-biblioteker og services er holdt adskilt.

### 3. Datamodel

Datamodellen er designet til at afspejle et forenklet, men realistisk billede af en lufthavns operationer. Centrale tabeller i projektet er:

- `PASSPORTS`
  simulerede passagerer med pasnummer, navn og land
- `FLIGHTS`
  afgange med planlagte og faktiske tider, status, gate, terminal, destination og flytype
- `FLIGHT_TICKETS` / billetdata
  kobling mellem passager og afgang, inklusive saede, check-in-type og tidsstempler
- `AIRCRAFT_MODELS`
  flymetadata som saedekapacitet, producent, motor og IATA/ICAO-koder
- `AIRPORTS`
  referenceoplysninger om destinationer og lufthavne
- `DATEVIEW`
  datodimension til tidsanalyse

Strukturen er lavet, saa rapporteringen kan arbejde pa tværs af passagerflow, punctualitet, kapacitet og geografiske moenstre.

### 4. Semantisk model og rapportering

Power BI-delen er leveret som PBIP-projekt med semantisk model og Tabular Editor-assets. Det betyder, at loesningen ikke kun viser visualiseringer, men ogsaa den model- og maale-lag, der ligger bag:

- semantisk model i `src/workspace-serve/SemanticModel`
- Tabular scripts og DAX-maalinger i `src/workspace-serve/Tabular`
- helper-bibliotek til Tabular Editor i `src/workspace-serve/TabularEditorCLITool`

Det giver et godt billede af, hvordan teknisk modellering og rapportdesign spiller sammen i et moderne BI-setup.

## Datagrundlag og simulation

En vigtig del af projektet er, at billet- og passagerdata er syntetiske. Det er et bevidst designvalg.

I stedet for at bruge foelsomme eller utilgaengelige driftsdata simulerer projektet et plausibelt forloeb:

- passagerer faar realistiske pasnumre, navne og nationaliteter
- fly kobles til saedekapacitet via flymodeller
- belægningsgrader varierer efter ugedag og tidspunkt
- check-in foregaar som `online` eller `onsite`
- security-passager placeres i forhold til afgangstid

Det giver et kontrolleret miljoe, hvor man stadig kan analysere operationelle mønstre og vise relevante KPI'er.

## Rapporten i Power BI

Rapporten er bygget som tre fokuserede sider, der tilsammen fortaeller historien om drift, passagerflow og kapacitet.

### Side 1: Overblik

Foerste side giver et ledelsesoverblik over den valgte periode:

- antal passagerer og fly
- punctualitet og rettidighed
- fordeling paa status
- top-flyselskaber og destinationer
- udvikling over tid
- geografisk visning af destinationer

![Power BI overblik](./assets/pbi-page-1.png)

Denne side fungerer som projektets indgang og samler de vigtigste operationelle noegletal i et hurtigt laesbart dashboard.

### Side 2: Passagerflow og tidsmoenstre

Anden side gaar i dybden med passagerernes rejse gennem terminalen:

- hvor tidligt der checkes ind
- hvor tidligt passagerer gaar gennem security
- forskelle mellem `online` og `onsite` check-in
- andel af passagerer, der kommer gennem security i god tid
- moenstre over dagen og paa tværs af datoer

![Power BI passagerflow](./assets/pbi-page-2.png)

Siden er saerligt relevant til at vurdere belastning, timing og potentielle flaskehalse i passagerflowet.

### Side 3: Kapacitet og udnyttelse

Tredje side fokuserer paa, hvor godt saedekapaciteten udnyttes:

- samlet og gennemsnitlig belægningsgrad
- variation efter flystoerrelse
- forskelle mellem selskaber og omraader
- udvikling over tid
- visualisering af et gennemsnitligt fly paa saedeniveau

![Power BI kapacitet](./assets/pbi-page-3.png)

Denne del viser, hvordan efterspoergsel og kapacitet kan analyseres i samme loesning og gøres let forstaelig for forretningen.

## Teknologier og projektindhold

Projektet samler flere discipliner i samme repository:

- Python til simulation, integration og datalogik
- Docker til koerbare services
- PostgreSQL til lagring og relationsmodel
- SQL til schema-, tabel- og view-opbygning
- Power BI til rapportering
- Tabular Editor 2 til maale- og modelautomatisering
- PBIP/TMDL-assets til versionsstyret BI-udvikling

Det er en styrke ved projektet, at hele loesningen ligger samlet og versionsstyret, saa baade kode, model og rapport kan gennemgaas i samme repository.

## Repository-struktur

De vigtigste mapper er:

- `docs/`
  rapport, projektside og GitHub Pages-indhold
- `res/`
  referencefiler, billeder og Power BI-assets
- `src/code/libraries/`
  genbrugelige Python-komponenter
- `src/code/runtime_definitions/`
  runtimefiler til ingestion, tabeller, views og simulationer
- `src/code/service/etl/`
  de Docker-baserede services
- `src/workspace-serve/SemanticModel/`
  PBIP-projekt og semantisk model
- `src/workspace-serve/Tabular/`
  Tabular scripts og DAX-maalinger

## Hvorfor projektet er interessant

AIRPORT-projektet er interessant, fordi det viser mere end en klassisk dashboard-øvelse. Det viser hele vejen fra datakilder til beslutningsstøtte:

- et realistisk forretningsproblem
- et syntetisk, men meningsfuldt datagrundlag
- en teknisk pipeline, der kan koeres igen
- en model, der understoetter analyser paa tværs af flere emner
- en rapport, der er baade visuel og analytisk

Med andre ord demonstrerer projektet evnen til at arbejde end-to-end med data engineering, datamodellering og BI-formidling i samme levering.

## Afslutning

Dette repository dokumenterer en samlet Airport-case, hvor operationelle data, syntetiske simulationer og moderne BI-vaerktoejer bliver bundet sammen i en praktisk loesning.

Resultatet er en rapportplatform, der giver indsigt i:

- trafik og punctualitet
- passagerflow og timing
- kapacitet og belægningsgrad

Projektet er derfor baade en teknisk demonstration og et konkret eksempel paa, hvordan datadrevne beslutningsgrundlag kan bygges, selv naar rigtige driftsdata ikke er direkte tilgaengelige.
