---
search:
  boost: .9
---

# Panretin

**sores caused by Kaposi sarcoma**

[Criteria Document](https://mygainwell-my.sharepoint.com/:w:/g/personal/kaelyn_dobbins_gainwelltechnologies_com/ESsK4W3sG2tPt1Jzj29GMioByLCno9xh5sexyl_S_F6GGg?e=BVkZOz){:target="_blank" rel="noopener}

## Criteria { data-search-exclude }

<table>
<thead>
<tr class="header">
<th><strong>Criteria Title</strong></th>
<th>Topical Retinoid</th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Criteria Subtitle</strong></td>
<td>Panretin (alitretinoin)</td>
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
<td>PANRETIN</td>
<td>041643</td>
<td>GCNSeqNo</td>
</tr>
</tbody>
</table>

| **Sequence Number** | **Question ID** | **Default Next Question ID** | **Question Type** | **Question Text**                                                                                               | **Choice Text**                           | **Next Question ID**     |
| ------------------- | --------------- | ---------------------------- | ----------------- | --------------------------------------------------------------------------------------------------------------- | ----------------------------------------- | ------------------------ |
| 1                   | 1233            |                              | Select            | Is this request being prescribed in accordance with Food and Drug Administration (FDA) approved labeling?       | Y                                         | 1234                     |
|                     |                 |                              |                   |                                                                                                                 | N                                         | 1235                     |
| 2                   | 1234            |                              | Select            | Is the patient new to therapy (initial authorization request) or continuing therapy (re-authorization request)? | New Start (initial authorization request) | END (Approve x 90 days)  |
|                     |                 |                              |                   |                                                                                                                 | Continuation (re-authorization request)   | END (Approve x 365 days) |
| 3                   | 1235            |                              | Free Text         | Please provide the rationale for the medication being requested.                                                | END (Pending Manual Review)               |                          |

LENGTH OF AUTHORIZATIONS: Initial authorizations will be for 90 days;
Re-Authorization requests 365 days.

|||
| ------------------ | -------- |
| **Last Approved ** | 5/1/2023 |
| **Other**          |          |
