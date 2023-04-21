---
search:
  boost: 1
---

# Fax View

This information is intended to give rules on how to approach fax view and the best practice to reduce the number of PAs that incorrectly make it into the PA queue.

## Types of requests that can be received in fax view: 

- New Requests 
- Re-auth Requests 
- Dose Increases 
- Duplicate Requests 
- Same Drug Different strengths 
- Invalid Requests 

## Workflow for Fax Queue Agents

(03/01/23) Moving forward, the workflow for the fax queue agents will be to:

- 1st- work the fax queue until there are no more faxes 
- 2nd- when there are no more faxes, add drug names 
- 3rd- when there are no more drug names to be added, work PAs 

| | |
| :--- | :--- |
| New Requests | New requests include any medication that a PA has not been approved for that medication in the past 365 days. |
| Re-Auth Requests | Re-Auth requests are for any medication that has been approved in the past 365 days, These should only be loaded IF current request expires in the next 30 calendar days. If the current PA does not expire in the next 30 calendar days the tech should reject this PA and send an fax back through open text of the current approved PA fax. |
| Dose Increases | Dose increase requests are any request where there is currently an approved PA but the prescriber is increasing what the member is taking. Since the system does not allow more than 1 PA under the same NDC, GCN or HicL this is the only situation where the Gelatin capsules drug name and GCN should be used. The reason we use it is because we do not want to cancel or close the existing PA without promise that the new one gets approved. 
| Duplicate Requests | Duplicate Requests is any request for an already approved PA for the same strength, dose, and day supply that is already approved. When a request like this is received they should not be loaded and instead rejected and a fax of the approval letter we have on file should be sent out via open text. |
| Same Drug, Different Strengths | Same drug different strengths is an example of when a member needs two different doses of the same ingredient IE member needs two different strengths of Adderall or a Hemophilia medication. Since the system does not allow the duplicate PA’s of the same GCN or NDC we will load these by using the Hicl. Using the Hicl allows the PA to get approved and all needed strengths will pay. |
| Invalid Requests | Invalid requests are any fax that is: Incomplete, on the wrong form, using the incorrect ID number ect. With these requests we are to reject from fax view and fill out the corresponding reject fax template found on the OneNote to use and send to the prescriber. |
