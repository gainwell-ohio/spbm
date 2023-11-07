**Central Nervous System (CNS) Agents: Narcolepsy** 

| Criteria 1    | NP- Sunosi, Wakix, Xyrem, Sodium Oxybate |
| ------------- | ---------------------------------------- |
| Criteria 2    | NP- Xywav                                |
| Criteria 3\*  | Amphetamine/Dextroamphetamine IR         |
| Criteria 4 \* | Amphetamine/Dextroamphetamine ER         |
| Criteria 5\*  | Dextroamphetamine ER                     |
| Criteria 6 \* | Methylphenidate Tab, Methylphenidate ER  |

\*Items have standalone criteria sets – in both ADHD and Narcolepsy
classes

  - AR, QL for ADHD class

  - AR for narcolepsy class

<table>
<thead>
<tr class="header">
<th><strong>Criteria Title</strong> </th>
<th>Central Nervous System (CNS) Agents: Narcolepsy</th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Criteria Subtitle</strong> </td>
<td>Sunosi, Wakix, Xyrem, Sodium Oxybate</td>
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
<td>SODIUM OXYBATE</td>
<td>050813</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>SUNOSI</td>
<td>079597</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>SUNOSI</td>
<td>079598</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>WAKIX</td>
<td>079457</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>WAKIX</td>
<td>079458</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>XYREM</td>
<td>050813</td>
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
<td>2</td>
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
<td>3</td>
<td>1000 </td>
<td> </td>
<td>Select and Free Text</td>
<td><p>Has the patient had an inadequate clinical response of at least <span class="underline">30 days</span> with at least <span class="underline">two preferred</span> drugs - either (1) modafinil or armodafinil; or (2) preferred methylphenidate or amphetamine drug?</p>
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
<td>4</td>
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
<td>5</td>
<td>1002</td>
<td></td>
<td>Select</td>
<td>Is the request for brand Xyrem or generic sodium oxybate?</td>
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
<td>1005</td>
</tr>
<tr class="odd">
<td>6</td>
<td>1003</td>
<td></td>
<td>Select</td>
<td>Which product is being requested?</td>
<td>Brand Xyrem</td>
<td>1005</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Generic sodium oxybate</td>
<td>1004</td>
</tr>
<tr class="odd">
<td>7</td>
<td>1004</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the brand medication been attempted and failed or is the brand medication contraindicated?  </p>
<p>If yes, please submit documentation.</p></td>
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
<td>1235</td>
</tr>
<tr class="odd">
<td>8</td>
<td>1005</td>
<td></td>
<td>Select</td>
<td><p>Is the request for any of the following:</p>
<p>1) a nonsolid oral dosage formulation</p>
<p>2) a non-preferred extended release formulation</p>
<p>3) a non-preferred brand name that has a preferred generic product</p></td>
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
<td>END (Pending Manual Review)</td>
</tr>
<tr class="odd">
<td>9</td>
<td>1006</td>
<td></td>
<td>Select and Free Text</td>
<td>Has the provider submitted documentation of medical necessity for the requested product (i.e. medical reasons for why the patient cannot be changed to a solid oral dosage formulation, inadequate clinical response with a product’s immediate release formulation, or inadequate clinical response or allergy of two or more generic labelers)?</td>
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
<td>10</td>
<td>1234</td>
<td></td>
<td>Select and Free Text  </td>
<td><p>Has the provider submitted documentation of the patient’s clinical response to treatment and ongoing safety monitoring?</p>
<p> </p></td>
<td> Y    </td>
<td>END (Pending Manual Review) </td>
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
<td>11</td>
<td>1235</td>
<td></td>
<td>Free Text</td>
<td>Please provide the rationale for the medication being requested. </td>
<td>END (Pending Manual Review)</td>
<td></td>
</tr>
<tr class="even">
<td>12</td>
<td>1236</td>
<td></td>
<td>Free Text</td>
<td>Please explain the reason(s) why the patient is unable to use medications not requiring prior approval.</td>
<td>END (Pending Manual Review)</td>
<td></td>
</tr>
</tbody>
</table>

LENGTH OF AUTHORIZATIONS: 365 days

| **Last Approved ** | 4/20/2023 |
| ------------------ | --------- |
| **Other**          |           |

 

<table>
<thead>
<tr class="header">
<th><strong>Criteria Title</strong> </th>
<th>Central Nervous System (CNS) Agents: Narcolepsy</th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Criteria Subtitle</strong> </td>
<td>Xywav</td>
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
<td>XYWAV</td>
<td>081341</td>
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
<td>2</td>
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
<td>3</td>
<td>1000</td>
<td></td>
<td>Select and Free Text</td>
<td>Has the provider submitted documentation of the patient’s documented adherence to a sodium restricted diet? </td>
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
<td>4</td>
<td>1001 </td>
<td> </td>
<td>Select and Free Text</td>
<td><p>Has the patient had an inadequate clinical response of at least <span class="underline">30 days</span> with at least <span class="underline">two preferred</span> drugs - either (1) modafinil or armodafinil; or (2) preferred methylphenidate or amphetamine drug?</p>
<p>If yes, please submit the medication trials and dates.</p></td>
<td>Y </td>
<td>1003</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N </td>
<td>1002</td>
</tr>
<tr class="odd">
<td>5</td>
<td>1002</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the provider submitted documentation of medical necessity beyond convenience for why the patient cannot be changed to a preferred drug (i.e., allergies, drug-drug interactions, contraindications, or intolerances)?</p>
<p>If yes, please submit the medication name and reason for inability to use. </p></td>
<td>Y   </td>
<td>1003</td>
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
<td>1003</td>
<td></td>
<td>Select</td>
<td><p>Is the request for any of the following:</p>
<p>1) a nonsolid oral dosage formulation</p>
<p>2) a non-preferred extended release formulation</p>
<p>3) a non-preferred brand name that has a preferred generic product</p></td>
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
<td>END (Pending Manual Review)</td>
</tr>
<tr class="odd">
<td>7</td>
<td>1004</td>
<td></td>
<td>Select and Free Text</td>
<td>Has the provider submitted documentation of medical necessity for the requested product (i.e. medical reasons for why the patient cannot be changed to a solid oral dosage formulation, inadequate clinical response with a product’s immediate release formulation, or inadequate clinical response or allergy of two or more generic labelers)?</td>
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
<td>8</td>
<td>1234</td>
<td></td>
<td>Select and Free Text  </td>
<td><p>Has the provider submitted documentation of the patient’s clinical response to treatment and ongoing safety monitoring?</p>
<p> </p></td>
<td>Y    </td>
<td>END (Pending Manual Review) </td>
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

LENGTH OF AUTHORIZATIONS: 365 Days 

| **Last Approved ** | 4/20/2023 |
| ------------------ | --------- |
| **Other**          |           |

**  
**

<table>
<thead>
<tr class="header">
<th><strong>Criteria Title</strong> </th>
<th>Central Nervous System (CNS) Agents: Attention Deficit Hyperactivity Disorder Agents, Narcolepsy</th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Criteria Subtitle</strong> </td>
<td>Amphetamine/Dextroamphetamine IR</td>
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
<td>AMPHETAMINE/DEXTROAMPHETAMINE IR</td>
<td>004999</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>AMPHETAMINE/DEXTROAMPHETAMINE IR</td>
<td>005000</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>AMPHETAMINE/DEXTROAMPHETAMINE IR</td>
<td>005001</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>AMPHETAMINE/DEXTROAMPHETAMINE IR</td>
<td>034359</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>AMPHETAMINE/DEXTROAMPHETAMINE IR</td>
<td>047131</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>AMPHETAMINE/DEXTROAMPHETAMINE IR</td>
<td>047132</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>AMPHETAMINE/DEXTROAMPHETAMINE IR</td>
<td>047133</td>
<td>GCNSeqNo</td>
</tr>
</tbody>
</table>

| **Sequence Number ** | **Question ID ** | **Default Next Question ID ** | **Question Type ** | **Question Text **                                                                           | **Choice Text **            | **Next Question ID **       |
| -------------------- | ---------------- | ----------------------------- | ------------------ | -------------------------------------------------------------------------------------------- | --------------------------- | --------------------------- |
| 1                    | 0996             |                               | Select             | What is the patient’s diagnosis?                                                             | Narcolepsy                  | 0997                        |
|                      |                  |                               |                    |                                                                                              | ADHD                        | 0998                        |
|                      |                  |                               |                    |                                                                                              | Other                       | 1235                        |
| 2                    | 0997             |                               | Select             | Is the patient younger than 3 years old?                                                     | Y                           | 1235                        |
|                      |                  |                               |                    |                                                                                              | N                           | 1238                        |
| 3                    | 0998             |                               | Select             | Is the patient younger than 3 years old?                                                     | Y                           | 1235                        |
|                      |                  |                               |                    |                                                                                              | N                           | 0999                        |
| 4                    | 0999             |                               | Select             | Is Amphetamine-Dextroamphetamine Tab 30 MG being requested?                                  | Y                           | 1001                        |
|                      |                  |                               |                    |                                                                                              | N                           | 1000                        |
| 5                    | 1000             |                               | Select             | Ohio Medicaid covers up to 102 tablets per 34 days. Does this request meet this requirement? | Y                           | END (Pending Manual Review) |
|                      |                  |                               |                    |                                                                                              | N                           | 1237                        |
| 6                    | 1001             |                               | Select             | Ohio Medicaid covers up to 68 tablets per 34 days. Does this request meet this requirement?  | Y                           | END (Pending Manual Review) |
|                      |                  |                               |                    |                                                                                              | N                           | 1237                        |
| 7                    | 1235             |                               | Free Text          | Please provide the rationale for the medication being requested.                             | END (Pending Manual Review) |                             |
| 8                    | 1237             |                               | Free Text          | Please provide the rationale for the dose and frequency being requested.                     | END (Pending Manual Review) |                             |
| 9                    | 1238             |                               | Free Text          | A PA is not required for those 3 years of age and older.                                     | END (Pending Manual Review) |                             |

LENGTH OF AUTHORIZATIONS: 365 Days 

| **Last Approved ** | 4/20/2023 |
| ------------------ | --------- |
| **Other**          |           |

**  
**

<table>
<thead>
<tr class="header">
<th><strong>Criteria Title</strong> </th>
<th>Central Nervous System (CNS) Agents: Attention Deficit Hyperactivity Disorder Agents, Narcolepsy</th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Criteria Subtitle</strong> </td>
<td>Amphetamine/Dextroamphetamine ER</td>
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
<td>AMPHETAMINE/DEXTROAMPHETAMINE ER</td>
<td>048701</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>AMPHETAMINE/DEXTROAMPHETAMINE ER</td>
<td>048702</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>AMPHETAMINE/DEXTROAMPHETAMINE ER</td>
<td>048703</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>AMPHETAMINE/DEXTROAMPHETAMINE ER</td>
<td>050428</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>AMPHETAMINE/DEXTROAMPHETAMINE ER</td>
<td>050429</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>AMPHETAMINE/DEXTROAMPHETAMINE ER</td>
<td>050430</td>
<td>GCNSeqNo</td>
</tr>
</tbody>
</table>

| **Sequence Number ** | **Question ID ** | **Default Next Question ID ** | **Question Type ** | **Question Text **                                                                           | **Choice Text **            | **Next Question ID **       |
| -------------------- | ---------------- | ----------------------------- | ------------------ | -------------------------------------------------------------------------------------------- | --------------------------- | --------------------------- |
| 1                    | 0996             |                               | Select             | What is the patient’s diagnosis?                                                             | Narcolepsy                  | 0997                        |
|                      |                  |                               |                    |                                                                                              | ADHD                        | 0998                        |
|                      |                  |                               |                    |                                                                                              | Other                       | 1235                        |
| 2                    | 0997             |                               | Select             | Is the patient younger than 6 years old?                                                     | Y                           | 1235                        |
|                      |                  |                               |                    |                                                                                              | N                           | 1238                        |
| 3                    | 0998             |                               | Select             | Is the patient younger than 6 years old?                                                     | Y                           | 1235                        |
|                      |                  |                               |                    |                                                                                              | N                           | 0999                        |
| 4                    | 0999             |                               | Select             | Ohio Medicaid covers up to 34 capsules per 34 days. Does this request meet this requirement? | Y                           | END (Pending Manual Review) |
|                      |                  |                               |                    |                                                                                              | N                           | 1237                        |
| 5                    | 1235             |                               | Free Text          | Please provide the rationale for the medication being requested.                             | END (Pending Manual Review) |                             |
| 6                    | 1237             |                               | Free Text          | Please provide the rationale for the dose and frequency being requested.                     | END (Pending Manual Review) |                             |
| 7                    | 1238             |                               | Free Text          | A PA is not required for those 6 years of age and older.                                     | END (Pending Manual Review) |                             |

LENGTH OF AUTHORIZATIONS: 365 Days 

| **Last Approved ** | 4/20/2023 |
| ------------------ | --------- |
| **Other**          |           |

<table>
<thead>
<tr class="header">
<th><strong>Criteria Title</strong> </th>
<th>Central Nervous System (CNS) Agents: Attention Deficit Hyperactivity Disorder Agents, Narcolepsy</th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Criteria Subtitle</strong> </td>
<td>Dextroamphetamine ER</td>
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
<td>DEXTROAMPHETAMINE ER</td>
<td>005005</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>DEXTROAMPHETAMINE ER</td>
<td>005006</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>DEXTROAMPHETAMINE ER</td>
<td>005007</td>
<td>GCNSeqNo</td>
</tr>
</tbody>
</table>

| **Sequence Number ** | **Question ID ** | **Default Next Question ID ** | **Question Type ** | **Question Text **                                                                            | **Choice Text **            | **Next Question ID **       |
| -------------------- | ---------------- | ----------------------------- | ------------------ | --------------------------------------------------------------------------------------------- | --------------------------- | --------------------------- |
| 1                    | 0996             |                               | Select             | What is the patient’s diagnosis?                                                              | Narcolepsy                  | 0997                        |
|                      |                  |                               |                    |                                                                                               | ADHD                        | 0998                        |
|                      |                  |                               |                    |                                                                                               | Other                       | 1235                        |
| 2                    | 0997             |                               | Select             | Is the patient younger than 6 years old?                                                      | Y                           | 1235                        |
|                      |                  |                               |                    |                                                                                               | N                           | 1238                        |
| 3                    | 0998             |                               | Select             | Is the patient younger than 6 years old?                                                      | Y                           | 1235                        |
|                      |                  |                               |                    |                                                                                               | N                           | 0999                        |
| 4                    | 0999             |                               | Select             | Is Dextroamphetamine Sulfate ER Cap 15 MG being requested?                                    | Y                           | 1001                        |
|                      |                  |                               |                    |                                                                                               | N                           | 1000                        |
| 5                    | 1000             |                               | Select             | Ohio Medicaid covers up to 34 capsules per 34 days. Does this request meet this requirement?  | Y                           | END (Pending Manual Review) |
|                      |                  |                               |                    |                                                                                               | N                           | 1237                        |
| 6                    | 1001             |                               | Select             | Ohio Medicaid covers up to 136 capsules per 34 days. Does this request meet this requirement? | Y                           | END (Pending Manual Review) |
|                      |                  |                               |                    |                                                                                               | N                           | 1237                        |
| 7                    | 1235             |                               | Free Text          | Please provide the rationale for the medication being requested.                              | END (Pending Manual Review) |                             |
| 8                    | 1237             |                               | Free Text          | Please provide the rationale for the dose and frequency being requested.                      | END (Pending Manual Review) |                             |
| 9                    | 1238             |                               | Free Text          | A PA is not required for those 6 years of age and older.                                      | END (Pending Manual Review) |                             |

LENGTH OF AUTHORIZATIONS: 365 Days 

| **Last Approved ** | 4/20/2023 |
| ------------------ | --------- |
| **Other**          |           |

<table>
<thead>
<tr class="header">
<th><strong>Criteria Title</strong> </th>
<th>Central Nervous System (CNS) Agents: Attention Deficit Hyperactivity Disorder Agents, Narcolepsy</th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Criteria Subtitle</strong> </td>
<td>Methylphenidate Tab, Methylphenidate ER</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Approval Level</strong> </td>
<td>GCNSeqNo</td>
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
<td>METHYLPHENIDATE ER CAP (gen of Metadate CD, Ritalin LA)</td>
<td>004029</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>METHYLPHENIDATE ER CAP (gen of Metadate CD, Ritalin LA)</td>
<td>044072</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>METHYLPHENIDATE ER CAP (gen of Metadate CD, Ritalin LA)</td>
<td>053056</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>METHYLPHENIDATE ER CAP (gen of Metadate CD, Ritalin LA)</td>
<td>053057</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>METHYLPHENIDATE ER CAP (gen of Metadate CD, Ritalin LA)</td>
<td>053058</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>METHYLPHENIDATE ER CAP (gen of Metadate CD, Ritalin LA)</td>
<td>053059</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>METHYLPHENIDATE ER CAP (gen of Metadate CD, Ritalin LA)</td>
<td>053060</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>METHYLPHENIDATE ER CAP (gen of Metadate CD, Ritalin LA)</td>
<td>053061</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>METHYLPHENIDATE ER CAP (gen of Metadate CD, Ritalin LA)</td>
<td>053974</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>METHYLPHENIDATE ER CAP (gen of Metadate CD, Ritalin LA)</td>
<td>060545</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>METHYLPHENIDATE ER CAP (gen of Metadate CD, Ritalin LA)</td>
<td>060546</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>METHYLPHENIDATE ER CAP (gen of Metadate CD, Ritalin LA)</td>
<td>060547</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>METHYLPHENIDATE ER CAP (gen of Metadate CD, Ritalin LA)</td>
<td>072092</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>METHYLPHENIDATE ER TAB (gen of Concerta, Methylin ER, Ritalin SR)</td>
<td>045981</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>METHYLPHENIDATE ER TAB (gen of Concerta, Methylin ER, Ritalin SR)</td>
<td>045982</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>METHYLPHENIDATE ER TAB (gen of Concerta, Methylin ER, Ritalin SR)</td>
<td>047318</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>METHYLPHENIDATE ER TAB (gen of Concerta, Methylin ER, Ritalin SR)</td>
<td>050172</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>METHLYPHENIDATE TAB</td>
<td>004026</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>METHLYPHENIDATE TAB</td>
<td>004027</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>METHLYPHENIDATE TAB</td>
<td>004028</td>
<td>GCNSeqNo</td>
</tr>
</tbody>
</table>

| **Sequence Number ** | **Question ID ** | **Default Next Question ID ** | **Question Type ** | **Question Text **                                                                           | **Choice Text **                                                                                  | **Next Question ID **       |
| -------------------- | ---------------- | ----------------------------- | ------------------ | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | --------------------------- |
| 1                    | 2002             |                               | Select             | What is the patient’s diagnosis?                                                             | Narcolepsy                                                                                        | 2003                        |
|                      |                  |                               |                    |                                                                                              | ADHD                                                                                              | 2004                        |
|                      |                  |                               |                    |                                                                                              | Other                                                                                             | 1235                        |
| 2                    | 2003             |                               | Select             | Is the patient younger than 6 years old?                                                     | Y                                                                                                 | 1235                        |
|                      |                  |                               |                    |                                                                                              | N                                                                                                 | 1238                        |
| 3                    | 2004             |                               | Select             | Is the patient younger than 6 years old?                                                     | Y                                                                                                 | 1235                        |
|                      |                  |                               |                    |                                                                                              | N                                                                                                 | 2005                        |
| 4                    | 2005             |                               | Select             | Which product is being requested?                                                            | Methylphenidate HCl Tab (all strengths)                                                           | 2006                        |
|                      |                  |                               |                    |                                                                                              | Methylphenidate HCl CR Cap (generic Metadate- all strengths)                                      | 2007                        |
|                      |                  |                               |                    |                                                                                              | Methylphenidate HCl CR Tab (<span class="underline">all strengths excluding 10 MG & 20 MG</span>) | 2008                        |
|                      |                  |                               |                    |                                                                                              | Methylphenidate HCl CR Tab 10 MG & 20 MG                                                          | 2009                        |
|                      |                  |                               |                    |                                                                                              | Other                                                                                             | END (Pending Manual Review) |
| 5                    | 2006             |                               | Select             | Ohio Medicaid covers up to 102 tablets per 34 days. Does this request meet this requirement? | Y                                                                                                 | END (Pending Manual Review) |
|                      |                  |                               |                    |                                                                                              | N                                                                                                 | 1237                        |
| 6                    | 2007             |                               | Select             | Ohio Medicaid covers up to 34 capsules per 34 days. Does this request meet this requirement? | Y                                                                                                 | END (Pending Manual Review) |
|                      |                  |                               |                    |                                                                                              | N                                                                                                 | 1237                        |
| 7                    | 2008             |                               | Select             | Ohio Medicaid covers up to 34 tablets per 34 days. Does this request meet this requirement?  | Y                                                                                                 | END (Pending Manual Review) |
|                      |                  |                               |                    |                                                                                              | N                                                                                                 | 1237                        |
| 8                    | 2009             |                               | Select             | Ohio Medicaid covers up to 102 tablets per 34 days. Does this request meet this requirement? | Y                                                                                                 | END (Pending Manual Review) |
|                      |                  |                               |                    |                                                                                              | N                                                                                                 | 1237                        |
| 9                    | 1235             |                               | Free Text          | Please provide the rationale for the medication being requested.                             | END (Pending Manual Review)                                                                       |                             |
| 10                   | 1237             |                               | Free Text          | Please provide the rationale for the dose and frequency being requested.                     | END (Pending Manual Review)                                                                       |                             |
| 11                   | 1238             |                               | Free Text          | A PA is not required for those 6 years of age and older.                                     | END (Pending Manual Review)                                                                       |                             |

LENGTH OF AUTHORIZATIONS: 365 Days 

| **Last Approved ** | 4/20/2023 |
| ------------------ | --------- |
| **Other**          |           |
