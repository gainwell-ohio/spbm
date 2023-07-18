---
search:
  boost: 1
---

# Payment Status

![Alt text](Pay%20Status%20Descriptions.png)




# Additional Payment Status

**ADJUDICATED**
The claim has run through initial review of business rules and applied edits but has not been ok’d to pay/approved for payment. A user would only see the ADJUCATED status if they are manually adjudicating a claim. If the claim goes through mass adjudication, it will either be PAY or DENY.

**DENIED**
The claim has failed business rules and has gone through the payment process.

**DENY**
The claim has failed header and/or line-level business rules and has not been submitted to the payment process.

**PAID**
The claim has been finalized and has gone through the payment process.

**PAY**
The claim has been adjudicated and all edits have been satisfied. It is now ready to go through the payment process.

**PEND**
The claim has been set aside for review to determine if it should be paid or denied.

**RCLPAID**
RCL means reclassification. Claim was adjusted as part of a financial process to change the fund used to pay the claim. The adjustment claim has completed the financial cycle, and is finalized.

**RCLRVRSD**
RCL means reclassification. The claim has been reversed as part of a financial process to change the fund used to pay the claim. As a rule, the payment amount does not change, and the process is invisible to the provider.

**RCLWAITPAY**
RCL means reclassification. The claim has been adjusted as part of a financial process to change the fund used to pay the claim, and is currently going through the financial cycle.

**RCLWAITREV**
RCL means reclassification. The claim has been reversed as part of a financial process to change the fund used to pay the claim, and is currently going through the financial cycle.

**REV**
The claim is part of a correction process for a PAID claim where incorrect benefits were issued. The REV claim is a mirror image of the PAID claim with negative values. When the REV claim goes through the payment process, it ensures that the erroneous payment is backed out of the provider payment and that the reversal is reflected on the remittance advice. In most cases, a claim in REV status has a corresponding adjustment claim where benefits are recalculated and reissued.

**REVSYNCH**
The working environment has the option to synchronize reversal, and the adjustment claims configuration option is set to Yes. During claim reversal, the user has indicated that payment should be synchronized for the reversed claim and the adjustment claim, which updates the claim's status to REVSYNCH so that the claim will be withheld from payment until the associated adjustment claims have been released. REVSYNCH claims will be automatically released for payment when the adjustment claims are in PAY or DENY status. A REVSYNCH claim will be released for payment when its status is reverted to REV.

**REVERSED**
The claim has been finalized. Checks have been printed and the payment process is complete, but errors have been identified and a mirror image of the claim has been created to correct the errors.

**WAITDENY**
The claim has failed business rules and has been submitted for payment, but the payment process is not complete. The status will move to DENIED when the payment process is complete. Claims in this status will be locked from any further edits.

**WAITPAY**
The claim has been approved for payment and submitted to the payment process, but that process has not yet been completed. When the process finishes, the status will change to PAID. Claims in this status will be locked from any further edits.

**WAITREV**
A reversal claim has been created and submitted to the payment process, but that process is not yet complete.

**WARN**
An informational message that does not affect claim payment or denial.

 
