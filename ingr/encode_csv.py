import csv
import os
import sys
from tqdm import tqdm

# Difference benc_dir to aenc_dir, Return result to list.
def diff_encoded(benc_dir, aenc_dir):
  # Convert file in dir convert to list.
  enc = os.listdir(benc_dir)
  encoded = os.listdir(aenc_dir)
  # Difference between enc to encoded.
  set_enc_encoded = set(enc) - set(encoded)
  set_enc_encoded = list(set_enc_encoded)
  # Messages when you don't need encode.
  if len(set_enc_encoded) is 0:
    print('Don\'t need encoding!')
  return set_enc_encoded

# Create a folder to save the encoded file.
def encode_mkdir(dir_path):
  try:
    os.mkdir(dir_path)
  except FileExistsError:
    print('%sを作成できませんでした、既存であるか既に使われている名前です。' % dir_path)
  return None

# Encode the path_files_to_encode, and save this in path_encodedfile_dir
def encode_csvfile(path_files_to_encode, path_encodedfile_dir):
  try:
      # Open the file to encode.
    with open(path_files_to_encode, "r", newline='', encoding="shift_jis") as r:
        content = csv.reader(r)
        result = list(content)
        for row in content:
            result.append(row)
        # Delete 2 rows.
        del result[:2]
    # Set output files name.
    filename = os.path.basename(path_files_to_encode)
    path_output = os.path.join(path_encodedfile_dir, filename)
    # path_output = "%s/%s" % (path_encodedfile_dir, filename)
    # Encoding UTF-8 and write rows.
    with open(path_output, "w", newline='', encoding="UTF-8") as w:
          writer = csv.writer(w)
          writer.writerows(result)
    return None
  except UnicodeDecodeError:
    print('文字コードエラーで%sをエンコードできませんでした。' % path_files_to_encode)

# Main Encode Program.
def encode_csv(benc_dir, aenc_dir):
  encode_mkdir(aenc_dir)
  # Remove extra file in directory.
  rmf = '.DS_Store'
  if rmf in os.listdir(benc_dir):
    os.remove(os.path.join(benc_dir, rmf))
  if rmf in os.listdir(aenc_dir):
    os.remove(os.path.join(aenc_dir, rmf))
  encode_list = tqdm(diff_encoded(benc_dir, aenc_dir))
  # encoded_mkdir(aenc_dir)
  for benc_list in encode_list:
    benc_list = os.path.join(benc_dir, benc_list)
    encode_csvfile(benc_list, aenc_dir)
  return None

# For example...
# encode_csv('/Users/Daiki/Desktop/research/log','/Users/Daiki/Desktop/research/log_encoded2')