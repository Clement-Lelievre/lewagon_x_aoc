from string import ascii_lowercase, ascii_uppercase

INPUT = """gtZDjBcmpcDgpZcmmbgtdtqmCGVCGGsvhCFCCqvmCMMM
JrhfzfLTNfJhPnhQnfzHfCFFQFSGvMFCGQFsQSMSVs
TllTRrfNNlfzwhtZBZgtRDBp
vMdwjZdjwjvjdTZZvCcQMGnQMQcbcgLLCL
rsVhfmssPWzDVGCLJSbCgPLSQG
lfWNDHDgfszFRTFtwwNjdv
GLPqVqdVGCLCdczjMjzMfzld
JnWQvJDmvWBtlMzhrzfHQgcz
tDtJDDDDtWRRmBwJwWtpPRsGCGScLPGSqspNCS
ChVzZzfNDzNJmBQfjjJfmH
MrTMPMncGMJvPPvPWTbrMWvgmBgQwgdpwmdpdpjwpHQcdw
SPvvvbqrFvMvZzJzsFVzVJNV
mvBbvMFqbMMVVmtCBHpDdDPTDspdNWPDVP
zjSfftcQtwtSfQSpNDppsNsjPNdRPP
fgfStJShrgvvCLLv
GmFnNNwbFFbhQQGQnGwwwfBgnMMqVDBZVVBMfMVzVz
vWzRRHzTHcgfZDVfBgfH
SSTvrvRcPpcvjFGwNGbNpbwQwz
FFgbZZFZgFmpstLgmbtzqNrwVPlMPlSWWrMPNp
QQhTvjhcvjjvTcTcTfCcSRwwWzwzPMrzWNNWVVhwrwWq
GRQBfCRnGGTcDvBfGvffCCjnFZtFFgStJLbLHbFLJZdgmd
pppdjcrMMRDJLJdRcwRDrwssqHGGDHsZHHsvBVtvmVHV
nlCFWzGzzQFlSlhGWnPzFbSsBZmsssmVVmsBvnHqvNVqqm
lFTTTCSQSTrdGJJLJG
jpsGMgsmghQwQsMmhlQshjtTNTRTnFqRWnnqRfFnnt
SLBCHrcvZHbSvSZrSvSWnfvVNvftVlFRTqnRTq
JrzdZbBcHBCrrlHrrSsMgmGpJPDPQmpgQgPG
cmcZHgwgMgHSLmtjLfWPNNrWBNfffp
JTqGTsClHslVVRVCVGVJGnBrjdnnrdBNvjPNBNBrWvnW
VVlQlqTFJlzzlsVGsRCZMthHDbwbFhgcbwHchg
qgZjgjjbssqgsjlNqjhTtdrfQdTdWLLnDVfHtHWd
zcGMBDDzcLnztfQQQz
JSppJcBScMmMFFBRCpRCMmGlggvjhbhlNlglwbslCZjhDZ
hvhmqcqwwcTBvvwQnRQnRnTRFzFzQz
jWLPPtPsgMtpdLMLWllpgLLQFQhFJjnVrzFrVFhnRzJJrJ
WPWffgtSdspdhSMdlSdtfBbHmSvqbNBCCmcBmcvcCH
frVcrVcggfSZJfbbJvBd
hwWQnwhWQmQmThTSsdvvSMBTBzcb
wGnFFCGlQwntGtCtwntwDmFwRgLrHqNRqqcNNgRrHHLggCjp
wRSwwHDMsRGHvNBNjTgvjgJD
mcLcFCclWQWQpPQWVQcQcvvNJjrNBTrvgJgBvTRvCg
VFPbQLchQLSRfbMtdHGH
lfVrhnlRRqrJZVDJdHSWCvJCJSbj
BFsgcgMNNQgSvbfCff
ffNPcMtzqPlnmRGh
ZJplFmRJmWRJRWmTJCvtTtnLCtndCqtqnr
SQsVPQHBQZNSNSLCfSLrcLcrrr
VMjPjbNMDsVHmRllmZpZWmjh
LcTLRbJhhdhLJbbclfVvfWQVWFRWFFfq
rZNttSNvtgsPPFsqBFPWQF
HGCSmHrrwNnHGMLpDhbzzpmJJv
VlSWzRtWSJqWdfhdqBdF
mTDHsmmmcHpgrCgCrTsMMtqfsFNsZqfdMZMNbd
TDcpvrpHCprCpHrmcQvTHgTQzSnLJnPPJlLzwJtRVJwLjJ
vZSWZJZJFvhZldZHdvvlphZSNGNnmzwCPNHNHGNrrRHGCPmP
bjfgcbjTQTFQBnGRRBCBNwBnCz
csqscsbssQLsgQcLgLQLQTQpFdlhdvdZdpZWhJplShWWtq
QgQvHnfflfBwQCfwlfglnQQccNcRqGGcjmcsGjddwdzsJc
DhZbTLZTDMVTsRzsqsRjszTz
FSZVtMLMMWbSgqSvPQlnpH
MMPllnnBmfSHvBgCLf
whZjGRJdjcNjjhRjCvgCfbSvCZLHfpZs
RRWGWwNRWwhwclmrgFmngFPMWm
VVHQGDGDGsdRrmZBQZRCVHZCNcSTTPMwwvTTwSSNqBqvgMvN
nfhdLfjFnJpblLbJjWhtnjWPScNnwSTPTPqTvgngNNvSvS
fpWljtpLjflfLfzlhZGQHZQVddHrrQRDRz
VCHCjwCwMSZSqQzhhQqcWZJD
GGGrFFgNRNNgmfnTdgmWQpczvPvQPWQJGDpzzc
lgTttRTgmfNRntrTTngrCbjCwJCHjLBBHlMVMsbB
szgPPlCblggVszhLmzvcvNrqpjNqmrqqpGvG
wBQDtBfQDtFvLjjctLqTMr
ZFWWdDLQFwSfDSBSQQBWnnnQVdbhgRVbsHzsshbClzzCVggb
VpVsHVcqcMVMMNHpsspstbMqzBztJZTBBfJfzTvZfvWJWSTv
mDDQgCQQQHdrwgSvZSmJJZvWfJJf
drCjggDlPdgrlbjNcnhcHsbpsj
cNNDRRpDcNcTpppsqHLQGLfRLvHzLH
lFntJjtbFFlsmsjvnGqHWLfhfqzzQh
sgPbjBJtPgbPJblblJgbgbwdBTwDCwpwrdZZVcCcDppc
GGclMjLnnjCMchcChLMLcnnzRFJDZJSRSzzzzDSShszPRS
VHgFQgwVwfNNpQVfHzQsPPPJDbmZbJDJbS
HfNVWdHVvgHgVWVNppNWVHwTlvBFcClBCjcTLTlBnnLrTL
GTLdlJhffQwDRvWLrp
HVZVNjjsPqzNjNNmNgDWMrRQpWvWRHrDHBWp
VCqVzjPjCpVqCVPCsbctcnblcGlTbGnlbFJf
flHdfdBNdZcflBMjqMjBNfZQhvJbGvqvsshJQsJCJDWvvD
gFTzRRpzRTwbgbLmtCvsJhWsChrWCrtWCC
VzzzFbVRLPznmRBffPNBHNMdlZfl
FFFMwCqJFFmrRwgnbLrL
GpjGpQHQpfjdjDRnLrbrRQmJzzgg
BphfhDcNcHNvPBvSqJMWJS
NndbWpDBNbjvWLZqWsWQ
JPFFTSPfgcMgftQQGjvTmsGqzssG
gPgcfcVFgcHqSqVhbBCHlpbbpDlhDD
FSdfWFTTBnjsDCjsmrrT
pQzLRVLppLGcQjqbmVDJsChCvCbVsm
qHLRGqqZzGjLqBNMFdnHlNlBFN
DjqbfBTchDjqqCjjCTWNTbdzSVzGZQGBwZnQnVwpSSnQ
ssJlPrtvMsRLrrJQGNZJSpZpGzSG
rlFssHsvPRPMvFmtHvtqjhTgjbqhWqNmNqgDNh
vcpnRqwwLLbvvcGpDQWDFSCgMrWWQWRR
gtNfBfllrFlHrlrl
ZPzftBmsNBNBPJBZPmZPNtmPdGLsqbwqpqcndVLLGpVGvqgV
vRBfQqqBQPfbrFvPBvPbhLDVDVDQZVVtZtlWLLLt
jcJmFFwnhJVZLWVl
sHTcmNNHzncmcjmdsBCrBCPCrBBqCFrqzb
bbZRnGmNnBGGMNRTgCmWWGGSrvSvFHvzFvFQDF
LjwphpdPdLpLJVqfJrQzDzfrvQHSvDcQrQ
DJphdwDsnmbZsTZM
rdNrZNBSzSztnNzWCcNpHlMwlwHWlM
QqLGLJvLjtvQWhgHgchHwHJw
GtjTGtDRqvfLRGnrzsmZmfrVFBrV
TdMhZrTTNvwphcLL
WnnmffmDWnWPsPCJNpNcpNVNQp
fsjbWfFFfnmmDsFDnnflSSdczlMdTHTzTTRRBdtT
cMcPcMcwgWJMjWWhFWCCQCmqCFdh
bSLVLblnNnLbVfnsbSbCChSQdChptpdqZrmCmZ
DLGNfnGVDNDHbfzjRcRgqHMRBJPc
HVFVlVHjzjjlCJjHjCjnvDrggrgLdqzddMqrzz
SSfBTmtNdLqngvrm
TwnNfPWWpBSBNtTHZCGlPHCQJHZHPV
prvccpFQpMcQBwsvssshdwSTPD
qbGHVbNJGqwdPgDrTsDJ
fGbGqqlGGHflqLlzZBBrRcrtrZlp
fCSPhltMBmPmbdgd
DjvJJscvTsHHDbWzBWsWbdwgLB
VVHDZvTppRcJVFFppvvRJDJqMSGqCtZdthttrnthSZMGCr
ZcSrSdrhDjBDDCmZdZmZjhwVHwqVVsMwgswVVwMfhw
PNvzTPNbnzcPbGQNJTvqwsWgVgVMMWpQqwgHpp
JTPGPTzNttnbRTPlPtNNRlFrFmBcmDljjmBFSCmLZZBr
mNvRRCVMtNRdFNtMtBHHprpHgJgJWwpBnprg
LZDDlSLlTslDfbcpJJWndwcscnwr
qdZZGSDhMVRCGtmC
VGFjjgBShGdGzQczcGRG
MppqCDfCMwfLDfvNmrtWstRcMPzRMRsRsPQS
NwDCffLppbqqrqvTBngSbnBHglZllH
vdllJVDzmVDVqvvWvdqJlcWrCsfCsfSSsSJfCSfQQCCbCQ
jnTHZPZHMjZhMjTpHgMpgnbNqBstnfrtSSrBSNssCrfN
LHLTFLjTMTTTwjHhpHTcwmDcWVDlvRDmvqwWlW
rqQsSStdmsdLqlNNPGlGlV
FpFpzJNTcHzRHRHlGwFVLFBLFGVvlw
WCCjWRNJTJWhQhbhrbnd
jsQjfrRTRwzSsRTgNchlnlhqcnlQmQ
dFDtdFBDddHLJpVpHHtVbtHFCWlWlGlNlmGggNqgglmcchqb
dLDHMVdLtBBDBFVJBFthtJHRTvsMSvsTrTSRvPPjPzSwRP
CSPpSrLlrlPrPchLnSlbDbbRttDVhbGRDDJRtD
fzfvmzTMmfsFszsHZsHMHVfwtbjBDDGjtRBjQQGGJb
HmvmTFmqmTsHqzzzzdTsMMScndccdLppnLCSPcCLrVgr
pfMflRnfrnjrpjnFzDpfDMmMLRTLZVTgLsvdZgLLZHSVWZRd
tBGNhwPGcNBBWwZddsSTTPgVLPdT
JwthtwbbhNBQhwhbBCrzpnprnWnprlzWlClD
PPnZZjnFNDjlJJhtMddfTTdD
QGLHFWvQJtzfpvCt
swqSmmQWLQwFWLwwRcqNNBnnbgPqbPNbglVZ
GCLSjjZGZhpvGtBgjJlnJDhhJMVDPnJlJP
mNtQQwNzQRHWdJHnPTsddlln
zQrfmbtNbcQcrzmrRBZqBcvpjSGLZGLZBB
zGNzgsjDssvNbPlWJfJq
RLMVSRMLhCLZSMZHDSJWvpcqfbfhvpJqcWPv
dMVHLFHLZMLRLLFRHHHVZMgDTntgstGwznzGGnzjDFwG
wCLCHLBwzBtQRLHLbNFFfdqdDqVrVfBN
JGvljmgGZvMlfDRRnnnZnfND
GppRlgJlSllSgjMsmllpTjcCLczWztPWPwwwzWThtcQh
WvHbvvWnFHszDRSltcCctCFD
gCmJmCCPTPqpgrZtjdRtDRplcSjS
rJJrQPPJQmrmrhGTznCfLMMbfvWfbCWQ
TqBWtTbFBNNRRtwQpJJvvvZPpTSQ
fRMfsMssrGhSmMwSQvvZJm
VggcVlsCgHnVFnndbbnR
NdrSSWBNPPSWWHPPlwlLZHLZLMhjlLLH
pVptMTgVTzLwZTzlbF
qsRmRJtsMvMqgqgRvCdcSrWSPcWrDmmdBN
nbJnfqWcmCMnSBSHwzWBsHHz
dVpdvdppdptppDlvlHcczSgNcgww
VGTdTVtGtRLFPTDbcfCmmcCQJQjcrT
VTjrjrjTlTjQMdpGrWMSHvSG
wnNJbDmttnwnhNwcJmNGdvWvMSfvMfhSSppSdp
JznFnNsGnzzGFDJsFNmLgVVQZBlLZjQTLTjTls
hpngHwcpWHgjjfhzTJBfBB
RFFbFlQlSdRsbRQQMGPRGdSGjBvvNTvzZMBvjzBBTJTvMBBT
GPSSPDDDFzGlGGRzLzGGPRWqnprcgCHwCHpwHWVcncLV
LLlLGffQLPRThRwP
MpZjbmznWqmqZznmzmpZqZnMRgPBCTPfgRTTwTjhwBPPghjP
VnZpMsMMJnWsmnJpJmzrtFlGQFrHGvSvfHStNV
MQqHMQPnqmpDdTLLRnDjsj
NGFzwgtLBtFFGrrCtzgfgCNgSsdTDSSTsdssjDdSlZRjTSBs
zCwNLthfrbCgzzhqhmccJPhQHVmV
SndBVcgdqcRBRcdPBBcVcQTSSMLMlTssMNMWsHMsLQ
GmJvZvhqpvZtNwwWLTTLwMMm
JFJpzFGZqjvhGZcjBPcCBBPnnVBc
rJWbqTvwvJNbPDPPvLcZvPDp
QMnfBsjmFPLcHRDfPp
lQlMlmtFsMMBstljlnGhtMhmGNqJqTcWNNbWdGwdNNJCrTrq
LcjcNCQNQWDpRDjRTj
vWvszVVSsBGWsTJRFHRJTTSTRJ
vvGbtqbGVVBqtzbqvBdzVLWNLClwnwMLWlQNMfdPQP
TWBZsWrjzZzWBrBsrrsTLNNJvFnJVmlSFFQnGpmnSJJS
qdCggdqqqhhqwhRbCwbCPqhlJFPPGJQVvvvnpVVmPnnFvS
ffgCfghDqDdCsGWZjTsLrsfW
QzQSSQmzSsLQcLmrcsLzccgqCnwqCtZDnDnrZwgnqTTT
hFRHHRPRPMtWPGVPRlMljRPCgWBBDTgJBgnwqTZDBZDWDB
jPjPHRMjjvdjVFhdNfbsbbQfbcddmNtL
jJlTqMqJtdztJqzcSJSlTdSlprLsRRHwcRRrsrHbrnnRHsHL
VVVMWNNWmNmLnPLRHrLp
NGhfvvVWBNfNNCNCQTMqjzgTQBSSSqll
SSSRMRSRpnMRHLqWLfPlDGlGWldD
hbNtlmvrNrsVDWsGPfPfqG
jvbBNmvlJjRcCzHFppCJ
hhWWPjnBGBGnjqBWSnhhsNLllLNcLczJcqcTlLTlfl
FHvFFMHwdmvrDbwCbbvHwdHnZTMLzTNTczflJTZclzNLlLcJ
HdFFvdDvpCDdrnwrGhBQhWRRpsjQWWQW
sBsvtJtdRdjNbWWrTllqlNgg
nSZSnPPZzMSnSlScWWWgrVWCrqgrWMWr
lzSncQcLZLzlwDvtdDdFdFJJhHvJ
lpsTLDlTtFtlWHPDvvgPfgMrQQJM
zmNbzcNjzldjwmbdbhhjcjRgfwrgvMwMMSRJSvQQvrRf
ZhjqcjzNhmzNqBqNznmcWHplCFGnpCtFsGWHHWsH
ZPGQBFHFbhSrHqtfSrSr
nMdznzzMDTnjMQrMWtrMptplqpqS
wzjczJmccTJCmcVghZBJbPBQBbVh
wLLMJbqSBBnnJhbvbFSSRRlztTrHzrrrrd
QNNGVPjWPGVqltTHWCqCdH
sjNGmmGVGgQNGDVmsVpgqQVpMDhvbLwMffZfhZbLnfLLLZwb
gQLcQrMtBPdwSBsSlmBm
TfCpTJnTbfqgsgwgppsSzp
jVbvTnvWfJnJjjbfCjWWjrFPrLMtcDPgLMQQRtgZVF
gwpHvpgwngGHcnvNvgnmsqCzmMzlfqmmqzHHCm
JrdSLdBVPRDtRtPfPPzCJhjqmljzmmqszzsM
SWLDDtVdrZWtSBRZfRcwgFGnpNFpnTnWnTvT
rpcnHrwrhWccNZDDBBgBVCSW
nmzFRRjFmmJQNDJC
qznMlqGnzRtRGvqGFRPrdMhwTpTLfLcppLHp
wthvbmhmChWMRJLJzngZpzLLNC
SsdBVjSTjBdffBFfcSdVHfTrnDZGpQgNZHNnLZGpJngJGLng
sSdTcdVScdcrccjcrBPrBSjcvmRRwlWPhwmqtgWhMPtmMMqR
CJJBdBCrHdBhtRHctBQhRMrBwZpwZWNZNSNTwSNpQWpZsSSW
LVFnvnbDjLsDPsPqFFvPvDnTzSTwNwPZpSmpSpgmgZWNTW
LjlflbFjsvVlrHcrHtrfcChH
tVLJGNRtfBBNGBrfrbzmfhPsrsPC
DWWDQHQgllSFqFzcsJmzzSSzmrrs
MJFQDgMqnHlDvFdGNBNNZGNVVvjV
wnNwGCBBFNWBqjFBnLLGVDHhHmDPHvZTjTvTrPvD
bMbttVScMJQtdgSgstbJRSPmrTHmHmrmmSDZlrPrPDhv
cMbgpsbVbzbdRMRFWLqzBfLGwwwwfW
JpSnGSGpbGgsWWPHJrdfsT
MNsRqNNvMQDTLWHlffNHLN
qqmtRzRvCRRQDqjqjDmsmRpZwSZbcwbnCcCSBBnSSnnC
TWqlqpRqRptqlRhrmtGGzhbSrSdz
VgsBVMvgVZfZvPsMVNvfZfvVbSPdhFPFhbzLhJdGFJmLhhhL
QZgvZgvHwbwHbMsMRllRjDRDnQRqlRjl
fsPQwnHnHLLfnBBnwwGtjTGRWTWTWwhV
jblbdjZFDMbGllqTGTtVlq
gmdMgZMbjpZDcrrDgdmszsPLpQfpBPPnNQNLLz
HRsPPGMhLPMrnPchPSwStjbSttSvtHSqQw
dfsCfpCJVJCvdFBFwStwjj
gTNWmWfTNVZVJzZWpWJgTpfhnDrMnDclgDlDrDRnRcMLDs
ZQZQJMqdwmZvqfPmwRjpBBjHjnshnjtt
zcTPTLDTFWLGTrTSWPcDSSHjRlhRsDhHslslssBRljjj
TrNFLbTWrGNZvmvVQPQV
htfLgmtSLcTWNLcT
slbHlBBGbqRsblBHvdNJJcjFFNBTVWWWcn
bbQsHMMblHrMsGRqvQhwCTQCwtQCzSpfmS
zmqdphmFmSpTzhdqhFmwjjGbtcvDbcGGjllGQjSP
HJFrMCsVLrHRRMCNrVMVnctvstlGcQlPtGGjQtGlvP
RFLHLVWrNgVJzwzwfgffwdfp
vdMjSmMMpmMWhRpndRmZnhvHqLpGHcJGGGDLHHLGcfcLfc
lPBwwrsCgLFggcqqLW
TWszsWNBTNdmSRvjbZZT
zFlBGpzzzLLNjBwPcwwmcNPfWNQn
VHSHRJTJDSVVnmcVVPpWmpnf
DMZHHrDHHrJrrZrShZsHGbMBbFgGjGCgjpFlBzzb
FVMpsvTqvqMssVsWZSrqWFvwlGDGwQzwfwQQNLzDlwlZwf
hPbgBHhJJcJPwCwDpNllCCHC
pnjbBmjgbgmqtSmsTtsF
DHZHmfTmCfjDZHMZmzffHHnQwwTBdQwbSdBGBQwhBQTQww
cqstRFWNtLrNFwdVShlBSlhBRl
StJWpLptNWLtJcpqPrFHDjZzzvnDDHPCZjPvvz
hzffhGVGGhzRqTBLTqHL
sFFFsMQlwJMsmrBFSNHTHNqrTS
pbdsJMdJMJbwbmJJtbTtgnffGgVVChvD
FvJnFnCpQTddSSmFdFpPPsVhppDjBzjDVhDV
RgZMZbsgzlDPlhjb
cHHHRgRZgfHHZGZfHZcLLHrrCrmJCmddrsvdJsmvFFQG
dpJDdZwLnvdvFmFMmHjslMLH
CGCztgPhWCWhzzzNNPGfrrWfmbbsmmHjFHDMsbHMsjFPjbHm
rNQDGzzhCCfNrzrDzChTcZZvQcTRJpTwdvQpVc
VpvNGhGHGNhHbPsbVbvfFtLCzSCFSBsCFSFCLB
MlqJwTnrRRrRnMlQMHfHzHzWFWtmTzLWFC
ljZDDHqqjqRbpNhjNNgcgc
qrQtDzcQzbrcfdbqrQrthtscSsvpvnsSHpTpLpspmsSs
CVwNNVRNBSHsLSFBTv
CVVVNZjlVlGwlGlljNlWJVrrfqbPQQqHqJhhftbfDJqf
lpmrPDPDjPlmWrVzPztZwFjtFbBnRtZbbcRL
dnqJCCgQdNqbqRbRbBLt
QGhGddGCTdMHNTGgshgJhzvSmWWPSsnprpPzWzsWlr
hCJHTdJJNvTdSSNssjvfwgntwDgtgwDGCtZwtRRB
mbllFmFMFbMVWWLpbpZwwBZTZnnVwnTggtDB
MmzLQpFPTmPzHvfJNNzhNs
dzgBwzlgrrBrVLLlwLBgBlgRScDMMDDswMsHZRGDsZGZmM
HPfPbjCFJjCvfnnsjsDDcccmZsRSMc
hCvHfWPPnvJhPWpqNNhqLqzLqLLd
"""
score_dict = {
    letter: ascii_lowercase.index(letter) + 1
    if letter in ascii_lowercase
    else ascii_uppercase.index(letter) + 27
    for letter in ascii_uppercase + ascii_lowercase
}
priority_scores = 0
inp = [row.strip() for row in INPUT.splitlines() if row.strip()]

for bag in inp:
    one, two = bag[: (l := len(bag) // 2)], bag[l:]
    common_letter = set(one).intersection(set(two))
    priority_scores += score_dict[list(common_letter)[0]]

print(priority_scores)

# part 2
# almost the same problem except we don't compare first and second half of each row, but groups of 3 consecutive rows
priority_scores = 0

for i in range(0, len(inp), 3):
    common_letter = (
        set(inp[i]).intersection(set(inp[i + 1])).intersection(set(inp[i + 2]))
    )
    priority_scores += score_dict[list(common_letter)[0]]

print(priority_scores)
