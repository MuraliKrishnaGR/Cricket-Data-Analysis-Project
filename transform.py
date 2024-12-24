import os
import zipfile
import json
import pandas as pd

# Define paths
download_dir = os.path.join(os.getcwd(), "downloads")
extracted_dir = os.path.join(os.getcwd(), "extracted")
output_dir = os.path.join(os.getcwd(), "datasets")

os.makedirs(extracted_dir, exist_ok=True)
os.makedirs(output_dir, exist_ok=True)

def unzip_files(zip_dir, output_dir):
    """Extract all zip files in the directory."""
    for file_name in os.listdir(zip_dir):
        if file_name.endswith(".zip"):
            zip_path = os.path.join(zip_dir, file_name)
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                extract_to = os.path.join(output_dir, os.path.splitext(file_name)[0])
                os.makedirs(extract_to, exist_ok=True)
                zip_ref.extractall(extract_to)
                print(f"Extracted: {zip_path} to {extract_to}")

def clean_dataframe(df):
    """
    Preprocess the DataFrame:
    - Simplify column names
    - Handle missing values
    - Remove duplicates
    - Normalize data types
    """
    # Simplify column names
    df.columns = [
        col.replace('meta.', '')
           .replace('info.', '')
           .replace('outcome.', 'outcome_')
           .replace('event.', 'event_')
           .replace('officials.', 'officials_')
           .replace('.', '_')
           .replace('info.', '')
           .replace('registry.people.', '')
           .replace('players.', 'players_')
           .replace('.', '_')  # Replace remaining dots with underscores
        for col in df.columns
    ]
    
    df.columns = ['_'.join(col.split('.')[-2:]) for col in df.columns]


    # Convert non-hashable types to strings
    for col in df.columns:
        df[col] = df[col].apply(lambda x: str(x) if isinstance(x, (list, dict)) else x)

    # Handle missing values
    df.fillna({
        'player_of_match': 'Unknown',
        'result': 'No Result'
    }, inplace=True)

    # Drop columns with more than 50% missing values
    missing_threshold = 0.5 * len(df)
    df.dropna(axis=1, thresh=missing_threshold, inplace=True)

    # Drop duplicate rows
    df.drop_duplicates(inplace=True)

    # Normalize dates if 'dates' column exists
    if 'dates' in df.columns:
        df['dates'] = pd.to_datetime(df['dates'], errors='coerce')

    return df



def process_json_files(extracted_dir):
    """Process JSON files and return cleaned DataFrames for each match type."""
    dataframes = {}

    for match_type_dir in os.listdir(extracted_dir):
        match_type_path = os.path.join(extracted_dir, match_type_dir)
        if os.path.isdir(match_type_path):
            match_type = match_type_dir.split('_')[0].capitalize()
            print(f"Processing {match_type} matches...")
            match_dataframes = []

            for json_file in os.listdir(match_type_path):
                if not json_file.endswith(".json"):
                    continue

                json_path = os.path.join(match_type_path, json_file)
                try:
                    with open(json_path, 'r') as file:
                        match_data = json.load(file)
                        df = pd.json_normalize(match_data)  # Flatten nested JSON
                        df = clean_dataframe(df)  # Clean and preprocess the DataFrame
                        match_dataframes.append(df)
                except (json.JSONDecodeError, KeyError) as e:
                    print(f"Error processing {json_file}: {e}")

            # Combine all DataFrames for the match type
            dataframes[match_type] = pd.concat(match_dataframes, ignore_index=True) if match_dataframes else pd.DataFrame()
            print(f"{match_type} DataFrame shape: {dataframes[match_type].shape}")

    return dataframes

if __name__ == "__main__":
    # Step 1: Unzip files
    unzip_files(download_dir, extracted_dir)

    # Step 2: Process JSON files into cleaned DataFrames
    dataframes = process_json_files(extracted_dir)

    # Step 3: Save the cleaned DataFrames as CSVs
    for match_type, df in dataframes.items():
        file_path = os.path.join(output_dir, f"{match_type.lower()}_matches.csv")
        df.to_csv(file_path, index=False)
        print(f"Saved {match_type} matches to {file_path}")
