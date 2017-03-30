# Development Setup
## Mac
- Install brew from http://brew.sh
- 'brew install python3'
- Create virtualenv 'virtualenv env'
- Activate virtualenv 'source env/bin/activate'
- Install dependencies 'pip install -r requirements.txt'
- Update local NVD 'python mirror_nvd.py'
- Search for software package vulnerability 
  'python vulnerable.py <vendor_name> <product_name> <version>'

## Linux
- Create virtualenv 'virtualenv env'
- Activate virtualenv 'source env/bin/activate'
- Install dependencies 'pip install -r requirements.txt'
- Update local NVD 'python mirror_nvd.py'
- Search for software package vulnerability 
  'python vulnerable.py <vendor_name> <product_name> <version>'
