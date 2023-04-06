# Missing Image on PA

[Missing Image Email :material-email:](https://mygainwell-my.sharepoint.com/:u:/r/personal/christopher_nguyen_gainwelltechnologies_com/Documents/Evergreen/Emails/RE_%20INC0022507%20can%20be%20resolved_closed.msg?csf=1&web=1&e=YYwVet){ .md-button .md-button--primary target="_blank" rel="noopener"}

Also, 

Prior to finalizing the process we need to put a drug in for the blank medication to cancel.

There is no dummy NDC to put in there for a canellation, but usually we can get a dx code from OCR, possibly making an educated guess with while looking at claims and PA history to enter in anything to just cancel.

For example one has a diagnosis of migraines and there are rejections for a Nurtec, it may be a pretty good chance that the drug being requested is Nurtec
 
The cancelation language can be adjusted to reflect this:

**Drug XXXXXX was selected due to not knowing exactly what medication is being requested. This PA seems to be created by OCR lacking an image to further process and must be cancelled.**
 
 
If there are issues with prescribers/pharmacies calling in to check on status of a PA, if they are aware of the date and time we can surmise this is the best option until OCR makes the new image to process.

I realize this isn’t the most surefire process to get these going, but I believe is the best option at this moment to get them out of workflow and reprocessed.
 
Thanks again and sorry for the multiple emails, if any questions please ask

Thanks,

Justin

From: Collingwood, Justin

To: Holsapple, Rich

Hello

This outage thing seems to be a frequent occurrence since go live so I propose for out current situation and future outages:

1. If we receive a PA indicating fax but no image attached check to see how received, FISOCRPA or a human
- If human, contact the person through teams to inquire if this was indeed a fax, a call, if they used the call template, any information to be garnered
- If FISOCRPA, it is likely an outage issue
 
FISOCRPA creates PAs by reading the bar codes on the forms and then automatically creates a PA to be processed. It seems that from what is discussed below that if it is not able to generate an image the PDF will be sent to the fax queue to be processed.

How we can tell if this is happening is that if a PA is generated but no image from FISOCRPA ANDthe drug portion is missing due to OCR not able to read it, then there is more than likely an outage issue and the PDF was sent to fax que. We can not search fax que at this time unfortunately, but this is more than likely what is happening.

**Please note that the above situation will happen with almost all drugs EXCEPTthose with specific forms OCR knows is for the drug in question programmed that way, like Omnipod and Synagis, those drugs will show in the instance of a PA being generated with no image due to OCR “knowing” by bar code that is what should go in there**
 
After discussing with Rich since this is the information we can go on and we do not want to go past the 24 mark waiting and to limit extra work if we get Prior Authorizations that fit the OCR outage description above, we are to cancel these imageless PAs.

We can not work them due to not being able to trust the lacking information, we can not trust the fax/phone number to respond to due to HIPAA reasons, we must cancel them to remove them from the workflow believing what is described below that an image will be created.
 
Also if we cancel them and a call is received where someone is questioning we are able to look up and take notes on the canceled one for future reference.
 
**When canceling I would use verbiage like:**

This PA seems to be created by OCR lacking an image to further process and must be cancelled.
 
If any questions or any odd FISOCRPA things going on, please feel free to ask
 
Thanks,

Justin 

