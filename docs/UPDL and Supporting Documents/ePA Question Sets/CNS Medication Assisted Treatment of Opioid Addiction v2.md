---
search:
  boost: .9
---

# CNS Agents - Medication Assisted Treatment of Opioid Addiction 

[Criteria Document](https://mygainwell-my.sharepoint.com/:w:/g/personal/kaelyn_dobbins_gainwelltechnologies_com/ESczEqyaAbFMrAkm801V6VsB4GQS1v2Gu3SIK6KPQHU3Hg?e=LD13n0){:target="_blank" rel="noopener}

|||
| ---------- | ------------------ |
| Criteria 1 | Buprenorphine (NP) |
| Criteria 2 | Lucemyra (NP, QL)  |

   

<table>
<thead>
<tr class="header">
<th><strong>Criteria Title</strong> </th>
<th>Central Nervous System (CNS) Agents: Medication Assisted Treatment of Opioid Addiction</th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Criteria Subtitle</strong> </td>
<td>Buprenorphine</td>
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
<td>BUPRENORPHINE 2 MG SL TAB </td>
<td>029312 </td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>BUPRENORPHINE 8 MG SL TAB</td>
<td>029313</td>
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
<td>1220</td>
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
<td>Is the patient currently pregnant?</td>
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
<td>1000</td>
</tr>
<tr class="odd">
<td>4</td>
<td>1000</td>
<td></td>
<td>Select</td>
<td>Is the patient currently breastfeeding?</td>
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
<td>1001</td>
</tr>
<tr class="odd">
<td>5</td>
<td>1001</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Does the patient have an allergy or other contraindication to preferred products?</p>
<p>If yes, please provide documentation to support.</p></td>
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
<td>6</td>
<td>1002</td>
<td></td>
<td>Select</td>
<td>Has the patient been explained the difference between an allergic reaction and symptoms of opioid withdraw?</td>
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
<td>1235</td>
</tr>
<tr class="odd">
<td>7</td>
<td>1003</td>
<td></td>
<td>Select</td>
<td>Has the physician reviewed the OARRS report within 7 days prior to the prior authorization request?</td>
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
<td>8</td>
<td>1004</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the provider submitted documentation of the patient’s diagnosis and ICD-10 Code?</p>
<p>Please note that requests are not approvable for pain.</p></td>
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
<td>9</td>
<td>1005</td>
<td></td>
<td>Select</td>
<td>Has the patient been referred to counseling for addiction treatment?</td>
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
<td>10</td>
<td>1006</td>
<td></td>
<td>Select</td>
<td>Has the patient been offered a prescription for a naloxone kit?</td>
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
<td>11</td>
<td>1007</td>
<td></td>
<td>Select</td>
<td><p>Is the dose greater than 16 mg buprenorphine equivalents per day?</p>
<p>Please note: Doses greater than 24mg/day will not be authorized.</p></td>
<td>Y</td>
<td>1008</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N</td>
<td>1009</td>
</tr>
<tr class="odd">
<td>12</td>
<td>1008</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the provider submitted rationale to support why 16 mg buprenorphine equivalents per day is being exceeded?</p>
<p>Please note: Doses greater than 24mg/day will not be authorized.</p></td>
<td>Y</td>
<td>1009</td>
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
<td>1009</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the provider submitted documentation of the patient’s next appointment to assess induction therapy?</p>
<p>Please provide date of appointment.</p></td>
<td>Y</td>
<td>1010</td>
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
<td>1010</td>
<td> </td>
<td>Select and Free Text</td>
<td><p>Has the patient had an inadequate clinical response of at least <span class="underline">30 days</span> with at least <span class="underline">two preferred</span> drugs?</p>
<p>If yes, please submit the medication trials and dates.</p></td>
<td>Y </td>
<td>1012</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N </td>
<td>1011</td>
</tr>
<tr class="odd">
<td>15</td>
<td>1011</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the provider submitted documentation of medical necessity beyond convenience for why the patient cannot be changed to a preferred drug (i.e., allergies, drug-drug interactions, contraindications, or intolerances)?</p>
<p>If yes, please submit the medication name and reason for inability to use. </p></td>
<td>Y   </td>
<td>1012</td>
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
<td>16</td>
<td>1012</td>
<td></td>
<td>Select</td>
<td><p>Is the request for any of the following:</p>
<p>1) a nonsolid oral dosage formulation</p>
<p>2) a non-preferred extended release formulation</p>
<p>3) a non-preferred brand name that has a preferred generic product</p></td>
<td>Y</td>
<td>1013</td>
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
<td>17</td>
<td>1013</td>
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
<td>18</td>
<td>1220</td>
<td></td>
<td>Select and Free Text  </td>
<td>Has the provider submitted documentation of the patient’s clinical response to treatment and ongoing safety monitoring?</td>
<td> Y    </td>
<td>1221</td>
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
<td>19</td>
<td>1221</td>
<td></td>
<td>Select</td>
<td>Is the patient currently pregnant?</td>
<td> Y    </td>
<td>1225</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td> N    </td>
<td>1222</td>
</tr>
<tr class="odd">
<td>20</td>
<td>1222</td>
<td></td>
<td>Select</td>
<td>Is the patient currently breastfeeding?</td>
<td> Y    </td>
<td>1225</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td> N    </td>
<td>1223</td>
</tr>
<tr class="odd">
<td>21</td>
<td>1223</td>
<td></td>
<td>Select</td>
<td>Does the patient have an allergy or other contraindication to naloxone?</td>
<td> Y    </td>
<td>1224</td>
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
<td>22</td>
<td>1224</td>
<td></td>
<td>Select</td>
<td>Has the patient been explained the difference between an allergic reaction and symptoms of opioid withdrawal?</td>
<td> Y    </td>
<td>1225</td>
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
<td>23</td>
<td>1225</td>
<td></td>
<td>Select</td>
<td>Has the provider submitted documentation of the current duration of treatment as of the date of this request?</td>
<td> Y    </td>
<td>1226</td>
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
<td>24</td>
<td>1226</td>
<td></td>
<td>Select</td>
<td>Has the provider submitted documentation of the frequency of physician meetings?</td>
<td> Y    </td>
<td>1227</td>
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
<td>25</td>
<td>1227</td>
<td></td>
<td>Select and Free Text</td>
<td>Has the patient been actively participating in counseling AND has been compliant with all sessions? Has the provider submitted documentation of the date of last counseling?</td>
<td> Y    </td>
<td>1228</td>
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
<td>26</td>
<td>1228</td>
<td></td>
<td>Select</td>
<td>Has the dose been reduced in the past 6 months?</td>
<td> Y    </td>
<td>1230</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td> N    </td>
<td>1229</td>
</tr>
<tr class="odd">
<td>27</td>
<td>1229</td>
<td></td>
<td>Select and Free Text</td>
<td>Has the provider submitted documentation of why there has not been an evaluation for the dose reduction since the previous PA request?</td>
<td> Y    </td>
<td>1230</td>
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
<td>28</td>
<td>1230</td>
<td></td>
<td>Select</td>
<td>Has the physician reviewed the OARRS report within 7 days prior to the PA request?</td>
<td> Y    </td>
<td>1231</td>
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
<td>29</td>
<td>1231</td>
<td></td>
<td>Select</td>
<td>Has the patient received opioids, benzodiazepines, sedative hypnotics, carisoprodol or tramadol?</td>
<td> Y    </td>
<td>1232</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td> N    </td>
<td>1234</td>
</tr>
<tr class="odd">
<td>30</td>
<td>1232</td>
<td></td>
<td>Select</td>
<td>Has the physician coordinated with all prescribers of controlled substances and determined treatment should continue?</td>
<td> Y    </td>
<td>1233</td>
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
<td>31</td>
<td>1233</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has an addiction specialist recommended to continue substance abuse treatment?</p>
<p>Please documentation of the addiction specialist consulted, phone number, and date.</p></td>
<td> Y    </td>
<td>1234</td>
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
<td>32</td>
<td>1234</td>
<td></td>
<td>Select and Free Text</td>
<td>Has the provider submitted documentation of lab testing requirements being met (at least twice per quarter for first year of treatment; once per quarter thereafter)?</td>
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
<td>33</td>
<td>1235</td>
<td></td>
<td>Free Text</td>
<td>Please provide the rationale for the medication being requested. </td>
<td>END (Pending Manual Review)</td>
<td></td>
</tr>
<tr class="even">
<td>34</td>
<td>1236</td>
<td></td>
<td>Free Text</td>
<td>Please explain the reason(s) why the patient is unable to use medications not requiring prior approval.</td>
<td>END (Pending Manual Review)</td>
<td></td>
</tr>
</tbody>
</table>

LENGTH OF AUTHORIZATIONS: 180 days

| **Last Approved ** | 4/20/2023 |
| ------------------ | --------- |
| **Other**          |           |

 

<table>
<thead>
<tr class="header">
<th><strong>Criteria Title</strong> </th>
<th>Central Nervous System (CNS) Agents: Medication Assisted Treatment of Opioid Addiction</th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Criteria Subtitle</strong> </td>
<td>Lucemyra</td>
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
<td>LUCEMYRA</td>
<td>019113</td>
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
<td>1000</td>
<td></td>
<td>Select and Free Text</td>
<td>Has the provider submitted documentation that the drug was initiated in an inpatient setting?</td>
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
<td>1001</td>
</tr>
<tr class="odd">
<td>3</td>
<td>1001</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the provider submitted medical justification supporting why an opioid taper (such as with buprenorphine or methadone) cannot be used?</p>
<p>If yes, please submit documentation.</p></td>
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
<td>1235</td>
</tr>
<tr class="odd">
<td>4</td>
<td>1002</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the patient had an inadequate clinical response or contraindication to clonidine?</p>
<p>If yes, please submit documentation.</p></td>
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
<td>1235 </td>
</tr>
<tr class="odd">
<td>5</td>
<td>1003</td>
<td></td>
<td>Select</td>
<td>Has the physician reviewed the OARRS report within 7 days prior to the prior authorization request?</td>
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
<td>Select and Free Text</td>
<td><p>Has the provider submitted documentation of the patient’s diagnosis and ICD-10 Code?</p>
<p>Please note that requests are not approvable for pain.</p></td>
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
<td>7</td>
<td>1005</td>
<td></td>
<td>Select</td>
<td>Has the patient been referred to counseling for addiction treatment?</td>
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
<td>Has the patient been offered a prescription for a naloxone kit?</td>
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
<td></td>
<td>Select and Free Text</td>
<td><p>Has the provider submitted documentation of the patient’s next appointment to assess induction therapy?</p>
<p>Please provide date of appointment.</p></td>
<td>Y</td>
<td>1008</td>
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
<td>1008</td>
<td> </td>
<td>Select and Free Text</td>
<td><p>Has the patient had an inadequate clinical response of at least <span class="underline">30 days</span> with at least <span class="underline">two preferred</span> drugs?</p>
<p>If yes, please submit the medication trials and dates.</p></td>
<td>Y </td>
<td>1010</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>N </td>
<td>1009</td>
</tr>
<tr class="odd">
<td>11</td>
<td>1009</td>
<td></td>
<td>Select and Free Text</td>
<td><p>Has the provider submitted documentation of medical necessity beyond convenience for why the patient cannot be changed to a preferred drug (i.e., allergies, drug-drug interactions, contraindications, or intolerances)?</p>
<p>If yes, please submit the medication name and reason for inability to use. </p></td>
<td>Y   </td>
<td>1010</td>
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
<td>12</td>
<td>1010</td>
<td></td>
<td>Select</td>
<td><p>Is the request for any of the following:</p>
<p>1) a nonsolid oral dosage formulation</p>
<p>2) a non-preferred extended release formulation</p>
<p>3) a non-preferred brand name that has a preferred generic product</p></td>
<td>Y</td>
<td>1011</td>
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
<td>13</td>
<td>1011</td>
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

LENGTH OF AUTHORIZATIONS: 14 Days 

| **Last Approved ** | 4/20/2023 |
| ------------------ | --------- |
| **Other**          |           |
