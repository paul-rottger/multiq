import os
import pandas as pd
from google.cloud import translate_v3 as translate
from tqdm import tqdm
import glob
import json

def get_project_id_from_service_account():
    key_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    if not key_path:
        raise ValueError("Please set the GOOGLE_APPLICATION_CREDENTIALS environment variable to your service account key JSON file.")
    with open(key_path) as f:
        key_data = json.load(f)
    return key_data.get("project_id")

def detect_language(text, client, project_id, location='global'):
    response = client.detect_language(
        content=text,
        parent=f"projects/{project_id}/locations/{location}",
    )
    detected_language = max(response.languages, key=lambda x: x.confidence)
    return detected_language.language_code

def detect_languages_in_folder(input_folder, output_folder):
    client = translate.TranslationServiceClient()
    project_id = get_project_id_from_service_account()
    if not project_id:
        raise ValueError("Project ID not found in the service account key JSON file.")

    os.makedirs(output_folder, exist_ok=True)
    input_files = glob.glob(os.path.join(input_folder, "*.csv"))

    for input_file in tqdm(input_files, desc="Overall Progress", unit="file"):
        df = pd.read_csv(input_file)
        tqdm.pandas(desc=f"Detecting languages in {os.path.basename(input_file)}")
        df['detected_language'] = df['translate_output'].progress_apply(lambda x: detect_language(x, client, project_id))
        output_file = os.path.join(output_folder, os.path.basename(input_file))
        df.to_csv(output_file, index=False)

if __name__ == '__main__':
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'PATH/TO/KEY/.json'
    input_folder = 'PATH/TO/INTPUT/FOLDER/'
    output_folder = 'PATH/TO/OUTPUT/FOLDER/'
    detect_languages_in_folder(input_folder, output_folder)
