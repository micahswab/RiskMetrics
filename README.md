### System Description
GHRiskMetrics is a planned contribution to [GHData](https://github.com/OSSHealth/ghdata) that will provide metrics such as source code licenses and potential code vulnerabilities. It will connect to Nomos, the license scanner behind [FOSSology](https://www.fossology.org), to gather license information on the code within a GitHub repository. GHRiskMetrics will also calculate the provided software package’s [Common Platform Enumeration (CPE)](https://scap.nist.gov/specifications/cpe/) and check to see if it is found in the [National Vulnerability Database (NVD)](https://nvd.nist.gov). Its presence in this database could indicate a documented security vulnerability with the software package.


### Development Environment
Development is currently being performed on macOS 10.12.3 and Windows 10 using Python 3.6.0. This GHData feature will not rely on the GHTorrent database, only the additional RiskMetrics Table to store collected metrics.
Project collaborators can commit freely. But please keep the other collaboarators in the loop for big changes.
Non-collaborators interested in contributing should contact Micah (mswab@unomaha.edu) or Kiet (khtran@unomaha.edu)

### Database Schema

The following table is a required addition to the [GHTorrent](http://ghtorrent.org/downloads.html) database utilized by GHData for the GHRiskMetrics feature.

| RiskMetrics Table | Data Type     |
| ----------------- | ------------- |
| ID*               | integer       |
| Repository        | varchar(n)    |
| CPE               | varchar(n)    |
| Vulnerable        | boolean       |
| NumLicenses       | integer       |
| NumFilesLicensed  | integer       |
| Time_Collected    | datetime      |

\* indicates primary key

### Data Flow Diagram

![Data Flow Diagram](data_flow_diagram.png)

### License & Copyright Declarations

Source code licensed under MIT.

Documents licensed under CC BY-SA 4.0.

All work copyright © Micah Swab and Kiet Tran 2017.

### License Scanner instructions :
Go to the md file instruction to use license scanner. It will help you how to use it perfectly
