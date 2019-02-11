import csv
import os
import sys
from tqdm import tqdm
from import_csv import InfluxDB_CSV


class InfluxDB_CSV():
  def encode_csv(self, path_files_to_encode, path_encodedfile_dir):
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
    path_output = "%s/encoded_%s" % (path_encodedfile_dir, filename)
    # Encoding UTF-8 and write rows.
    with open(path_output, "w", newline='', encoding="UTF-8") as w:
        writer = csv.writer(w)
        writer.writerows(result)


def diff_encoded(benc_dir, aenc_dir):
  # Remove .DS_Store file.
  rmf = '.DS_Store'
  if rmf in benc_dir:
    benc_dir.remove(rmf)
  if rmf in aenc_dir:
    aenc_dir.remove(rmf)
  # Convert file in dir convert to list.
  enc = os.listdir(benc_dir)
  encoded = os.listdir(aenc_dir)
  set_enc_encoded = set(enc) - set(encoded)
  set_enc_encoded = list(set_enc_encoded)
  # Messages when you don't need encode.
  if len(set_enc_encoded) is 0:
    print('Don\'t need encoding!')
  return set_enc_encoded



encode_file = '/Users/Daiki/Desktop/research/log/20180930_235959_00000026.CSV'
encode_dir = '/Users/Daiki/Desktop/research/log'
encoded_dir = '/Users/Daiki/Desktop/research/log_encoded'


# diff_encoded(encode_dir, encoded_dir)
# encode_csv(encode_file, encoded_dir)