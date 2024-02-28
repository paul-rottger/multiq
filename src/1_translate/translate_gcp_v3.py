import pandas as pd
import os
from google.cloud import translate_v3 as translate
from google.oauth2 import service_account
from tqdm import tqdm

# Set up Google Translate credentials
credentials_path = 'PATH/TO/KEY/.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

# Get all available gcp languages
def get_supported_languages():
    credentials = service_account.Credentials.from_service_account_file(os.environ['GOOGLE_APPLICATION_CREDENTIALS'])
    project_id = credentials.project_id

    if project_id is None:
        raise Exception("Could not determine the Google Cloud project ID from the service account key")

    client = translate.TranslationServiceClient(credentials=credentials)

    parent = f"projects/{project_id}/locations/global"

    response = client.get_supported_languages(parent=parent)
    # skipping English otherwise the script crashes translating from and to English
    languages = [language.language_code for language in response.languages if language.language_code != 'en']
    return languages

def translate_text(target: str, text: str) -> dict:
    credentials = service_account.Credentials.from_service_account_file(os.environ['GOOGLE_APPLICATION_CREDENTIALS'])
    project_id = credentials.project_id

    if project_id is None:
        raise Exception("Could not determine the Google Cloud project ID from the service account key")

    client = translate.TranslationServiceClient(credentials=credentials)

    parent = f"projects/{project_id}/locations/global"

    response = client.translate_text(
        contents=[text],
        mime_type='text/plain',
        source_language_code='en',
        target_language_code=target,
        parent=parent,
    )

    translation = response.translations[0]
    result = {
        "translatedText": translation.translated_text,
        "detectedSourceLanguage": translation.detected_language_code,
    }
    return result

def translate_and_save(input_csv, output_folder, target_languages=None, all_languages=False, start_from_language=None):
    df = pd.read_csv(input_csv, encoding='utf-8')

    if 'domain' in df.columns:
        domain_present = True
    else:
        domain_present = False

    if all_languages:
        print("Fetching supported languages...")
        target_languages = get_supported_languages()
        print(f"{len(target_languages)} languages found.")

    # Exclude the input language from translations -- en - English hardcoded
    if 'en' in target_languages:
        target_languages.remove('en')

    # Restart from a specific language
    if start_from_language:
        if start_from_language in target_languages:
            start_index = target_languages.index(start_from_language)
            target_languages = target_languages[start_index:]
        else:
            raise ValueError(f"Language code {start_from_language} not found in target languages.")

    # Adding a progress bar for the overall translation process
    for target_language in tqdm(target_languages, desc="Overall Progress", unit="language"):
        output_rows = []

        # Adding a progress bar for translating each row
        for _, row in tqdm(df.iterrows(), total=len(df), desc=f"Translating to {target_language}", unit="row"):
            prompt = row['prompt']
            id = row['id']
            if domain_present:
                domain = row['domain']
            else:
                domain = None

            result = translate_text(target_language, prompt)

            output_row = {
                'id': id,
                'prompt_language': 'en',
                'prompt': prompt,
                'translate_output': result["translatedText"],
                'domain': domain,
                'detected_language': result["detectedSourceLanguage"]
            }
            output_rows.append(output_row)

        output_df = pd.DataFrame(output_rows)
        input_file_name = os.path.basename(input_csv).replace(".csv", "")
        output_file = os.path.join(output_folder, f"{target_language}_{input_file_name}.csv")
        output_df.to_csv(output_file, index=False, encoding='utf-8')
        print(f"Translation to {target_language} completed and saved to {output_file}")


if __name__ == '__main__':
    input_csv = 'PATH/TO/INPUT/FILE.csv'
    output_folder = 'PATH/TO/OUTPUT/FOLDER/'
    translate_and_save(input_csv, output_folder, all_languages=True, start_from_language=None)

