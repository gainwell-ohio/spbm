---
search:
  boost: 1
---

# Navigating COB Rejects

1. Prescription rejects for member having another primary insurance (7011 edit). 

2. Instruct pharmacy to bill the primary insurance BIN, PCN and ID (enrollment ID shown next to primary) that shows up in a rejection as the primary insurance and Gainwell as secondary 

3. Once the primary is billed and the claim rejects, see the following rejection codes and next steps: 

| Reject | Definition | Send Email | Next Steps |
| :--- | :--- | :--- | :--- |
| A5 | Med not covered (Medicare) | NO | Pharmacy should bill with OCC 3. If Medicaid covered drug/supply, claim will pay |
| MR | Med not on formulary for primary | NO | Pharmacy should bill with OCC 3. If Medicaid covered drug/supply, claim will pay |
| 65, 66, 67, 68, 69 | Shoes coverage inactive | YES | Send email to Eligibility email using template. |
| 70 | Med not covered under primary | NO | Pharmacy should bill with OCC 3. If Medicaid covered drug/supply, claim will pay. |
| 75 | Primary needs PA for medication | NO | Primary must be contacted to resolve their rejection. |
| 76 | Primary Ins limits quantity | NO | Primary must be contacted to resolve their rejection. |
| 6E | Rejecting with Primary | NO | Primary must be contacted to resolve their rejection. |

- When to EO 7011
- NEVER EO Medicare eligible rejects   
- When BIN and PCN does not show in rejection, ask pharmacy to bill with OCC 1. 
    - If pharmacy states they cannot use OCC 1, OK to EO 7011 + OK to send email to eligibility. 
