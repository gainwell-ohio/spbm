---
search:
  boost: .9
---

# Stimate

[Criteria Document](https://mygainwell-my.sharepoint.com/:w:/g/personal/kaelyn_dobbins_gainwelltechnologies_com/Edq6qd7aQMlMolG7W7eT1loB12CcmysVuZaLwcAms36-9g?e=d6bLg2){:target="_blank" rel="noopener}

**von Willebrand's disease, hemophilia A**

|            |                                                  |
| ---------- | ------------------------------------------------ |
| Criteria 1 | Stimate (von Willebrand's disease, hemophilia A) |

  

<table>
<thead>
<tr class="header">
<th><strong>Criteria Title</strong></th>
<th>Nasal synthetic vasopressin analogue</th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Criteria Subtitle</strong></td>
<td>Stimate (desmopressin acetate)</td>
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
<td>Corresponding Code (s)</td>
<td>Type of Code (GCNSeqNo, HICL, NDC)</td>
</tr>
<tr class="even">
<td></td>
<td>STIMATE</td>
<td>022139</td>
<td>GCNSeqNo</td>
</tr>
</tbody>
</table>

  

<table>
<thead>
<tr class="header">
<th><strong>Sequence Number</strong>  </th>
<th><strong>Question ID</strong>  </th>
<th><strong>Default Next Question ID</strong>  </th>
<th><strong>Question Type</strong>  </th>
<th><strong>Question Text</strong>  </th>
<th><strong>Choice Text</strong>  </th>
<th><strong>Next Question ID</strong>  </th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1  </td>
<td>1001  </td>
<td>  </td>
<td>Select  </td>
<td><p>Is the patient new to therapy (initial authorization request) or continuing therapy (re-authorization request)?   </p>
<p> </p></td>
<td>New Start (initial authorization request)</td>
<td>1002 </td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Continuation (re-authorization request)     </td>
<td>1234</td>
</tr>
<tr class="odd">
<td>2  </td>
<td>1002  </td>
<td></td>
<td>Select  </td>
<td>Is this request being prescribed in accordance with Food and Drug Administration (FDA) approved labeling?    </td>
<td>Y  </td>
<td>1003 </td>
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
<td>3  </td>
<td>1003  </td>
<td>  </td>
<td>Select and Free Text  </td>
<td>Has the provider submitted documentation of a Stimate challenge test performed prior to initiation of therapy?</td>
<td>Y  </td>
<td>END (Approve x 30 days)</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N  </td>
<td>1235 </td>
</tr>
<tr class="odd">
<td>4</td>
<td>1234  </td>
<td></td>
<td>Select and Free Text  </td>
<td><p>Has the provider submitted documentation of clinical response?</p>
<p> </p></td>
<td>Y  </td>
<td>END (Approve x 365 days) </td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N  </td>
<td>1235 </td>
</tr>
<tr class="odd">
<td>5</td>
<td>1235  </td>
<td>  </td>
<td>Free Text  </td>
<td>Please provide the rationale for the medication being requested.   </td>
<td>END (Pending Manual Review) </td>
<td></td>
</tr>
</tbody>
</table>

LENGTH OF AUTHORIZATIONS: Initial authorizations will be for 30 days;
Subsequent authorizations will be for 365 days 

| **Last Approved ** | 4/13/2023 |
| ------------------ | --------- |
| **Other**          |           |
