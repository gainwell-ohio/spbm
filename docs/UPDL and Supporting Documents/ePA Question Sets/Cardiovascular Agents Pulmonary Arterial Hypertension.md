---
search:
  boost: .9
---

# Cardiovascular Agents- Pulmonary Arterial Hypertension

[Criteria Document](https://mygainwell-my.sharepoint.com/:w:/g/personal/kaelyn_dobbins_gainwelltechnologies_com/EWb6PfEXN7tCtjDs_XmdU2kB3I2LXfe4NjHfv5xWfmgwSg?e=Uxf32J){:target="_blank" rel="noopener}

|||
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Criteria 1 | Preferred Products- Ambrisentan, Sildenafil, Tadalafil, Tracleer Tab (BvG)                                                                            |
| Criteria 2 | Sildenafil Susp (P, AR, PA), Tadliq (P, AR, PA)                                                                                                       |
| Criteria 3 | NP products- Adempas, Bosentan (Tracleer Tab is P, BvG, PA), Epoprostenol, Opsumit, Orenitram, Tracleer Susp, Treprostonil, Tyvaso, Uptravi, Ventavis |

   

 

<table>
<thead>
<tr class="header">
<th><strong>Criteria Title</strong></th>
<th>CardiovascularAgents: Pulmonary Arterial Hypertension</th>
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
<td>AMBRISENTAN</td>
<td>062792</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>AMBRISENTAN</td>
<td>062793</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>SILDENAFIL</td>
<td>059211</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>TADALAFIL</td>
<td>065368</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>TRACLEER TAB</td>
<td>048987</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>TRACLEER TAB</td>
<td>048988</td>
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
<td>1001</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the patient taken the drug in the previous 120 days?   </p>
<p>If yes, please submit documentation of recent use.</p></td>
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
<td>1002</td>
</tr>
<tr class="odd">
<td>2</td>
<td>1002  </td>
<td></td>
<td>Select </td>
<td><p>Is the patient new to therapy (initial authorization request) or continuing therapy (re-authorization request)?  </p>
<p>  </p></td>
<td>New Start (initial authorization request)</td>
<td>1003</td>
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
<td>3</td>
<td>1003  </td>
<td></td>
<td>Select </td>
<td>Is this request being prescribed in accordance with Food and Drug Administration (FDA) approved labeling?  </td>
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
<td>1235 </td>
</tr>
<tr class="odd">
<td>4</td>
<td>1004</td>
<td>  </td>
<td>Select</td>
<td>Is the request for inhalation or intravenous agent?</td>
<td>Y  </td>
<td>1005</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N  </td>
<td>1006</td>
</tr>
<tr class="odd">
<td>5</td>
<td>1005</td>
<td></td>
<td>Select  </td>
<td><p>Does the patient have class III or IV symptoms defined by the New York Heart Association (NYHA) Functional Class for</p>
<p>Pulmonary Hypertension?</p></td>
<td>Y  </td>
<td>END (Pending Manual Review)</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N  </td>
<td>1235 </td>
</tr>
<tr class="odd">
<td>6</td>
<td>1006</td>
<td></td>
<td>Select and Free Text</td>
<td>Has the provider submitted documentation of New York Heart Association (NYHA) Functional Class for Pulmonary Hypertension and symptoms experienced by patient?</td>
<td>Y  </td>
<td>END (Pending Manual Review)</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N  </td>
<td>1235 </td>
</tr>
<tr class="odd">
<td>7</td>
<td>1234</td>
<td></td>
<td>Select and Free Text  </td>
<td>Has the provider submitted documentation of the patient’s clinical response to treatment and ongoing safety monitoring?</td>
<td> Y    </td>
<td>END (Pending Manual Review)</td>
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
<td>8</td>
<td>1235</td>
<td></td>
<td>Free Text</td>
<td>Please provide the rationale for the medication being requested. </td>
<td>END (Pending Manual Review)</td>
<td></td>
</tr>
</tbody>
</table>

LENGTH OF AUTHORIZATIONS: 365 Days

 

| **Last Approved ** | 8/22/2023 |
| ------------------ | --------- |
| **Other**          |           |

<table>
<thead>
<tr class="header">
<th><strong>Criteria Title</strong></th>
<th>CardiovascularAgents: Pulmonary Arterial Hypertension</th>
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
<td>Sildenafil Susp, Tadliq</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Approval Level</strong></td>
<td>GCNSeqNo</td>
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
<td>Corresponding Code (s)</td>
<td>Type of Code (GCNSeqNo, HICL, NDC)</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>SILDENAFIL SUSP</td>
<td>069921</td>
<td>GCNSeqNo</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>TADLIQ</td>
<td>083592</td>
<td>GCNSeqNo</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Sequence Number</strong>  </td>
<td><strong>Question ID</strong>  </td>
<td><strong>Default Next Question ID</strong>  </td>
<td><strong>Question Type</strong>  </td>
<td><strong>Question Text</strong>  </td>
<td><strong>Choice Text</strong>  </td>
<td><strong>Next Question ID</strong>  </td>
</tr>
<tr class="odd">
<td>1</td>
<td>1001</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the patient taken the drug in the previous 120 days?   </p>
<p>If yes, please submit documentation of recent use.</p></td>
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
<td>1002</td>
</tr>
<tr class="odd">
<td>2</td>
<td>1002  </td>
<td></td>
<td>Select </td>
<td><p>Is the patient new to therapy (initial authorization request) or continuing therapy (re-authorization request)?  </p>
<p>  </p></td>
<td>New Start (initial authorization request)</td>
<td>1003</td>
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
<td>3</td>
<td>1003  </td>
<td></td>
<td>Select </td>
<td>Is this request being prescribed in accordance with Food and Drug Administration (FDA) approved labeling?  </td>
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
<td>1235 </td>
</tr>
<tr class="odd">
<td>4</td>
<td>1004</td>
<td></td>
<td>Select and Free Text</td>
<td>Has the provider submitted documentation of New York Heart Association (NYHA) Functional Class for Pulmonary Hypertension and symptoms experienced by patient?</td>
<td>Y  </td>
<td>1005</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N  </td>
<td>1235 </td>
</tr>
<tr class="odd">
<td>5</td>
<td>1005</td>
<td></td>
<td>Select</td>
<td>What product is being requested?</td>
<td>Sildenafil Susp</td>
<td>1006</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Tadliq</td>
<td>1008</td>
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
<td>6</td>
<td>1006</td>
<td></td>
<td>Select</td>
<td>Is the patient 18 years and older? </td>
<td>Y</td>
<td>1007</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N</td>
<td>END (Pending Manual Review)</td>
</tr>
<tr class="even">
<td>7</td>
<td>1007</td>
<td></td>
<td>Select and Free Text </td>
<td><p>Is the patient unable to swallow a standard tablet and/or capsule formulation?</p>
<p>If yes, please submit documentation.</p></td>
<td>Y  </td>
<td>END (Pending Manual Review)</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N  </td>
<td>1235 </td>
</tr>
<tr class="even">
<td>8</td>
<td>1008</td>
<td></td>
<td>Select</td>
<td>Is the patient younger than 18 years?</td>
<td>Y</td>
<td>1235</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N</td>
<td>END (Pending Manual Review)</td>
</tr>
<tr class="even">
<td>9</td>
<td>1234</td>
<td></td>
<td>Select and Free Text  </td>
<td><p>Has the provider submitted documentation of the patient’s clinical response to treatment and ongoing safety monitoring?</p>
<p> </p></td>
<td> Y    </td>
<td>END (Pending Manual Review)</td>
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
<td>10</td>
<td>1235</td>
<td></td>
<td>Free Text</td>
<td>Please provide the rationale for the medication being requested. </td>
<td>END (Pending Manual Review)</td>
<td></td>
</tr>
</tbody>
</table>

LENGTH OF AUTHORIZATIONS: 365 Days

| **Last Approved ** | 8/22/2023 |
| ------------------ | --------- |
| **Other**          |           |

**  
**

<table>
<thead>
<tr class="header">
<th><strong>Criteria Title</strong></th>
<th>CardiovascularAgents: Pulmonary Arterial Hypertension</th>
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
<td>ADEMPAS</td>
<td>071525</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>ADEMPAS</td>
<td>071526</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>ADEMPAS</td>
<td>071527</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>ADEMPAS</td>
<td>071528</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>ADEMPAS</td>
<td>071529</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>BOSENTAN</td>
<td>048987</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>BOSENTAN</td>
<td>048988</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>EPOPROSTENOL</td>
<td>067588</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>EPOPROSTENOL</td>
<td>069964</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>EPOPROSTENOL</td>
<td>017608</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>EPOPROSTENOL</td>
<td>024472</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>OPSUMIT</td>
<td>071567</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>ORENITRAM</td>
<td>071807</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>ORENITRAM</td>
<td>071808</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>ORENITRAM</td>
<td>071809</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>ORENITRAM</td>
<td>071810</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>ORENITRAM</td>
<td>077482</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>TRACLEER SUSP</td>
<td>077706</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>TREPROSTINIL</td>
<td>071807</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>TREPROSTINIL</td>
<td>071808</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>TREPROSTINIL</td>
<td>071809</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>TREPROSTINIL</td>
<td>071810</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>TREPROSTINIL</td>
<td>077482</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>TREPROSTINIL</td>
<td>050408</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>TREPROSTINIL</td>
<td>050409</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>TREPROSTINIL</td>
<td>050410</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>TREPROSTINIL</td>
<td>050411</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>TREPROSTINIL</td>
<td>065501</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>TREPROSTINIL</td>
<td>065500</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>TYVASO</td>
<td>065502</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>TYVASO</td>
<td>083419</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>TYVASO</td>
<td>083420</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>TYVASO</td>
<td>083421</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>TYVASO</td>
<td>083422</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>TYVASO</td>
<td>083425</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>TYVASO</td>
<td>083430</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>TYVASO</td>
<td>083431</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>UPTRAVI</td>
<td>075312</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>UPTRAVI</td>
<td>075313</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>UPTRAVI</td>
<td>075314</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>UPTRAVI</td>
<td>075315</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>UPTRAVI</td>
<td>075316</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>UPTRAVI</td>
<td>075317</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>UPTRAVI</td>
<td>075318</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>UPTRAVI</td>
<td>075319</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>UPTRAVI</td>
<td>075321</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>UPTRAVI</td>
<td>082563</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>VENTAVIS</td>
<td>060297</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>VENTAVIS</td>
<td>065483</td>
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
<td>1001</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the patient taken the drug in the previous 120 days?   </p>
<p>If yes, please submit documentation of recent use.</p></td>
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
<td>1002</td>
</tr>
<tr class="odd">
<td>2</td>
<td>1002  </td>
<td></td>
<td>Select </td>
<td><p>Is the patient new to therapy (initial authorization request) or continuing therapy (re-authorization request)?  </p>
<p>  </p></td>
<td>New Start (initial authorization request)</td>
<td>1003</td>
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
<td>3</td>
<td>1003  </td>
<td></td>
<td>Select </td>
<td>Is this request being prescribed in accordance with Food and Drug Administration (FDA) approved labeling?  </td>
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
<td>1235 </td>
</tr>
<tr class="odd">
<td>4</td>
<td>1004</td>
<td>  </td>
<td>Select and Free Text</td>
<td><p>Has the patient had an inadequate clinical response of at least <span class="underline">30 days</span> with at least <span class="underline">two preferred</span> drugs, <span class="underline">one</span> of which must be a phosphodiesterase-5 inhibitor?</p>
<p>If yes, please submit the medication trials and dates.</p></td>
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
<td>1005</td>
</tr>
<tr class="odd">
<td>5</td>
<td>1005</td>
<td>  </td>
<td>Select and Free Text</td>
<td><p>Has the provider submitted documentation of medical necessity beyond convenience for why the patient cannot be changed to a preferred drug (i.e., allergies, drug-drug interactions, contraindications, or intolerances)?</p>
<p>If yes, please submit the medication name and reason for inability to use. </p></td>
<td>Y   </td>
<td>1006</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N   </td>
<td>1236</td>
</tr>
<tr class="odd">
<td>6</td>
<td>1006</td>
<td></td>
<td>Select  </td>
<td>Is this request for generic bosentan? </td>
<td>Y  </td>
<td>1007</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N  </td>
<td>1008</td>
</tr>
<tr class="odd">
<td>7</td>
<td>1007</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the brand medication been attempted and failed or is the brand medication contraindicated?  </p>
<p>If yes, please submit documentation.</p></td>
<td>Y  </td>
<td>1010</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N  </td>
<td>1235</td>
</tr>
<tr class="odd">
<td>8</td>
<td>1008</td>
<td>  </td>
<td>Select</td>
<td>Is the request for inhalation or intravenous agents?</td>
<td>Y  </td>
<td>1009</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N  </td>
<td>1010</td>
</tr>
<tr class="odd">
<td>9</td>
<td>1009</td>
<td></td>
<td>Select  </td>
<td><p>Does the patient have class III or IV symptoms defined by the New York Heart Association (NYHA) Functional Class for</p>
<p>Pulmonary Hypertension?</p></td>
<td>Y  </td>
<td>END (Pending Manual Review)</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N  </td>
<td>1235 </td>
</tr>
<tr class="odd">
<td>10</td>
<td>1010</td>
<td></td>
<td>Select and Free Text</td>
<td>Has the provider submitted documentation of New York Heart Association (NYHA) Functional Class for Pulmonary Hypertension and symptoms experienced by patient?</td>
<td>Y  </td>
<td>1011</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N  </td>
<td>1235</td>
</tr>
<tr class="odd">
<td>11</td>
<td>1011</td>
<td></td>
<td>Select</td>
<td><p>Is the request for any of the following:</p>
<p>1) a nonsolid oral dosage formulation</p>
<p>2) a non-preferred extended release formulation</p>
<p>3) a non-preferred brand name that has a preferred generic product</p></td>
<td>Y</td>
<td>1012</td>
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
<td>12</td>
<td>1012</td>
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
<td>13</td>
<td>1234</td>
<td></td>
<td>Select and Free Text  </td>
<td><p>Has the provider submitted documentation of the patient’s clinical response to treatment and ongoing safety monitoring?</p>
<p>    </p></td>
<td> Y    </td>
<td>END (Pending Manual Review)</td>
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
<td>14</td>
<td>1235</td>
<td></td>
<td>Free Text</td>
<td>Please provide the rationale for the medication being requested. </td>
<td>END (Pending Manual Review)</td>
<td></td>
</tr>
<tr class="even">
<td>15</td>
<td>1236</td>
<td></td>
<td>Free Text</td>
<td>Please explain the reason(s) why the patient is unable to use medications not requiring prior approval.</td>
<td>END (Pending Manual Review)</td>
<td></td>
</tr>
</tbody>
</table>

LENGTH OF AUTHORIZATIONS: 365 Days

| **Last Approved ** | 8/22/2023 |
| ------------------ | --------- |
| **Other**          |           |
