# SPDX-License-Identifier: MIT

import sys, json, os, re, requests
import nvd, scancode

from glob import glob
from os import path, remove
from subprocess import call
from collections import OrderedDict
from shutil import rmtree

def main(argv):

    if len(argv) <= 1:
        print("Usage: ./riskmetrics.py <github-repo-url>")
        exit(2)
    
    repo_url = argv[1]
    repo_info = re.search(r'github\.com/([^/]+)/([^/]+)', repo_url)

    if repo_info is None:
        print("Unable to parse url: %s" % repo_url)
        exit(1)

    owner = repo_info.group(1)
    repo = repo_info.group(2)
    version = get_latest_version(owner, repo)

    cpe1 = construct_cpe(owner, repo, version)
    cpe2 = construct_cpe(repo, repo, version)

    nvd.update()

    vulnerable = nvd.search(cpe1)
    if vulnerable is False:
        vulnerable = nvd.search(cpe2)

    download_repo(owner, repo)
    repo_dir = glob(owner + '-' + repo + '*')[0]

    scancode.install()
    scancode.scan(repo_dir)

    rmtree(repo_dir)

    data_json = json.loads('{"results" : "none"}')

    parent_dir = path.dirname(path.realpath(__file__))
    directory = str(path.dirname(parent_dir))
    print (directory)
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('info.json'):
                with open(path.join(subdir, file),'r') as f:
                    data_json = json.load(f)

    all_licenses = data_json['results']
    if all_licenses == "none":
        print ('Failed to scan package. Exiting.')
        exit(1)

    count_empty_file = 0
    for element in all_licenses:
        if (element['licenses'] == []):
            count_empty_file = count_empty_file + 1

    count_file_with_license = data_json['resource_count'] - count_empty_file

    list_license = []
    for _ in item_generator(data_json,"short_name"):
        list_license.append(_)

    list_license.sort()

    data = {
        "Number of files with a license" : count_file_with_license,
        "Number of files without a license" : count_empty_file,
        "Types of licenses" : list(OrderedDict.fromkeys(list_license)),
        "CPE located in NVD" : vulnerable
    }

    metrics = json.dumps(data, indent = 2)

    remove('info.json')

    display(metrics)


def item_generator(json_input, lookup_key):
    """
    Find key item in nested dictionary.

    Args:
        json_input (dict): Dictionary in which to find key.
        lookup_key (str): The key to look for in the dictionary.
    """
    if isinstance(json_input, dict):
        for k, v in json_input.iteritems():
            if k == lookup_key:
                yield v
            else:
                for child_val in item_generator(v, lookup_key):
                    yield child_val
    elif isinstance(json_input, list):
        for item in json_input:
            for item_val in item_generator(item, lookup_key):
                yield item_val


def download_repo(owner, repo):
    """
    Download the specified github repo.

    Args:
        owner (str): The owner of the repo.
        repo (str): The name of the repo.
    """
    r = requests.get("https://api.github.com/repos/" + 
                           owner + "/" + repo + "/tarball")
    tarball = repo + '.tar.gz'

    with open(tarball, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=1024):
            fd.write(chunk)

    call(['tar', '-xzvf', tarball])
    remove(tarball)


def get_latest_version(owner, repo):
    """
    Find the version of the repo's latest published release.

    Args:
        owner (str): The owner of the repo.
        repo (str): The name of the repo.

    Returns:
        str: The version of the latest published release of the repo, or the 
             empty string if no version is found. 
    """
    response = requests.get("https://api.github.com/repos/" + 
                            owner + "/" + repo + "/releases/latest")
    try:
        release = response.json()
        found = re.search(r'([\d.]+)', release['tag_name'])
        if found is None:
            found = re.search(r'([\d.]+)', release['name'])
            if found is None:
                print("Unable to find version of latest release...")
                version = ""
        version = found.group(1)
    except:
        print("Unable to retrieve latest published release...")
        version = ""
    return version


def construct_cpe(vendor, product, version):
    """
    Construct a Common Platform Enumeration (CPE) for a given software.

    Args:
        vendor (str): The vendor name of the software.
        product (str): The product name of the software.
        version (str): The software version.

    Returns:
        str: The constructed CPE. 
    """
    return 'cpe:/a:' + vendor + ':' + product + ':' + version


def display(metrics):
    """
    Display the risk metrics created on the repo to stdout.

    Args:
        metrics (dict): The risk metrics on the repo.
    """
    print ('\nResults:\n')
    print (metrics)
    print ('\nNotes:\n')
    print ('* A Common Platform Enumeration (CPE) in the National Vulnerability Database (NVD)')
    print ('  is not necessarily indicitive of a vulnerable project, nor is a CPE not in the NVD') 
    print ('  indicitive of a secure project.\n')
    print ('* License information gathered using the scancode-toolkit-1.6.0 from nexB.\n')


if __name__ == "__main__":
    main(sys.argv)

