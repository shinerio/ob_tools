import sys
import os
import re
import argparse

from oss_client import oss_client

all_img = {}

def parse_args():
    parse = argparse.ArgumentParser(description='markdown convertor')
    parse.add_argument('--vaultpath', type=str)
    parse.add_argument('--input', type=str)
    parse.add_argument('--outputpath', type=str)
    parse.add_argument('--attachment', type=str)
    args = parse.parse_args()
    return args


def get_all_attachment(path):
    files = os.listdir(path)
    for file in files:
        fi_d = os.path.join(path, file)
        if os.path.isdir(fi_d):
            get_all_attachment(fi_d)
        elif file.lower().endswith(('svg', '.gif', '.png', '.jpg', '.jpeg')):
            all_img[file.split('.')[0]] = os.path.join(path, fi_d)


if __name__ == '__main__':
    args = parse_args()
    input = args.vaultpath + args.input
    output = args.outputpath + args.input
    attachment = args.vaultpath + args.attachment
    get_all_attachment(attachment)
    link_re = re.compile('!\[\[.*\]\]')
    oss_client = oss_client()
    output_lines = []
    with open(input, 'r') as f:
        for line in f.readlines():
            all_links = set(link_re.findall(line))
            for link in all_links:
                if all_img[link[3:-2]]:
                    url = oss_client.put(all_img[link[3:-2]])
                    line = '![' + link[3:-2] + '](' + line.replace(link, url) + ')'
            output_lines.append(line)
    if not os.path.exists(os.path.dirname(output)):
        os.makedirs(os.path.dirname(output))
    with open(output, 'w') as f:
        for line in output_lines:
            f.write(line)
