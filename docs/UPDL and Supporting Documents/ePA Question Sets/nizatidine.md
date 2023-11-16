---
search:
  boost: .9
---

# Nizatidine

**stomach ulcers**

[Criteria Document](https://mygainwell-my.sharepoint.com/:w:/g/personal/kaelyn_dobbins_gainwelltechnologies_com/EVmMMWy9u1lNtaOi8T4bhn8BTT7LlI2Z3U_NjYz36ytT2A?e=2xHDJl){:target="_blank" rel="noopener}

<table>
<thead>
<tr class="header">
<th><strong>Criteria Title</strong> </th>
<th>H-2 Antagonist</th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Criteria Subtitle</strong> </td>
<td>Nizatidine</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Approval Level</strong> </td>
<td>GCNSeqNo </td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><p><strong>Products </strong> </p>
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
<td>Drug Name  </td>
<td>Corresponding Code (s) </td>
<td>Type of Code (GCNSeqNo, HICL, NDC) </td>
</tr>
<tr class="even">
<td></td>
<td>NIZATIDINE</td>
<td>011679</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>NIZATIDINE</td>
<td>011680</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>NIZATIDINE</td>
<td>057867</td>
<td>GCNSeqNo</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr class="header">
<th><strong>Sequence Number </strong></th>
<th><strong>Question ID </strong></th>
<th><strong>Default Next Question ID </strong></th>
<th><strong>Question Type </strong></th>
<th><strong>Question Text </strong></th>
<th><strong>Choice Text </strong></th>
<th><strong>Next Question ID </strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1 </td>
<td>0997</td>
<td></td>
<td>Select </td>
<td><p>Is the patient new to therapy (initial authorization request) or continuing therapy (re-authorization request)?  </p>
<p>  </p></td>
<td>New Start (initial authorization request)</td>
<td>0998</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Continuation (re-authorization request)  </td>
<td>1233</td>
</tr>
<tr class="odd">
<td>2</td>
<td>0998</td>
<td></td>
<td>Select </td>
<td>Is this request being prescribed in accordance with Food and Drug Administration (FDA) approved labeling?  </td>
<td>Y </td>
<td>0999</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N </td>
<td>1235 </td>
</tr>
<tr class="odd">
<td>3</td>
<td>0999</td>
<td></td>
<td>Select </td>
<td>Is the patient’s condition clinically unstable or was nizatidine initiated in hospital to treat a gastrointestinal (GI) bleed or other serious acute condition? </td>
<td>Y  </td>
<td>1002</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N  </td>
<td>1000</td>
</tr>
<tr class="odd">
<td>4</td>
<td>1000 </td>
<td> </td>
<td>Select and Free Text</td>
<td><p>Has the patient had an inadequate clinical response to at least 30 days with one preferred drug in the past 90 days?</p>
<p>If yes, please submit the medication trials and dates.</p></td>
<td>Y </td>
<td>1002</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N </td>
<td>1001</td>
</tr>
<tr class="odd">
<td>5</td>
<td>1001</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Does the patient have a contraindication with one preferred drug?</p>
<p>If yes, please submit the medication name and reason for inability to use. </p></td>
<td>Y   </td>
<td>1002</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N   </td>
<td>1236 </td>
</tr>
<tr class="odd">
<td>6</td>
<td>1002</td>
<td></td>
<td>Select</td>
<td>What is the patient’s diagnosis?  </td>
<td>Duodenal ulcer </td>
<td>END (Approve x 365 days)</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Other</td>
<td>END (Approve x 84 days)</td>
</tr>
<tr class="odd">
<td>7</td>
<td>1233</td>
<td></td>
<td>Select and Free Text  </td>
<td>Has the provider submitted documentation of the patient’s clinical response to treatment and ongoing safety monitoring?</td>
<td> Y    </td>
<td>1234  </td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N    </td>
<td>1235 </td>
</tr>
<tr class="odd">
<td>8</td>
<td>1234</td>
<td></td>
<td>Select</td>
<td>What is the patient’s diagnosis?  </td>
<td>Duodenal ulcer </td>
<td>END (Approve x 365 days)</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Other </td>
<td>END (Approve x 84 days)  </td>
</tr>
<tr class="odd">
<td>9</td>
<td>1235</td>
<td></td>
<td>Free Text</td>
<td>Please provide the rationale for the medication being requested. </td>
<td>END (Pending Manual Review)</td>
<td></td>
</tr>
<tr class="even">
<td>10</td>
<td>1236</td>
<td></td>
<td>Free Text</td>
<td>Please explain the reason(s) why the patient is unable to use medications not requiring prior approval.</td>
<td>END (Pending Manual Review)</td>
<td></td>
</tr>
</tbody>
</table>

LENGTH OF AUTHORIZATION: Authorizations will be for 84 days unless
diagnosis is duodenal ulcer. 

| **Last Approved ** | 4/20/2023 |
| ------------------ | --------- |
| **Other**          |           |
