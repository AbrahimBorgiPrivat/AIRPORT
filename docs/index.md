---
title: AIRPORT
description: End-to-end data- og rapporteringsprojekt med simulerede passagerdata, eksterne flydata og Power BI-rapportering.
permalink: /
---

<style>
  .airport-page {
    --navy: #15284b;
    --navy-soft: #223a68;
    --ink: #1b2430;
    --muted: #5f6b7a;
    --line: #d8dee8;
    --panel: #f4f6fa;
    --white: #ffffff;
    --accent: #f1cf2f;
    --accent-soft: #fff5bf;
    --shadow: 0 18px 40px rgba(21, 40, 75, 0.12);
    color: var(--ink);
    font-family: "Trebuchet MS", "Segoe UI", sans-serif;
    line-height: 1.65;
    margin: 0 auto;
    max-width: 1180px;
    padding: 20px 0 56px;
  }

  .airport-page * {
    box-sizing: border-box;
  }

  .airport-page .hero {
    background:
      radial-gradient(circle at top right, rgba(241, 207, 47, 0.26), transparent 26%),
      linear-gradient(135deg, #f9fbfe 0%, #eef2f8 100%);
    border: 1px solid var(--line);
    border-radius: 28px;
    box-shadow: var(--shadow);
    overflow: hidden;
    padding: 34px;
  }

  .airport-page .hero-grid {
    align-items: center;
    display: grid;
    gap: 28px;
    grid-template-columns: 1.05fr 0.95fr;
  }

  .airport-page .eyebrow {
    color: var(--navy-soft);
    font-size: 0.82rem;
    font-weight: 700;
    letter-spacing: 0.18em;
    margin-bottom: 14px;
    text-transform: uppercase;
  }

  .airport-page h1,
  .airport-page h2,
  .airport-page h3 {
    color: var(--navy);
    font-family: Georgia, "Times New Roman", serif;
    letter-spacing: -0.02em;
    margin: 0;
  }

  .airport-page h1 {
    font-size: clamp(2.3rem, 5vw, 4.1rem);
    line-height: 1.02;
    margin-bottom: 18px;
  }

  .airport-page h2 {
    font-size: clamp(1.55rem, 3vw, 2.25rem);
    margin-bottom: 10px;
  }

  .airport-page h3 {
    font-size: 1.2rem;
    margin-bottom: 8px;
  }

  .airport-page p {
    margin: 0 0 14px;
  }

  .airport-page .lead {
    color: var(--muted);
    font-size: 1.05rem;
    margin-bottom: 22px;
    max-width: 62ch;
  }

  .airport-page .hero-actions {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    margin-bottom: 20px;
  }

  .airport-page .button {
    border-radius: 999px;
    display: inline-block;
    font-size: 0.95rem;
    font-weight: 700;
    padding: 12px 18px;
    text-decoration: none;
    transition: transform 0.18s ease, box-shadow 0.18s ease;
  }

  .airport-page .button:hover {
    box-shadow: 0 12px 24px rgba(21, 40, 75, 0.14);
    transform: translateY(-1px);
  }

  .airport-page .button.primary {
    background: var(--navy);
    color: var(--white);
  }

  .airport-page .button.secondary {
    background: var(--white);
    border: 1px solid var(--line);
    color: var(--navy);
  }

  .airport-page .hero-note {
    background: rgba(255, 255, 255, 0.82);
    border: 1px solid rgba(21, 40, 75, 0.08);
    border-radius: 18px;
    color: var(--muted);
    padding: 14px 16px;
  }

  .airport-page .hero-visual {
    align-self: stretch;
    display: grid;
    gap: 14px;
  }

  .airport-page .visual-card {
    background: var(--white);
    border: 1px solid rgba(21, 40, 75, 0.08);
    border-radius: 24px;
    box-shadow: 0 16px 34px rgba(21, 40, 75, 0.1);
    overflow: hidden;
    padding: 16px;
  }

  .airport-page .visual-card img {
    border-radius: 16px;
    display: block;
    width: 100%;
  }

  .airport-page .visual-meta {
    align-items: center;
    display: flex;
    gap: 12px;
    margin-bottom: 14px;
  }

  .airport-page .visual-meta img {
    border-radius: 14px;
    box-shadow: 0 8px 18px rgba(21, 40, 75, 0.18);
    height: 54px;
    width: 54px;
  }

  .airport-page .visual-meta span {
    color: var(--muted);
    display: block;
    font-size: 0.92rem;
  }

  .airport-page .stats {
    display: grid;
    gap: 14px;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    margin: 22px 0 0;
  }

  .airport-page .stat {
    background: var(--white);
    border: 1px solid var(--line);
    border-radius: 20px;
    padding: 18px 18px 16px;
  }

  .airport-page .stat strong {
    color: var(--navy);
    display: block;
    font-family: Georgia, "Times New Roman", serif;
    font-size: 2rem;
    line-height: 1;
    margin-bottom: 8px;
  }

  .airport-page .stat span {
    color: var(--muted);
    display: block;
    font-size: 0.94rem;
  }

  .airport-page .quick-nav {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin: 24px 0 10px;
  }

  .airport-page .chip {
    background: var(--white);
    border: 1px solid var(--line);
    border-radius: 999px;
    color: var(--navy);
    font-size: 0.92rem;
    font-weight: 700;
    padding: 10px 14px;
    text-decoration: none;
  }

  .airport-page .section {
    margin-top: 26px;
  }

  .airport-page .panel {
    background: var(--white);
    border: 1px solid var(--line);
    border-radius: 26px;
    padding: 28px;
  }

  .airport-page .panel.alt {
    background: linear-gradient(180deg, #f7f9fc 0%, #eef3fa 100%);
  }

  .airport-page .grid {
    display: grid;
    gap: 18px;
  }

  .airport-page .grid.two {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

  .airport-page .grid.three {
    grid-template-columns: repeat(3, minmax(0, 1fr));
  }

  .airport-page .card {
    background: var(--panel);
    border: 1px solid rgba(21, 40, 75, 0.08);
    border-radius: 22px;
    padding: 20px;
  }

  .airport-page .card.emphasis {
    background: linear-gradient(145deg, var(--navy) 0%, #1f3a6b 100%);
    color: var(--white);
  }

  .airport-page .card.emphasis h3,
  .airport-page .card.emphasis p,
  .airport-page .card.emphasis li {
    color: var(--white);
  }

  .airport-page .kicker {
    color: var(--navy-soft);
    font-size: 0.8rem;
    font-weight: 700;
    letter-spacing: 0.14em;
    margin-bottom: 10px;
    text-transform: uppercase;
  }

  .airport-page ul {
    margin: 0;
    padding-left: 18px;
  }

  .airport-page li {
    margin: 0 0 8px;
  }

  .airport-page .step {
    display: grid;
    gap: 14px;
    grid-template-columns: 56px 1fr;
  }

  .airport-page .step-no {
    align-items: center;
    background: var(--accent-soft);
    border-radius: 18px;
    color: var(--navy);
    display: flex;
    font-family: Georgia, "Times New Roman", serif;
    font-size: 1.5rem;
    font-weight: 700;
    height: 56px;
    justify-content: center;
    width: 56px;
  }

  .airport-page .report-card {
    background: var(--white);
    border: 1px solid rgba(21, 40, 75, 0.1);
    border-radius: 24px;
    overflow: hidden;
  }

  .airport-page .report-card img {
    display: block;
    width: 100%;
  }

  .airport-page .report-copy {
    padding: 18px 20px 20px;
  }

  .airport-page .tag-row {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-top: 14px;
  }

  .airport-page .tag {
    background: var(--accent-soft);
    border-radius: 999px;
    color: var(--navy);
    font-size: 0.88rem;
    font-weight: 700;
    padding: 8px 12px;
  }

  .airport-page pre {
    background: #111c33;
    border-radius: 20px;
    color: #edf2ff;
    font-size: 0.92rem;
    margin: 0;
    overflow-x: auto;
    padding: 20px;
  }

  .airport-page code {
    font-family: Consolas, "Courier New", monospace;
  }

  .airport-page .footer-cta {
    align-items: center;
    background: linear-gradient(135deg, #182d52 0%, #27487f 100%);
    border-radius: 28px;
    color: var(--white);
    display: grid;
    gap: 18px;
    grid-template-columns: 1.2fr 0.8fr;
    margin-top: 28px;
    padding: 28px;
  }

  .airport-page .footer-cta h2,
  .airport-page .footer-cta p {
    color: var(--white);
  }

  .airport-page .footer-cta .button.primary {
    background: var(--accent);
    color: var(--navy);
  }

  .airport-page .footer-cta .button.secondary {
    background: rgba(255, 255, 255, 0.1);
    border-color: rgba(255, 255, 255, 0.2);
    color: var(--white);
  }

  @media (max-width: 960px) {
    .airport-page .hero-grid,
    .airport-page .footer-cta,
    .airport-page .grid.two,
    .airport-page .grid.three,
    .airport-page .stats {
      grid-template-columns: 1fr;
    }

    .airport-page .hero,
    .airport-page .panel,
    .airport-page .footer-cta {
      padding: 22px;
    }
  }
</style>

<div class="airport-page">
  <section class="hero">
    <div class="hero-grid">
      <div>
        <div class="eyebrow">Airport Case / Data Engineering / Power BI</div>
        <h1>AIRPORT</h1>
        <p class="lead">
          En end-to-end data- og rapporteringsloesning, der kombinerer simulerede passagerdata,
          eksterne flydata og en Power BI-rapport i et samlet, versionsstyret projekt.
        </p>
        <div class="hero-actions">
          <a class="button primary" href="./Abrahim_Borgi_AIRPORT_Simulation_Project.pdf">Laes rapporten</a>
          <a class="button secondary" href="https://github.com/AbrahimBorgiPrivat/AIRPORT">Se repository</a>
        </div>
        <div class="hero-note">
          Projektet er udviklet som en realistisk airport-case uden adgang til interne systemer
          eller rigtige passagerdata. Fokus er derfor baade teknisk pipeline, datamodel og
          beslutningsstoettende rapportering.
        </div>
      </div>

      <div class="hero-visual">
        <div class="visual-card">
          <div class="visual-meta">
            <img src="./assets/cph-logo.png" alt="Airport logo" />
            <div>
              <strong style="display:block; color:#15284b;">Power BI Demo</strong>
              <span>Overblik over drift, flow og kapacitet</span>
            </div>
          </div>
          <img src="./assets/pbi-page-1.png" alt="Power BI overblik" />
        </div>
      </div>
    </div>

    <div class="stats">
      <div class="stat">
        <strong>4</strong>
        <span>Docker-baserede ETL-services</span>
      </div>
      <div class="stat">
        <strong>3</strong>
        <span>Rapportsider i Power BI</span>
      </div>
      <div class="stat">
        <strong>1</strong>
        <span>Semantisk model med Tabular-assets</span>
      </div>
      <div class="stat">
        <strong>E2E</strong>
        <span>Fra datakilde til visualisering</span>
      </div>
    </div>
  </section>

  <nav class="quick-nav" aria-label="Sektioner">
    <a class="chip" href="#overblik">Overblik</a>
    <a class="chip" href="#forretningsmaal">Forretningsmaal</a>
    <a class="chip" href="#arkitektur">Arkitektur</a>
    <a class="chip" href="#datagrundlag">Datagrundlag</a>
    <a class="chip" href="#rapport">Power BI</a>
    <a class="chip" href="#stack">Teknologier</a>
    <a class="chip" href="#struktur">Repository</a>
  </nav>

  <section class="section panel alt" id="overblik">
    <div class="kicker">Executive Summary</div>
    <h2>Et BI-projekt bygget som en rigtig leverance</h2>
    <div class="grid two" style="margin-top:18px;">
      <div class="card emphasis">
        <h3>Projektets pointe</h3>
        <p>
          AIRPORT viser, hvordan man kan bygge en trovaerdig analyse- og rapporteringsloesning
          under praktiske begraensninger: uden adgang til interne driftskilder, men stadig med et
          klart forretningsmaal og et professionelt output.
        </p>
      </div>
      <div class="card">
        <h3>Det du ser i projektet</h3>
        <ul>
          <li>Simulation af passagerer, billetter og timing omkring check-in og security</li>
          <li>Indlaesning af flyafgange, lufthavnsmetadata og flymodeller</li>
          <li>PostgreSQL-tabeller, views og upsert-logik til genkoerbar dataload</li>
          <li>PBIP-projekt med semantisk model, DAX og interaktive dashboards</li>
        </ul>
      </div>
    </div>
  </section>

  <section class="section panel" id="forretningsmaal">
    <div class="kicker">Formaal</div>
    <h2>Hvilke spoergsmaal projektet skal kunne besvare</h2>
    <div class="grid two" style="margin-top:18px;">
      <div class="card">
        <h3>Operationelt overblik</h3>
        <ul>
          <li>Hvor mange passagerer og afgange er haandteret i perioden?</li>
          <li>Hvor stor en andel af flyene afgaar rettidigt?</li>
          <li>Hvilke selskaber, destinationer og tidspunkter driver belastningen?</li>
        </ul>
      </div>
      <div class="card">
        <h3>Flow og kapacitet</h3>
        <ul>
          <li>Hvornar checker passagerer ind og passerer security?</li>
          <li>Hvor mange kommer igennem i god tid?</li>
          <li>Hvor godt udnyttes flyenes saedekapacitet?</li>
        </ul>
      </div>
    </div>
  </section>

  <section class="section panel alt" id="arkitektur">
    <div class="kicker">Arkitektur</div>
    <h2>Loesningen er bygget i tydelige lag</h2>
    <div class="grid two" style="margin-top:18px;">
      <div class="card">
        <div class="step">
          <div class="step-no">1</div>
          <div>
            <h3>Datakilder</h3>
            <p>
              Projektet kombinerer syntetiske data, API-data og JSON-referencefiler for at skabe
              et analyseunivers, der ligner virkelige airport-scenarier.
            </p>
          </div>
        </div>
      </div>
      <div class="card">
        <div class="step">
          <div class="step-no">2</div>
          <div>
            <h3>ETL-services</h3>
            <p>
              Fire Docker-services haandterer ingestion, simulation, tabeloprettelse og view-logik,
              saa loesningen kan koeres og opdateres kontrolleret.
            </p>
          </div>
        </div>
      </div>
      <div class="card">
        <div class="step">
          <div class="step-no">3</div>
          <div>
            <h3>Datamodel</h3>
            <p>
              PostgreSQL anvendes til relationel lagring af flights, passports, ticket-data,
              aircraft_models, airports og datodimensioner.
            </p>
          </div>
        </div>
      </div>
      <div class="card">
        <div class="step">
          <div class="step-no">4</div>
          <div>
            <h3>Semantisk model og rapport</h3>
            <p>
              Power BI, PBIP og Tabular Editor binder det hele sammen i en rapport, der er nem at
              laese og stadig teknisk veldokumenteret.
            </p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section panel" id="datagrundlag">
    <div class="kicker">Datagrundlag</div>
    <h2>Syntetiske data, eksterne kilder og praktisk modellering</h2>
    <div class="grid three" style="margin-top:18px;">
      <div class="card">
        <h3>Simulationer</h3>
        <p>
          Passagerer, pasnumre, nationaliteter, check-in-type, check-in-tider og security-passager
          bliver genereret i Python for at skabe et plausibelt operationelt flow.
        </p>
      </div>
      <div class="card">
        <h3>Eksterne data</h3>
        <p>
          Historiske flyafgange og lufthavnsmetadata giver projektet et realistisk anker, saa
          dashboards ikke kun bygger paa antagelser.
        </p>
      </div>
      <div class="card">
        <h3>Referencefiler</h3>
        <p>
          Flymodeller og kapacitetsdata fra JSON goer det muligt at analysere belaegning,
          flystoerrelser og udnyttelsesrater paa tværs af afgange.
        </p>
      </div>
    </div>

    <div class="grid two" style="margin-top:18px;">
      <div class="card">
        <h3>Centrale tabeller</h3>
        <ul>
          <li><code>PASSPORTS</code> med passageridentitet og land</li>
          <li><code>FLIGHTS</code> med status, destination, gate og tider</li>
          <li><code>FLIGHT_TICKETS</code> med saede, check-in-type og tidsstempler</li>
          <li><code>AIRCRAFT_MODELS</code> med saeder, producent og kodevaerdier</li>
          <li><code>AIRPORTS</code> og <code>DATEVIEW</code> som reference- og analysedata</li>
        </ul>
      </div>
      <div class="card emphasis">
        <h3>Hvorfor simulation giver mening her</h3>
        <p>
          Billet- og passagerdata er med vilje syntetiske. Det giver et sikkert og kontrolleret
          setup, hvor man stadig kan demonstrere realistiske moenstre, kapacitetsudfordringer og
          analytiske KPI'er uden at arbejde med foelsomme driftsdata.
        </p>
      </div>
    </div>
  </section>

  <section class="section panel alt" id="rapport">
    <div class="kicker">Power BI Report</div>
    <h2>Tre dashboards med hver sit fokus</h2>
    <div class="grid three" style="margin-top:18px;">
      <article class="report-card">
        <img src="./assets/pbi-page-1.png" alt="Dashboard side 1" />
        <div class="report-copy">
          <h3>Side 1: Overblik</h3>
          <p>
            Samler de vigtigste KPI'er om trafik, punctualitet, selskaber, destinationer og
            belastning over tid. Det er rapportens ledelsesview.
          </p>
        </div>
      </article>

      <article class="report-card">
        <img src="./assets/pbi-page-2.png" alt="Dashboard side 2" />
        <div class="report-copy">
          <h3>Side 2: Passagerflow</h3>
          <p>
            Gaar i dybden med check-in, security og timing frem mod afgang. Her bliver terminalflow
            og potentielle flaskehalse synlige.
          </p>
        </div>
      </article>

      <article class="report-card">
        <img src="./assets/pbi-page-3.png" alt="Dashboard side 3" />
        <div class="report-copy">
          <h3>Side 3: Kapacitet</h3>
          <p>
            Viser hvordan saedekapacitet bliver brugt pa tværs af flystoerrelser, selskaber,
            omraader og datoer, inklusiv et visuelt seat-layout.
          </p>
        </div>
      </article>
    </div>

    <div class="tag-row">
      <span class="tag">Punctualitet</span>
      <span class="tag">Passenger Flow</span>
      <span class="tag">Security Timing</span>
      <span class="tag">Seat Utilization</span>
      <span class="tag">Interactive Slicers</span>
      <span class="tag">PBIP + TMDL</span>
    </div>
  </section>

  <section class="section panel" id="stack">
    <div class="kicker">Teknologier</div>
    <h2>Stack og leveranceindhold</h2>
    <div class="grid two" style="margin-top:18px;">
      <div class="card">
        <h3>Kerneteknologier</h3>
        <ul>
          <li>Python til ingestion, simulation og datalogik</li>
          <li>Docker til koerbare ETL-services</li>
          <li>PostgreSQL til relationsmodel og persistens</li>
          <li>SQL til schema-, tabel- og view-opbygning</li>
          <li>Power BI til rapportering og interaktion</li>
          <li>Tabular Editor 2 til model- og DAX-automatisering</li>
        </ul>
      </div>
      <div class="card">
        <h3>Hvorfor repository'et er staerkt</h3>
        <p>
          Hele loesningen er versionsstyret i samme projekt: kode, runtime-definitioner, SQL,
          semantisk model, DAX og rapport-assets. Det goer det nemt at forstaa baade teknikken og
          den forretningsmaessige leverance i samme gennemgang.
        </p>
      </div>
    </div>
  </section>

  <section class="section panel alt" id="struktur">
    <div class="kicker">Repository</div>
    <h2>Projektstruktur</h2>
    <pre><code>AIRPORT/
|-- docs/
|   |-- assets/
|   |-- index.md
|   `-- Abrahim_Borgi_AIRPORT_Simulation_Project.pdf
|-- res/
|-- src/
|   |-- code/
|   |   |-- libraries/
|   |   |-- runtime_definitions/
|   |   `-- service/
|   `-- workspace-serve/
`-- README.md</code></pre>
  </section>

  <section class="footer-cta">
    <div>
      <div class="kicker" style="color:#dbe5ff;">Afslutning</div>
      <h2>Fra datakilde til beslutningsstoette</h2>
      <p>
        AIRPORT er mere end et dashboard. Det er en samlet case, der viser data engineering,
        modellering og BI-formidling som en sammenhaengende leverance.
      </p>
    </div>
    <div class="hero-actions" style="justify-content:flex-start; margin:0;">
      <a class="button primary" href="./Abrahim_Borgi_AIRPORT_Simulation_Project.pdf">Aabn rapporten</a>
      <a class="button secondary" href="https://github.com/AbrahimBorgiPrivat/AIRPORT">Aabn GitHub</a>
    </div>
  </section>
</div>
