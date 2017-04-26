## System Description
RiskMetrics provides risk management metrics for any given software package. It utilizes nexB's [scancode-toolkit](https://github.com/nexB/scancode-toolkit) to scan a software package's source code for license information (i.e., how many files are licensed, what types of licenses are used, etc.). RiskMetrics also checks the provided software package’s [Common Platform Enumeration (CPE)](https://scap.nist.gov/specifications/cpe/) against the [National Vulnerability Database (NVD)](https://nvd.nist.gov). Presence in this database indicates a documented security vulnerability within the software package.

### Use Case
- _Title:_ Provide Risk Management Metrics on Software Package
- _Primary Actor:_ Open Source Contemplator (someone interested in utilizing OSS)
- _Goal in Context:_ Provide metrics for determination of risk in any given software package
- _Stakeholders:_ Open Source Contemplator, Software Package Vendor
- _Preconditions_ Software package is present in system
- _Main Success Scenario:_ Software package is analyzed and results outputted
- _Failed End Conditions:_ Software package fails to be analyzed
- _Trigger:_ Executes ./start.sh and provides software package

## Dependencies
* macOS Sierra (10.12.x)
* [Python 2.7.x](https://www.python.org/download/releases/2.7/)
* [Python 3.6.x](https://www.python.org/downloads/release/python-360/)
* [virtualenv](https://virtualenv.pypa.io/en/stable/)
* [scancode-toolkit-1.6.0](https://github.com/nexB/scancode-toolkit)

## Installation
### Mac
0. macoOS Sierra ships with Python 2.7
1. Install Python 3
   1. Install [Homebrew](http://brew.sh)
   2. In a terminal, run `brew install python3`
2. Install [virtualenv](https://virtualenv.pypa.io/en/stable/)
3. In a Terminal, set your working directory where you want to install RiskMetrics
4. In that directory, run `git clone https://github.com/hacksmath/RiskMetrics.git`
5. In a Terminal, set your working directory to the newly cloned RiskMetrics
6. In RiskMetrics, run `./setup.sh`

## Usage
0. Retrieve a software package to analyze
1. In RiskMetrics, run `./start.sh`
2. You will be prompted to enter the absolute file path to the software package
3. You will be prompted for the software package's vendor
4. You will be prompted for the software package's name
5. You will be prompted for the software package's version
6. The results will be displayed on the Terminal 

## Development Environment
Development is currently being performed on macOS Sierra and Windows 10 using Python 2.7 and 3.6. See developement setup instructions in riskmetrics for more information on how to start developing.

Those interested in contributing should contact Micah (mswab@unomaha.edu) or Kiet (khtran@unomaha.edu).

### Data Flow Diagram

![Data Flow Diagram](DFDv3.png)

### Database Schema
This section is intentionally empty as no generated data is currently being cached.

### License & Copyright Declarations

RiskMetrics source code licensed under MIT.

Documents licensed under CC BY-SA 4.0.

All work copyright © Micah Swab, Kiet Tran 2017.
