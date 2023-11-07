# CV Agents - Angina, Hypertension & Heart Failure

|||
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Criteria 1 | Hemangeol (P, PA)                                                                                                                                                                                                                                                                                                                                           |
| Criteria 2 | Entresto (P, PA)                                                                                                                                                                                                                                                                                                                                            |
| Criteria 3 | Kerendia (NP)                                                                                                                                                                                                                                                                                                                                               |
| Criteria 4 | Camzyos (NP)                                                                                                                                                                                                                                                                                                                                                |
| Criteria 5 | Verquvo (NP)                                                                                                                                                                                                                                                                                                                                                |
| Criteria 6 | Sotylize Soln (NP, AR)                                                                                                                                                                                                                                                                                                                                      |
| Criteria 7 | Non-Dihydropyridines: Diltiazem 24HR ER Tabs (NP, QL), Verapamil 200, 300mg ER 24HR (NP, QL)                                                                                                                                                                                                                                                                |
| Criteria 8 | NP Agents: Aliskiren, Aspruzyo Sprinkle, Candesartan, Candesartan/HCTZ, Carospir, Carvedilol ER, Clonidine ER (generic of Nexicon XR), Corlanor, Edarbi, Edarbyclor, Hydralazine/HCTZ, Innopran XL, Israpidine, Kapspargo, Katerzia, Levamlodipine, Nebivolol (BvG), Nisoldipine, Norliqva, Nymalize, Qbrelis, Tekturna/HCTZ, Telmisartan, Telmisartan/HCTZ |
| Criteria 9 | Nimodipine (NP)                                                                                                                                                                                                                                                                                                                                             |

## Hemangeol

<table>
<thead>
<tr class="header">
<th><strong>Criteria Title</strong> </th>
<th>Cardiovascular Agents: Angina, Hypertension &amp; Heart Failure</th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Criteria Subtitle</strong> </td>
<td>Hemangeol</td>
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
<td>Corresponding Code(s) </td>
<td>Type of Code (GCNSeqNo, HICL, NDC) </td>
</tr>
<tr class="even">
<td></td>
<td>HEMANGEOL</td>
<td>072352</td>
<td>GCNSeqNo</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr class="header">
<th><strong>Sequence Number</strong>    </th>
<th><strong>Question ID</strong>    </th>
<th><strong>Default Next Question ID</strong>    </th>
<th><strong>Question Type</strong>    </th>
<th><strong>Question Text</strong>    </th>
<th><strong>Choice Text</strong>    </th>
<th><strong>Next Question ID</strong>    </th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>0009 </td>
<td>  </td>
<td>Select  </td>
<td>Is the patient new to therapy (initial authorization request) or continuing therapy (re-authorization request)?   </td>
<td>New Start (initial authorization request)</td>
<td>1000</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Continuation (re-authorization request) </td>
<td>1233</td>
</tr>
<tr class="odd">
<td>2  </td>
<td>1000 </td>
<td>  </td>
<td>Select  </td>
<td>Is this request being prescribed in accordance with Food and Drug Administration (FDA) approved labeling? </td>
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
<td>1235 </td>
</tr>
<tr class="odd">
<td>3</td>
<td>1001</td>
<td>  </td>
<td>Select and Free Text </td>
<td><p>Has the provider submitted documentation of the patient’s weight?</p>
<p> </p>
<p>If yes, please submit documentation.</p></td>
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
<td>1235</td>
</tr>
<tr class="odd">
<td>4</td>
<td>1233 </td>
<td>  </td>
<td>Select and Free Text    </td>
<td>Has the provider submitted documentation of the patient’s clinical response to treatment and ongoing safety monitoring? </td>
<td>Y </td>
<td>1234</td>
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
<td>1234</td>
<td></td>
<td>Select and Free Text </td>
<td><p>Has the provider submitted documentation of the patient’s weight?</p>
<p>  </p>
<p>If yes, please submit documentation.</p></td>
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
<td>1235</td>
</tr>
<tr class="odd">
<td>6</td>
<td>1235   </td>
<td>   </td>
<td>Free Text  </td>
<td>Please provide the rationale for the medication being requested.   </td>
<td>END (Pending Manual Review)  </td>
<td></td>
</tr>
</tbody>
</table>

LENGTH OF AUTHORIZATIONS: 365 Days

|||
| ------------------ | --------- |
| **Last Approved ** | 5/16/2023 |
| **Other**          |           |

## Entresto

<table>
<thead>
<tr class="header">
<th><strong>Criteria Title</strong> </th>
<th>Cardiovascular Agents: Angina, Hypertension &amp; Heart Failure</th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Criteria Subtitle</strong> </td>
<td>Entresto</td>
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
<td>Corresponding Code(s) </td>
<td>Type of Code (GCNSeqNo, HICL, NDC) </td>
</tr>
<tr class="even">
<td></td>
<td>ENTRESTO</td>
<td>074408</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>ENTRESTO</td>
<td>074409</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>ENTRESTO</td>
<td>074410</td>
<td>GCNSeqNo</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr class="header">
<th><strong>Sequence Number</strong>    </th>
<th><strong>Question ID</strong>    </th>
<th><strong>Default Next Question ID</strong>    </th>
<th><strong>Question Type</strong>    </th>
<th><strong>Question Text</strong>    </th>
<th><strong>Choice Text</strong>    </th>
<th><strong>Next Question ID</strong>    </th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>0009 </td>
<td>  </td>
<td>Select  </td>
<td>Is the patient new to therapy (initial authorization request) or continuing therapy (re-authorization request)?   </td>
<td>New Start (initial authorization request)</td>
<td>1000</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Continuation (re-authorization request) </td>
<td>1233</td>
</tr>
<tr class="odd">
<td>2  </td>
<td>1000 </td>
<td>  </td>
<td>Select  </td>
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
<td>1235 </td>
</tr>
<tr class="odd">
<td>3</td>
<td>1001</td>
<td>  </td>
<td>Select and Free Text </td>
<td><p>Has the provider submitted documentation of chronic heart failure classified as either New York Heart Association (NYHA) Class II-IV</p>
<p>or American College of Cardiology (ACC)/American Heart Association (AHA) Stage B-D?</p></td>
<td>Y </td>
<td>END (Approve x 365 days) </td>
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
<td>4</td>
<td>1233 </td>
<td>  </td>
<td>Select and Free Text   </td>
<td>Has the provider submitted documentation of the patient’s clinical response to treatment and ongoing safety monitoring? </td>
<td>Y </td>
<td>1234</td>
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
<td>1234</td>
<td></td>
<td>Select and Free Text </td>
<td><p>Has the provider submitted documentation of chronic heart failure classified as either New York Heart Association (NYHA) Class II-IV</p>
<p>or American College of Cardiology (ACC)/American Heart Association (AHA) Stage B-D?</p></td>
<td>Y </td>
<td>END (Approve x 365 days) </td>
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
<td>6</td>
<td>1235   </td>
<td>   </td>
<td>Free Text  </td>
<td>Please provide the rationale for the medication being requested.   </td>
<td>END (Pending Manual Review)  </td>
<td></td>
</tr>
</tbody>
</table>

LENGTH OF AUTHORIZATIONS: 365 Days

|||
| ------------------ | --------- |
| **Last Approved ** | 5/16/2023 |
| **Other**          |           |

## Kerendia

<table>
<thead>
<tr class="header">
<th><strong>Criteria Title</strong> </th>
<th>Cardiovascular Agents: Angina, Hypertension &amp; Heart Failure</th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Criteria Subtitle</strong> </td>
<td>Kerendia</td>
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
<td>KERENDIA</td>
<td>082499</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>KERENDIA</td>
<td>082500</td>
<td>GCNSeqNo</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr class="header">
<th><strong>Sequence Number</strong>    </th>
<th><strong>Question ID</strong>    </th>
<th><strong>Default Next Question ID</strong>    </th>
<th><strong>Question Type</strong>    </th>
<th><strong>Question Text</strong>    </th>
<th><strong>Choice Text</strong>    </th>
<th><strong>Next Question ID</strong>    </th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>0009 </td>
<td>  </td>
<td>Select  </td>
<td>Is the patient new to therapy (initial authorization request) or continuing therapy (re-authorization request)?   </td>
<td>New Start (initial authorization request)</td>
<td>1000</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Continuation (re-authorization request) </td>
<td>1234</td>
</tr>
<tr class="odd">
<td>2  </td>
<td>1000 </td>
<td>  </td>
<td>Select  </td>
<td>Is this request being prescribed in accordance with Food and Drug Administration (FDA) approved labeling? </td>
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
<td>1235 </td>
</tr>
<tr class="odd">
<td>3 </td>
<td>1001 </td>
<td>  </td>
<td>Select and Free Text  </td>
<td><p>Has the patient had an inadequate clinical response of at least <span class="underline">30 days</span> of at least <span class="underline">two preferred</span> drugs <span class="underline">within the same class</span>, if indicated for diagnosis?    </p>
<p>  </p>
<p>If yes, please submit the medication trials and dates. </p></td>
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
<td>4 </td>
<td>1002 </td>
<td>  </td>
<td>Select and Free Text </td>
<td><p>Has the provider submitted documentation of medical necessity beyond convenience for why the patient cannot be changed to a preferred drug (i.e., allergies, drug-drug interactions, contraindications, or intolerances)? </p>
<p>  </p>
<p>If yes, please submit the medication name and reason for inability to use.</p></td>
<td>Y </td>
<td>1003 </td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N </td>
<td>1236 </td>
</tr>
<tr class="odd">
<td>5</td>
<td>1003</td>
<td></td>
<td>Select</td>
<td>Does the provider attest that the patient is on a maximally tolerated dose of an angiotensin-converting enzyme inhibitor or angiotensin receptor blocker?</td>
<td>Y </td>
<td>1004</td>
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
<td>6</td>
<td>1004</td>
<td></td>
<td>Select and Free Text  </td>
<td>Has the provider submitted documentation of an inadequate clinical response to a SGLT2 Inhibitor?</td>
<td>Y </td>
<td>1006</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N </td>
<td>1005</td>
</tr>
<tr class="odd">
<td>7</td>
<td>1005</td>
<td></td>
<td>Select and Free Text  </td>
<td><p>Has the provider submitted documentation of medical necessity beyond convenience for why the</p>
<p>patient cannot try a SGLT2 inhibitor (i.e., chronic kidney disease diagnosis)?</p></td>
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
<td>8 </td>
<td>1006</td>
<td> </td>
<td>Select  </td>
<td><p>Is the request for any of the following:  </p>
<p>1) a nonsolid oral dosage formulation</p>
<p>2) a non-preferred extended release formulation </p>
<p>3) a non-preferred brand name that has a preferred generic product </p></td>
<td>Y </td>
<td>1007</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N </td>
<td>END (Pending Manual Review)</td>
</tr>
<tr class="odd">
<td>9</td>
<td>1007</td>
<td> </td>
<td>Select and Free Text  </td>
<td>Has the provider submitted documentation of medical necessity for the requested product (i.e. medical reasons for why the patient cannot be changed to a solid oral dosage formulation, inadequate clinical response with a product’s immediate release formulation, or inadequate clinical response or allergy of two or more generic labelers)? </td>
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
<td>1235 </td>
</tr>
<tr class="odd">
<td>10</td>
<td>1234 </td>
<td>  </td>
<td><p>Select and Free Text   </p>
<p>     </p></td>
<td>Has the provider submitted documentation of the patient’s clinical response to treatment and ongoing safety monitoring? </td>
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
<td>11</td>
<td>1235   </td>
<td>   </td>
<td>Free Text  </td>
<td>Please provide the rationale for the medication being requested.   </td>
<td>END (Pending Manual Review)  </td>
<td></td>
</tr>
<tr class="even">
<td>12</td>
<td>1236  </td>
<td>  </td>
<td>Free Text  </td>
<td>Please explain the reason(s) why the patient is unable to use medications not requiring prior approval.  </td>
<td>END (Pending Manual Review) </td>
<td></td>
</tr>
</tbody>
</table>

LENGTH OF AUTHORIZATIONS: 365 Days

|||
| ------------------ | --------- |
| **Last Approved ** | 5/16/2023 |
| **Other**          |           |

## Camzyos

<table>
<thead>
<tr class="header">
<th><strong>Criteria Title</strong> </th>
<th>Cardiovascular Agents: Angina, Hypertension &amp; Heart Failure</th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Criteria Subtitle</strong> </td>
<td>Camzyos</td>
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
<td>CAMZYOS</td>
<td>083317</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>CAMZYOS</td>
<td>083318</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>CAMZYOS</td>
<td>083319</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>CAMZYOS</td>
<td>083320</td>
<td>GCNSeqNo</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr class="header">
<th><strong>Sequence Number</strong>    </th>
<th><strong>Question ID</strong>    </th>
<th><strong>Default Next Question ID</strong>    </th>
<th><strong>Question Type</strong>    </th>
<th><strong>Question Text</strong>    </th>
<th><strong>Choice Text</strong>    </th>
<th><strong>Next Question ID</strong>    </th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>0009 </td>
<td>  </td>
<td>Select  </td>
<td>Is the patient new to therapy (initial authorization request) or continuing therapy (re-authorization request)?   </td>
<td>New Start (initial authorization request)</td>
<td>1000</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Continuation (re-authorization request) </td>
<td>1234</td>
</tr>
<tr class="odd">
<td>2  </td>
<td>1000 </td>
<td>  </td>
<td>Select  </td>
<td>Is this request being prescribed in accordance with Food and Drug Administration (FDA) approved labeling? </td>
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
<td>1235 </td>
</tr>
<tr class="odd">
<td>3 </td>
<td>1001 </td>
<td>  </td>
<td>Select and Free Text  </td>
<td><p>Has the patient had an inadequate clinical response of at least <span class="underline">30 days</span> of at least <span class="underline">two preferred</span> drugs <span class="underline">within the same class</span>, if indicated for diagnosis?    </p>
<p>  </p>
<p>If yes, please submit the medication trials and dates. </p></td>
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
<td>4 </td>
<td>1002 </td>
<td>  </td>
<td>Select and Free Text </td>
<td><p>Has the provider submitted documentation of medical necessity beyond convenience for why the patient cannot be changed to a preferred drug (i.e., allergies, drug-drug interactions, contraindications, or intolerances)? </p>
<p>  </p>
<p>If yes, please submit the medication name and reason for inability to use. </p></td>
<td>Y </td>
<td>1003 </td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N </td>
<td>1236 </td>
</tr>
<tr class="odd">
<td>5</td>
<td>1003</td>
<td></td>
<td>Select</td>
<td>Is the medication being prescribed by or in consultation with a cardiologist?</td>
<td>Y </td>
<td>1004</td>
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
<td>6</td>
<td>1004</td>
<td></td>
<td>Select and Free Text  </td>
<td><p>Has the provider submitted documentation of New York Heart Association (NYHA) Class II-III symptoms and left ventricular</p>
<p>ejection fraction greater than or equal to 55 percent?</p>
<p>If yes, please submit documentation.</p></td>
<td>Y </td>
<td>1005</td>
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
<td>7 </td>
<td>1005</td>
<td> </td>
<td>Select  </td>
<td><p>Is the request for any of the following:  </p>
<p>1) a nonsolid oral dosage formulation</p>
<p>2) a non-preferred extended release formulation </p>
<p>3) a non-preferred brand name that has a preferred generic product </p></td>
<td>Y </td>
<td>1006</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N </td>
<td>END (Pending Manual Review)</td>
</tr>
<tr class="odd">
<td>8</td>
<td>1006</td>
<td> </td>
<td>Select and Free Text  </td>
<td>Has the provider submitted documentation of medical necessity for the requested product (i.e. medical reasons for why the patient cannot be changed to a solid oral dosage formulation, inadequate clinical response with a product’s immediate release formulation, or inadequate clinical response or allergy of two or more generic labelers)? </td>
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
<td>1235 </td>
</tr>
<tr class="odd">
<td>9</td>
<td>1234 </td>
<td>  </td>
<td><p>Select and Free Text   </p>
<p>     </p></td>
<td>Has the provider submitted documentation of the patient’s clinical response to treatment and ongoing safety monitoring? </td>
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
<td>10</td>
<td>1235   </td>
<td>   </td>
<td>Free Text  </td>
<td>Please provide the rationale for the medication being requested.   </td>
<td>END (Pending Manual Review)  </td>
<td></td>
</tr>
<tr class="even">
<td>11</td>
<td>1236  </td>
<td>  </td>
<td>Free Text  </td>
<td>Please explain the reason(s) why the patient is unable to use medications not requiring prior approval.  </td>
<td>END (Pending Manual Review) </td>
<td></td>
</tr>
</tbody>
</table>

LENGTH OF AUTHORIZATIONS: 365 Days

|||
| ------------------ | --------- |
| **Last Approved ** | 5/16/2023 |
| **Other**          |           |

## Verquvo

<table>
<thead>
<tr class="header">
<th><strong>Criteria Title</strong> </th>
<th>Cardiovascular Agents: Angina, Hypertension &amp; Heart Failure</th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Criteria Subtitle</strong> </td>
<td>Verquvo</td>
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
<td>VERQUVO</td>
<td>081858</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>VERQUVO</td>
<td>081859</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>VERQUVO</td>
<td>081860</td>
<td>GCNSeqNo</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr class="header">
<th><strong>Sequence Number</strong>    </th>
<th><strong>Question ID</strong>    </th>
<th><strong>Default Next Question ID</strong>    </th>
<th><strong>Question Type</strong>    </th>
<th><strong>Question Text</strong>    </th>
<th><strong>Choice Text</strong>    </th>
<th><strong>Next Question ID</strong>    </th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>0009 </td>
<td>  </td>
<td>Select  </td>
<td>Is the patient new to therapy (initial authorization request) or continuing therapy (re-authorization request)?   </td>
<td>New Start (initial authorization request)</td>
<td>1000</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Continuation (re-authorization request) </td>
<td>1234</td>
</tr>
<tr class="odd">
<td>2  </td>
<td>1000 </td>
<td>  </td>
<td>Select  </td>
<td>Is this request being prescribed in accordance with Food and Drug Administration (FDA) approved labeling? </td>
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
<td>1235 </td>
</tr>
<tr class="odd">
<td>3 </td>
<td>1001 </td>
<td>  </td>
<td>Select and Free Text  </td>
<td><p>Has the patient had an inadequate clinical response of at least <span class="underline">30 days</span> of at least <span class="underline">two preferred</span> drugs <span class="underline">within the same class</span>, if indicated for diagnosis?    </p>
<p>  </p>
<p>If yes, please submit the medication trials and dates. </p></td>
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
<td>4 </td>
<td>1002 </td>
<td>  </td>
<td>Select and Free Text </td>
<td><p>Has the provider submitted documentation of medical necessity beyond convenience for why the patient cannot be changed to a preferred drug (i.e., allergies, drug-drug interactions, contraindications, or intolerances)? </p>
<p>  </p>
<p>If yes, please submit the medication name and reason for inability to use. </p></td>
<td>Y </td>
<td>1003 </td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N </td>
<td>1236 </td>
</tr>
<tr class="odd">
<td>5</td>
<td>1003</td>
<td></td>
<td>Select and Free Text</td>
<td>Has the provider submitted documentation of the patient’s ejection fraction?</td>
<td>Y </td>
<td>1004</td>
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
<td>6</td>
<td>1004</td>
<td></td>
<td>Select</td>
<td>Has the patient been hospitalized for the treatment of heart failure in the previous 180 days?</td>
<td>Y </td>
<td>1006</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N </td>
<td>1005</td>
</tr>
<tr class="odd">
<td>7 </td>
<td>1005</td>
<td></td>
<td>Select</td>
<td>Has the patient needed treatment with an outpatient intravenous diuretic in the previous 90 days?</td>
<td>Y </td>
<td>1006</td>
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
<td>8</td>
<td>1006</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the patient been treated with an agent from ALL the following unless contraindicated:</p>
<p>1.Angiotensin-converting enzyme inhibitor, angiotensin II receptor blocker, OR an angiotensin receptor neprilysin inhibitor</p>
<p>2.Beta-blocker</p>
<p>3.Aldosterone antagonist and/or SGLT2 inhibitor as appropriate for renal function</p>
<p>If yes, please submit documentation.</p></td>
<td>Y</td>
<td>1007</td>
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
<td>1007</td>
<td> </td>
<td>Select  </td>
<td><p>Is the request for any of the following:  </p>
<p>1) a nonsolid oral dosage formulation</p>
<p>2) a non-preferred extended release formulation </p>
<p>3) a non-preferred brand name that has a preferred generic product </p></td>
<td>Y </td>
<td>1008</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N </td>
<td>END (Pending Manual Review)</td>
</tr>
<tr class="odd">
<td>10</td>
<td>1008</td>
<td> </td>
<td>Select and Free Text  </td>
<td>Has the provider submitted documentation of medical necessity for the requested product (i.e. medical reasons for why the patient cannot be changed to a solid oral dosage formulation, inadequate clinical response with a product’s immediate release formulation, or inadequate clinical response or allergy of two or more generic labelers)? </td>
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
<td>1235 </td>
</tr>
<tr class="odd">
<td>11</td>
<td>1234 </td>
<td>  </td>
<td><p>Select and Free Text   </p>
<p>     </p></td>
<td>Has the provider submitted documentation of the patient’s clinical response to treatment and ongoing safety monitoring? </td>
<td>Y </td>
<td>END (Pending Manual Review) </td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N</td>
<td>1235 </td>
</tr>
<tr class="odd">
<td>12</td>
<td>1235   </td>
<td>   </td>
<td>Free Text  </td>
<td>Please provide the rationale for the medication being requested.   </td>
<td>END (Pending Manual Review)  </td>
<td></td>
</tr>
<tr class="even">
<td>13</td>
<td>1236  </td>
<td>  </td>
<td>Free Text  </td>
<td>Please explain the reason(s) why the patient is unable to use medications not requiring prior approval.  </td>
<td>END (Pending Manual Review) </td>
<td></td>
</tr>
</tbody>
</table>

LENGTH OF AUTHORIZATIONS: 365 Days

|||
| ------------------ | --------- |
| **Last Approved ** | 5/16/2023 |
| **Other**          |           |

## Sotylize Soln

<table>
<thead>
<tr class="header">
<th><strong>Criteria Title</strong> </th>
<th>Cardiovascular Agents: Angina, Hypertension &amp; Heart Failure</th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Criteria Subtitle</strong> </td>
<td>Sotylize Soln</td>
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
<td>SOTYLIZE SOLN</td>
<td>073475</td>
<td>GCNSeqNo</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr class="header">
<th><strong>Sequence Number</strong>    </th>
<th><strong>Question ID</strong>    </th>
<th><strong>Default Next Question ID</strong>    </th>
<th><strong>Question Type</strong>    </th>
<th><strong>Question Text</strong>    </th>
<th><strong>Choice Text</strong>    </th>
<th><strong>Next Question ID</strong>    </th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>0999 </td>
<td>  </td>
<td>Select  </td>
<td>Is the patient new to therapy (initial authorization request) or continuing therapy (re-authorization request)?   </td>
<td>New Start (initial authorization request)</td>
<td>1000</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Continuation (re-authorization request) </td>
<td>1234</td>
</tr>
<tr class="odd">
<td>2</td>
<td>1000 </td>
<td>  </td>
<td>Select  </td>
<td>Is this request being prescribed in accordance with Food and Drug Administration (FDA) approved labeling? </td>
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
<td>1235 </td>
</tr>
<tr class="odd">
<td>3</td>
<td>1001 </td>
<td>  </td>
<td>Select and Free Text  </td>
<td><p>Has the patient had an inadequate clinical response of at least <span class="underline">30 days</span> of at least <span class="underline">two preferred</span> drugs <span class="underline">within the same class</span>, if indicated for diagnosis?    </p>
<p>  </p>
<p>If yes, please submit the medication trials and dates. </p></td>
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
<td>4</td>
<td>1002 </td>
<td>  </td>
<td>Select and Free Text </td>
<td><p>Has the provider submitted documentation of medical necessity beyond convenience for why the patient cannot be changed to a preferred drug (i.e., allergies, drug-drug interactions, contraindications, or intolerances)? </p>
<p>  </p>
<p>If yes, please submit the medication name and reason for inability to use. </p></td>
<td>Y </td>
<td>1003 </td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N </td>
<td>1236 </td>
</tr>
<tr class="odd">
<td>5</td>
<td>1003</td>
<td> </td>
<td>Select  </td>
<td><p>Is the request for any of the following:  </p>
<p>1) a nonsolid oral dosage formulation</p>
<p>2) a non-preferred extended release formulation </p>
<p>3) a non-preferred brand name that has a preferred generic product </p></td>
<td>Y </td>
<td>1004</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N </td>
<td>1005</td>
</tr>
<tr class="odd">
<td>6</td>
<td>1004</td>
<td> </td>
<td>Select and Free Text  </td>
<td>Has the provider submitted documentation of medical necessity for the requested product (i.e. medical reasons for why the patient cannot be changed to a solid oral dosage formulation, inadequate clinical response with a product’s immediate release formulation, or inadequate clinical response or allergy of two or more generic labelers)? </td>
<td>Y </td>
<td>1005</td>
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
<td>1005</td>
<td></td>
<td>Select</td>
<td>Is the patient 6 years of age and older?</td>
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
<td>8</td>
<td>1006</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Is the patient unable to swallow a tablet and/or capsule formulation?</p>
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
<td>9 </td>
<td>1234 </td>
<td>  </td>
<td><p>Select and Free Text   </p>
<p>     </p></td>
<td><p>Has the provider submitted documentation of the patient’s clinical response to treatment and ongoing safety monitoring? </p>
<p>   </p></td>
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
<td>10</td>
<td>1235   </td>
<td>   </td>
<td>Free Text  </td>
<td>Please provide the rationale for the medication being requested.   </td>
<td>END (Pending Manual Review)  </td>
<td></td>
</tr>
<tr class="even">
<td>11</td>
<td>1236  </td>
<td>  </td>
<td>Free Text  </td>
<td>Please explain the reason(s) why the patient is unable to use medications not requiring prior approval.  </td>
<td>END (Pending Manual Review) </td>
<td></td>
</tr>
</tbody>
</table>

LENGTH OF AUTHORIZATIONS: 365 Days

|||
| ------------------ | --------- |
| **Last Approved ** | 5/16/2023 |
| **Other**          |           |

## Non-Preferred Non-Dihydropyridines

<table>
<thead>
<tr class="header">
<th><strong>Criteria Title</strong> </th>
<th>Cardiovascular Agents: Angina, Hypertension &amp; Heart Failure</th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Criteria Subtitle</strong> </td>
<td>Non-Preferred Non-Dihydropyridines</td>
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
<td>DILTIAZEM 24 HR ER TABS</td>
<td>051802</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>DILTIAZEM 24 HR ER TABS</td>
<td>051803</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>DILTIAZEM 24 HR ER TABS</td>
<td>051804</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>DILTIAZEM 24 HR ER TABS</td>
<td>051805</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>DILTIAZEM 24 HR ER TABS</td>
<td>051806</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>DILTIAZEM 24 HR ER TABS</td>
<td>051801</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>VERAPAMIL 200, 300 mg ER 24 HR</td>
<td>041652</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>VERAPAMIL 200, 300 mg ER 24 HR</td>
<td>041653</td>
<td>GCNSeqNo</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr class="header">
<th><strong>Sequence Number</strong>    </th>
<th><strong>Question ID</strong>    </th>
<th><strong>Default Next Question ID</strong>    </th>
<th><strong>Question Type</strong>    </th>
<th><strong>Question Text</strong>    </th>
<th><strong>Choice Text</strong>    </th>
<th><strong>Next Question ID</strong>    </th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>0009 </td>
<td>  </td>
<td>Select  </td>
<td>Is the patient new to therapy (initial authorization request) or continuing therapy (re-authorization request)?   </td>
<td>New Start (initial authorization request)</td>
<td>1000</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Continuation (re-authorization request) </td>
<td>1234</td>
</tr>
<tr class="odd">
<td>2  </td>
<td>1000 </td>
<td>  </td>
<td>Select  </td>
<td>Is this request being prescribed in accordance with Food and Drug Administration (FDA) approved labeling? </td>
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
<td>1235 </td>
</tr>
<tr class="odd">
<td>3 </td>
<td>1001 </td>
<td>  </td>
<td>Select and Free Text  </td>
<td><p>Has the patient had an inadequate clinical response of at least <span class="underline">30 days</span> of at least <span class="underline">two preferred</span> drugs <span class="underline">within the same class</span>, if indicated for diagnosis?    </p>
<p>  </p>
<p>If yes, please submit the medication trials and dates. </p></td>
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
<td>4 </td>
<td>1002 </td>
<td>  </td>
<td>Select and Free Text </td>
<td><p>Has the provider submitted documentation of medical necessity beyond convenience for why the patient cannot be changed to a preferred drug (i.e., allergies, drug-drug interactions, contraindications, or intolerances)? </p>
<p>  </p>
<p>If yes, please submit the medication name and reason for inability to use. </p></td>
<td>Y </td>
<td>1003 </td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N </td>
<td>1236 </td>
</tr>
<tr class="odd">
<td>5</td>
<td>1003</td>
<td> </td>
<td>Select  </td>
<td><p>Is the request for any of the following:  </p>
<p>1) a nonsolid oral dosage formulation</p>
<p>2) a non-preferred extended release formulation </p>
<p>3) a non-preferred brand name that has a preferred generic product </p></td>
<td>Y </td>
<td>1004</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N </td>
<td>END (Pending Manual Review)</td>
</tr>
<tr class="odd">
<td>6</td>
<td>1004</td>
<td> </td>
<td>Select and Free Text  </td>
<td>Has the provider submitted documentation of medical necessity for the requested product (i.e. medical reasons for why the patient cannot be changed to a solid oral dosage formulation, inadequate clinical response with a product’s immediate release formulation, or inadequate clinical response or allergy of two or more generic labelers)? </td>
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
<td>1235 </td>
</tr>
<tr class="odd">
<td>7 </td>
<td>1234 </td>
<td>  </td>
<td><p>Select and Free Text   </p>
<p>     </p></td>
<td>Has the provider submitted documentation of the patient’s clinical response to treatment and ongoing safety monitoring? </td>
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
<td>8 </td>
<td>1235   </td>
<td>   </td>
<td>Free Text  </td>
<td>Please provide the rationale for the medication being requested.   </td>
<td>END (Pending Manual Review)  </td>
<td></td>
</tr>
<tr class="even">
<td>9</td>
<td>1236  </td>
<td>  </td>
<td>Free Text  </td>
<td>Please explain the reason(s) why the patient is unable to use medications not requiring prior approval.  </td>
<td>END (Pending Manual Review) </td>
<td></td>
</tr>
</tbody>
</table>

LENGTH OF AUTHORIZATIONS: 365 Days

|||
| ------------------ | --------- |
| **Last Approved ** | 5/16/2023 |
| **Other**          |           |

## Non-Preferred Products

<table>
<thead>
<tr class="header">
<th><strong>Criteria Title</strong> </th>
<th>Cardiovascular Agents: Angina, Hypertension &amp; Heart Failure</th>
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
<td>ALISKIREN</td>
<td>062288</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>ALISKIREN</td>
<td>062289</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>ASPRUZYO SPRINKLE</td>
<td>083128</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>ASPRUZYO SPRINKLE</td>
<td>083129</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>CANDESARTAN</td>
<td>037015</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>CANDESARTAN</td>
<td>037016</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>CANDESARTAN</td>
<td>037017</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>CANDESARTAN</td>
<td>040659</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>CANDESARTAN/HCTZ</td>
<td>045425</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>CANDESARTAN/HCTZ</td>
<td>046624</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>CANDESARTAN/HCTZ</td>
<td>064285</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>CAROSPIR</td>
<td>046605</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>CARVEDILOL ER</td>
<td>061811</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>CARVEDILOL ER</td>
<td>061812</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>CARVEDILOL ER</td>
<td>061813</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>CARVEDILOL ER</td>
<td>061814</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>CLONIDINE HCL ER</td>
<td>066917</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>CORLANOR</td>
<td>060186</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>CORLANOR</td>
<td>060187</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>CORLANOR</td>
<td>079666</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>EDARBI</td>
<td>067113</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>EDARBI</td>
<td>067115</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>EDARBYCLOR</td>
<td>068389</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>EDARBYCLOR</td>
<td>068390</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>INNOPRAN XL</td>
<td>033370</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>INNOPRAN XL</td>
<td>051907</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>ISRADIPINE</td>
<td>015888</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>ISRADIPINE</td>
<td>015889</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>KAPSPARGO</td>
<td>078119</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>KAPSPARGO</td>
<td>078120</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>KAPSPARGO</td>
<td>078121</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>KAPSPARGO</td>
<td>078122</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>KATERZIA</td>
<td>079995</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>LEVAMLODIPINE</td>
<td>080610</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>LEVAMLODIPINE</td>
<td>080611</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>NEBIVOLOL</td>
<td>036654</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>NEBIVOLOL</td>
<td>063510</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>NEBIVOLOL</td>
<td>063511</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>NEBIVOLOL</td>
<td>064945</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>NISOLDIPINE</td>
<td>024499</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>NISOLDIPINE</td>
<td>024500</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>NISOLDIPINE</td>
<td>024501</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>NISOLDIPINE</td>
<td>063730</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>NISOLDIPINE</td>
<td>063731</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>NISOLDIPINE</td>
<td>063732</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>NISOLDIPINE</td>
<td>063733</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>NORLIQVA</td>
<td>080176</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>NYMALIZE</td>
<td>080991</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>NYMALIZE</td>
<td>080992</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>NYMALIZE</td>
<td>082451</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>QBRELIS</td>
<td>076442</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>TEKTURNA/HCTZ</td>
<td>063589</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>TEKTURNA/HCTZ</td>
<td>063590</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>TEKTURNA/HCTZ</td>
<td>063591</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>TEKTURNA/HCTZ</td>
<td>063592</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>TELMISARTAN</td>
<td>040910</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>TELMISARTAN</td>
<td>040911</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>TELMISARTAN</td>
<td>047126</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>TELMISARTAN/HCTZ</td>
<td>047324</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>TELMISARTAN/HCTZ</td>
<td>047326</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>TELMISARTAN/HCTZ</td>
<td>057690</td>
<td>GCNSeqNo</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr class="header">
<th><strong>Sequence Number</strong>    </th>
<th><strong>Question ID</strong>    </th>
<th><strong>Default Next Question ID</strong>    </th>
<th><strong>Question Type</strong>    </th>
<th><strong>Question Text</strong>    </th>
<th><strong>Choice Text</strong>    </th>
<th><strong>Next Question ID</strong>    </th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>0009 </td>
<td>  </td>
<td>Select  </td>
<td>Is the patient new to therapy (initial authorization request) or continuing therapy (re-authorization request)?   </td>
<td>New Start (initial authorization request)</td>
<td>1000</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Continuation (re-authorization request) </td>
<td>1234</td>
</tr>
<tr class="odd">
<td>2  </td>
<td>1000 </td>
<td>  </td>
<td>Select  </td>
<td>Is this request being prescribed in accordance with Food and Drug Administration (FDA) approved labeling? </td>
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
<td>1235 </td>
</tr>
<tr class="odd">
<td>3 </td>
<td>1001 </td>
<td>  </td>
<td>Select and Free Text  </td>
<td><p>Has the patient had an inadequate clinical response of at least <span class="underline">30 days</span> of at least <span class="underline">two preferred</span> drugs <span class="underline">within the same class</span>, if indicated for diagnosis?    </p>
<p>  </p>
<p>If yes, please submit the medication trials and dates. </p></td>
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
<td>4 </td>
<td>1002 </td>
<td>  </td>
<td>Select and Free Text </td>
<td><p>Has the provider submitted documentation of medical necessity beyond convenience for why the patient cannot be changed to a preferred drug (i.e., allergies, drug-drug interactions, contraindications, or intolerances)? </p>
<p>  </p>
<p>If yes, please submit the medication name and reason for inability to use. </p></td>
<td>Y </td>
<td>1003 </td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N </td>
<td>1236 </td>
</tr>
<tr class="odd">
<td>5</td>
<td>1003</td>
<td></td>
<td>Select</td>
<td>Is the request for generic nebivolol?</td>
<td>Y </td>
<td>1004</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N </td>
<td>1005</td>
</tr>
<tr class="odd">
<td>6</td>
<td>1004</td>
<td></td>
<td>Select and Free Text  </td>
<td><p>Has the brand medication been attempted and failed or is the brand medication contraindicated?  </p>
<p>If yes, please submit documentation.</p></td>
<td>Y </td>
<td>1005</td>
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
<td>7</td>
<td>1005</td>
<td> </td>
<td>Select  </td>
<td><p>Is the request for any of the following:  </p>
<p>1) a nonsolid oral dosage formulation</p>
<p>2) a non-preferred extended release formulation </p>
<p>3) a non-preferred brand name that has a preferred generic product </p></td>
<td>Y </td>
<td>1006</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N </td>
<td>END (Pending Manual Review)</td>
</tr>
<tr class="odd">
<td>8 </td>
<td>1006</td>
<td> </td>
<td>Select and Free Text  </td>
<td>Has the provider submitted documentation of medical necessity for the requested product (i.e. medical reasons for why the patient cannot be changed to a solid oral dosage formulation, inadequate clinical response with a product’s immediate release formulation, or inadequate clinical response or allergy of two or more generic labelers)? </td>
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
<td>1235 </td>
</tr>
<tr class="odd">
<td>9</td>
<td>1234 </td>
<td>  </td>
<td><p>Select and Free Text   </p>
<p>     </p></td>
<td><p>Has the provider submitted documentation of the patient’s clinical response to treatment and ongoing safety monitoring? </p>
<p>   </p></td>
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
<td>10</td>
<td>1235   </td>
<td>   </td>
<td>Free Text  </td>
<td>Please provide the rationale for the medication being requested.   </td>
<td>END (Pending Manual Review)  </td>
<td></td>
</tr>
<tr class="even">
<td>11</td>
<td>1236  </td>
<td>  </td>
<td>Free Text  </td>
<td>Please explain the reason(s) why the patient is unable to use medications not requiring prior approval.  </td>
<td>END (Pending Manual Review) </td>
<td></td>
</tr>
</tbody>
</table>

LENGTH OF AUTHORIZATIONS: 365 Days

|||
| ------------------ | --------- |
| **Last Approved ** | 5/16/2023 |
| **Other**          |           |

## Nimodipine

<table>
<thead>
<tr class="header">
<th><strong>Criteria Title</strong> </th>
<th>Cardiovascular Agents: Angina, Hypertension &amp; Heart Failure</th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Criteria Subtitle</strong> </td>
<td>Nimodipine</td>
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
<td>NIMODIPINE</td>
<td>000579</td>
<td>GCNSeqNo</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr class="header">
<th><strong>Sequence Number</strong>    </th>
<th><strong>Question ID</strong>    </th>
<th><strong>Default Next Question ID</strong>    </th>
<th><strong>Question Type</strong>    </th>
<th><strong>Question Text</strong>    </th>
<th><strong>Choice Text</strong>    </th>
<th><strong>Next Question ID</strong>    </th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>0009 </td>
<td>  </td>
<td>Select  </td>
<td>Is the patient new to therapy (initial authorization request) or continuing therapy (re-authorization request)?   </td>
<td>New Start (initial authorization request)</td>
<td>1000</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Continuation (re-authorization request) </td>
<td>1234</td>
</tr>
<tr class="odd">
<td>2  </td>
<td>1000 </td>
<td>  </td>
<td>Select  </td>
<td>Is this request being prescribed in accordance with Food and Drug Administration (FDA) approved labeling? </td>
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
<td>1235 </td>
</tr>
<tr class="odd">
<td>3 </td>
<td>1001 </td>
<td>  </td>
<td>Select and Free Text  </td>
<td><p>Has the patient had an inadequate clinical response of at least <span class="underline">30 days</span> of at least <span class="underline">two preferred</span> drugs <span class="underline">within the same class</span>, if indicated for diagnosis?    </p>
<p>  </p>
<p>If yes, please submit the medication trials and dates. </p></td>
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
<td>4 </td>
<td>1002 </td>
<td>  </td>
<td>Select and Free Text </td>
<td><p>Has the provider submitted documentation of medical necessity beyond convenience for why the patient cannot be changed to a preferred drug (i.e., allergies, drug-drug interactions, contraindications, or intolerances)? </p>
<p>  </p>
<p>If yes, please submit the medication name and reason for inability to use. </p></td>
<td>Y </td>
<td>1003 </td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N </td>
<td>1236 </td>
</tr>
<tr class="odd">
<td>5</td>
<td>1003</td>
<td> </td>
<td>Select  </td>
<td><p>Is the request for any of the following:  </p>
<p>1) a nonsolid oral dosage formulation</p>
<p>2) a non-preferred extended release formulation </p>
<p>3) a non-preferred brand name that has a preferred generic product </p></td>
<td>Y </td>
<td>1004</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N </td>
<td>END (Pending Manual Review)</td>
</tr>
<tr class="odd">
<td>6</td>
<td>1004</td>
<td> </td>
<td>Select and Free Text  </td>
<td>Has the provider submitted documentation of medical necessity for the requested product (i.e. medical reasons for why the patient cannot be changed to a solid oral dosage formulation, inadequate clinical response with a product’s immediate release formulation, or inadequate clinical response or allergy of two or more generic labelers)? </td>
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
<td>1235 </td>
</tr>
<tr class="odd">
<td>7 </td>
<td>1234 </td>
<td>  </td>
<td><p>Select and Free Text   </p>
<p>     </p></td>
<td>Has the provider submitted documentation of the patient’s clinical response to treatment and ongoing safety monitoring? </td>
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
<td>8 </td>
<td>1235   </td>
<td>   </td>
<td>Free Text  </td>
<td>Please provide the rationale for the medication being requested.   </td>
<td>END (Pending Manual Review)  </td>
<td></td>
</tr>
<tr class="even">
<td>9</td>
<td>1236  </td>
<td>  </td>
<td>Free Text  </td>
<td>Please explain the reason(s) why the patient is unable to use medications not requiring prior approval.  </td>
<td>END (Pending Manual Review) </td>
<td></td>
</tr>
</tbody>
</table>

LENGTH OF AUTHORIZATIONS: 21 Days

|||
| ------------------ | --------- |
| **Last Approved ** | 5/16/2023 |
| **Other**          |           |
