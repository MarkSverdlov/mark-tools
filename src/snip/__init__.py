import pandas as pd
import argparse


def main():
    parser = argparse.ArgumentParser(description="Process Vim snippets.")
    parser.add_argument("key", type=str, help="The key to search for in the snippets.")
    args = parser.parse_args()

    docs = pd.read_csv("~/.vim/docs/snippets.doc", sep=' ', header=None, escapechar='\\')
    docs = docs.iloc[:, 1:]
    docs.columns = ['snippet', 'description', 'options']
    results = docs[docs['description'].str.contains(args.key, case=False)]
    print(results[['snippet', 'description']].set_index('snippet'))

