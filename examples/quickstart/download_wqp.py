#!/usr/bin/env python3
"""
HWIN-Bench v1.0 — WQP/STORET Download Script

Downloads data from the Water Quality Portal for HWIN-Bench subsets.
"""

import argparse
import requests
import pandas as pd
from pathlib import Path
import time
import sys

WQP_BASE_URL = "https://www.waterqualitydata.us/data/Result/search"


def download_wqp(bbox=None, statecode=None, start_date='1950-01-01', end_date='2024-12-31', 
                 datasource='NWIS,WQX', output_file=None, chunk_size=100000):
    """
    Download data from Water Quality Portal.
    
    Args:
        bbox: Bounding box as (min_lon, min_lat, max_lon, max_lat)
        statecode: FIPS state code (e.g., 'US:06' for California)
        start_date: Start date (YYYY-MM-DD)
        end_date: End date (YYYY-MM-DD)
        datasource: Data source ('NWIS', 'WQX', or 'NWIS,WQX')
        output_file: Output CSV path
        chunk_size: Rows per request
    """
    params = {
        'startDateLo': start_date,
        'startDateHi': end_date,
        'dataSource': datasource,
        'mimeType': 'csv',
        'zip': 'no',
    }
    
    if bbox:
        params['bBox'] = ','.join(map(str, bbox))
    if statecode:
        params['statecode'] = statecode
        
    print(f"Downloading from WQP with params: {params}")
    
    # First, get total count
    count_params = params.copy()
    count_params['mimeType'] = 'tsv'
    count_params['countOnly'] = 'true'
    
    response = requests.get(WQP_BASE_URL, params=count_params, timeout=60)
    if response.status_code != 200:
        print(f"Error getting count: {response.status_code}")
        return None
        
    total_rows = int(response.text.strip())
    print(f"Total rows to download: {total_rows}")
    
    if total_rows == 0:
        print("No data found for query")
        return pd.DataFrame()
    
    # Download in chunks
    all_chunks = []
    for start in range(0, total_rows, chunk_size):
        chunk_params = params.copy()
        chunk_params['startIndex'] = start
        chunk_params['maxResults'] = chunk_size
        
        print(f"Downloading chunk {start//chunk_size + 1}/{(total_rows-1)//chunk_size + 1}...")
        
        response = requests.get(WQP_BASE_URL, params=chunk_params, timeout=120)
        if response.status_code != 200:
            print(f"Error downloading chunk: {response.status_code}")
            print(response.text[:500])
            break
            
        # Parse CSV
        from io import StringIO
        chunk_df = pd.read_csv(StringIO(response.text), low_memory=False)
        all_chunks.append(chunk_df)
        
        if len(chunk_df) < chunk_size:
            break
            
        time.sleep(1)  # Be nice to the server
    
    if not all_chunks:
        return pd.DataFrame()
        
    df = pd.concat(all_chunks, ignore_index=True)
    print(f"Downloaded {len(df)} rows")
    
    if output_file:
        df.to_csv(output_file, index=False)
        print(f"Saved to {output_file}")
        
    return df


def download_sfbay(output_file='data/datasets/HWIN-WQP-SFBAY/observations_raw.csv'):
    """Download San Francisco Bay subset."""
    # SF Bay bounding box
    bbox = (-123.5, 37.0, -121.5, 38.5)
    return download_wqp(bbox=bbox, output_file=output_file)


def download_storet_state(state_fips, output_file):
    """Download STORET data for a US state."""
    statecode = f'US:{state_fips}'
    return download_wqp(statecode=statecode, datasource='WQX', output_file=output_file)


def main():
    parser = argparse.ArgumentParser(description='Download WQP/STORET data for HWIN-Bench')
    parser.add_argument('--dataset', choices=['sfbay', 'storet-ca', 'storet-tx', 'storet-ri', 'all'],
                       default='all', help='Dataset to download')
    parser.add_argument('--output-dir', default='data/datasets', help='Output directory')
    parser.add_argument('--start-date', default='1950-01-01', help='Start date (YYYY-MM-DD)')
    parser.add_argument('--end-date', default='2024-12-31', help='End date (YYYY-MM-DD)')
    
    args = parser.parse_args()
    
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    if args.dataset in ['sfbay', 'all']:
        print("=" * 60)
        print("Downloading WQP San Francisco Bay...")
        download_sfbay(output_file=output_dir / 'HWIN-WQP-SFBAY' / 'observations_raw.csv')
    
    if args.dataset in ['storet-ca', 'all']:
        print("=" * 60)
        print("Downloading STORET California...")
        download_storet_state('06', output_dir / 'HWIN-STORET-CA' / 'observations_raw.csv')
    
    if args.dataset in ['storet-tx', 'all']:
        print("=" * 60)
        print("Downloading STORET Texas...")
        download_storet_state('48', output_dir / 'HWIN-STORET-TX' / 'observations_raw.csv')
    
    if args.dataset in ['storet-ri', 'all']:
        print("=" * 60)
        print("Downloading STORET Rhode Island...")
        download_storet_state('44', output_dir / 'HWIN-STORET-RI' / 'observations_raw.csv')
    
    print("=" * 60)
    print("Download complete!")


if __name__ == '__main__':
    main()