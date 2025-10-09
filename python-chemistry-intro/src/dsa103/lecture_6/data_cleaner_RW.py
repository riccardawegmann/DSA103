from pathlib import Path

import pandas as pd


def load_and_clean_setup_data(filepath: Path, setup_name: str, convert_to_celcius: bool):
    """Load and standardize data from one setup"""

    #read csv files
    df = pd.read_csv(Path(filepath))
    df_copy = df.copy()

    #rename
    df_copy = df_copy.rename(columns={df_copy.columns[0]: 'time_min', df_copy.columns[1]: 'temperature_C', df_copy.columns[2]: 'concentration_M', 
                           df_copy.columns[3]: 'ph_value',df_copy.columns[4]: 'yield_percent'})
    
    #change units, Fahrenheit to celcius
    if convert_to_celcius == True:
        df_copy['temperature_C'] = ((df_copy['temperature_C'] - 32) / 1.8). round(1)
        setup_name = df_copy 
    else:
        setup_name = df_copy 

    return setup_name


def combine_datasets(setup_a_data: pd.DataFrame, setup_b_data: pd.DataFrame):
    """Combine datasets from both setups"""

    #add lables
    setup_a_data['setup'] = 'A'
    setup_b_data['setup'] = 'B'

    #combine both setups
    combined_df = pd.concat([setup_a_data, setup_b_data], ignore_index=True)

    return combined_df