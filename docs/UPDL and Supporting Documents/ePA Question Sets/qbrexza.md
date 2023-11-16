---
search:
  boost: .9
---

# Qbrexza

**axillary hyperhidrosis**

[Criteria Document](https://mygainwell-my.sharepoint.com/:w:/g/personal/kaelyn_dobbins_gainwelltechnologies_com/EeXPh8Wc6ntNvwZOOej7-4cB9Mk4OVQH229czS_R9gMaOg?e=53hlr8){:target="_blank" rel="noopener}

<table>
<thead>
<tr class="header">
<th><strong>Criteria Title</strong></th>
<th>Topical - astringents / protectants</th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Criteria Subtitle</strong></td>
<td>Qbrexza (glycopyrronium)</td>
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
<td>QBREXZA</td>
<td>078624</td>
<td>GCNSeqNo</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr class="header">
<th><strong>Sequence Number</strong></th>
<th><strong>Question ID</strong></th>
<th><strong>Default Next Question ID</strong></th>
<th><strong>Question Type</strong></th>
<th><strong>Question Text</strong></th>
<th><strong>Choice Text</strong></th>
<th><strong>Next Question ID</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>1000</td>
<td></td>
<td>Select</td>
<td>Is this request being prescribed in accordance with Food and Drug Administration (FDA) approved labeling?</td>
<td>Y</td>
<td>1001</td>
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
<td>2</td>
<td>1001</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the patient had an inadequate clinical response of at least 30 days with either Drysol or Xerac-AC Solution?</p>
<p>If yes, please submit the medication trials and dates.</p></td>
<td>Y</td>
<td>1003</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N</td>
<td>1002</td>
</tr>
<tr class="odd">
<td>3</td>
<td>1002</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Does the patient have a contraindication with either Drysol or Xerac-AC Solution?</p>
<p>If yes, please submit the medication name and reason for inability to use.</p></td>
<td>Y</td>
<td>1003</td>
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
<td>4</td>
<td>1003</td>
<td></td>
<td>Select</td>
<td><p>Ohio Medicaid covers up to 30 cloths per 30 days.</p>
<p>Does this request meet this requirement?</p></td>
<td>Y</td>
<td>END (Approve x 365 days)</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N</td>
<td>1236</td>
</tr>
<tr class="odd">
<td>5</td>
<td>1235</td>
<td></td>
<td>Free Text</td>
<td>Please provide the rationale for the medication being requested. </td>
<td>END (Pending Manual Review)</td>
<td></td>
</tr>
<tr class="even">
<td>6</td>
<td>1236</td>
<td></td>
<td>Free Text</td>
<td>Please provide the rationale for the dose and frequency being requested.</td>
<td>END (Pending Manual Review)</td>
<td></td>
</tr>
</tbody>
</table>

LENGTH OF AUTHORIZATIONS: Up to 365 Days.

|||
| ------------------ | -------- |
| **Last Approved ** | 5/1/2023 |
| **Other**          |          |
