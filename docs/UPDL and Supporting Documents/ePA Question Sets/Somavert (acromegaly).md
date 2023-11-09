# Somavert

[Criteria Document](https://mygainwell-my.sharepoint.com/:w:/g/personal/kaelyn_dobbins_gainwelltechnologies_com/EUq5m1vy939MtGcB9KIqXuIBvHG2ZvQJffPgzl8lXAcV-w?e=S5sdFt){:target="_blank" rel="noopener}

**acromegaly**

<table>
<thead>
<tr class="header">
<th><strong>Criteria Title</strong></th>
<th>GH Receptor Antagonist</th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Criteria Subtitle</strong></td>
<td>Somavert (pegvisomant)</td>
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
<td>X</td>
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
<td>SOMAVERT</td>
<td>051916</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>SOMAVERT</td>
<td>051917</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>SOMAVERT</td>
<td>051918</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>SOMAVERT</td>
<td>072769</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>SOMAVERT</td>
<td>072770</td>
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
<td>Is this request being prescribed in accordance with Food and Drug Administration (FDA) approved labeling? </td>
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
<td><p>Has the patient had an inadequate clinical response or contraindication to other therapies?</p>
<p>If yes, please submit documentation.  </p></td>
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
<td><p>Has the provider submitted documentation of the patient’s</p>
<p>baseline liver function tests (LFTs)?</p>
<p>If yes, please submit documentation.  </p></td>
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
<td><p>Has the provider submitted documentation of the patient’s liver function tests (LFTs)?</p>
<p> </p>
<p>If yes, please submit documentation. </p></td>
<td>Y </td>
<td>END (Pending Manual Review) </td>
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

LENGTH OF AUTHORIZATIONS: Initial authorizations will be for 180 days;
subsequent authorizations will be for 180 days and require documentation
of LFTs 

| **Last Approved** | 4/10/2023 |
| ----------------- | --------- |
| **Other**         |           |
