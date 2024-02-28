import os
import pandas as pd
import glob
import fasttext
from huggingface_hub import hf_hub_download
from tqdm import tqdm
from custom_language_mapping import CUSTOM_MAPPING
import re

def convert_code(code):
    return CUSTOM_MAPPING.get(code, 'unknown')

def get_possible_matches(language):
    return_list = []
    iso_from_list =  convert_code(language)

    return_list.append(iso_from_list)

    # Add exceptions for GlotLID
    if language == 'ku':
        return_list.extend(['kmr', 'kur', 'sdh'])
    if language == 'gom':
        return_list.extend(['gom', 'kur', 'kok'])
    if language == 'qu':
        return_list.extend(['que', 'quf', 'quh', 'quk', 'qul', 'qup', 'qur', 'qux', 'quy', 'quz', 'qva', 'qvc', 'qve', 
                            'qvh', 'qvl', 'qvm', 'qvn', 'qvo', 'qvp', 'qvs', 'qvw', 'qwa', 'qwc', 'qwh', 'qws', 'qxa', 
                            'qxc', 'qxh', 'qxn', 'qxo', 'qxp', 'qxt', 'qxu', 'qxw'])
    if language == 'az':
        return_list.extend(['aze', 'azj'])
    if language == 'doi':
        return_list.extend(['doi'])
    if language == 'sr':
        return_list.extend(['scc', 'srp', 'hrv'])
    if language == 'hr':
        return_list.extend(['hrv', 'srp', 'bos'])
    if language == 'ps':
        return_list.extend(['pbt', 'pbu', 'pst'])
    if language == 'ak':
        return_list.extend(['twi'])
    if language == 'yi':
        return_list.extend(['ydd', 'yds', 'yid', 'yih'])
    if language == 'no':
        return_list.extend(['nno', 'nob', 'nor'])
    if language == 'hmn':
        return_list.extend(['hmn'])
    if language == 'et':
        return_list.extend(['est'])
    if language == 'ar':
        return_list.extend(['ara', 'arq', 'ars', 'ary', 'arz'])
    if language == 'gn':
        return_list.extend(['grn'])
    if language == 'bs':
        return_list.extend(['hrv', 'bos'])
    if language == 'or':
        return_list.extend(['ory'])
    if language == 'sw':
        return_list.extend(['swa', 'swc'])
    if language == 'ms':
        return_list.extend(['mly', 'msa', 'zlm'])
    if language == 'ne':
        return_list.extend(['nep', 'msa'])
    if language == 'sq':
        return_list.extend(['aln', 'als'])
    if language == 'lv':
        return_list.extend(['lvs'])
    if language == 'uz':
        return_list.extend(['uzb', 'uzn', 'uzs'])
    if language == 'mn':
        return_list.extend(['cmg', 'khk'])
    if language == 'ti':
        return_list.extend(['tig'])
    if language == 'fa':
        return_list.extend(['fas'])
    if language == 'haw':
        return_list.extend(['mri'])
    if language == 'ay':
        return_list.extend(['ayc', 'aym'])
    if language == 'om':
        return_list.extend(['gax', 'hae', 'orm'])
    if language == 'mg':
        return_list.extend(['skg', 'tdx', 'tkg', 'txy', 'xmv', 'xmw', 'bhr', 'bjq', 'bmm', 'bzc', 'mlg', 'msh'])
    if language == 'st':
        return_list.extend(['tsn'])
    if language == 'zh':
        return_list.extend(['cmn', 'wuu', 'yue', 'zhx', 'cdo', 'cjy', 'cnp', 'cpi', 'cpx', 'csp', 'czh', 'czo', 'gan', 'hak', 'hsn', 'ltc', 'mnp', 'nan'])
    if language == 'zh-CN':
        return_list.extend(['cmn', 'wuu', 'yue', 'zhx', 'cdo', 'cjy', 'cnp', 'cpi', 'cpx', 'csp', 'czh', 'czo', 'gan', 'hak', 'hsn', 'ltc', 'mnp', 'nan'])
    if language == 'zh-TW':
        return_list.extend(['cmn', 'wuu', 'yue', 'zhx', 'cdo', 'cjy', 'cnp', 'cpi', 'cpx', 'csp', 'czh', 'czo', 'gan', 'hak', 'hsn', 'ltc', 'mnp', 'nan'])

    return return_list

def get_language_details(iso_639_code):
    iso_639_3_code = convert_code(iso_639_code)
    return iso_639_3_code

def clean_text(text):
    if pd.isna(text):
        return ""
    cleaned_text = re.sub(r'\s+', ' ', text).strip()
    return cleaned_text

def detect_language_and_script(text, model):
    cleaned_text = clean_text(text)
    predictions = model.predict(cleaned_text)
    if predictions:
        label = predictions[0][0]
        parts = label.replace('__label__', '').split('_')
        return parts[0], parts[1] if len(parts) > 1 else 'Unknown'
    return 'Unknown', 'Unknown'

def download_and_load_model():
    model_path = hf_hub_download(repo_id="cis-lmu/glotlid", filename="model.bin", cache_dir=None)
    model = fasttext.load_model(model_path)
    return model

def process_file(input_file, output_folder, model):
    df = pd.read_csv(input_file)

    df['model_completion'] = df['model_completion'].apply(clean_text)

    df['iso_639_3'] = df['language'].apply(get_language_details)

    df['iso_range'] = df['language'].apply(get_possible_matches)

    # Detecting languages
    tqdm.pandas(desc=f"Detecting languages in {os.path.basename(input_file)}")
    df[['detected_language', 'detected_script']] = df['model_completion'].progress_apply(
        lambda x: pd.Series(detect_language_and_script(x, model))
    )

    output_file = os.path.join(output_folder, os.path.basename(input_file))
    df.to_csv(output_file, index=False)

def main():
    model = download_and_load_model()
    input_folder = 'PATH/TO/INTPUT/FOLDER/'
    output_folder = 'PATH/TO/OUTPUT/FOLDER/'
    os.makedirs(output_folder, exist_ok=True)

    input_files = glob.glob(os.path.join(input_folder, "*.csv"))
    for input_file in tqdm(input_files, desc="Processing Files", unit="file"):
        process_file(input_file, output_folder, model)

if __name__ == '__main__':
    main()
