# Emflaza

**Duchenne muscular dystrophy**

<table>
<thead>
<tr class="header">
<th><strong>Criteria Title</strong></th>
<th>Glucocorticoid</th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Criteria Subtitle</strong></td>
<td>Emflaza (deflazacort)</td>
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
<td>EMFLAZA</td>
<td>027604</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>EMFLAZA</td>
<td>027605</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>EMFLAZA</td>
<td>077113</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>EMFLAZA</td>
<td>077116</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>EMFLAZA</td>
<td>077117</td>
<td>GCNSeqNo</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr class="header">
<th><strong>Sequence Number</strong>  </th>
<th><strong>Question ID</strong>  </th>
<th><strong>Default Next Question ID</strong>  </th>
<th><strong>Question Type</strong>  </th>
<th><strong>Question Text</strong>  </th>
<th><strong>Choice Text</strong>  </th>
<th><strong>Next Question ID</strong>  </th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1 </td>
<td>1000 </td>
<td> </td>
<td>Select </td>
<td>Is this request being prescribed in accordance with Food and Drug Administration (FDA) approved labeling? </td>
<td><p>Y </p>
<p> </p></td>
<td>1001 </td>
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
<td>2 </td>
<td>1001 </td>
<td> </td>
<td>Select  </td>
<td>Is the medication being prescribed by or in consultation with a neurologist or specialist in Duchenne Muscular Dystrophy? </td>
<td>Y  </td>
<td>1002 </td>
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
<td>3 </td>
<td>1002 </td>
<td> </td>
<td>Select and Free Text  </td>
<td><p>Has the patient had an inadequate clinical response of at least 180 days to prednisone? </p>
<p> </p>
<p>If yes, please submit the medication trials and dates. </p></td>
<td>Y  </td>
<td>1004 </td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N  </td>
<td>1003 </td>
</tr>
<tr class="odd">
<td>4 </td>
<td>1003 </td>
<td> </td>
<td>Select and Free Text  </td>
<td><p>Does the patient have a contraindication to prednisone?  </p>
<p> </p>
<p>If yes, please submit the medication name and reason for inability to use.  </p></td>
<td><p>Y </p>
<p> </p>
<p> </p>
<p> </p></td>
<td>1004 </td>
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
<td><p>5 </p>
<p> </p></td>
<td>1004 </td>
<td> </td>
<td>Select and Free Text </td>
<td><p>Has the provider submitted documentation of the patient’s weight?  </p>
<p> </p>
<p>If yes, please provide documentation of the patient’s weight. </p></td>
<td>Y  </td>
<td>END (Pending Manual Review) </td>
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
<td>6 </td>
<td>1235 </td>
<td> </td>
<td>Free Text </td>
<td>Please provide the rationale for the medication being requested.  </td>
<td>END (Pending Manual Review) </td>
<td></td>
</tr>
</tbody>
</table>

LENGTH OF AUTHORIZATIONS: 365 Days

| **Last Approved** | 4/13/2023 |
| ----------------- | --------- |
| **Other**         |           |
