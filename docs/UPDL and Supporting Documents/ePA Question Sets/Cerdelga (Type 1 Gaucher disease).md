<table>
<thead>
<tr class="header">
<th><strong>Criteria Title</strong></th>
<th>Inhibitor of glucosylceramide synthase</th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Criteria Subtitle</strong></td>
<td>Cerdelga (eliglustat)</td>
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
<td>CERDELGA</td>
<td>072709</td>
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
<td>3</td>
<td>1001</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the provider submitted documentation of a Food and Drug Administration (FDA)-cleared test to evaluate cytochrome P450 enzyme (CYP)2D6 functionality and determined the patient not to be an ultra-rapid metabolizer?</p>
<p>If yes, please provide documentation.</p></td>
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
<td><p>Has the provider submitted documentation of the patient’s baseline hemoglobin level, platelet count, spleen volume and liver volume tests/examination?</p>
<p>If yes, please provide documentation.</p></td>
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
<td>5</td>
<td>2000</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the provider submitted documentation of clinical response or stabilization?</p>
<p>Please note: The provider is required to submit documentation of the patient’s hemoglobin level, platelet count, spleen volume and liver volume tests/examination at least annually.</p>
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
<td>6</td>
<td>1235</td>
<td></td>
<td>Free Text</td>
<td>Please provide the rationale for the medication being requested. </td>
<td>END (Pending Manual Review)</td>
<td></td>
</tr>
</tbody>
</table>

LENGTH OF AUTHORIZATIONS: 365 Days

| **Last Approved** | 4/10/2023 |
| ----------------- | --------- |
| **Other**         |           |
