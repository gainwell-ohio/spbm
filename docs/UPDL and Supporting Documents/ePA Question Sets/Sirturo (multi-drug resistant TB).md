<table>
<thead>
<tr class="header">
<th><strong>Criteria Title</strong></th>
<th>Diarylquinoline Antimycobacterial</th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Criteria Subtitle</strong></td>
<td>Sirturo (bedaq uiline)</td>
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
<td>SIRTURO</td>
<td>070413</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>SIRTURO</td>
<td>081261</td>
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
<td>0999</td>
<td> </td>
<td>Select </td>
<td><p>Is the patient new to therapy (initial authorization request) or continuing therapy (re-authorization request)?  </p>
<p>  </p></td>
<td>New Start (initial authorization request)</td>
<td>1000</td>
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
<td>1000</td>
<td></td>
<td>Select</td>
<td>Is this request being prescribed in accordance with Food and Drug Administration (FDA) approved labeling?  </td>
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
<td>3</td>
<td>1001</td>
<td></td>
<td>Select</td>
<td>Is the medication being prescribed by an Infectious Disease specialist?</td>
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
<td><p>Has the provider submitted documentation of the patient’s electrocardiogram (ECG), liver enzymes and electrolyte levels?</p>
<p>If yes, please provide documentation.</p></td>
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
<td>Select</td>
<td><p>The initial 14 days of therapy is limited to a quantity of 28 or 56 for the 100 mg tablets or a quantity of 140 or 280 tablets for the 20 mg tablets.</p>
<p>Does the request meet this requirement?</p></td>
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
<td>1236</td>
</tr>
<tr class="odd">
<td>6</td>
<td>2000</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the provider submitted documentation of the patient’s electrocardiogram (ECG) obtained 2 weeks after initiation and another ECG about 10 weeks later?</p>
<p>If yes, please provide documentation.</p></td>
<td>Y</td>
<td>2001 </td>
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
<td>2001</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the provider submitted documentation that the patient’s QT interval has been evaluated for continued drug therapy (recommended to be less than 500 milliseconds)?</p>
<p>If yes, please provide documentation.</p></td>
<td>Y</td>
<td>2002</td>
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
<td>2002</td>
<td></td>
<td>Select</td>
<td><p>The remaining 22 weeks of therapy is limited to a quantity of 66 or 132 tablets for the 100 mg tablets or a quantity of 330 or 660 tablets for the 20 mg tablets.</p>
<p>Does the request meet this requirement?</p></td>
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
<td>1236</td>
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
<td>Please provide the rationale for the dose and frequency being requested.</td>
<td>END (Pending Manual Review)</td>
<td></td>
</tr>
</tbody>
</table>

LENGTH OF AUTHORIZATIONS: Initial authorizations will be for 14 days and
limited to a quantity of 28 or 56 of the 100 mg tablets or a quantity of
140 or 280 of the 20 mg tablets. Subsequent authorizations will be for
22 weeks of therapy limited to a quantity of 66 or 132 of the 100 mg
tablets or a quantity of 330 or 660 of the 20 mg tablets.

| **Last Approved** | 4/10/2023 |
| ----------------- | --------- |
| **Other**         |           |
