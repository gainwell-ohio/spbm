---
search:
  boost: 1
---

# COB Reference Sheet

## Coordination of Benefits

[Coordination of Benefits - COB - Billing Instructions 11.18.22.docx](https://mygainwell-my.sharepoint.com.mcas.ms/:w:/g/personal/jessica_cain_gainwelltechnologies_com/EZXs06cDYjRBosZXdgRxCXYBuEO28Mi43BDXn5z6X31tow?e=GeZWGa){:target="_blank" rel="noopener"}
  

**COB** -COB stands for Coordination of Benefits.  This is when a member has more than one plan for their pharmacy benefit.  

- If you see COB Pharmacy in VUE360RX this means, we show that the member has a primary payer.  
    - You must click the thumbnail beside the COB Pharmacy line to see the name of the primary payer.  
    - You can see the primary payers processing information (BIN/PCN/GROUP/PHONE) on the claim rejection message as well as in the response transaction to the pharmacy.  

Medicaid is usually the payer of last resort.  The **ONLY** exception is if the member has BCMH (Bureau for Children with Medical Handicaps). 

If a member has another insurance (COB Pharmacy) in VUE360RX, and the pharmacy does not bill the other insurance first, the claim will be rejected as REJECT 41 (Bill other payer). 

**If you receive a call regarding claims rejecting with edit 7011:** 

- Provide the pharmacy with the primary coverage name (shown under COB Pharmacy). 
    - Provide the pharmacy with the primary coverage BIN/PCN/Group (VUE360RX details below) 
- Ask the pharmacy to bill the primary coverage (COB Pharmacy) and Gainwell as secondary using OCC 2. 
    - If OCC 2 does work, proceed to the next step below:  
- Ask the pharmacy to bill the primary coverage (COB Pharmacy) and Gainwell as secondary using OCC 3.  
    - If the pharmacy receives an eligibility rejection from the primary (reject 65-69) the claim will still pay if it is a Medicaid covered drug using OCC 3.  
        - Document in your call note as follows: 
            - Name of the person you spoke with at the pharmacy.  
            - Documentation that you advised pharmacy to bill using OCC 3. 
            - Documentation that you provided primary payer BIN/PCN/GROUP/PHONE 
            - Documentation that a paid claim was received. 

**The pharmacy MUST bill with OCC 2, then OCC 3. These steps must be followed if the primary billing information shows in the rejection.** 

## Example Documentation:

Spoke with Mandy at the pharmacy.  Verified that primary payer processing information was provided to the pharmacy. Advised pharmacy to bill claim using OCC 3.  Verified that paid claim was received.    

- If we are unable to provide the pharmacy with the primary coverage BIN/PCN/GROUP and they are sure the member no longer has the primary coverage, then; 
    - Ask the pharmacy to bill using OCC 1.  If the pharmacy can’t/won't use OCC 1 then; 
    - Provide the Edit Override 7011. **Note – Technicians are allowed to provide this override and do NOT need to approval from a Senior Tech/Supervisor or RPh ** 
        - The E/O should be put in for up to 30 days.  
        - Document in your call note as follows: 
            - Name of the person you spoke with at the pharmacy.  
            - Documentation that you verified there was no primary payer processing information (BIN/PCN/GROUP/PHONE) on the rejected claim. 
            - Documentation that the pharmacy could not bill using OCC 1.

**Example Documentation:**

Spoke with Mandy at the pharmacy.  Verified that primary payer processing information was not available on the rejected claim.  Verified with pharmacy that they could not use OCC1.  Provided override.   

- If you were unable to see the primary payers BIN/PCN/GROUP in the rejection message in VUE360RX reach out to the eligibility chat providing the information in the below template so that the eligibility can be researched.  
    - Member ID# 
    - Member Name 
    - Member DOB 
    - Claim ID#

## Definitions

OPAP – **Other Payer Amount Paid** -This is the amount that the primary payer paid towards the claim. 

OPPRA – **Other Payer Patient Responsibility Amount** -This is the dollar amount left over from the primary payer and the amount that is being billed to Ohio Medicaid.

OPRC- **Other Payer Reject Code** – These are the reject codes returned on the claim when the primary payer rejects the claim.  

## COB Scenario 3 Pharmacy Assistance  

If a pharmacy states that they need assistance billing an Ohio Medicaid plan as secondary (meaning the member has primary coverage other than Ohio Medicaid) please advise the pharmacy to use one of the below Other Coverage Codes (OCC) depending on the situation: 

- **OCC 0** – A pharmacy would use Other Coverage Code 0 (OCC 0) if the member ONLY has Ohio Medicaid  
- **OCC 1** – A pharmacy would use Other Coverage Code (OCC 1) when the primary coverage on file for the patient is no longer active.  
- **OCC 2** – A pharmacy would use other coverage code 2 (OCC 2) if they have billed the primary insurance and the primary insurance pays. 
- **OCC 3** – A pharmacy would use other coverage code 3 (OCC 3) if they have billed the primary insurance and the primary insurance rejects the claim.   In this instance, Ohio Medicaid will only coverage the claim if it is an Ohio Medicaid covered drug AND the primary plan rejects with one of the following rejects: 
    - A5 
    - MR 
    - 65-69 (eligibility rejects) 
    - 70 

    **NOTE** If the rejection code is NOT one of the above codes, it will reject as NCPDP Reject code: 6E – M/I Other Payer Reject Code and the pharmacy would need to reach out to the primary payer for resolution.  

- **OCC 4** – A pharmacy would use other coverage code 4 (OCC 4) if they have billed the primary insurance and the primary insurance pays the claim (does not reject) but pays $0.00.   This typically happens because the member has a deductible to meet before the primary insurance will pay the claim.

*If you receive a call from the member or a managed care plan, suggest that they have the pharmacy reach out to Gainwell for assistance with billing the claim.   

**If the member or managed care plan states that the pharmacy refused to call us, please place them on hold, make an outbound call to the pharmacy and walk them through processing the claim.  

## TPL Billing Information Examples: 

On the rejected claim, you can see the primary payer's information shown below:

![Alt text](COB%20Reference3.png)

On the members profile, you can also provide the member's identification number shown below under the Health Plan ID.

![Alt text](COB%20Reference1.png)

You can also find the TPL billing information by reviewing the "Response Detail"

![Alt text](COB%20Reference2.png)

If you do not see the primary payers billing information, this is when you reach out to the eligibility chat.

**Additional examples:**

Member ID: 106046028299 

Member ID: 910001561387 

Member ID: 106959440499 

Member ID: 107006264999 

Member ID: 184588168703 

Member ID: 184373757604 

Member ID:  784015775903 

Member ID:  254475279904 

example
