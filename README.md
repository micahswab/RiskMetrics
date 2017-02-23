### System Description
GHRiskMetrics is a planned contribution to GHData that will provide metrics such as source code licenses and potential code vulnerabilities. It will connect to Nomos, the license scanner behind FOSSology, to gather detailed license information on GitHub repositories. GHRiskMetrics will also calculate the provided software package’s Common Platform Enumeration (CPE) and check to see if it is found in the National Vulnerability Database (NVD).


### Development Environment
Development is being performed in Python.
Project collaborators can commit freely. But please keep the other collaboarators in the loop for big changes.
Non-collaborators interested in contributing should contact Micah (mswab@unomaha.edu) or Kiet (ktran@unomaha.edu)

### Database Schema

| RiskMetrics Table | Data Type     |
| ----------------- | ------------- |
| Repository        | varchar(n)    |
| CPE               | varchar(n)    |
| Vulnerable        | boolean       |
| NumLicenses       | integer       |
| NumFilesLicensed  | integer       |

### Data Flow Diagram

![alt tag](DFD.png)

### License & Copyright Declarations

Source code licensed under MIT.

Documents licensed under CC BY-SA 4.0.

All work copyright © Micah Swab and Kiet Tran 2017.
