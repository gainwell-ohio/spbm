---
search:
  boost: .9
---

# Signifor, Signifor LAR

**Cushing's disease**

[Criteria Document](https://mygainwell-my.sharepoint.com/:w:/g/personal/kaelyn_dobbins_gainwelltechnologies_com/EZs-CWcWfq9Hu8ErFysoK2YBGvcKf5XN0ZmG4VKk4N-lyA?e=WyCUd9){:target="_blank" rel="noopener}

<table>
<thead>
<tr class="header">
<th><strong>Criteria Title</strong></th>
<th>Somatostatin Analogue</th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Criteria Subtitle</strong></td>
<td>Signifor (pasireotide), Signifor LAR (pasireotide)</td>
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
<td>SIGNIFOR</td>
<td>070367</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>SIGNIFOR</td>
<td>070368</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>SIGNIFOR</td>
<td>070369</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>SIGNIFOR LAR</td>
<td>073222</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>SIGNIFOR LAR</td>
<td>073223</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>SIGNIFOR LAR</td>
<td>073224</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>SIGNIFOR LAR</td>
<td>078783</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>SIGNIFOR LAR</td>
<td>078784</td>
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
<td>1</td>
<td>0999</td>
<td></td>
<td>Select</td>
<td>Which medication is being requested?</td>
<td>Signifor (pasireotide)</td>
<td>1000</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Signifor LAR (pasireotide)</td>
<td>3000</td>
</tr>
<tr class="odd">
<td>2</td>
<td>1000</td>
<td></td>
<td>Select</td>
<td><p>Is the patient new to therapy (initial authorization request) or continuing therapy (re-authorization request)?  </p>
<p>  </p></td>
<td>New Start (initial authorization request)</td>
<td>1001</td>
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
<td>3</td>
<td>1001</td>
<td></td>
<td>Select</td>
<td>Is this request being prescribed in accordance with Food and Drug Administration (FDA) approved labeling?  </td>
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
<td>4</td>
<td>1002</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the provider submitted documentation of the patient’s baseline fasting plasma glucose, hemoglobin A1c, liver function tests, electrocardiogram, gall bladder ultrasound, and electrolyte levels prior to initiation of therapy?</p>
<p>If yes, please provide documentation. </p></td>
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
<td>5</td>
<td>1003</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Does the patient have a contraindication to therapy with ketoconazole, cabergoline, metyrapone, or octreotide? </p>
<p>If yes, please submit the medication name and reason for inability to use.</p></td>
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
<td>1004</td>
</tr>
<tr class="odd">
<td>6</td>
<td>1004</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the patient had an inadequate clinical response of at least 30 days of therapy with ketoconazole, cabergoline, metyrapone, or octreotide within the past 60 days? </p>
<p>If yes, please submit the medication trials and dates.</p></td>
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
<td>7</td>
<td>2000</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the provider submitted documentation of a cortisol level checked 60 days after initiation of therapy?</p>
<p>If yes, please provide documentation.</p></td>
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
<td>8</td>
<td>3000</td>
<td></td>
<td>Select</td>
<td>Is the patient new to therapy (initial authorization request) or continuing therapy (re-authorization request)?</td>
<td>New Start (initial authorization request </td>
<td>3001</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Continuation (re-authorization request) </td>
<td>4000</td>
</tr>
<tr class="odd">
<td>9</td>
<td>3001</td>
<td></td>
<td>Select</td>
<td>Is this request being prescribed in accordance with Food and Drug Administration (FDA) approved labeling?  </td>
<td>Y</td>
<td>3002</td>
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
<td>10</td>
<td>3002</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the provider submitted documentation of the patient’s baseline fasting plasma glucose, hemoglobin A1c, liver function tests, electrocardiogram, gall bladder ultrasound, and electrolyte levels prior to initiation of therapy?</p>
<p>If yes, please provide documentation. </p></td>
<td>Y</td>
<td>3003</td>
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
<td>11</td>
<td>3003</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the provider submitted clinical rationale for prescribing Signifor LAR instead of Signifor?</p>
<p>If yes, please provide documentation.</p></td>
<td>Y </td>
<td>3004</td>
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
<td>12</td>
<td>3004</td>
<td></td>
<td>Select</td>
<td>Has the patient had inadequate clinical response to surgery or surgery is not an option?</td>
<td>Y </td>
<td>END (Pending Manual Review)</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N </td>
<td>1235</td>
</tr>
<tr class="odd">
<td>13</td>
<td>4000</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the provider submitted documentation of clinical response?</p>
<p>If yes, please submit documentation.</p></td>
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
<td>14</td>
<td>1235</td>
<td></td>
<td>Free Text</td>
<td>Please provide the rationale for the medication being requested. </td>
<td>END (Pending Manual Review)</td>
<td></td>
</tr>
</tbody>
</table>

LENGTH OF AUTHORIZATIONS:

Signifor-Initial authorizations:60 days, subsequent authorizations: 365
days.

Signifor LAR- 365 days.

| **Last Approved** | 4/10/2023 |
| ----------------- | --------- |
| **Other**         |           |
