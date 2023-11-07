**Infectious Disease Agents: Antibiotics – Quinolones** 

| Criteria 1 | NP- Baxdela, Ciprofloxacin ER, Moxifloxacin, Ofloxacin |
| ---------- | ------------------------------------------------------ |
| Criteria 2 | P with AR- Ciprofloxacin Susp                          |

<table>
<thead>
<tr class="header">
<th><strong>Criteria Title</strong> </th>
<th>Infectious Disease Agents: Antibiotics – Quinolones</th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Criteria Subtitle</strong> </td>
<td>Non-Preferred Products</td>
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
<td>Drug Name  </td>
<td>Corresponding Code (s) </td>
<td>Type of Code (GCNSeqNo, HICL, NDC) </td>
</tr>
<tr class="even">
<td></td>
<td>BAXDELA</td>
<td>077491</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>BAXDELA</td>
<td>077492</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>CIPROFLOXACIN ER</td>
<td>051576</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>CIPROFLOXACIN ER</td>
<td>053004</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>MOXIFLOXACIN</td>
<td>043879</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>OFLOXACIN</td>
<td>015601</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>OFLOXACIN</td>
<td>015602</td>
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
<td>0996</td>
<td></td>
<td>Select and Free Text </td>
<td><p>Does the patient have an infection that is caused by an organism resistant to <strong>ALL</strong> preferred antibiotics? </p>
<p> </p>
<p>If yes, please provide documentation of the diagnosis and any culture and sensitivity reports. </p></td>
<td>Y </td>
<td>END (Approve x 30 days)</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N </td>
<td>0997 </td>
</tr>
<tr class="odd">
<td>2</td>
<td>0997</td>
<td></td>
<td>Select</td>
<td><p>Is the patient completing a course of therapy that was started in the hospital or other similar location or was started before Medicaid eligibility?</p>
<p>Please note: only the remaining course will be authorized.</p></td>
<td>Y </td>
<td>END (Approve x 30 days)</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N </td>
<td>0998</td>
</tr>
<tr class="odd">
<td>3</td>
<td>0998</td>
<td></td>
<td>Select </td>
<td><p>Is the patient new to therapy (initial authorization request) or continuing therapy (re-authorization request)?  </p>
<p>  </p></td>
<td>New Start (initial authorization request)</td>
<td>0999</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Continuation (re-authorization request)  </td>
<td>1234</td>
</tr>
<tr class="odd">
<td>4</td>
<td>0999</td>
<td></td>
<td>Select </td>
<td>Is this request being prescribed in accordance with Food and Drug Administration (FDA) approved labeling?  </td>
<td>Y </td>
<td>1000</td>
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
<td>5</td>
<td>1000 </td>
<td> </td>
<td>Select and Free Text</td>
<td><p>Has the patient had an inadequate clinical response of at least <span class="underline">3 days</span> with at least <span class="underline">one preferred</span> drug?</p>
<p>The preferred alternatives may include the following: Ciprofloxacin, Levofloxacin.</p>
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
<td>6</td>
<td>1001</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the provider submitted documentation of medical necessity beyond convenience for why the patient cannot be changed to a preferred drug (i.e., allergies, drug-drug interactions, contraindications, or intolerances)?</p>
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
<td>7</td>
<td>1002</td>
<td></td>
<td>Select</td>
<td><p>Is the request for any of the following:</p>
<p>1) a nonsolid oral dosage formulation</p>
<p>2) a non-preferred extended release formulation</p>
<p>3) a non-preferred brand name that has a preferred generic product</p></td>
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
<td>END (Approve x 30 days)</td>
</tr>
<tr class="odd">
<td>8</td>
<td>1003</td>
<td></td>
<td>Select and Free Text</td>
<td>Has the provider submitted documentation of medical necessity for the requested product (i.e. medical reasons for why the patient cannot be changed to a solid oral dosage formulation, inadequate clinical response with a product’s immediate release formulation, or inadequate clinical response or allergy of two or more generic labelers)?</td>
<td>Y</td>
<td>END (Approve x 30 days)</td>
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
<td>9</td>
<td>1234</td>
<td></td>
<td>Select and Free Text  </td>
<td>Has the provider submitted documentation of the patient’s clinical response to treatment, ongoing safety monitoring, AND medical necessity for continued use?</td>
<td> Y    </td>
<td>END (Approve x 30 days)</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td> N    </td>
<td>1235 </td>
</tr>
<tr class="odd">
<td>10</td>
<td>1235</td>
<td></td>
<td>Free Text</td>
<td>Please provide the rationale for the medication being requested. </td>
<td>END (Pending Manual Review)</td>
<td></td>
</tr>
<tr class="even">
<td>11</td>
<td>1236</td>
<td></td>
<td>Free Text</td>
<td>Please explain the reason(s) why the patient is unable to use medications not requiring prior approval.</td>
<td>END (Pending Manual Review)</td>
<td></td>
</tr>
</tbody>
</table>

LENGTH OF AUTHORIZATIONS: Based on indication

| **Last Approved ** | 5/5/2023 |
| ------------------ | -------- |
| **Other**          |          |

 

<table>
<thead>
<tr class="header">
<th><strong>Criteria Title</strong> </th>
<th>Infectious Disease Agents: Antibiotics – Quinolones</th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Criteria Subtitle</strong> </td>
<td>Ciprofloxacin Susp</td>
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
<td>Drug Name  </td>
<td>Corresponding Code (s) </td>
<td>Type of Code (GCNSeqNo, HICL, NDC) </td>
</tr>
<tr class="even">
<td></td>
<td>CIPROFLOXACIN SUSP</td>
<td>039551</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>CIPROFLOXACIN SUSP</td>
<td>039552</td>
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
<td>1</td>
<td>1233</td>
<td></td>
<td>Select</td>
<td><p>Is the patient 12 years and older?</p>
<p>Please note: a PA is only required for patients 12 years and older.</p></td>
<td>Y</td>
<td>1234</td>
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
<td>2</td>
<td>1234</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Is the patient able to swallow a standard tablet and/or capsule formulation?</p>
<p>If no, please submit documentation.</p></td>
<td>Y</td>
<td>1235</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N</td>
<td>END (Pending Manual Review)</td>
</tr>
<tr class="odd">
<td>3</td>
<td>1235</td>
<td></td>
<td>Free Text</td>
<td>Please provide the rationale for the medication being requested. </td>
<td>END (Pending Manual Review)</td>
<td></td>
</tr>
<tr class="even">
<td>4</td>
<td>1236</td>
<td></td>
<td>Free Text</td>
<td>A PA is not required for those younger than 12 years of age.</td>
<td>END (Pending Manual Review)</td>
<td></td>
</tr>
</tbody>
</table>

LENGTH OF AUTHORIZATIONS: Based on indication

| **Last Approved ** | 5/5/2023 |
| ------------------ | -------- |
| **Other**          |          |
