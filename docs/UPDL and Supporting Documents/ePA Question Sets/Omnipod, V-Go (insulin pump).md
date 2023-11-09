# Omnipod, V-Go

[Criteria Document](https://mygainwell-my.sharepoint.com/:w:/g/personal/kaelyn_dobbins_gainwelltechnologies_com/EQ4qdidyvxpGjdwJP4Zi6UsBtShseV6HY81mvCIBIYka9Q?e=QOlW60){:target="_blank" rel="noopener}

**insulin pump** 

|            |                              |
| ---------- | ---------------------------- |
| Criteria 1 | Omnipod, V-Go (insulin pump) |

  

<table>
<thead>
<tr class="header">
<th><strong>Criteria Title</strong></th>
<th>Diabetic Insulin Pump</th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Criteria Subtitle</strong></td>
<td>Omnipod, V-Go</td>
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
<td>Corresponding Code (s)</td>
<td>Type of Code (GCNSeqNo, HICL, NDC)</td>
</tr>
<tr class="even">
<td></td>
<td>OMNIPOD</td>
<td>082933</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>OMNIPOD</td>
<td>083217</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>OMNIPOD</td>
<td>083219</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>OMNIPOD</td>
<td>082513</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>OMNIPOD</td>
<td>082512</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>OMNIPOD</td>
<td>083229</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>V-GO</td>
<td>068529</td>
<td>GCNSeqNo</td>
</tr>
<tr class="odd">
<td></td>
<td>V-GO</td>
<td>068533</td>
<td>GCNSeqNo</td>
</tr>
<tr class="even">
<td></td>
<td>V-GO</td>
<td>068534</td>
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
<td>1  </td>
<td>1001  </td>
<td>  </td>
<td>Select  </td>
<td>Is the patient new to therapy (initial authorization request) or continuing therapy (re-authorization request)?   </td>
<td>New Start (initial authorization request)</td>
<td>1002 </td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Continuation (re-authorization request)</td>
<td>1234</td>
</tr>
<tr class="odd">
<td>2  </td>
<td>1002  </td>
<td>  </td>
<td>Select</td>
<td>Is this request being prescribed in accordance with Food and Drug Administration (FDA) approved labeling?     </td>
<td>Y  </td>
<td>1003</td>
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
<td>3  </td>
<td>1003  </td>
<td>  </td>
<td>Select  </td>
<td>Does the patient require insulin injections greater than or equal to 3 times a day and self-home glucose monitoring greater than or equal to 4 times a day? </td>
<td>Y  </td>
<td>1004 </td>
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
<td>4  </td>
<td>1004  </td>
<td>  </td>
<td>Select and Free Text  </td>
<td>Is the patient adherent to the insulin therapy recommended by an endocrinologist as demonstrated by monitoring logs and claims history maintained for at least 3 months?  </td>
<td>Y  </td>
<td>1005 </td>
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
<td>5 </td>
<td>1005 </td>
<td> </td>
<td>Select </td>
<td><p>Does the patient meet ONE of the following criteria while compliant with insulin regimen: </p>
<ol type="1">
<li><p>HgA1C greater than 7 percent  </p></li>
<li><p>History of recurrent hypoglycemia  </p></li>
<li><p>Wide fluctuations in blood glucose before mealtime  </p></li>
<li><p>A marked early morning increase in fasting blood sugar (dawn phenomenon glucose level exceeds 200mg/dL)  </p></li>
<li><p>History of ketoacidosis  </p></li>
<li><p>A history of severe glycemic excursions </p></li>
</ol></td>
<td><p>Y </p>
<p> </p>
<p> </p>
<p> </p>
<p> </p>
<p> </p>
<p> </p>
<p> </p></td>
<td>1006 </td>
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
<td>6 </td>
<td>1006 </td>
<td> </td>
<td>Select </td>
<td>Is the patient capable of managing the pump and that the desired improvement in metabolic control can be achieved (or someone assisting the individual)? </td>
<td><p>Y </p>
<p> </p>
<p> </p></td>
<td>1007 </td>
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
<td>1007 </td>
<td> </td>
<td>Select </td>
<td>Has the patient completed a comprehensive diabetes education program within the previous 365 days? </td>
<td><p>Y </p>
<p> </p>
<p> </p></td>
<td>1008 </td>
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
<td>1008 </td>
<td> </td>
<td>Select and Free Text  </td>
<td>Has the provider submitted a letter or documentation indicating the patient regularly works with a certified diabetes educator?</td>
<td><p>Y </p>
<p> </p>
<p> </p></td>
<td>1009 </td>
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
<td>9 </td>
<td><p>1009 </p>
<p> </p></td>
<td> </td>
<td>Select </td>
<td>Which product is being requested? </td>
<td>Omnipod </td>
<td>1010 </td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>V-Go </td>
<td>1011 </td>
</tr>
<tr class="odd">
<td>10 </td>
<td>1010 </td>
<td> </td>
<td>Select </td>
<td><p>Does the patient have a diagnosis of Type 1 or Type 2 diabetes?  </p>
<p> </p></td>
<td><p>Y </p>
<p> </p></td>
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
<td>11 </td>
<td>1011 </td>
<td> </td>
<td>Select </td>
<td><p>Does the patient have a diagnosis of Type 2 diabetes? </p>
<p> </p></td>
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
<td>12 </td>
<td>1234  </td>
<td>  </td>
<td>Select and Free Text </td>
<td>Has the provider submitted documentation of objective evidence of improvement in control of diabetes relative to baseline?</td>
<td>Y  </td>
<td>END (Pending Manual Review) </td>
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
<td>13 </td>
<td>1235  </td>
<td>  </td>
<td>Free Text  </td>
<td>Please provide the rationale for the medication being requested.   </td>
<td> END (Pending Manual Review) </td>
<td></td>
</tr>
</tbody>
</table>

LENGTH OF AUTHORIZATIONS: 365 days  

 

 

| **Last Approved ** | 4/13/2023 |
| ------------------ | --------- |
| **Other**          |           |
