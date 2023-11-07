# Synagis

**RSV prevention**

<table>
<thead>
<tr class="header">
<th><strong>Criteria Title</strong></th>
<th>Monoclonal antibody for RSV</th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Criteria Subtitle</strong></td>
<td>Synagis (palivizumab)</td>
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
<td>SYNAGIS</td>
<td>059245</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>SYNAGIS</td>
<td>059246</td>
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
<td>0998</td>
<td></td>
<td>Select</td>
<td>Is this request being prescribed in accordance with Food and Drug Administration (FDA) approved labeling?  </td>
<td>Y</td>
<td>0999</td>
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
<td>2</td>
<td>0999</td>
<td> </td>
<td>Select </td>
<td><p>What is the patient’s diagnosis?</p>
<p>  </p></td>
<td>Prematurity</td>
<td>1000</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Chronic Lung Disease</td>
<td>2000</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Congenital Heart Disease</td>
<td>3000</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Congenital abnormalities of the airway or neuromuscular disease</td>
<td>4000</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Heart Transplant</td>
<td>5000</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Immunocompromised</td>
<td>6000</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Other</td>
<td>1235</td>
</tr>
<tr class="even">
<td>3</td>
<td>1000</td>
<td></td>
<td>Select</td>
<td>Is the patient an infant born before 29 weeks, 0 day’s gestations who is less than 12 months of age at the start of Respiratory Syncytial Virus (RSV) season?</td>
<td>Y</td>
<td>1231</td>
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
<td>2000</td>
<td></td>
<td>Select</td>
<td>What is the infant’s gestation age and current age?</td>
<td>Infants born at less than 32 weeks AND is currently less than 12 months of age</td>
<td>2001</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><p>Infants born at less than 32 weeks</p>
<p>AND is currently between 12 to 24 months of age</p></td>
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
<td>5</td>
<td>2001</td>
<td></td>
<td>Select</td>
<td>Has the patient required greater than 21 percent oxygen for at least the first 28 DAYS after birth?</td>
<td>Y</td>
<td>1231</td>
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
<td>2002</td>
<td></td>
<td>Select</td>
<td>Has the patient required at least 28 days of greater than 21 percent oxygen after birth and continues to require supplemental oxygen, diuretics, or chronic systemic corticosteroid therapy within 6 months of the start of the second Respiratory Syncytial Virus (RSV) season?</td>
<td>Y </td>
<td>1231</td>
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
<td>7</td>
<td>3000</td>
<td></td>
<td>Select</td>
<td>Is the patient an infant who is less than 12 months of age with a diagnosis of hemodynamically significant heart disease who will most likely benefit from immunoprophylaxis?</td>
<td>Y</td>
<td>3001</td>
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
<td>3001</td>
<td></td>
<td>Select</td>
<td>Please select the patient’s diagnosis.</td>
<td><p>Infants with acyanotic heart disease receiving drugs to control congestive</p>
<p>heart failure and who will require surgery</p></td>
<td>1231</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Infants with moderate to severe pulmonary hypertension receiving drugs to control pulmonary hypertension</td>
<td>1231</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><p>Infants with a cyanotic heart defect who are prescribed therapy in</p>
<p>consultation with a pediatric cardiologist</p></td>
<td>1231</td>
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
<td>4000</td>
<td></td>
<td>Select</td>
<td><p>Is the patient less than 12 months of age with a diagnosis of a neuromuscular condition that compromises</p>
<p>handling of respiratory secretions?</p></td>
<td>Y </td>
<td>1231</td>
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
<td>10</td>
<td>5000</td>
<td></td>
<td>Select</td>
<td>Is the patient less than 24 months of age who has had a heart transplant during Respiratory Syncytial Virus (RSV) season?</td>
<td>Y </td>
<td>1231</td>
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
<td>11</td>
<td>6000</td>
<td></td>
<td>Select</td>
<td>Is the patient less than 24 months of age who has a diagnosis that supports they are profoundly immunocompromised during the Respiratory Syncytial Virus (RSV) season (e.g. chemotherapy)?</td>
<td>Y </td>
<td>1231</td>
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
<td>12</td>
<td>1231</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the provider submitted documentation that the patient has not had Respiratory Syncytial Virus (RSV) during the current season?</p>
<p>If yes, please submit documentation. </p></td>
<td>Y </td>
<td>1232</td>
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
<td>1232</td>
<td></td>
<td>Select</td>
<td><p>Is the medication being requested for use during the Respiratory Syncytial Virus (RSV) season AND not exceeding 1 dose per month (or 5 doses per single RSV season)?</p>
<p>Please note: The 2023-2024 RSV Season is November 1<sup>st</sup> to March 31<sup>st</sup>.</p></td>
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

LENGTH OF AUTHORIZATIONS: Valid through length of request

| **Last Approved** | 10/13/2023 |
| ----------------- | ---------- |
| **Other**         |            |
