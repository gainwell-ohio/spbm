---
search:
  boost: .9
---

# Gastroinstinal Agents - Proton Pump Inhibitors

[Criteria Document](https://mygainwell-my.sharepoint.com/:w:/g/personal/kaelyn_dobbins_gainwelltechnologies_com/EablvZtd5N9Fl1gDbh_BylkBmwQedxmb3nWTHFREOafmCA?e=Mu2UNp){:target="_blank" rel="noopener}

## Criteria { data-search-exclude }

|||
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Criteria 1 | Protonix Pak (P, AR, BvG), Pantoprazole Packet (NP, AR)                                                                                                                                         |
| Criteria 2 | Non-Preferred: Aciphex, Dexilant (BvG), dexlansoprazole (BvG), Esomeprazole, Esomeprazole Granules (BvG), Konvomep, Lansoprazole ODT, Omeprazole/Sodium Bicarbonate, Prilosec Susp, Rabeprazole |
| Criteria 3 | Omeprazole Tab (NP, AR)                                                                                                                                                                         |
| Criteria 4 | Omeprazole Cap, Pantoprazole Tab (P, AR)                                                                                                                                                        |

## Protonix Pak, Pantoprazole Packet

<table>
<thead>
<tr class="header">
<th><strong>Criteria Title</strong> </th>
<th>Gastrointestinal Agents: Proton Pump Inhibitors</th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Criteria Subtitle</strong> </td>
<td>Protonix Pak, Pantoprazole Packet</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Approval Level</strong> </td>
<td> GCNSeqNo</td>
<td></td>
<td></td>
<td></td>
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
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>PROTONIX PAK</td>
<td>063700</td>
<td>GCNSeqNo</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>PANTOPRAZOLE PACKET</td>
<td>063700</td>
<td>GCNSeqNo</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Sequence Number</strong></td>
<td><strong>Question ID</strong></td>
<td><strong>Default Next Question ID</strong></td>
<td><strong>Question Type</strong></td>
<td><strong>Question Text</strong></td>
<td><strong>Choice Text</strong></td>
<td><strong>Next Question ID</strong></td>
</tr>
<tr class="odd">
<td>1</td>
<td>0095</td>
<td></td>
<td>Select</td>
<td>What product is being requested?</td>
<td>Brand Protonix Pak</td>
<td>0096</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Generic pantoprazole packet</td>
<td>0098</td>
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
<td>0096</td>
<td></td>
<td>Select</td>
<td><p>Is the patient 6 years and older?</p>
<p>Please note: a PA is only required for patients 6 years and older.</p></td>
<td>Y</td>
<td>0097</td>
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
<td>3</td>
<td>0097</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Is the patient unable to swallow a tablet and/or capsule formulation?</p>
<p>If yes, please submit documentation.</p></td>
<td>Y</td>
<td>END (Approve x 180 days)</td>
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
<td>0098</td>
<td></td>
<td>Select</td>
<td>Was the drug initiated in the hospital for the treatment of a condition such as a GI bleed or the presence of a gastrostomy and/or jejunostomy (G, GJ, J-tube)?</td>
<td>Y</td>
<td>END (Approve x 180 days)</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N</td>
<td>0099</td>
</tr>
<tr class="even">
<td>5</td>
<td>0099</td>
<td></td>
<td>Select</td>
<td><p>Is the patient new to therapy (initial authorization request) or continuing therapy (re-authorization request)? </p>
<p> </p></td>
<td>New Start (initial authorization request</td>
<td>0100</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Continuation (re-authorization request) </td>
<td>1234</td>
</tr>
<tr class="even">
<td>6</td>
<td>0100</td>
<td></td>
<td>Select</td>
<td>Is this request being prescribed in accordance with Food and Drug Administration (FDA) approved labeling?</td>
<td>Y</td>
<td>0101</td>
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
<td>0101</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the patient had an inadequate clinical response of at least <span class="underline">30 days</span> with at least <span class="underline">two preferred</span> drugs?</p>
<p>If yes, please submit the medication trials and dates.</p></td>
<td>Y</td>
<td>0103</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N</td>
<td>0102</td>
</tr>
<tr class="even">
<td>8</td>
<td>0102</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the provider submitted documentation of medical necessity beyond convenience for why the patient cannot be changed to a preferred drug (i.e., allergies, drug-drug interactions, contraindications, or intolerances)?</p>
<p>If yes, please submit the medication name and reason for inability to use.</p></td>
<td>Y</td>
<td>0103</td>
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
<td>9</td>
<td>0103</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the brand medication been attempted and failed or is the brand medication contraindicated? </p>
<p>If yes, please submit documentation.</p></td>
<td>Y</td>
<td>0104</td>
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
<td>10</td>
<td>0104</td>
<td></td>
<td>Select</td>
<td><p>Is the request for any of the following:</p>
<p>1) a nonsolid oral dosage formulation</p>
<p>2) a non-preferred extended release formulation</p>
<p>3) a non-preferred brand name that has a preferred generic product</p></td>
<td>Y</td>
<td>0105</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N</td>
<td>0106</td>
</tr>
<tr class="even">
<td>11</td>
<td>0105</td>
<td></td>
<td>Select and Free Text</td>
<td>Has the provider submitted documentation of medical necessity for the requested product (i.e. medical reasons for why the patient cannot be changed to a solid oral dosage formulation, inadequate clinical response with a product’s immediate release formulation, or inadequate clinical response or allergy of two or more generic labelers)?</td>
<td>Y</td>
<td>0106</td>
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
<td>12</td>
<td>0106</td>
<td></td>
<td>Select</td>
<td>Is the patient 6 years and older?</td>
<td>Y</td>
<td>0107</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N</td>
<td>1001</td>
</tr>
<tr class="even">
<td>13</td>
<td>0107</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Is the patient unable to swallow a tablet and/or capsule formulation?</p>
<p>If yes, please submit documentation.</p></td>
<td>Y</td>
<td>1001</td>
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
<td>14</td>
<td>1001</td>
<td></td>
<td>Select  </td>
<td><p>Is the request for once daily or twice daily dosing?</p>
<p>     </p></td>
<td>Once Daily Dosing</td>
<td>END (Pending Manual Review)</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Twice Daily Dosing</td>
<td>1002</td>
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
<td>15</td>
<td>1002</td>
<td></td>
<td>Select</td>
<td>Does the patient have a diagnosis of H. Pylori?</td>
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
<td>16</td>
<td>1003</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the provider submitted documentation of the H. Pylori diagnosis?</p>
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
<td>17</td>
<td>1004</td>
<td></td>
<td>Select</td>
<td>What is the patient’s diagnosis?</td>
<td>Carcinoma of GI Tract</td>
<td>1005</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>COPD</td>
<td>1005</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Crest Syndrome</td>
<td>1005</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Dyspepsia</td>
<td>1005</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Esophageal Varices</td>
<td>1005</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Gastritis</td>
<td>1005</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Gastroparesis</td>
<td>1005</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Scleroderma</td>
<td>1005</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Symptomatic uncomplicated Barret’s Esophagus</td>
<td>1005</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Systemic Mastocytosis</td>
<td>1005</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Zollinger Ellison Syndrome</td>
<td>1005</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Other</td>
<td>1005</td>
</tr>
<tr class="odd">
<td>18</td>
<td>1005</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the provider submitted documentation of the patient’s diagnosis?</p>
<p>If yes, please submit documentation.</p></td>
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
<td>19</td>
<td>1006</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the patient failed once daily dosing of the requested drug?</p>
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
<td>20</td>
<td>1234</td>
<td></td>
<td>Select and Free Text</td>
<td>Has the provider submitted documentation of the patient’s clinical response to treatment and ongoing safety monitoring?</td>
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
<td>21</td>
<td>1235</td>
<td></td>
<td>Free Text</td>
<td>Please provide the rationale for the medication being requested.</td>
<td>END (Pending Manual Review)</td>
<td></td>
</tr>
<tr class="even">
<td>22</td>
<td>1236</td>
<td></td>
<td>Free Text</td>
<td>Please explain the reason(s) why the patient is unable to use medications not requiring prior approval.</td>
<td>END (Pending Manual Review)</td>
<td></td>
</tr>
<tr class="odd">
<td>23</td>
<td>1237</td>
<td></td>
<td>Free Text</td>
<td>A PA is not required for those younger than 6 years of age.</td>
<td>END (Pending Manual Review)</td>
<td></td>
</tr>
</tbody>
</table>

LENGTH OF AUTHORIZATIONS: Dependent on diagnosis

|||
| ------------------ | --------- |
| **Last Approved ** | 8/11/2023 |
| **Other**          |           |

## Non-Preferred Products

<table>
<thead>
<tr class="header">
<th><strong>Criteria Title</strong> </th>
<th>Gastrointestinal Agents: Proton Pump Inhibitors</th>
<th></th>
<th></th>
<th></th>
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
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Approval Level</strong> </td>
<td> GCNSeqNo</td>
<td></td>
<td></td>
<td></td>
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
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>ACIPHEX</td>
<td>040941</td>
<td>GCNSeqNo</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>DEXILANT</td>
<td>064793</td>
<td>GCNSeqNo</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>DEXILANT</td>
<td>064794</td>
<td>GCNSeqNo</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>DEXLANSOPRAZOLE DR 30 MG CAP</td>
<td>064793</td>
<td>GCNSeqNo</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>DEXLANSOPRAZOLE DR 60 MG CAP</td>
<td>064794</td>
<td>GCNSeqNo</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>ESOMPERAZOLE</td>
<td>046649</td>
<td>GCNSeqNo</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>ESOMEPRAZOLE</td>
<td>047525</td>
<td>GCNSeqNo</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>ESOMEPRAZOLE</td>
<td>047526</td>
<td>GCNSeqNo</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>ESOMEPRAZOLE GRANULES</td>
<td>062245</td>
<td>GCNSeqNo</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>ESOMEPRAZOLE GRANULES</td>
<td>062246</td>
<td>GCNSeqNo</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>ESOMEPRAZOLE GRANULES</td>
<td>063668</td>
<td>GCNSeqNo</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>KONVOMEP</td>
<td>083784</td>
<td>GCNSeqNo</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>LANSOPRAZOLE ODT</td>
<td>051653</td>
<td>GCNSeqNo</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>LANSOPRAZOLE ODT</td>
<td>051654</td>
<td>GCNSeqNo</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>OMEPRAZOLE/SODIUM BICARBONATE</td>
<td>060471</td>
<td>GCNSeqNo</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>OMEPRAZOLE/SODIUM BICARBONATE</td>
<td>060472</td>
<td>GCNSeqNo</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>OMEPRAZOLE/SODIUM BICARBONATE</td>
<td>060473</td>
<td>GCNSeqNo</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>OMEPRAZOLE/SODIUM BICARBONATE</td>
<td>060474</td>
<td>GCNSeqNo</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>PRILOSEC SUSP</td>
<td>064774</td>
<td>GCNSeqNo</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>PRILOSEC SUSP</td>
<td>064775</td>
<td>GCNSeqNo</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>RABEPRAZOLE</td>
<td>040941</td>
<td>GCNSeqNo</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Sequence Number</strong></td>
<td><strong>Question ID</strong></td>
<td><strong>Default Next Question ID</strong></td>
<td><strong>Question Type</strong></td>
<td><strong>Question Text</strong></td>
<td><strong>Choice Text</strong></td>
<td><strong>Next Question ID</strong></td>
</tr>
<tr class="even">
<td>1</td>
<td>0098</td>
<td></td>
<td>Select</td>
<td>Was the drug being requested initiated in the hospital for the treatment of a condition such as a GI bleed or the presence of a gastrostomy and/or jejunostomy (G, GJ, J-tube)?</td>
<td>Y</td>
<td>END (Approve x 180 days)</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N</td>
<td>0099</td>
</tr>
<tr class="even">
<td>2</td>
<td>0099</td>
<td></td>
<td>Select</td>
<td><p>Is the patient new to therapy (initial authorization request) or continuing therapy (re-authorization request)? </p>
<p> </p></td>
<td>New Start (initial authorization request</td>
<td>0100</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Continuation (re-authorization request) </td>
<td>1234</td>
</tr>
<tr class="even">
<td>3</td>
<td>0100</td>
<td></td>
<td>Select</td>
<td>Is this request being prescribed in accordance with Food and Drug Administration (FDA) approved labeling?</td>
<td>Y</td>
<td>0101</td>
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
<td>0101</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the patient had an inadequate clinical response of at least <span class="underline">30 days</span> with at least <span class="underline">two preferred</span> drugs?</p>
<p>If yes, please submit the medication trials and dates.</p></td>
<td>Y</td>
<td>0103</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N</td>
<td>0102</td>
</tr>
<tr class="even">
<td>5</td>
<td>0102</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the provider submitted documentation of medical necessity beyond convenience for why the patient cannot be changed to a preferred drug (i.e., allergies, drug-drug interactions, contraindications, or intolerances)?</p>
<p>If yes, please submit the medication name and reason for inability to use.</p></td>
<td>Y</td>
<td>0103</td>
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
<td>6</td>
<td>0103</td>
<td></td>
<td>Select</td>
<td><p>Is the request for any of the following:</p>
<p>1) a nonsolid oral dosage formulation</p>
<p>2) a non-preferred extended release formulation</p>
<p>3) a non-preferred brand name that has a preferred generic product</p></td>
<td>Y</td>
<td>0104</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N</td>
<td>0105</td>
</tr>
<tr class="even">
<td>7</td>
<td>0104</td>
<td></td>
<td>Select and Free Text</td>
<td>Has the provider submitted documentation of medical necessity for the requested product (i.e. medical reasons for why the patient cannot be changed to a solid oral dosage formulation, inadequate clinical response with a product’s immediate release formulation, or inadequate clinical response or allergy of two or more generic labelers)?</td>
<td>Y</td>
<td>0105</td>
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
<td>0105</td>
<td></td>
<td>Select</td>
<td><p>Is the request for any of the following products:</p>
<p>Brand Dexilant, generic dexlansoprazole, or generic esomeprazole granules?</p></td>
<td>Y</td>
<td>0106</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N</td>
<td>1001</td>
</tr>
<tr class="even">
<td>9</td>
<td>0106</td>
<td></td>
<td>Select</td>
<td>Which drug is being requested?</td>
<td>Brand Dexilant</td>
<td>1001</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Generic dexlansoprazole</td>
<td>0107</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Generic esomeprazole granules</td>
<td>0107</td>
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
<td>10</td>
<td>0107</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the brand medication been attempted and failed or is the brand medication contraindicated? </p>
<p>If yes, please submit documentation.</p></td>
<td>Y</td>
<td>1001</td>
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
<td>1001</td>
<td></td>
<td>Select  </td>
<td><p>Is the request for once daily or twice daily dosing?</p>
<p>     </p></td>
<td>Once Daily Dosing</td>
<td>END (Approve x 180 days)</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Twice Daily Dosing</td>
<td>1002</td>
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
<td>1002</td>
<td></td>
<td>Select</td>
<td>Does the patient have a diagnosis of H. Pylori?</td>
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
<td>13</td>
<td>1003</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the provider submitted documentation of the H. Pylori diagnosis?</p>
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
<td>14</td>
<td>1004</td>
<td></td>
<td>Select</td>
<td>What is the patient’s diagnosis?</td>
<td>Carcinoma of GI Tract</td>
<td>1005</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>COPD</td>
<td>1005</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Crest Syndrome</td>
<td>1005</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Dyspepsia</td>
<td>1005</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Esophageal Varices</td>
<td>1005</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Gastritis</td>
<td>1005</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Gastroparesis</td>
<td>1005</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Scleroderma</td>
<td>1005</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Symptomatic uncomplicated Barret’s Esophagus</td>
<td>1005</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Systemic Mastocytosis</td>
<td>1005</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Zollinger Ellison Syndrome</td>
<td>1005</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Other</td>
<td>1005</td>
</tr>
<tr class="odd">
<td>15</td>
<td>1005</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the provider submitted documentation of the patient’s diagnosis?</p>
<p>If yes, please submit documentation.</p></td>
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
<td>16</td>
<td>1006</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the patient failed once daily dosing of the requested drug?</p>
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
<td>17</td>
<td>1234</td>
<td></td>
<td>Select and Free Text</td>
<td>Has the provider submitted documentation of the patient’s clinical response to treatment and ongoing safety monitoring?</td>
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
<td>18</td>
<td>1235</td>
<td></td>
<td>Free Text</td>
<td>Please provide the rationale for the medication being requested.</td>
<td>END (Pending Manual Review)</td>
<td></td>
</tr>
<tr class="even">
<td>19</td>
<td>1236</td>
<td></td>
<td>Free Text</td>
<td>Please explain the reason(s) why the patient is unable to use medications not requiring prior approval.</td>
<td>END (Pending Manual Review)</td>
<td></td>
</tr>
</tbody>
</table>

LENGTH OF AUTHORIZATIONS: Dependent on diagnosis

|||
| ------------------ | --------- |
| **Last Approved ** | 8/11/2023 |
| **Other**          |           |

## Omeprazole Tab

<table>
<thead>
<tr class="header">
<th><strong>Criteria Title</strong> </th>
<th>Gastrointestinal Agents: Proton Pump Inhibitors</th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Criteria Subtitle</strong> </td>
<td>Omeprazole Tab</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Approval Level</strong> </td>
<td> GCNSeqNo</td>
<td></td>
<td></td>
<td></td>
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
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>OMEPRAZOLE TAB</td>
<td>054334</td>
<td>GCNSeqNo</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>OMEPRAZOLE TAB</td>
<td>025703</td>
<td>GCNSeqNo</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Sequence Number</strong></td>
<td><strong>Question ID</strong></td>
<td><strong>Default Next Question ID</strong></td>
<td><strong>Question Type</strong></td>
<td><strong>Question Text</strong></td>
<td><strong>Choice Text</strong></td>
<td><strong>Next Question ID</strong></td>
</tr>
<tr class="odd">
<td>1</td>
<td>0098</td>
<td></td>
<td>Select</td>
<td>Was the drug being requested initiated in the hospital for the treatment of a condition such as a GI bleed or the presence of a gastrostomy and/or jejunostomy (G, GJ, J-tube)?</td>
<td>Y</td>
<td>END (Approve x 180 days)</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N</td>
<td>0099</td>
</tr>
<tr class="odd">
<td>2</td>
<td>0099</td>
<td></td>
<td>Select</td>
<td><p>Is the patient new to therapy (initial authorization request) or continuing therapy (re-authorization request)? </p>
<p> </p></td>
<td>New Start (initial authorization request)</td>
<td>0100</td>
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
<td>3</td>
<td>0100</td>
<td></td>
<td>Select</td>
<td>Is this request being prescribed in accordance with Food and Drug Administration (FDA) approved labeling?</td>
<td>Y</td>
<td>0101</td>
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
<td>0101</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the patient had an inadequate clinical response of at least <span class="underline">30 days</span> with at least <span class="underline">two preferred</span> drugs?</p>
<p>If yes, please submit the medication trials and dates.</p></td>
<td>Y</td>
<td>0103</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N</td>
<td>0102</td>
</tr>
<tr class="odd">
<td>5</td>
<td>0102</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the provider submitted documentation of medical necessity beyond convenience for why the patient cannot be changed to a preferred drug (i.e., allergies, drug-drug interactions, contraindications, or intolerances)?</p>
<p>If yes, please submit the medication name and reason for inability to use.</p></td>
<td>Y</td>
<td>0103</td>
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
<td>0103</td>
<td></td>
<td>Select</td>
<td><p>Is the request for any of the following:</p>
<p>1) a nonsolid oral dosage formulation</p>
<p>2) a non-preferred extended release formulation</p>
<p>3) a non-preferred brand name that has a preferred generic product</p></td>
<td>Y</td>
<td>0104</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N</td>
<td>1000</td>
</tr>
<tr class="odd">
<td>7</td>
<td>0104</td>
<td></td>
<td>Select and Free Text</td>
<td>Has the provider submitted documentation of medical necessity for the requested product (i.e. medical reasons for why the patient cannot be changed to a solid oral dosage formulation, inadequate clinical response with a product’s immediate release formulation, or inadequate clinical response or allergy of two or more generic labelers)?</td>
<td>Y</td>
<td>1000</td>
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
<td>1000</td>
<td></td>
<td>Select  </td>
<td><p>Is the patient 21 years and older?</p>
<p>   </p></td>
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
<td>END (Approve x 180 days)</td>
</tr>
<tr class="odd">
<td>9</td>
<td>1001</td>
<td></td>
<td>Select  </td>
<td><p>Is the request for once daily or twice daily dosing?</p>
<p>     </p></td>
<td>Once Daily Dosing</td>
<td>END (Approve x 180 days)</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Twice Daily Dosing</td>
<td>1002</td>
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
<td>10</td>
<td>1002</td>
<td></td>
<td>Select</td>
<td>Does the patient have a diagnosis of H. Pylori?</td>
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
<td>1004</td>
</tr>
<tr class="even">
<td>11</td>
<td>1003</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the provider submitted documentation of the H. Pylori diagnosis?</p>
<p>If yes, please submit documentation.</p></td>
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
<td>12</td>
<td>1004</td>
<td></td>
<td>Select</td>
<td>What is the patient’s diagnosis?</td>
<td>Carcinoma of GI Tract</td>
<td>1005</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>COPD</td>
<td>1005</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Crest Syndrome</td>
<td>1005</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Dyspepsia</td>
<td>1005</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Esophageal Varices</td>
<td>1005</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Gastritis</td>
<td>1005</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Gastroparesis</td>
<td>1005</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Scleroderma</td>
<td>1005</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Symptomatic uncomplicated Barret’s Esophagus</td>
<td>1005</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Systemic Mastocytosis</td>
<td>1005</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Zollinger Ellison Syndrome</td>
<td>1005</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Other</td>
<td>1005</td>
</tr>
<tr class="even">
<td>13</td>
<td>1005</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the provider submitted documentation of the patient’s diagnosis?</p>
<p>If yes, please submit documentation.</p></td>
<td>Y</td>
<td>1006</td>
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
<td>14</td>
<td>1006</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the patient failed once daily dosing of the requested drug?</p>
<p>If yes, please submit documentation.</p></td>
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
<td>15</td>
<td>1234</td>
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
<td>16</td>
<td>1235</td>
<td></td>
<td>Free Text</td>
<td>Please provide the rationale for the medication being requested.</td>
<td>END (Pending Manual Review)</td>
<td></td>
</tr>
<tr class="odd">
<td>17</td>
<td>1236</td>
<td></td>
<td>Free Text</td>
<td>Please explain the reason(s) why the patient is unable to use medications not requiring prior approval.</td>
<td>END (Pending Manual Review)</td>
<td></td>
</tr>
</tbody>
</table>

LENGTH OF AUTHORIZATIONS: Dependent on diagnosis

|||
| ------------------ | --------- |
| **Last Approved ** | 8/11/2023 |
| **Other**          |           |

## Omeprazole Cap, Pantoprazole Tab

<table>
<thead>
<tr class="header">
<th><strong>Criteria Title</strong> </th>
<th>Gastrointestinal Agents: Proton Pump Inhibitors</th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Criteria Subtitle</strong> </td>
<td>Omeprazole Cap, Pantoprazole Tab</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Approval Level</strong> </td>
<td> GCNSeqNo</td>
<td></td>
<td></td>
<td></td>
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
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>OMEPRAZOLE CAP</td>
<td>066403</td>
<td>GCNSeqNo</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>OMEPRAZOLE CAP</td>
<td>033530</td>
<td>GCNSeqNo</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>OMEPRAZOLE CAP</td>
<td>043136</td>
<td>GCNSeqNo</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>OMEPRAZOLE CAP</td>
<td>043137</td>
<td>GCNSeqNo</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>PANTOPRAZOLE TAB</td>
<td>027462</td>
<td>GCNSeqNo</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>PANTOPRAOZLE TAB</td>
<td>039545</td>
<td>GCNSeqNo</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Sequence Number</strong></td>
<td><strong>Question ID</strong></td>
<td><strong>Default Next Question ID</strong></td>
<td><strong>Question Type</strong></td>
<td><strong>Question Text</strong></td>
<td><strong>Choice Text</strong></td>
<td><strong>Next Question ID</strong></td>
</tr>
<tr class="odd">
<td>1</td>
<td>0999</td>
<td></td>
<td>Select  </td>
<td>Is the patient 21 years and older?</td>
<td>Y</td>
<td>1000</td>
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
<td>1000</td>
<td></td>
<td>Select  </td>
<td><p>Is the request for once daily or twice daily dosing?</p>
<p>     </p></td>
<td>Once Daily Dosing</td>
<td>1237</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Twice Daily Dosing</td>
<td>1001</td>
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
<td>1001</td>
<td></td>
<td>Select</td>
<td>Was the drug being requested initiated in the hospital for the treatment of a condition such as a GI bleed or the presence of a gastrostomy and/or jejunostomy (G, GJ, J-tube)?</td>
<td>Y</td>
<td>END (Approve x 180 days)</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N</td>
<td>1002</td>
</tr>
<tr class="even">
<td>4</td>
<td>1002</td>
<td></td>
<td>Select</td>
<td>Does the patient have a diagnosis of H. Pylori?</td>
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
<td>1004</td>
</tr>
<tr class="even">
<td>5</td>
<td>1003</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the provider submitted documentation of the H. Pylori diagnosis?</p>
<p>If yes, please submit documentation.</p></td>
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
<td>6</td>
<td>1004</td>
<td></td>
<td>Select</td>
<td>What is the patient’s diagnosis?</td>
<td>Carcinoma of GI Tract</td>
<td>1005</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>COPD</td>
<td>1005</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Crest Syndrome</td>
<td>1005</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Dyspepsia</td>
<td>1005</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Esophageal Varices</td>
<td>1005</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Gastritis</td>
<td>1005</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Gastroparesis</td>
<td>1005</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Scleroderma</td>
<td>1005</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Symptomatic uncomplicated Barret’s Esophagus</td>
<td>1005</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Systemic Mastocytosis</td>
<td>1005</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Zollinger Ellison Syndrome</td>
<td>1005</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Other</td>
<td>1005</td>
</tr>
<tr class="even">
<td>7</td>
<td>1005</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the provider submitted documentation of the patient’s diagnosis?</p>
<p>If yes, please submit documentation.</p></td>
<td>Y</td>
<td>1006</td>
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
<td>1006</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the patient failed once daily dosing of the requested drug?</p>
<p>If yes, please submit documentation.</p></td>
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
<td>9</td>
<td>1235</td>
<td></td>
<td>Free Text</td>
<td>Please provide the rationale for the medication being requested.</td>
<td>END (Pending Manual Review)</td>
<td></td>
</tr>
<tr class="odd">
<td>10</td>
<td>1236</td>
<td></td>
<td>Free Text</td>
<td>A PA is not required for those younger than 21 years old.</td>
<td>END (Pending Manual Review)</td>
<td></td>
</tr>
<tr class="even">
<td>11</td>
<td>1237</td>
<td></td>
<td>Free Text</td>
<td>A PA is not required for those requesting once daily dosing.</td>
<td>END (Pending Manual Review)</td>
<td></td>
</tr>
</tbody>
</table>

LENGTH OF AUTHORIZATIONS: Dependent on diagnosis

|||
| ------------------ | --------- |
| **Last Approved ** | 8/11/2023 |
| **Other**          |           |
