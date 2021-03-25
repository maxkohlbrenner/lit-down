import wget
import pandas as pd
import argparse
from os import path, mkdir

def main():

    # parsing
    parser = argparse.ArgumentParser()
    parser.add_argument("literature_filepath")
    args = parser.parse_args()
    # ------------------------------------

    literature_path = args.literature_filepath
    if not literature_path.endswith('.csv') or not path.exists(literature_path):
        print('ERROR: literature_filepath needs to specify a valid .csv file')
        return

    # path handling, create the folder
    literature_basename = literature_path.split('/')[-1].split('.csv')[0]
    working_dir    = path.dirname(literature_path)
    literature_dir = path.join(working_dir, literature_basename)
    if not path.exists(literature_dir):
        mkdir(literature_dir)


    lit_df = pd.read_csv(literature_path)
    nrows = lit_df.shape[0]
    for i, (index, row) in enumerate(lit_df.iterrows()):
        print('{}/{}'.format(i+1, nrows))
        name, url = row['name'], row['url']
        pdfpath = path.join(literature_dir, '{}.pdf'.format(name))
        if not path.exists(pdfpath):
            try:
                wget.download(url, pdfpath)
            except Exception as e:
                print('... error: {}'.format(e))
        else:
            print('{} already exists, skip'.format(name).format(name))

    print('...finished')

if __name__ == "__main__":
    main()
