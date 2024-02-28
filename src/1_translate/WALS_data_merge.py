import os
import glob
import pandas as pd
from tqdm import tqdm


def merge_with_wals_data(df, wals_df_unique):
    df_copy = df.copy()

    # Merge for input language
    df_copy = df_copy.merge(wals_df_unique[['ISO639P3code', 'ID', 'Family', 'Latitude', 'Longitude', 'Glottocode']], left_on='iso_639_3',
                            right_on='ISO639P3code', how='left')
    df_copy.rename(columns={'Family': 'input_family', 'ID': 'input_WALS_Code'}, inplace=True)
    df_copy.rename(columns={'Latitude': 'input_latitude', 'Longitude': 'input_longitude', 'Glottocode': 'input_glottocode'}, inplace=True)

    # Merge for output language
    df_copy = df_copy.merge(wals_df_unique[['ISO639P3code', 'ID', 'Family']], left_on='detected_language',
                            right_on='ISO639P3code', how='left', suffixes=('', '_output'))
    df_copy.rename(columns={'Family': 'output_family', 'ID': 'output_WALS_Code'}, inplace=True)

    # Remove the ISO639P3code columns
    df_copy.drop(columns=['ISO639P3code', 'ISO639P3code_output'], inplace=True)

    # Manually add values from Grambank
    df_copy.loc[df_copy['language'] == 'co', 'input_family'] = 'Indo-European'
    df_copy.loc[df_copy['language'] == 'eo', 'input_family'] = 'Indo-European'
    df_copy.loc[df_copy['language'] == 'sa', 'input_family'] = 'Indo-European'


    # Replace NaN values with 'Unknown'
    df_copy.fillna('Unknown', inplace=True)

    return df_copy


def process_file(input_file, output_folder, wals_df_unique):
    df = pd.read_csv(input_file)
    processed_df = merge_with_wals_data(df, wals_df_unique)
    output_file = os.path.join(output_folder, os.path.basename(input_file))
    processed_df.to_csv(output_file, index=False)

def main():
    wals_url = 'https://raw.githubusercontent.com/cldf-datasets/wals/master/cldf/languages.csv'
    wals_df = pd.read_csv(wals_url)
    wals_df_unique = wals_df.drop_duplicates(subset='ISO639P3code')

    input_folder = 'PATH/TO/INTPUT/FOLDER/'
    output_folder = input_folder
    os.makedirs(output_folder, exist_ok=True)

    input_files = glob.glob(os.path.join(input_folder, "*.csv"))
    for input_file in tqdm(input_files, desc="Processing Files", unit="file"):
        process_file(input_file, output_folder, wals_df_unique)

if __name__ == "__main__":
    main()
