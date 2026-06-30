# TCR Dynamic

## Overview

This study establishes a multidimensional quantitative evaluation framework to systematically deconstruct the methodological confounders inherent to temporal T cell receptor (TCR) repertoire analysis. We reveal that widely reported clonal turnover and dynamic abundance shifts observed in sequencing data are fundamentally technical artifacts driven by stochastic sampling of low-expansion clones, phenotypic biases, and localized intra-tumor spatial heterogeneity.

## Structure & Figure Reproduction

The code is organized by corresponding main figures in the manuscript. Each directory contains standalone scripts to reproduce the data processing and visualization steps.

* **`Fig2/`**: Scripts for phenotypic clustering, compositional shifts of T cell subsets post-intervention, and temporal dynamics of TCR diversity and clonality.

* **`Fig3/`**: Pipelines comparing time-specific and time-across TCRs across untreated samples, multi-timepoint cohorts, and cross-platform (bulk vs. scTCR-seq) modalities.

* **`Fig4/`**: Code for evaluating sample-specific artifacts in biological replicates and validating mathematical distributions using *in silico* simulated repertoires.

* **`Fig5/`**: Benchmarking scripts for the six evaluated statistical models (NB, BB, P, NP, Binomial, Fisher) utilizing clinical single-cell datasets, PBMC, and tumor replicate cohorts.

* **`Fig6/`**: Scripts mapping dynamic TCR shifts to distinct T cell subsets to quantify phenotypic biases, and algorithms processing Slide-TCR data to evaluate localized intra-tumor spatial heterogeneity.

## Software Requirements

The analytical pipelines are implemented in both R and Python. 
**R Dependencies:**
* `Seurat` (Single-cell RNA/TCR integration and visualization)
* `ggplot2` (Data visualization)
* `vagen` (TCR diversity and Chao2 asymptotic estimation)
* `GPTCelltype` (Automated T cell subset annotation leveraging large language models)
* `forestmodel` (Forest plot visualization for statistical modeling results and differential comparisons)

* Other standard bioinformatics utilities.

**Python Dependencies:**
* `NoisET` (NOIse sampling learning & Expansion detection of T-cell receptors using Bayesian inference.)



<!------ 
## Fig1: Study design and evaluation framework for TCR dynamic analysis

## Fig2: Dominance of clonotype turnover under immunotherapy

+ Phenotypic clustering and compositional shifts of T cell subsets post-intervention

+ Temporal dynamics of TCR diversity and clonality

+ Defining characteristics of time-specific TCR clonotypes

## Fig3: Intrinsic repertoire topology dictates apparent TCR turnover

+ Comparison of time-specific and time-across TCRs in untreated samples across time points
+ Investigation of the proportion of emergent TCRs across multiple time points
+ Comparison of TCR temporal states between paired bulk and single-cell TCR data using different sequencing methods
+ Comparison of time-specific and time-across TCRs in cross-time point TCR data from different clinical backgrounds

## Fig4: Mathematical modeling reveals structural confounders of TCR turnover

+ Comparison of sample-specific and sample-across TCRs in biological replicates
+ Validation of patterns using simulated data
+ Investigation of influencing factors and applications of time-specific TCRs

## Fig5: Intrinsic clonal expansion levels confound dynamic TCR shifting

+ Evaluation of statistical models for detecting significantly expanded TCRs utilizing clinical single-cell TCR datasets

+ Benchmarking of differential abundance models across biological replicates and longitudinal cohorts in PBMC and tumor tissues

## Fig6: Tumor spatial heterogeneity and phenotypic bias on temporal TCR shifts

+ Phenotypic distribution of significantly expanded or contracted TCRs across distinct T cell subsets

+ Analysis of phenotypic biases and cell-type enrichment preferences among significantly expanded TCRs

+ Slide-TCR sequencing data reveals highly localized intra-tumor spatial heterogeneity

----->

















