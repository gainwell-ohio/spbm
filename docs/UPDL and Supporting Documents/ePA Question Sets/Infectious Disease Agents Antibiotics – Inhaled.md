| Criteria 1 | Non-Preferred: Arikayce (NP), Bethkis (NP, QL), Cayston (NP), Kitabis Pak (NP, QL), Tobi Podhaler (NP, QL) |
| ---------- | ---------------------------------------------------------------------------------------------------------- |
| Criteria 2 | Tobramycin (P, QL, PA)                                                                                     |

 

<table>
<thead>
<tr class="header">
<th><strong>Criteria Title</strong></th>
<th>Infectious Disease Agents: Antibiotics – Inhaled</th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Criteria Subtitle</strong></td>
<td>Non-Preferred Products</td>
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
<td>ARIKAYCE</td>
<td>079020</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>BETHKIS</td>
<td>064682</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>CAYSTON</td>
<td>065913</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>KITABIS PAK</td>
<td>073201</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>TOBI PODHALER</td>
<td>067462</td>
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
<td>Is the patient new to therapy (initial authorization request) or continuing therapy (re-authorization request)?</td>
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
<td>2000</td>
</tr>
<tr class="odd">
<td>2</td>
<td>1000</td>
<td></td>
<td>Select</td>
<td>Is this request being prescribed in accordance with Food and Drug Administration (FDA) approved labeling?</td>
<td>Y </td>
<td>1001</td>
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
<td>3</td>
<td>1001</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the provider submitted documentation of cultures demonstrating that the requested drug is prescribed in alignment with an approved indication?</p>
<p>If yes, please submit documentation.</p></td>
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
<td><p>Has the patient had an inadequate clinical response of at least 28 days with at least one preferred drug?</p>
<p>If yes, please submit the medication trials and dates.</p></td>
<td>Y</td>
<td>1004</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N</td>
<td>1003</td>
</tr>
<tr class="odd">
<td>5</td>
<td>1003</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the provider submitted documentation of medical necessity beyond convenience for why the patient cannot be changed to a preferred drug (i.e., allergies, drug-drug interactions, contraindications, or intolerances)? </p>
<p>If yes, please submit the medication name and reason for inability to use.</p></td>
<td>Y</td>
<td>1004</td>
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
<td>1004</td>
<td></td>
<td>Select</td>
<td><p>Is the request for any of the following:</p>
<p>1) a nonsolid oral dosage formulation</p>
<p>2) a non-preferred extended release formulation</p>
<p>3) a non-preferred brand name that has a preferred generic product</p></td>
<td>Y</td>
<td>1005</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N</td>
<td>1006</td>
</tr>
<tr class="odd">
<td>7</td>
<td>1005</td>
<td></td>
<td>Select and Free Text</td>
<td>Has the provider submitted documentation of medical necessity for the requested product (i.e. medical reasons for why the patient cannot be changed to a solid oral dosage formulation, inadequate clinical response with a product’s immediate release formulation, or inadequate clinical response or allergy of two or more generic labelers)?</td>
<td>Y</td>
<td>1006</td>
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
<td>1006</td>
<td></td>
<td>Select</td>
<td>What product is being requested?</td>
<td>Arikayce</td>
<td>END (Pending Manual Review)</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Bethkis</td>
<td>1007</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Cayston</td>
<td>END (Pending Manual Review)</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Kitabis Pak</td>
<td>1007</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Tobi Podhaler</td>
<td>1007</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Other</td>
<td>1235</td>
</tr>
<tr class="odd">
<td>9</td>
<td>1007</td>
<td></td>
<td>Select</td>
<td><p>Ohio Medicaid covers up to 56 doses in 56 days.</p>
<p>Does this request meet this requirement?</p></td>
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
<td>10</td>
<td>2000</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the provider submitted documentation of the patient’s clinical response to treatment and ongoing safety monitoring (i.e., culture conversion, symptom improvement)?</p>
<p>If yes, please submit documentation.</p></td>
<td>Y</td>
<td>2001</td>
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
<td>2001</td>
<td></td>
<td>Select</td>
<td>What product is being requested?</td>
<td>Arikayce</td>
<td>END (Pending Manual Review)</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Bethkis</td>
<td>2002</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Cayston</td>
<td>END (Pending Manual Review)</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Kitabis Pak</td>
<td>2002</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Tobi Podhaler</td>
<td>2002</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Other</td>
<td>1235</td>
</tr>
<tr class="odd">
<td>12</td>
<td>2002</td>
<td></td>
<td>Select</td>
<td><p>Ohio Medicaid covers up to 56 doses in 56 days.</p>
<p>Does this request meet this requirement?</p></td>
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
<td>13</td>
<td>1235</td>
<td></td>
<td>Free Text</td>
<td>Please provide the rationale for the medication being requested. </td>
<td>END (Pending Manual Review)</td>
<td></td>
</tr>
<tr class="even">
<td>14</td>
<td>1236</td>
<td></td>
<td>Free Text</td>
<td>Please explain the reason(s) why the patient is unable to use medications not requiring prior approval.</td>
<td>END (Pending Manual Review)</td>
<td></td>
</tr>
</tbody>
</table>

LENGTH OF AUTHORIZATIONS: Initial authorizations- 180 days; Subsequent
authorizations- 365 days

| **Last Approved** | 5/17/2023 |
| ----------------- | --------- |
| **Other**         |           |

<table>
<thead>
<tr class="header">
<th><strong>Criteria Title</strong></th>
<th>Infectious Disease Agents: Antibiotics – Inhaled</th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Criteria Subtitle</strong></td>
<td>Preferred Products</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Approval Level</strong></td>
<td>NDC-9</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><p><strong>Products</strong></p>
<table>
<thead>
<tr class="header">
<th>Preferred</th>
<th>X</th>
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
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>TOBRAMYCIN</td>
<td>064682</td>
<td>GCNSeqNo</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>TOBRAMYCIN</td>
<td>037042</td>
<td>GCNSeqNo</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>TOBRAMYCIN</td>
<td>073201</td>
<td>GCNSeqNo</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Sequence Number</strong> </td>
<td><strong>Question ID</strong> </td>
<td><strong>Default Next Question ID</strong> </td>
<td><strong>Question Type</strong> </td>
<td><strong>Question Text</strong> </td>
<td><strong>Choice Text</strong> </td>
<td><strong>Next Question ID</strong> </td>
</tr>
<tr class="even">
<td>1</td>
<td>0999</td>
<td></td>
<td>Select</td>
<td>Is the patient new to therapy (initial authorization request) or continuing therapy (re-authorization request)?</td>
<td>New Start (initial authorization request)</td>
<td>1000</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Continuation (re-authorization request)  </td>
<td>2000</td>
</tr>
<tr class="even">
<td>2</td>
<td>1000</td>
<td></td>
<td>Select</td>
<td>Is this request being prescribed in accordance with Food and Drug Administration (FDA) approved labeling?</td>
<td>Y </td>
<td>1001</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N </td>
<td>1235</td>
</tr>
<tr class="even">
<td>3</td>
<td>1001</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the provider submitted documentation of cultures demonstrating that the requested drug is prescribed in alignment with an approved indication?</p>
<p>If yes, please submit documentation.</p></td>
<td>Y</td>
<td>1002</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N</td>
<td>1235</td>
</tr>
<tr class="even">
<td>4</td>
<td>1002</td>
<td></td>
<td>Select</td>
<td><p>Ohio Medicaid covers up to 56 doses in 56 days.</p>
<p>Does this request meet this requirement?</p></td>
<td>Y</td>
<td>END (Pending Manual Review) </td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N</td>
<td>1235</td>
</tr>
<tr class="even">
<td>5</td>
<td>2000</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the provider submitted documentation of the patient’s clinical response to treatment and ongoing safety monitoring (i.e., culture conversion, symptom improvement)?</p>
<p>If yes, please submit documentation.</p></td>
<td>Y</td>
<td>2001</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N</td>
<td>1235</td>
</tr>
<tr class="even">
<td>6</td>
<td>2001</td>
<td></td>
<td>Select</td>
<td><p>Ohio Medicaid covers up to 56 doses in 56 days.</p>
<p>Does this request meet this requirement?</p></td>
<td>Y</td>
<td>END (Pending Manual Review)</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N</td>
<td>1235</td>
</tr>
<tr class="even">
<td>7</td>
<td>1235</td>
<td></td>
<td>Free Text</td>
<td>Please provide the rationale for the medication being requested. </td>
<td>END (Pending Manual Review)</td>
<td></td>
</tr>
</tbody>
</table>

LENGTH OF AUTHORIZATIONS: Initial authorizations- 180 days; Subsequent
authorizations- 365 days

| **Last Approved** | 5/17/2023 |
| ----------------- | --------- |
| **Other**         |           |
