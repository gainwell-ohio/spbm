---
search:
  boost: .9
---

# Ophthalmic Agents - Ophthalmic Steroids 

[Criteria Document](https://mygainwell-my.sharepoint.com/:w:/g/personal/kaelyn_dobbins_gainwelltechnologies_com/EbXPh2d-FgRBvD-ilrU4n7cB4SPcQIJNLOn6lPDaWuytPw?e=g9i5g6){:target="_blank" rel="noopener}

## Criteria { data-search-exclude }

<table>
<tbody>
<tr class="odd">
<td>Criteria 1   </td>
<td><p>NP- Inveltys, Lotemax SM, Loteprednol*</p>
<p>*- Preferred product has BvG designation</p></td>
</tr>
</tbody>
</table>

## Non-Preferred Products 

<table>
<thead>
<tr class="header">
<th><strong>Criteria Title</strong> </th>
<th>Ophthalmic Agents: Ophthalmic Steroids</th>
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
<td>INVELTYS</td>
<td>078802</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>LOTEMAX SM</td>
<td>079545</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>LOTEPREDNOL</td>
<td>039106</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>LOTEPREDNOL</td>
<td>070083</td>
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
<td>2</td>
<td>1000 </td>
<td> </td>
<td>Select and Free Text</td>
<td><p>Has the patient had an inadequate clinical response of at least <span class="underline">14 days</span> with at least <span class="underline">two preferred</span> drugs?</p>
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
<td>3</td>
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
<td>4</td>
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
<td>1004</td>
</tr>
<tr class="odd">
<td>5</td>
<td>1003</td>
<td></td>
<td>Select and Free Text</td>
<td>Has the provider submitted documentation of medical necessity for the requested product (i.e. medical reasons for why the patient cannot be changed to a solid oral dosage formulation, inadequate clinical response with a product’s immediate release formulation, or inadequate clinical response or allergy of two or more generic labelers)?</td>
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
<td>1235</td>
</tr>
<tr class="odd">
<td>6</td>
<td>1004</td>
<td></td>
<td>Select</td>
<td><p>Is the request for any of the following agents:</p>
<p>Generic loteprednol ophthalmic gel 0.5%, generic loteprednol ophthalmic suspension 0.5%, generic loteprednol ophthalmic suspension 0.2%?</p></td>
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
<td>END (Pending Manual Review)</td>
</tr>
<tr class="odd">
<td>7</td>
<td>1005</td>
<td></td>
<td>Select</td>
<td>Which product is being requested?</td>
<td>Loteprednol Ophthalmic Gel 0.5%</td>
<td>1006</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Loteprednol Ophthalmic Suspension 0.5%</td>
<td>1006</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Loteprednol Ophthalmic Suspension 0.2%</td>
<td>1006</td>
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
<td>8</td>
<td>1006</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the brand medication been attempted and failed or is the brand medication contraindicated?  </p>
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

LENGTH OF AUTHORIZATIONS: 30 days

|||
| ------------------ | -------- |
| **Last Approved ** | 6/2/2023 |
| **Other**          |          |
