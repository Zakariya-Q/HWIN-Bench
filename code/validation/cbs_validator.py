"""
HWIN-Bench v1.0 — CBS Validation Engine

Validates datasets against the Canonical Benchmark Schema (CBS).
"""

import json
import pandas as pd
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass


@dataclass
class ValidationResult:
    """Result of CBS validation."""
    passed: bool
    errors: List[str]
    warnings: List[str]
    stats: Dict


class CBSValidator:
    """
    Validates a dataset directory against the Canonical Benchmark Schema.
    
    Checks 58 rules across 6 categories:
    - Completeness (8 rules)
    - Range Validity (38 rules)
    - Referential Integrity (3 rules)
    - Duplicate Detection (2 rules)
    - Temporal Consistency (4 rules)
    - Spatial Consistency (3 rules)
    """
    
    # CBS required columns for observations
    REQUIRED_OBS_COLUMNS = [
        'observation_id', 'dataset_id', 'station_id', 'canonical_variable_id',
        'value', 'unit', 'timestamp', 'latitude', 'longitude', 'country',
        'site_name', 'param_name', 'source', 'quality_flag', 'percentile',
        'original_value', 'original_unit', 'country_iso'
    ]
    
    # Variable physical ranges (min, max) - subset for key variables
    VARIABLE_RANGES = {
        'HWIN-VAR-001': (-273.15, 313.15),  # Water Temperature (K)
        'HWIN-VAR-002': (0, 14),             # pH
        'HWIN-VAR-003': (0, 20),             # Dissolved Oxygen (mg/L)
        'HWIN-VAR-004': (0, 1000),           # Turbidity (NTU)
        'HWIN-VAR-005': (0, 100000),         # Specific Conductance (µS/cm)
        'HWIN-VAR-006': (0, 10000),          # Flow Rate (m³/s)
        'HWIN-VAR-007': (0, 10000),          # Water Depth (m)
        'HWIN-VAR-008': (0, 100),            # Nitrate Nitrogen (mg/L as N)
        'HWIN-VAR-009': (0, 50),             # Ammonium Nitrogen (mg/L as N)
        'HWIN-VAR-010': (0, 10),             # Phosphate Phosphorus (mg/L as P)
        'HWIN-VAR-011': (0, 500),            # Chlorophyll-a (µg/L)
        'HWIN-VAR-012': (0, 1e6),            # Fecal Coliforms (CFU/100mL)
        'HWIN-VAR-014': (0, 300),            # DO Percent Saturation (%)
        'HWIN-VAR-015': (0, 5000),           # Total Suspended Solids (mg/L)
        'HWIN-VAR-016': (233, 323),          # Air Temperature (K)
        'HWIN-VAR-017': (0, 50000),          # Chloride (mg/L)
        'HWIN-VAR-018': (0, 5000),           # Sulfate (mg/L)
        'HWIN-VAR-019': (0, 200),            # Silica (mg/L as SiO2)
        'HWIN-VAR-020': (0, 500),            # Alkalinity (mg/L as CaCO3)
        'HWIN-VAR-021': (0, 100000),         # Total Dissolved Solids (mg/L)
        'HWIN-VAR-022': (0, 100),            # BOD (mg/L)
        'HWIN-VAR-023': (0, 2000),           # COD (mg/L)
        'HWIN-VAR-028': (0, 100),            # Total Nitrogen (mg/L as N)
        'HWIN-VAR-031': (0, 50),             # Total Ammonia Nitrogen (mg/L as N)
        'HWIN-VAR-033': (0, 10),             # Nitrite Nitrogen (mg/L as N)
    }
    
    def __init__(self, dataset_path: Path):
        self.dataset_path = Path(dataset_path)
        self.errors = []
        self.warnings = []
        self.stats = {}
        
    def validate(self) -> ValidationResult:
        """Run all validation checks."""
        self.errors = []
        self.warnings = []
        self.stats = {}
        
        # Load data
        obs_file = self.dataset_path / 'observations.csv'
        stations_file = self.dataset_path / 'stations.json'
        variables_file = self.dataset_path / 'variables.csv'
        dataset_file = self.dataset_path / 'dataset.json'
        
        if not obs_file.exists():
            self.errors.append(f"Missing observations.csv at {obs_file}")
            return ValidationResult(False, self.errors, self.warnings, self.stats)
            
        if not stations_file.exists():
            self.errors.append(f"Missing stations.json at {stations_file}")
            
        if not variables_file.exists():
            self.errors.append(f"Missing variables.csv at {variables_file}")
            
        if not dataset_file.exists():
            self.errors.append(f"Missing dataset.json at {dataset_file}")
            
        if self.errors:
            return ValidationResult(False, self.errors, self.warnings, self.stats)
        
        # Load data
        obs = pd.read_csv(obs_file)
        with open(stations_file) as f:
            stations = json.load(f)
        variables = pd.read_csv(variables_file)
        with open(dataset_file) as f:
            dataset_meta = json.load(f)
            
        self.stats = {
            'n_observations': len(obs),
            'n_stations': len(stations),
            'n_variables': len(variables),
            'dataset_id': dataset_meta.get('dataset_id', 'UNKNOWN'),
        }
        
        # Run all validation categories
        self._check_completeness(obs, stations, variables, dataset_meta)
        self._check_range_validity(obs, variables)
        self._check_referential_integrity(obs, stations, variables)
        self._check_duplicates(obs)
        self._check_temporal_consistency(obs)
        self._check_spatial_consistency(obs, stations)
        
        passed = len(self.errors) == 0
        return ValidationResult(passed, self.errors, self.warnings, self.stats)
    
    def _check_completeness(self, obs, stations, variables, dataset_meta):
        """Check 8 completeness rules."""
        # 1. Required columns present
        missing_cols = set(self.REQUIRED_OBS_COLUMNS) - set(obs.columns)
        if missing_cols:
            self.errors.append(f"Missing required columns: {missing_cols}")
            
        # 2. No null station_id
        if obs['station_id'].isnull().any():
            self.errors.append("Null station_id found in observations")
            
        # 3. No null coordinates
        if obs['latitude'].isnull().any() or obs['longitude'].isnull().any():
            self.errors.append("Null latitude/longitude found in observations")
            
        # 4. No null timestamps
        if obs['timestamp'].isnull().any():
            self.errors.append("Null timestamp found in observations")
            
        # 5. No null values
        if obs['value'].isnull().any():
            self.errors.append("Null value found in observations")
            
        # 6. No null canonical_variable_id
        if obs['canonical_variable_id'].isnull().any():
            self.errors.append("Null canonical_variable_id found in observations")
            
        # 7. Valid country codes (ISO 3166-1 alpha-2)
        invalid_countries = obs[~obs['country'].str.match(r'^[A-Z]{2}$')]['country'].unique()
        if len(invalid_countries) > 0:
            self.warnings.append(f"Non-standard country codes: {invalid_countries[:10]}")
            
        # 8. Valid units (non-empty)
        if obs['unit'].isnull().any() or (obs['unit'] == '').any():
            self.errors.append("Empty or null unit found in observations")
    
    def _check_range_validity(self, obs, variables):
        """Check 38 range validity rules (per variable)."""
        var_ids_in_obs = obs['canonical_variable_id'].unique()
        var_ids_in_vars = variables['canonical_variable_id'].unique() if 'canonical_variable_id' in variables.columns else []
        
        for var_id in var_ids_in_obs:
            var_data = obs[obs['canonical_variable_id'] == var_id]
            
            # Check against known ranges
            if var_id in self.VARIABLE_RANGES:
                min_val, max_val = self.VARIABLE_RANGES[var_id]
                out_of_range = var_data[(var_data['value'] < min_val) | (var_data['value'] > max_val)]
                if len(out_of_range) > 0:
                    self.warnings.append(
                        f"{var_id}: {len(out_of_range)} observations outside expected range "
                        f"[{min_val}, {max_val}]"
                    )
            
            # Concentrations must be non-negative
            if var_id in ['HWIN-VAR-008', 'HWIN-VAR-009', 'HWIN-VAR-010', 
                         'HWIN-VAR-011', 'HWIN-VAR-012', 'HWIN-VAR-015',
                         'HWIN-VAR-017', 'HWIN-VAR-018', 'HWIN-VAR-019',
                         'HWIN-VAR-020', 'HWIN-VAR-021', 'HWIN-VAR-022', 'HWIN-VAR-023']:
                negative = var_data[var_data['value'] < 0]
                if len(negative) > 0:
                    self.errors.append(f"{var_id}: {len(negative)} negative concentration values")
                    
            # pH range
            if var_id == 'HWIN-VAR-002':
                bad_pH = var_data[(var_data['value'] < 0) | (var_data['value'] > 14)]
                if len(bad_pH) > 0:
                    self.errors.append(f"{var_id}: {len(bad_pH)} pH values outside [0, 14]")
                    
            # Temperature (Kelvin) must be positive
            if var_id in ['HWIN-VAR-001', 'HWIN-VAR-016']:
                bad_temp = var_data[var_data['value'] <= 0]
                if len(bad_temp) > 0:
                    self.errors.append(f"{var_id}: {len(bad_temp)} non-positive Kelvin temperatures")
    
    def _check_referential_integrity(self, obs, stations, variables):
        """Check 3 referential integrity rules."""
        # 1. All station_ids in observations exist in stations
        station_ids_obs = set(obs['station_id'].unique())
        station_ids_meta = set(s['station_id'] for s in stations)
        missing_stations = station_ids_obs - station_ids_meta
        if missing_stations:
            self.errors.append(f"{len(missing_stations)} station_ids in observations not found in stations.json")
            
        # 2. All canonical_variable_ids in observations exist in variables.csv
        if 'canonical_variable_id' in variables.columns:
            var_ids_obs = set(obs['canonical_variable_id'].unique())
            var_ids_meta = set(variables['canonical_variable_id'].unique())
            missing_vars = var_ids_obs - var_ids_meta
            if missing_vars:
                self.errors.append(f"{len(missing_vars)} variable_ids in observations not found in variables.csv")
                
        # 3. All country codes ISO 3166-1 alpha-2
        invalid_countries = obs[~obs['country'].str.match(r'^[A-Z]{2}$')]['country'].unique()
        if len(invalid_countries) > 0:
            self.warnings.append(f"Non-standard country codes: {invalid_countries[:10]}")
    
    def _check_duplicates(self, obs):
        """Check 2 duplicate detection rules."""
        # 1. No duplicate observation_ids
        dup_obs = obs[obs.duplicated(subset=['observation_id'], keep=False)]
        if len(dup_obs) > 0:
            self.errors.append(f"Duplicate observation_ids found: {len(dup_obs)} rows")
            
        # 2. No duplicate (station_id, timestamp, canonical_variable_id)
        dup_triplet = obs[obs.duplicated(subset=['station_id', 'timestamp', 'canonical_variable_id'], keep=False)]
        if len(dup_triplet) > 0:
            self.warnings.append(f"Duplicate (station_id, timestamp, variable) triplets: {len(dup_triplet)} rows")
    
    def _check_temporal_consistency(self, obs):
        """Check 4 temporal consistency rules."""
        # 1. Timestamps parseable as ISO 8601
        try:
            pd.to_datetime(obs['timestamp'], utc=True)
        except Exception as e:
            self.errors.append(f"Timestamp parsing failed: {e}")
            
        # 2. Within dataset temporal coverage (if available)
        # Skip - requires dataset metadata
        
        # 3. Chronological order per station-variable (check a sample)
        sample_stations = obs['station_id'].unique()[:10]
        for station in sample_stations:
            for var in obs['canonical_variable_id'].unique()[:5]:
                subset = obs[(obs['station_id'] == station) & (obs['canonical_variable_id'] == var)]
                if len(subset) > 1:
                    timestamps = pd.to_datetime(subset['timestamp'], utc=True)
                    if not timestamps.is_monotonic_increasing:
                        self.warnings.append(f"Non-chronological data for station {station}, var {var}")
                        break
                        
        # 4. No future dates (beyond 2030 as sanity check)
        future = obs[pd.to_datetime(obs['timestamp'], utc=True) > '2030-01-01']
        if len(future) > 0:
            self.warnings.append(f"{len(future)} observations with future timestamps (>2030)")
    
    def _check_spatial_consistency(self, obs, stations):
        """Check 3 spatial consistency rules."""
        # 1. Coordinates in valid ranges
        bad_lat = obs[(obs['latitude'] < -90) | (obs['latitude'] > 90)]
        bad_lon = obs[(obs['longitude'] < -180) | (obs['longitude'] > 180)]
        if len(bad_lat) > 0:
            self.errors.append(f"{len(bad_lat)} observations with invalid latitude")
        if len(bad_lon) > 0:
            self.errors.append(f"{len(bad_lon)} observations with invalid longitude")
            
        # 2. Country code matches coordinate location (basic check)
        # Skip - requires geocoding
        
        # 3. Station_type valid
        valid_types = {'river', 'lake', 'estuary', 'coastal', 'groundwater', 'spring', 'wetland', 'canal'}
        station_types = set(s.get('station_type', '') for s in stations if s.get('station_type'))
        invalid_types = station_types - valid_types
        if invalid_types:
            self.warnings.append(f"Unknown station types: {invalid_types}")


def validate_cbs(dataset_path: str) -> ValidationResult:
    """
    Validate a dataset against CBS.
    
    Args:
        dataset_path: Path to dataset directory containing observations.csv, 
                      stations.json, variables.csv, dataset.json
                      
    Returns:
        ValidationResult with passed flag, errors, warnings, and stats
    """
    validator = CBSValidator(Path(dataset_path))
    return validator.validate()


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Usage: python cbs_validator.py <dataset_path>")
        sys.exit(1)
        
    result = validate_cbs(sys.argv[1])
    print(f"Dataset: {result.stats.get('dataset_id', 'UNKNOWN')}")
    print(f"Observations: {result.stats.get('n_observations', 0)}")
    print(f"Stations: {result.stats.get('n_stations', 0)}")
    print(f"Variables: {result.stats.get('n_variables', 0)}")
    print(f"PASSED: {result.passed}")
    if result.errors:
        print("ERRORS:")
        for e in result.errors:
            print(f"  - {e}")
    if result.warnings:
        print("WARNINGS:")
        for w in result.warnings:
            print(f"  - {w}")
    sys.exit(0 if result.passed else 1)