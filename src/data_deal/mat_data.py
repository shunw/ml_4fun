import scipy.io
import pandas as pd
import numpy as np
import os

def extract_mat_to_df(file_path: str) -> dict[str, pd.DataFrame]:
    """
    Extracts data from a .mat file and converts compatible variables into pandas DataFrames.
    Returns a dictionary where keys are the variable names and values are DataFrames.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    try:
        mat = scipy.io.loadmat(file_path, squeeze_me=True)
    except Exception as e:
        print(f"Error loading .mat file: {e}")
        return {}

    data_frames = {}
    
    for key, value in mat.items():
        # Skip meta-information
        if key.startswith('__'):
            continue
            
        try:
            # Check if it's an array-like structure we can convert
            if isinstance(value, (np.ndarray, list)):
                if isinstance(value, np.ndarray) and value.ndim == 0:
                    # Handle 0-d array (scalar)
                    df = pd.DataFrame([value.item()])
                else:
                    df = pd.DataFrame(value)
                data_frames[key] = df
            elif isinstance(value, (int, float, str)):
                 data_frames[key] = pd.DataFrame([value])
            else:
                print(f"Skipping key '{key}': type {type(value)} not automatically convertible to DataFrame")
        except Exception as e:
            print(f"Could not convert key '{key}' to DataFrame. Error: {repr(e)}")

    return data_frames

def process_algae_data(file_path: str) -> pd.DataFrame:
    """
    Specific parser for the algae.mat file structure described in GEMINI.md.
    Returns a long-format DataFrame with columns: [raceway, parameter, time_days, value].
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    try:
        # struct_as_record=False loads MATLAB structs as Python objects with attributes
        mat = scipy.io.loadmat(file_path, squeeze_me=True, struct_as_record=False)
    except Exception as e:
        print(f"Error loading .mat file: {e}")
        return pd.DataFrame()

    if 'algae' not in mat:
        print("Key 'algae' not found in .mat file.")
        return pd.DataFrame()

    algae_structs = mat['algae']
    
    # Ensure it's iterable (handle case of single struct)
    if not isinstance(algae_structs, np.ndarray):
        algae_structs = [algae_structs]

    records = []
    
    # Fields to ignore or handle separately
    excluded_fields = {'comments'}

    for r_idx, raceway in enumerate(algae_structs):
        # In struct_as_record=False objects, fields are attributes.
        # We can get them via _fieldnames attribute if available or dir()
        # scipy.io.matlab.mio5_params.mat_struct usually has _fieldnames
        
        fields = getattr(raceway, '_fieldnames', [])
        if not fields:
             # Fallback if _fieldnames is not present, filter dir()
             fields = [f for f in dir(raceway) if not f.startswith('_')]

        for field in fields:
            if field in excluded_fields:
                continue

            try:
                param_data = getattr(raceway, field)
                
                # Check if it has 'data' and 'time_num' attributes
                if hasattr(param_data, 'data') and hasattr(param_data, 'time_num'):
                    data_vals = param_data.data
                    time_vals = param_data.time_num
                    
                    # Handle cases where data/time might be scalars or arrays
                    # Ensure they are 1D arrays for DataFrame construction
                    if np.ndim(data_vals) == 0: data_vals = [data_vals]
                    if np.ndim(time_vals) == 0: time_vals = [time_vals]
                    
                    # Flatten if they are column vectors like (N, 1)
                    data_vals = np.array(data_vals).flatten()
                    time_vals = np.array(time_vals).flatten()

                    if len(data_vals) != len(time_vals):
                        print(f"Warning: Length mismatch for Raceway {r_idx+1}, Field {field}. Data: {len(data_vals)}, Time: {len(time_vals)}")
                        # Truncate to shorter length? Or skip? Let's skip to be safe.
                        continue
                        
                    # Create temporary DataFrame for this parameter
                    temp_df = pd.DataFrame({
                        'raceway': r_idx + 1,
                        'parameter': field,
                        'time_days': time_vals,
                        'value': data_vals
                    })
                    records.append(temp_df)
            except Exception as e:
                print(f"Error processing Raceway {r_idx+1}, Field {field}: {e}")

    if not records:
        return pd.DataFrame()
        
    final_df = pd.concat(records, ignore_index=True)
    return final_df

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', help='mat file to parse', required=True)
    parser.add_argument('--mode', choices=['generic', 'algae'], default='generic', help='Parsing mode')
    
    args = parser.parse_args()
    
    if args.mode == 'algae':
        df = process_algae_data(args.file)
        print("\n--- Algae Data (Long Format) ---")
        print(df.head())
        print(df.info())
        print("\nUnique Parameters:", df['parameter'].unique())
        
        # Example of pivoting (optional view)
        # print("\n--- Pivot Sample (pH) ---")
        # ph_df = df[df['parameter'] == 'pH']
        # print(ph_df.head())
    else:
        dfs = extract_mat_to_df(args.file)
        for name, df in dfs.items():
            print(f"\n--- Variable: {name} ---")
            print(df.head())
            print(df.shape)
