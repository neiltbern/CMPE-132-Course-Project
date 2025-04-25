# CMPE-132-Course-Project

https://drive.google.com/file/d/1ykWi54jQo13P08zsI-WYUbIvvhKcPBaf/view?usp=sharing 
<-- Combined dataset of UNSW_2018_IoT_Botnet_Full5pc_1.csv - 4, representing 5% of the full data


| Feature                         | Description                                                                 |
|----------------------------------|-----------------------------------------------------------------------------|
| pkSeqID                         | Row Identifier                                                              |
| Stime                           | Record start time                                                           |
| Flgs                            | Flow state flags seen in transactions                                       |
| flgs_number                     | Numerical representation of feature flags                                   |
| Proto                           | Textual representation of transaction protocols present in network flow    |
| proto_number                    | Numerical representation of feature proto                                   |
| Saddr                           | Source IP address                                                           |
| Sport                           | Source port number                                                          |
| Daddr                           | Destination IP address                                                      |
| Dport                           | Destination port number                                                     |
| Pkts                            | Total count of packets in transaction                                       |
| Bytes                           | Total number of bytes in transaction                                        |
| State                           | Transaction state                                                           |
| state_number                    | Numerical representation of feature state                                   |
| Ltime                           | Record last time                                                            |
| Seq                             | Argus sequence number                                                       |
| Dur                             | Record total duration                                                       |
| Mean                            | Average duration of aggregated records                                      |
| Stddev                          | Standard deviation of aggregated records                                    |
| Sum                             | Total duration of aggregated records                                        |
| Min                             | Minimum duration of aggregated records                                      |
| Max                             | Maximum duration of aggregated records                                      |
| Spkts                           | Source-to-destination packet count                                          |
| Dpkts                           | Destination-to-source packet count                                          |
| Sbytes                          | Source-to-destination byte count                                            |
| Dbytes                          | Destination-to-source byte count                                            |
| Rate                            | Total packets per second in transaction                                     |
| Srate                           | Source-to-destination packets per second                                    |
| Drate                           | Destination-to-source packets per second                                    |
| TnBPSrcIP                       | Total Number of bytes per source IP                                         |
| TnBPDstIP                       | Total Number of bytes per Destination IP                                    |
| TnP_PSrcIP                      | Total Number of packets per source IP                                       |
| TnP_PDstIP                      | Total Number of packets per Destination IP                                  |
| TnP_PerProto                    | Total Number of packets per protocol                                        |
| TnP_Per_Dport                   | Total Number of packets per dport                                           |
| AR_P_Proto_P_SrcIP             | Average rate per protocol per Source IP (pkts/dur)                         |
| AR_P_Proto_P_DstIP             | Average rate per protocol per Destination IP                                |
| N_IN_Conn_P_SrcIP              | Number of inbound connections per source IP                                 |
| N_IN_Conn_P_DstIP              | Number of inbound connections per destination IP                            |
| AR_P_Proto_P_Sport             | Average rate per protocol per source port                                   |
| AR_P_Proto_P_Dport             | Average rate per protocol per destination port                              |
| Pkts_P_State_P_Protocol_P_DestIP | Packets grouped by state/protocol per destination IP                      |
| Pkts_P_State_P_Protocol_P_SrcIP  | Packets grouped by state/protocol per source IP                           |
| Attack                          | Class label: 0 = Normal, 1 = Attack                                         |
| Category                        | Traffic category                                                            |
| Subcategory                     | Traffic subcategory                                                         |

