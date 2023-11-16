---
search:
  boost: .9
---

# Nuedexta

[Criteria Document](https://mygainwell-my.sharepoint.com/:w:/g/personal/kaelyn_dobbins_gainwelltechnologies_com/Ecv_Q-iisDFErxX01OPr9wgB_rvP8oahEwrR8aC4vP8VHA?e=rUdF2e){:target="_blank" rel="noopener}

**pseudobulbar affect**

<table>
<thead>
<tr class="header">
<th><strong>Criteria Title</strong></th>
<th>Central Nervous System Agents</th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Criteria Subtitle</strong></td>
<td>Nuedexta (dextromethorphan hydrobromide / quinidine sulfate)</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Approval Level</strong></td>
<td>GCNSeqNo</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><p><strong>Products</strong></p>
<table>
<thead>
<tr class="header">
<th>Preferred</th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Non-Preferred</td>
<td></td>
</tr>
<tr class="even">
<td>Brand</td>
<td></td>
</tr>
<tr class="odd">
<td>Generic</td>
<td></td>
</tr>
<tr class="even">
<td>Other</td>
<td></td>
</tr>
</tbody>
</table></td>
<td>Drug Name</td>
<td>Corresponding Code(s)</td>
<td>Type of Code (GCNSeqNo, HICL, NDC)</td>
</tr>
<tr class="even">
<td></td>
<td>NUEDEXTA</td>
<td>066871</td>
<td>GCNSeqNo</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr class="header">
<th><strong>Sequence Number</strong> </th>
<th><strong>Question ID</strong> </th>
<th><strong>Default Next Question ID</strong> </th>
<th><strong>Question Type</strong> </th>
<th><strong>Question Text</strong> </th>
<th><strong>Choice Text</strong> </th>
<th><strong>Next Question ID</strong> </th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1 </td>
<td>0998</td>
<td> </td>
<td>Select </td>
<td><p>Is the patient new to therapy (initial authorization request) or continuing therapy (re-authorization request)?  </p>
<p>  </p></td>
<td>New Start (initial authorization request)</td>
<td>0999</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Continuation (re-authorization request)  </td>
<td>2000 </td>
</tr>
<tr class="odd">
<td>2</td>
<td>0999</td>
<td></td>
<td>Select</td>
<td>Is this request being prescribed in accordance with Food and Drug Administration (FDA) approved labeling? </td>
<td>Y</td>
<td>1000</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N</td>
<td>1235</td>
</tr>
<tr class="odd">
<td>3</td>
<td>1000</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the patient had an inadequate clinical response to a tricyclic</p>
<p>antidepressant (TCA) or a selective serotonin reuptake inhibitor (SSRI)?</p>
<p>If yes, please submit the medication trials and dates.</p></td>
<td>Y</td>
<td>1002</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N</td>
<td>1001</td>
</tr>
<tr class="odd">
<td>4</td>
<td>1001</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Does the patient have a contraindication to a tricyclic</p>
<p>antidepressant (TCA) or a selective serotonin reuptake inhibitor (SSRI)?</p>
<p>If yes, please submit the medication name and reason for inability to use.</p></td>
<td>Y</td>
<td>1002</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N</td>
<td>1235</td>
</tr>
<tr class="odd">
<td>5</td>
<td>1002</td>
<td></td>
<td><p>Select</p>
<p>and Free Text</p></td>
<td><p>Has the provider submitted documentation that patient’s baseline Center for Neurologic Study-Lability Scale (CNS-LS) score is greater than 13? </p>
<p> </p>
<p>If yes, please provide documentation. </p></td>
<td>Y</td>
<td>END (Pending Manual Review)</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N</td>
<td>1235</td>
</tr>
<tr class="odd">
<td>6</td>
<td>2000</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the provider submitted documentation of a positive response to therapy as  </p>
<p>evidenced by a decrease in the Center for Neurologic Study-Lability Scale (CNS-LS) score of at least 3 points from baseline?  </p>
<p> </p>
<p>If yes, please provide documentation. </p></td>
<td>Y</td>
<td>END (Pending Manual Review) </td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N</td>
<td>1235</td>
</tr>
<tr class="odd">
<td>7</td>
<td>1235</td>
<td></td>
<td>Free Text</td>
<td>Please provide the rationale for the medication being requested. </td>
<td>END (Pending Manual Review)</td>
<td></td>
</tr>
</tbody>
</table>

LENGTH OF AUTHORIZATIONS: Initial authorizations will be for 84 days;
subsequent authorizations will be for 365 days.

| **Last Approved** | 4/13/2023 |
| ----------------- | --------- |
| **Other**         |           |
