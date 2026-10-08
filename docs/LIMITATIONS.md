# Limitations — HWIN-Bench v1.0

Explicit documentation of known limitations, scope boundaries, and caveats for HWIN-Bench v1.0.

## Scope Limitations

### 1. Single Primary Benchmark Dataset
**Only GRQA v1.4 is used for the canonical regression benchmark** (Protocol §3.3). The four STORET/WQP datasets are included for:
- Transfer learning evaluation (Protocol §16)
- Demonstrating harmonization across heterogeneous sources
- Future benchmark extensions (v1.1+)

**Implication**: Claims about "global water quality prediction" are primarily supported by GRQA performance. STORET/WQP results are supplementary.

### 2. Classical ML Models Only
**v1.0 includes only 7 classical sklearn models** (Protocol §7):
- Linear Regression, Ridge, Lasso, ElasticNet
- Random Forest, Extra Trees, Gradient Boosting

**Excluded from v1.0** (reserved for v1.1+):
- XGBoost, LightGBM, CatBoost (in `hwin-baselines` repo)
- HWIN-Net deep learning models (in `hwin-net` repo)
- TabPFN, TabNet, other modern tabular methods

**Implication**: Benchmark does not represent state-of-the-art ML performance. It establishes a classical baseline.

### 3. MAX_SAMPLES Computational Cap
**200,000 observations per variable** (Protocol §4.1) applied to GRQA data:
- 10 of 11 benchmarkable variables are capped
- This is a **computational constraint**, not a scientific decision

**Implication**: Models are not trained on the full GRQA dataset (25.8M observations). Performance may improve with more data.

### 4. Single Regression Task
**v1.0 benchmarks only one task**: Point prediction of water quality variables from spatiotemporal features.

**Not included in v1.0**:
- Classification tasks (e.g., water quality class prediction)
- Time series forecasting (sequential prediction)
- Multi-variable joint prediction
- Anomaly detection
- Causal inference

### 5. Feature Set is Minimal
**Only 7 features** (Protocol §5): latitude, longitude, year, month, day_of_year, sin_doy, cos_doy.

**Excluded features** (known to improve water quality prediction):
- Watershed characteristics (land use, soil, geology)
- Upstream/downstream network topology
- Meteorological drivers (precipitation, temperature, radiation)
- Anthropogenic pressures (population, agriculture, industry)
- Remote sensing indices (NDVI, surface temperature)
- Hydrological signatures (flow, baseflow index)

**Implication**: This is a "spatiotemporal baseline" — real applications need richer features.

## Data Limitations

### 6. Spatial Bias in GRQA
GRQA v1.4 has **strong geographic bias**:
- **Overrepresented**: Europe, North America (especially US, Germany, France, UK)
- **Underrepresented**: Africa, South America, Southeast Asia, Arctic, Oceania
- **Missing**: Many developing nations with limited monitoring

**Implication**: Model performance may not generalize to data-scarce regions. Transfer learning to STORET (US-only) partially addresses this but remains US-centric.

### 7. Temporal Bias
- **Pre-1950**: Sparse data (<1% of observations)
- **1970-2000**: Peak monitoring activity
- **Post-2010**: Declining in some networks, increasing in others
- **2023 cutoff**: GRQA v1.4 ends at 2023

**Implication**: Models trained on historical data may not reflect current conditions (climate change, land use change).

### 8. Variable Coverage Imbalance
| Variable | GRQA Observations | Coverage |
|----------|-------------------|----------|
| Water Temperature | 5.5M | Excellent |
| pH | 4.7M | Excellent |
| Dissolved Oxygen | 2.8M | Good |
| Nitrate Nitrogen | 2.3M | Good |
| Phosphate Phosphorus | 2.9M | Good |
| DO Saturation | 1.7M | Moderate |
| TSS | 1.3M | Moderate |
| Nitrite Nitrogen | 1.3M | Moderate |
| Ammonium Nitrogen | 1.0M | Moderate |

**Implication**: Benchmark reliability varies by variable. Variables with fewer observations have higher uncertainty.

### 9. Harmonization Information Loss
Mapping 100+ source variables to 49 canonical variables involves:
- **Unit conversions** (with rounding/precision loss)
- **Synonym resolution** (Tier 3 mappings involve expert judgment)
- **Aggregation** (e.g., multiple nitrogen forms → Total Nitrogen)
- **Dropped variables** (source variables with no CVO mapping)

**Implication**: Harmonized data is not identical to source data. Per-observation provenance tracks transformations.

### 10. Quality Flag Heterogeneity
Source datasets use **different quality flag systems**:
- GEMSTAT: 0=good, 1=suspect, 2=bad, 3=below DL, 4=above DL, 9=missing
- WQP/STORET: Different flag codes per agency
- GRQA: Proprietary quality assessment

**HWIN-Bench approach**: Preserve original flags in `quality_flag` column; benchmark uses all data (flag=0 only would reduce samples).

## Methodological Limitations

### 11. GroupKFold by Station Only
Splits group by `station_id` but **do not account for**:
- Temporal autocorrelation within stations
- Spatial autocorrelation between nearby stations
- Watershed connectivity (upstream-downstream)

**Implication**: Performance estimates may be optimistic for truly independent predictions.

### 12. No Hyperparameter Tuning
All models use **fixed hyperparameters** (Protocol §7). No cross-validation for hyperparameter selection.

**Implication**: Reported performance is for default/reasonable settings, not optimal performance.

### 13. Single Train/Test Split Strategy
Only **5×5 GroupKFold** is evaluated. No:
- Spatial block CV
- Temporal CV (train on past, test on future)
- Leave-one-basin-out
- Leave-one-country-out

**Implication**: Generalization to unseen basins/regions/time periods not formally tested.

### 14. Transfer Learning Not Certified
Transfer learning (Protocol §16) has a **known NaN bug** (COMP-004) and was not part of the certified canonical execution.

**Implication**: Transfer learning results in v1.0 are preliminary and not benchmark-certified.

### 15. FAIR Assessment is Qualitative
Protocol §18 explicitly **prohibits numeric FAIR scores**. Only qualitative A-/A ratings.

**Implication**: Cannot quantitatively compare FAIRness across datasets/benchmarks.

## Statistical Limitations

### 16. Statistical Testing Not Implemented in v1.0
The protocol (§9.3) specifies Kruskal-Wallis, Wilcoxon signed-rank, Cliff's Delta, and Holm-Bonferroni correction, but **these were NOT implemented or executed in v1.0**. The protocol's statistical testing requirements are reserved for v1.1+.

**Implication**: No statistical hypothesis testing was performed on the canonical benchmark outputs. Only corrected confidence intervals (n=5, df=4) are provided.

### 17. Confidence Intervals Assumptions
95% CIs use **t-distribution on 5 unique fold means** (corrected from n=25 to n=5).

**Assumptions**:
- Fold means approximately normally distributed (CLT with n=5)
- The 5 seed repetitions are deterministic — folds are identical across seeds

**Implication**: CIs correctly use n=5 (df=4). The historical n=25 CIs were ~3× too narrow.

### 18. Effect Size Interpretation
Cliff's Delta is **non-parametric but pairwise**.

**Implication**: Effect sizes not directly comparable across variables with different scales.

## Technical Limitations

### 19. GRQA Size vs. Memory
Full GRQA harmonized: **25.8M rows × ~20 columns ≈ 4 GB memory** for observations alone.

**Workaround**: Benchmark uses MAX_SAMPLES=200K cap; full data available for custom experiments.

### 20. Windows Path Handling
Canonical paths in protocol use Windows absolute paths (`C:\Users\lenovo\...`).

**Implication**: Cross-platform reproduction requires path adaptation. Use relative paths or environment variables.

### 21. No GPU Acceleration
All models are **CPU-only sklearn implementations**. No GPU support in v1.0.

**Implication**: Training time scales linearly with cores; deep learning models (v1.1+) will need GPU.

## Scope Boundaries (What HWIN-Bench v1.0 Is NOT)

| Not a... | Explanation |
|----------|-------------|
| **Water quality model** | It's a benchmark for evaluating models |
| **Decision support tool** | No operational forecasting capability |
| **Regulatory compliance checker** | No legal/regulatory thresholds built in |
| **Real-time monitoring system** | Batch benchmark only |
| **Global coverage guarantee** | GRQA has known geographic gaps |
| **Causal inference framework** | Predictive correlation only |
| **Uncertainty quantification benchmark** | Point predictions only (no prediction intervals) |
| **Fairness/bias audit tool** | No demographic/environmental justice variables |

## Planned for v1.1+

| Feature | Status |
|---------|--------|
| XGBoost, LightGBM, CatBoost | In `hwin-baselines` repo |
| HWIN-Net deep learning | In `hwin-net` repo |
| Spatial block CV | Design phase |
| Temporal CV | Design phase |
| Prediction intervals | Research needed |
| Watershed features | Data acquisition phase |
| Global transfer benchmark | Requires more target regions |
| Causal benchmark | Separate track |

## Reporting Issues

If you discover additional limitations not documented here, please open a GitHub Issue with label `limitation`.

---

**Version**: 1.0.0  
**Protocol**: Frozen v1.0 — limitations are documented, not fixed  
**Last Updated**: 2026-08-11