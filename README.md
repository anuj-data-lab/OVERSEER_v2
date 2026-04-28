# OVERSEER_V2: Statistical Anomaly Detection Engine
**Market Intelligence & Data Integrity**

## Operational Overview
OVERSEER_V2 is a Python-based diagnostic pipeline designed to audit large-scale datasets for mathematical anomalies, logic failures, and statistical deviations. 

In enterprise data environments, raw extraction is insufficient. Data must be mathematically verified before it is injected into production models or business intelligence dashboards. This engine applies rigorous Z-score statistical analysis to automatically isolate corrupt or anomalous data points.

## Core Architecture
* **Language:** Python 3.x
* **Libraries:** `pandas`, `numpy`
* **Statistical Methodology:** Z-Score Deviation (Standard Deviation Thresholds)
* **Threat Detection Matrix:**
    * `STATISTICAL_PRICE_DEVIATION`: Identifies flash crashes or uncharacteristic market inflation.
    * `LOGIC_FAILURE`: Isolates physical impossibilities within the data structure (e.g., negative inventory levels).

## Deployment & Demonstration
This repository contains a demonstration environment consisting of two components:
1.  **Environment Generator:** A script that synthesizes 90 days of normal market distribution and injects controlled mathematical anomalies (The "Poison").
2.  **Diagnostic Engine:** The OVERSEER pipeline that ingests the dataset, calculates standard deviations dynamically, and outputs an isolated `THREAT_REPORT.csv`.

