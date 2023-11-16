---
search:
  boost: .9
---

# Rilutek

**ALS**

[Criteria Document](https://mygainwell-my.sharepoint.com/:w:/g/personal/kaelyn_dobbins_gainwelltechnologies_com/EQTwNvolkD9IhI-5oWcpoesB1KsdXX8ksGiq5Ez1jfhNiw?e=8AovuD){:target="_blank" rel="noopener}

<table>
<thead>
<tr class="header">
<th><strong>Criteria Title</strong></th>
<th>Benzothiazole for ALS</th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Criteria Subtitle</strong></td>
<td>Rilutek (riluzole)</td>
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
<td>RILUTEK</td>
<td>024508</td>
<td>GCNSeqNo</td>
</tr>
</tbody>
</table>

| **Sequence Number** | **Question ID** | **Default Next Question ID** | **Question Type** | **Question Text**                                                                                         | **Choice Text**             | **Next Question ID**     |
| ------------------- | --------------- | ---------------------------- | ----------------- | --------------------------------------------------------------------------------------------------------- | --------------------------- | ------------------------ |
| 1                   | 9000            |                              | Select            | Is this request being prescribed in accordance with Food and Drug Administration (FDA) approved labeling? | Y                           | 9001                     |
|                     |                 |                              |                   |                                                                                                           | N                           | 1235                     |
| 2                   | 9001            |                              | Select            | Has the medication been prescribed by or in consultation with a neurologist?                              | Y                           | END (Approve x 365 days) |
|                     |                 |                              |                   |                                                                                                           | N                           | 1235                     |
| 3                   | 1235            |                              | Free Text         | Please provide the rationale for the medication being requested.                                          | END (Pending Manual Review) |                          |

LENGTH OF AUTHORIZATION: 365 days

|||
| ------------------ | -------- |
| **Last Approved ** | 5/1/2023 |
| **Other**          |          |
