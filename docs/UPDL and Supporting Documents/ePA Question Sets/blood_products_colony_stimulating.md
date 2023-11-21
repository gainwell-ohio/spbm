---
search:
  boost: .9
---

# Blood Formation, Coagulation, and Thrombosis Agents - Colony Stimulating Factors  

[Criteria Document](https://mygainwell-my.sharepoint.com/:w:/g/personal/kaelyn_dobbins_gainwelltechnologies_com/EXHUWD4f8wJMqRKQs62HFlIBbT-tGDCFQ6zplb45vatEtw?e=crzYrA){:target="_blank" rel="noopener}

## Criteria { data-search-exclude }

|||
| ---------- | ------------------------------------------------------------------------------------------------------------------- |
| Criteria 1 | Preferred Agents- Neupogen (PA), Nivestym (PA), Nyvepria (PA), Ziextenzo (PA)                                       |
| Criteria 2 | Non-Preferred Agents – Fulphila, Fylnetra, Granix, Leukine, Neulasta, Releuko, Rolvedon, Stimufend, Udenyca, Zarxio |

## Preferred Products

<table>
<thead>
<tr class="header">
<th><strong>Criteria Title</strong></th>
<th>Blood Formation, Coagulation, and Thrombosis Agents: Colony Stimulating Factors</th>
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
<td>Corresponding Code (s)</td>
<td>Type of Code (GCNSeqNo, HICL, NDC)</td>
</tr>
<tr class="even">
<td></td>
<td>NEUPOGEN</td>
<td>015917</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>NEUPOGEN</td>
<td>045996</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>NEUPOGEN</td>
<td>045997</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>NEUPOGEN</td>
<td>046004</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>NIVESTYM</td>
<td>078719</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>NIVESTYM</td>
<td>078720</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>NIVESTYM</td>
<td>078721</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>NIVESTYM</td>
<td>078722</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>NYVEPRIA</td>
<td>081179</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>ZIEXTENZO</td>
<td>080432</td>
<td>GCNSeqNo</td>
</tr>
</tbody>
</table>

  

<table>
<thead>
<tr class="header">
<th><strong>Sequence Number</strong>  </th>
<th><strong>Question ID</strong>  </th>
<th><strong>Default Next Question ID</strong>  </th>
<th><strong>Question Type</strong>  </th>
<th><strong>Question Text</strong>  </th>
<th><strong>Choice Text</strong>  </th>
<th><strong>Next Question ID</strong>  </th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>0999</td>
<td></td>
<td>Select</td>
<td>Is the patient new to therapy (initial authorization request) or continuing therapy (re-authorization request)? </td>
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
<td>Has the provider submitted documentation of the patient’s diagnosis, weight, and duration of treatment?</td>
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
<td>1235</td>
</tr>
<tr class="odd">
<td>4</td>
<td>1233</td>
<td></td>
<td>Select and Free Text</td>
<td>Has the provider submitted documentation of the patient’s clinical response to treatment and ongoing safety monitoring? </td>
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
<td>1235</td>
</tr>
<tr class="odd">
<td>5</td>
<td>1234</td>
<td> </td>
<td>Select</td>
<td>What is the patient’s diagnosis? </td>
<td>Acute Myeloid Leukemia (AML)</td>
<td>END (Pending Manual Review)</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Malignancy at risk for febrile neutropenia or undergoing myeloablative chemotherapy prior to allogeneic or autologous bone marrow transplantation</td>
<td>END (Pending Manual Review)</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Myeloid Engraftment for bone marrow transplant (BMT)</td>
<td>END (Pending Manual Review) </td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Severe, chronic neutropenia with absolute neutrophil count (ANC) of less than 500/mm3 and have symptoms associated with neutropenia (e.g. fever, infections, oropharyngeal ulcers)</td>
<td><p>END (Pending Manual Review)  </p>
<p> </p>
<p> </p></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Hematopoietic radiation injury syndrome</td>
<td>END (Pending Manual Review)</td>
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
<td>6</td>
<td>1235 </td>
<td> </td>
<td>Free Text </td>
<td>Please provide the rationale for the medication being requested.  </td>
<td>END (Pending Manual Review) </td>
<td></td>
</tr>
</tbody>
</table>

LENGTH OF AUTHORIZATIONS:  

![](docs/images/BloodBlood%20Products%20Colony%20Stimulating%20Factors/media/image1.png) 

|||
| ------------------ | --------- |
| **Last Approved ** | 5/26/2023 |
| **Other**          |           |

## Non-Preferred Products

<table>
<thead>
<tr class="header">
<th><strong>Criteria Title</strong></th>
<th>Blood Formation, Coagulation, and Thrombosis Agents: Colony Stimulating Factors</th>
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
<td>Corresponding Code (s)</td>
<td>Type of Code (GCNSeqNo, HICL, NDC)</td>
</tr>
<tr class="even">
<td></td>
<td>FULPHILA</td>
<td>078537</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>FYLNETRA</td>
<td>083437</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>GRANIX</td>
<td>071653</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>GRANIX</td>
<td>071654</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>GRANIX</td>
<td>079217</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>GRANIX</td>
<td>079218</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>LEUKINE</td>
<td>015927</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>NEULASTA</td>
<td>049872</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>NEULASTA</td>
<td>073319</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>RELEUKO</td>
<td>083106</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>RELEUKO</td>
<td>083114</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>RELEUKO</td>
<td>083115</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>RELEUKO</td>
<td>083116</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>ROLVEDON</td>
<td>083823</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>STIMUFEND</td>
<td>083790</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>UDENYCA</td>
<td>079223</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>ZARXIO</td>
<td>073645</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>ZARXIO</td>
<td>073646</td>
<td>GCNSeqNo</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr class="header">
<th><strong>Sequence Number</strong>  </th>
<th><strong>Question ID</strong>  </th>
<th><strong>Default Next Question ID</strong>  </th>
<th><strong>Question Type</strong>  </th>
<th><strong>Question Text</strong>  </th>
<th><strong>Choice Text</strong>  </th>
<th><strong>Next Question ID</strong>  </th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>0999</td>
<td></td>
<td>Select</td>
<td>Is the patient new to therapy (initial authorization request) or continuing therapy (re-authorization request)? </td>
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
<td>Has the provider submitted documentation of the patient’s diagnosis, weight, and duration of treatment?</td>
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
<td><p>Has the patient had an inadequate clinical response of at least <span class="underline">14 days</span> with at least <span class="underline">one</span> preferred drug? </p>
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
<td><p>Has the provider submitted documentation of medical necessity beyond convenience for why the patient cannot be changed to a preferred drug (i.e., allergies, drug-drug interactions, contraindications, or intolerances)?  </p>
<p> </p>
<p>If yes, please submit the medication name and reason for inability to use.   </p></td>
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
<td>1234</td>
</tr>
<tr class="odd">
<td>7</td>
<td>1005</td>
<td></td>
<td>Select and Free Text</td>
<td>Has the provider submitted documentation of medical necessity for the requested product (i.e. medical reasons for why the patient cannot be changed to a solid oral dosage formulation, inadequate clinical response with a product’s immediate release formulation, or inadequate clinical response or allergy of two or more generic labelers)?</td>
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
<td>1235</td>
</tr>
<tr class="odd">
<td>8</td>
<td>1233</td>
<td></td>
<td>Select and Free Text</td>
<td>Has the provider submitted documentation of the patient’s clinical response to treatment and ongoing safety monitoring? </td>
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
<td>1235</td>
</tr>
<tr class="odd">
<td>9</td>
<td>1234</td>
<td> </td>
<td>Select</td>
<td>What is the patient’s diagnosis? </td>
<td>Acute Myeloid Leukemia (AML)</td>
<td>END (Pending Manual Review)</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Malignancy at risk for febrile neutropenia or undergoing myeloablative chemotherapy prior to allogeneic or autologous bone marrow transplantation</td>
<td>END (Pending Manual Review)</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Myeloid Engraftment for bone marrow transplant (BMT)</td>
<td>END (Pending Manual Review) </td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Severe, chronic neutropenia with absolute neutrophil count (ANC) of less than 500/mm3 and have symptoms associated with neutropenia (e.g. fever, infections, oropharyngeal ulcers)</td>
<td><p>END (Pending Manual Review)  </p>
<p> </p>
<p> </p></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Hematopoietic radiation injury syndrome</td>
<td>END (Pending Manual Review)</td>
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
<td>10</td>
<td>1235 </td>
<td> </td>
<td>Free Text </td>
<td>Please provide the rationale for the medication being requested.  </td>
<td>END (Pending Manual Review) </td>
<td></td>
</tr>
<tr class="even">
<td>11</td>
<td>1236</td>
<td></td>
<td>Free Text </td>
<td>Please explain the reason(s) why the patient is unable to use medications not requiring prior approval.  </td>
<td>END (Pending Manual Review) </td>
<td></td>
</tr>
</tbody>
</table>

LENGTH OF AUTHORIZATIONS:  

![](docs/images/BloodBlood%20Products%20Colony%20Stimulating%20Factors/media/image1.png) 

| **Last Approved ** | 5/26/2023 |
| ------------------ | --------- |
| **Other**          |           |
