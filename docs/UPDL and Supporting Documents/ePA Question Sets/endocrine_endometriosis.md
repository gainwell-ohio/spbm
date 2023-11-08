# Endocrine Agents - Endometriosis

[Criteria Document](https://mygainwell-my.sharepoint.com/:w:/g/personal/kaelyn_dobbins_gainwelltechnologies_com/EVyQREBNvtNIqbfZW4DxhvUB_f0ETegJHKh1OGjUGozwkg?e=O0hla3){:target="_blank" rel="noopener}

|||
| ---------- | -------------------------------------------------------------------------------------------------------- |
| Criteria 1 | NP Criteria- Synarel                                                                                     |
| Criteria 2 | Danazol (P, ST), Depo-Subq Provera 104 (P, ST), Lupaneta Pack (P, ST), Orilissa (P, ST), Zoladex (P, ST) |
| Criteria 3 | Lupron Depot 3.75, 11.25mg (P, QL, ST)                                                                   |
| Criteria 4 | Myfembree (P, QL, ST)                                                                                    |

## Synarel

<table>
<thead>
<tr class="header">
<th><strong>Criteria Title</strong> </th>
<th>Endocrine Agents: Endometriosis</th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Criteria Subtitle</strong> </td>
<td>Synarel</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Approval Level</strong> </td>
<td> GCNSeqNo</td>
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
<td>Corresponding Code(s) </td>
<td>Type of Code (GCNSeqNo, HICL, NDC) </td>
</tr>
<tr class="even">
<td></td>
<td> SYNAREL</td>
<td>044984</td>
<td>GCNSeqNo </td>
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
<td>1234</td>
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
<td>0999 </td>
<td> </td>
<td>Select and Free Text</td>
<td><p>Has the patient had an inadequate clinical response of at least <span class="underline">84 days</span> with at least <span class="underline">one preferred</span> NSAID?</p>
<p>If yes, please submit the medication trials and dates.</p></td>
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
<td>1002</td>
</tr>
<tr class="odd">
<td>4</td>
<td>1000</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the patient had an inadequate clinical response of at least <span class="underline">84 days</span> with at least <span class="underline">one preferred</span> oral contraceptive?</p>
<p>If yes, please submit the medication trials and dates.</p></td>
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
<td>1002</td>
</tr>
<tr class="odd">
<td>5</td>
<td>1001</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the patient had an inadequate clinical response of at least <span class="underline">84 days</span> with at least <span class="underline">one preferred</span> step-therapy drug?</p>
<p>If yes, please submit the medication trials and dates.</p></td>
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
<td>1002</td>
</tr>
<tr class="odd">
<td>6</td>
<td>1002</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the provider submitted documentation of medical necessity beyond convenience for why the patient cannot be changed to a preferred drug (i.e., allergies, drug-drug interactions, contraindications, or intolerances)?</p>
<p>If yes, please submit the medication name and reason for inability to use. </p></td>
<td>Y   </td>
<td>1003 </td>
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
<td>8</td>
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
<td>9</td>
<td>1234</td>
<td></td>
<td>Select and Free Text  </td>
<td>Has the provider submitted documentation of the patient’s clinical response to treatment and ongoing safety monitoring?</td>
<td> Y    </td>
<td>END (Pending Manual Review)  </td>
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

LENGTH OF AUTHORIZATIONS: 365 days

|||
| ------------------ | -------- |
| **Last Approved ** | 5/5/2023 |
| **Other**          |          |

## Danazol, Depo-Subq Provera 104, Lupaneta Pack, Orilissa, Zoladex

<table>
<thead>
<tr class="header">
<th><strong>Criteria Title</strong> </th>
<th>Endocrine Agents: Endometriosis</th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Criteria Subtitle</strong> </td>
<td>Danazol, Depo-Subq Provera 104, Lupaneta Pack, Orilissa, Zoladex</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Approval Level</strong> </td>
<td> GCNSeqNo</td>
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
<td>Corresponding Code(s) </td>
<td>Type of Code (GCNSeqNo, HICL, NDC) </td>
</tr>
<tr class="even">
<td></td>
<td> DANAZOL</td>
<td>006600</td>
<td>GCNSeqNo </td>
</tr>
<tr class="odd">
<td></td>
<td>DANAZOL</td>
<td>006601</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>DANAZOL</td>
<td>006602</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>DEPO-SUBQ PROVERA 104</td>
<td>058938</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>LUPANETA PACK</td>
<td>003274</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>ORILISSA</td>
<td>078657</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>ORILISSA</td>
<td>078659</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>ZOLADEX</td>
<td>044961</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>ZOLADEX</td>
<td>044962</td>
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
<td>1234</td>
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
<td>0999 </td>
<td> </td>
<td>Select and Free Text</td>
<td><p>Has the patient had an inadequate clinical response of at least <span class="underline">84 days</span> with at least <span class="underline">one preferred</span> NSAID?</p>
<p>If yes, please submit the medication trials and dates.</p></td>
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
<td>1002</td>
</tr>
<tr class="odd">
<td>4</td>
<td>1000</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the patient had an inadequate clinical response of at least <span class="underline">84 days</span> with at least <span class="underline">one preferred</span> oral contraceptive?</p>
<p>If yes, please submit the medication trials and dates.</p></td>
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
<td>1002</td>
</tr>
<tr class="odd">
<td>5</td>
<td>1002</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the provider submitted documentation of medical necessity beyond convenience for why the patient cannot be changed to a preferred drug (i.e., allergies, drug-drug interactions, contraindications, or intolerances)?</p>
<p>If yes, please submit the medication name and reason for inability to use. </p></td>
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
<td>6</td>
<td>1234</td>
<td></td>
<td>Select and Free Text  </td>
<td><p>Has the provider submitted documentation of the patient’s clinical response to treatment and ongoing safety monitoring?</p>
<p>    </p></td>
<td> Y    </td>
<td>END (Pending Manual Review)  </td>
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

LENGTH OF AUTHORIZATIONS: 365 Days

|||
| ------------------ | -------- |
| **Last Approved ** | 5/5/2023 |
| **Other**          |          |

## Lupron Depot 3.75, 11.25mg

<table>
<thead>
<tr class="header">
<th><strong>Criteria Title</strong> </th>
<th>Endocrine Agents: Endometriosis and Uterine Fibroids</th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Criteria Subtitle</strong> </td>
<td>Lupron Depot 3.75, 11.25mg</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Approval Level</strong> </td>
<td> GCNSeqNo</td>
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
<td>Corresponding Code(s) </td>
<td>Type of Code (GCNSeqNo, HICL, NDC) </td>
</tr>
<tr class="even">
<td></td>
<td>LUPRON DEPOT </td>
<td>044980</td>
<td>GCNSeqNo </td>
</tr>
<tr class="odd">
<td></td>
<td>LUPRON DEPOT</td>
<td>045017</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>LUPRON DEPOT</td>
<td>047665</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>LUPRON DEPOT</td>
<td>067738</td>
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
<td>What is the patient’s diagnosis?</td>
<td>Endometriosis</td>
<td>1000</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Uterine Fibroids</td>
<td>2000</td>
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
<td>2</td>
<td>1000</td>
<td></td>
<td>Select</td>
<td>Is the patient new to therapy (initial authorization request) or continuing therapy (re-authorization request)?  </td>
<td>New Start (initial authorization request)</td>
<td>1001</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Continuation (re-authorization request)  </td>
<td>1232</td>
</tr>
<tr class="even">
<td>3</td>
<td>1001</td>
<td></td>
<td>Select</td>
<td>Is this request being prescribed in accordance with Food and Drug Administration (FDA) approved labeling?  </td>
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
<td> </td>
<td>Select and Free Text</td>
<td><p>Has the patient had an inadequate clinical response of at least <span class="underline">84 days</span> with at least <span class="underline">one preferred</span> NSAID?</p>
<p>If yes, please submit the medication trials and dates.</p></td>
<td>Y </td>
<td>1003</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N </td>
<td>1004</td>
</tr>
<tr class="even">
<td>5</td>
<td>1003</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the patient had an inadequate clinical response of at least <span class="underline">84 days</span> with at least <span class="underline">one preferred</span> oral contraceptive?</p>
<p>If yes, please submit the medication trials and dates.</p></td>
<td>Y </td>
<td>END (Pending Manual Review)</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N </td>
<td>1004</td>
</tr>
<tr class="even">
<td>6</td>
<td>1004</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the provider submitted documentation of medical necessity beyond convenience for why the patient cannot be changed to a preferred drug (i.e., allergies, drug-drug interactions, contraindications, or intolerances)?</p>
<p>If yes, please submit the medication name and reason for inability to use.</p></td>
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
<td>1236</td>
</tr>
<tr class="even">
<td>7</td>
<td>2000</td>
<td></td>
<td>Select</td>
<td>Is the patient new to therapy (initial authorization request) or continuing therapy (re-authorization request)?  </td>
<td>New Start (initial authorization request)</td>
<td>2001</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Continuation (re-authorization request)  </td>
<td>1233</td>
</tr>
<tr class="even">
<td>8</td>
<td>2001</td>
<td></td>
<td>Select</td>
<td>Is this request being prescribed in accordance with Food and Drug Administration (FDA) approved labeling?  </td>
<td>Y</td>
<td>2002</td>
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
<td>9</td>
<td>2002</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the patient had an inadequate clinical response of at least <span class="underline">90 days</span> with at least <span class="underline">one preferred</span> oral contraceptive?</p>
<p>If yes, please submit the medication trials and dates.</p></td>
<td>Y</td>
<td>2004</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N</td>
<td>2003</td>
</tr>
<tr class="even">
<td>10</td>
<td>2003</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the provider submitted documentation of medical necessity beyond convenience for why the patient cannot be changed to a preferred drug (i.e., allergies, drug-drug interactions, contraindications, or intolerances)?</p>
<p>If yes, please submit the medication name and reason for inability to use.</p></td>
<td>Y</td>
<td>2004</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N</td>
<td>1236</td>
</tr>
<tr class="even">
<td>11</td>
<td>2004</td>
<td></td>
<td>Select</td>
<td><p>Ohio Medicaid covers a total lifetime duration of therapy of 180 days for Lupron Depot.</p>
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
<td>1237</td>
</tr>
<tr class="even">
<td>12</td>
<td>1232</td>
<td></td>
<td>Select and Free Text</td>
<td>Has the provider submitted documentation of the patient’s clinical response to treatment and ongoing safety monitoring?</td>
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
<td>13</td>
<td>1233</td>
<td></td>
<td>Select and Free Text  </td>
<td>Has the provider submitted documentation of the patient’s clinical response to treatment and ongoing safety monitoring?</td>
<td> Y    </td>
<td>1234  </td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td> N    </td>
<td>1235 </td>
</tr>
<tr class="even">
<td>14</td>
<td>1234</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Ohio Medicaid covers a total lifetime duration of therapy of 180 days for Lupron Depot.</p>
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
<td>1237</td>
</tr>
<tr class="even">
<td>15</td>
<td>1235</td>
<td></td>
<td>Free Text</td>
<td>Please provide the rationale for the medication being requested. </td>
<td>END (Pending Manual Review)</td>
<td></td>
</tr>
<tr class="odd">
<td>16</td>
<td>1236</td>
<td></td>
<td>Free Text</td>
<td>Please explain the reason(s) why the patient is unable to use medications not requiring prior approval.</td>
<td>END (Pending Manual Review)</td>
<td></td>
</tr>
<tr class="even">
<td>17</td>
<td>1237</td>
<td></td>
<td>Free Text</td>
<td>Please provide the rationale for the dose and frequency requested.</td>
<td>END (Pending Manual Review)</td>
<td></td>
</tr>
</tbody>
</table>

LENGTH OF AUTHORIZATIONS: Endometriosis- 365 Days; Uterine Fibroids- Up
to 180 days

|||
| ------------------ | -------- |
| **Last Approved ** | 5/5/2023 |
| **Other**          |          |

## Myfembree

<table>
<thead>
<tr class="header">
<th><strong>Criteria Title</strong> </th>
<th>Endocrine Agents: Endometriosis and Uterine Fibroids</th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Criteria Subtitle</strong> </td>
<td>Myfembree</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Approval Level</strong> </td>
<td> GCNSeqNo</td>
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
<td>Corresponding Code(s) </td>
<td>Type of Code (GCNSeqNo, HICL, NDC) </td>
</tr>
<tr class="even">
<td></td>
<td> MYFEMBREE</td>
<td>082317</td>
<td>GCNSeqNo </td>
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
<td>0997</td>
<td></td>
<td>Select </td>
<td>Is the patient new to therapy (initial authorization request) or continuing therapy (re-authorization request)?  </td>
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
<td>Select</td>
<td>What is the patient’s diagnosis?</td>
<td>Endometriosis</td>
<td>1000</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Uterine Fibroids</td>
<td>2000</td>
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
<td>4</td>
<td>1000</td>
<td> </td>
<td>Select and Free Text</td>
<td><p>Has the patient had an inadequate clinical response of at least <span class="underline">84 days</span> with at least <span class="underline">one preferred</span> NSAID?</p>
<p>If yes, please submit the medication trials and dates.</p></td>
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
<td>1002</td>
</tr>
<tr class="even">
<td>5</td>
<td>1001</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the patient had an inadequate clinical response of at least <span class="underline">84 days</span> with at least <span class="underline">one preferred</span> oral contraceptive?</p>
<p>If yes, please submit the medication trials and dates.</p></td>
<td>Y </td>
<td>1003</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N </td>
<td>1002</td>
</tr>
<tr class="even">
<td>6</td>
<td>1002</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the provider submitted documentation of medical necessity beyond convenience for why the patient cannot be changed to a preferred drug (i.e., allergies, drug-drug interactions, contraindications, or intolerances)?</p>
<p>If yes, please submit the medication name and reason for inability to use.</p></td>
<td>Y</td>
<td>1003</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N</td>
<td>1236</td>
</tr>
<tr class="even">
<td>7</td>
<td>1003</td>
<td></td>
<td>Select</td>
<td><p>Ohio Medicaid covers a total lifetime duration of therapy of 730 days between Oriahnn and Myfembree (if applicable).</p>
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
<td>8</td>
<td>2000</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the patient had an inadequate clinical response of at least <span class="underline">90 days</span> with at least <span class="underline">one preferred</span> oral contraceptive?</p>
<p>If yes, please submit the medication trials and dates.</p></td>
<td>Y</td>
<td>2002</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N</td>
<td>2001</td>
</tr>
<tr class="even">
<td>9</td>
<td>2001</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the provider submitted documentation of medical necessity beyond convenience for why the patient cannot be changed to a preferred drug (i.e., allergies, drug-drug interactions, contraindications, or intolerances)?</p>
<p>If yes, please submit the medication name and reason for inability to use.</p></td>
<td>Y</td>
<td>2002</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N</td>
<td>1236</td>
</tr>
<tr class="even">
<td>10</td>
<td>2002</td>
<td></td>
<td>Select</td>
<td><p>Ohio Medicaid covers a total lifetime duration of therapy of 730 days between Oriahnn and Myfembree.</p>
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
<td>11</td>
<td>1233</td>
<td></td>
<td>Select and Free Text  </td>
<td>Has the provider submitted documentation of the patient’s clinical response to treatment and ongoing safety monitoring?</td>
<td>Y    </td>
<td>1234</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N    </td>
<td>1235 </td>
</tr>
<tr class="even">
<td>12</td>
<td>1234</td>
<td></td>
<td>Select</td>
<td><p>Ohio Medicaid covers a total lifetime duration of therapy of 730 days between Oriahnn and Myfembree (if applicable).</p>
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
<td>13</td>
<td>1235</td>
<td></td>
<td>Free Text</td>
<td>Please provide the rationale for the medication being requested. </td>
<td>END (Pending Manual Review)</td>
<td></td>
</tr>
<tr class="odd">
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

LENGTH OF AUTHORIZATIONS: Endometriosis- 365 Days; Uterine Fibroids- Up to 180 days

|||
| ------------------ | -------- |
| **Last Approved ** | 5/5/2023 |
| **Other**          |          |
