from math import lcm
# directions = 'LR'
directions = 'LRRRLRRRLRRLRLRRLLRRLLRLRRRLRRLRRRLRRLLRLRLRRRLRLLRRRLLRLRRRLRLRRRLRRRLRRRLRRRLRLLLRRRLRRLRRLRRRLRLRLRRLRLRRRLRLRLRLRRRLRRLRLRRRLRRLRRRLRRLLRRRLLRLLRLRRRLRLLRRLLRRRLRLLRRLRLRRLRRRLRLRLRLLRLRRRLRRRLRLLLRRRLRLRRRLRRLRRLLLLRLRRRLRLRRRLLRRRLRRRLRRRLLLRLRLRLLLLRRRLRRLRRRLRLRLRLRRRLRLRRRR'

# paths = '''11A = (11B, XXX)
# 11B = (XXX, 11Z)
# 11Z = (11B, XXX)
# 22A = (22B, XXX)
# 22B = (22C, 22C)
# 22C = (22Z, 22Z)
# 22Z = (22B, 22B)
# XXX = (XXX, XXX)'''
paths = '''VJN = (LNC, RRK)
MJD = (HFS, VBQ)
GHK = (BDH, QGD)
GQG = (JVH, RGR)
RDL = (QPQ, CNG)
BDV = (JGN, RGX)
TFD = (XLG, NQT)
CVF = (DJM, PPL)
PSD = (BCF, RRX)
BLZ = (LPN, XVJ)
BFJ = (TGL, BXH)
PQM = (PDV, FPS)
BKF = (KMG, SGP)
RDF = (MJD, DKQ)
DCF = (BHS, QLT)
KCP = (JCM, MNP)
CDG = (HHP, GRD)
XDB = (XVQ, VHN)
ZZZ = (MTL, KNJ)
MPK = (SXH, GFC)
GLV = (HMD, QTM)
HMD = (QDQ, RKK)
TTS = (XGQ, TFD)
NHD = (BDV, XQJ)
RRL = (SNF, GQG)
PHN = (TDJ, JSG)
NXP = (GVF, FHP)
SFX = (KSN, MXH)
XQL = (MDH, GHK)
PBA = (RVX, RFP)
LLN = (KKM, DMV)
LLK = (XXH, HRX)
LQF = (TXG, GXX)
JGD = (NHQ, FHM)
VMH = (NMK, KVC)
SVD = (TTS, FTS)
VMS = (FMF, CDD)
RGR = (XQB, XVC)
VTF = (MMF, FVC)
HVC = (RDT, LJH)
MXG = (KGF, NST)
GQN = (NGC, RSC)
RKN = (KXL, CCR)
DDD = (NKM, JKX)
DGF = (NNJ, NLC)
TFV = (FGC, JTQ)
CFK = (LSC, JFX)
HPG = (JHQ, PLV)
RSL = (RFJ, FCJ)
JSG = (DRM, KHD)
XBK = (NST, KGF)
QQD = (RND, LCX)
DJD = (QHF, KQJ)
LFP = (QVN, CVF)
TRB = (KTH, DDD)
KJX = (KLJ, HCS)
FPR = (SVC, NXM)
RDR = (TSN, BPL)
LNC = (TXR, LGB)
SKV = (MCX, PTV)
KCF = (NGC, RSC)
SFH = (MRD, TNL)
RPR = (KKM, DMV)
HXH = (LLN, RPR)
JLS = (LFT, PNR)
LCX = (QVG, MCT)
KGV = (NMB, KJN)
KKM = (JLC, SKV)
GXX = (QXJ, QNJ)
CTH = (JRH, GHR)
QVN = (PPL, DJM)
NGM = (TMK, VNN)
TJF = (LSS, LPS)
NNJ = (NKJ, VHH)
GNS = (PVJ, LMF)
SPP = (NQM, NQM)
FCV = (XHF, QPD)
HJX = (VLV, XQF)
SVC = (DPK, QVV)
KHD = (TMN, LCB)
NQM = (NRS, NRS)
MHD = (XGH, DJD)
NVG = (KVM, KPJ)
DJM = (FNG, HXS)
TVJ = (KCV, QFK)
CMV = (VPV, NNM)
DQR = (KNX, FJM)
XXH = (JPV, XLP)
GQQ = (LHB, BTF)
JPM = (SNM, DDX)
GFS = (VCL, QCN)
JMH = (RMP, BFJ)
VBQ = (HMV, XNS)
RPQ = (JFP, JKF)
GQV = (MRT, LMQ)
HGX = (JRR, LDL)
VRC = (FXJ, VNK)
XHF = (JMJ, DTV)
KFD = (BTM, PQT)
NKM = (MXJ, MMR)
CXX = (VRC, XBJ)
SXK = (KTM, DSB)
NQF = (TSV, DTT)
RND = (MCT, QVG)
LFX = (TMF, VTF)
SXS = (PCC, RVJ)
MKF = (SHQ, VSG)
PFQ = (SJX, GLV)
SGT = (NVV, QPT)
NXM = (DPK, QVV)
DGL = (NFM, TPX)
JTQ = (LMM, HSM)
DFL = (DQC, DJG)
MXH = (NXL, THH)
HPV = (GFX, CTH)
LSC = (PNB, HXX)
VFQ = (PTM, KGC)
GLP = (BQF, NKQ)
DDX = (QQD, QKV)
HRX = (XLP, JPV)
KJL = (GSH, HHF)
HJN = (PKS, ZZZ)
FPS = (QBL, GNG)
HLS = (PDT, HGT)
XHT = (LFB, FDC)
RCC = (VKG, TJF)
NXL = (XNH, XNH)
PDX = (FHR, SSC)
JPL = (SSC, FHR)
CNH = (DTM, TTT)
CJB = (KPJ, KVM)
GHX = (QLD, GHQ)
MSG = (MXG, XBK)
PQQ = (QPT, NVV)
QGG = (MQR, MQR)
QBL = (SPP, JHH)
FQQ = (VQD, KJX)
QRD = (LQD, RKN)
JKD = (FVD, BXL)
DJX = (XVK, JJH)
LCV = (RRL, CHK)
BCF = (NRG, MRL)
TXR = (XQK, PGF)
BDH = (KMK, BVK)
GTK = (KSN, MXH)
HHP = (PMP, PFQ)
QLD = (PTH, RDF)
RFJ = (MHD, SPL)
KFR = (SHF, SHF)
VBD = (JCC, LDD)
MVL = (HST, GRL)
SHK = (XHT, RLT)
XQB = (MVJ, QQM)
LQD = (KXL, CCR)
DMS = (LMK, LSK)
FXQ = (GRL, HST)
MXJ = (HGX, FVB)
FHM = (SPN, HQJ)
MKB = (FCD, FCD)
QDD = (VLN, HCB)
PTF = (DQC, DJG)
RFH = (JHJ, PHN)
GRD = (PMP, PFQ)
DMD = (MMP, GLP)
HCQ = (JQG, FLR)
VPV = (TRG, BQQ)
PDV = (QBL, GNG)
CCT = (GMX, KCP)
BCV = (DJX, DKC)
VKG = (LSS, LPS)
NGH = (TDQ, PHM)
JVM = (KJK, GQQ)
KMG = (MFS, QST)
MPD = (LLF, PQN)
QHK = (PNR, LFT)
HHK = (RCC, HGD)
MTL = (MVX, PJX)
PJM = (NFM, TPX)
BTM = (QKX, FRC)
QKM = (NHQ, FHM)
XVF = (PQN, LLF)
NHG = (BSG, VBD)
KQJ = (XDB, BVX)
XKL = (QLC, LFP)
VXX = (QLT, BHS)
MVJ = (DLL, JTX)
SJP = (BTM, PQT)
QRT = (HHP, GRD)
XFM = (LSC, JFX)
RQH = (NGH, RPH)
QDG = (TQS, MJR)
PQT = (FRC, QKX)
FHR = (SCF, FCV)
DTV = (XHV, HXM)
RGX = (RXQ, NGM)
XVM = (RKN, LQD)
KPV = (RLJ, LVJ)
NRG = (JLM, SJG)
NPD = (RCP, HJN)
KLJ = (DXV, PMS)
LSJ = (GXX, TXG)
QLJ = (KXS, DSS)
SGP = (MFS, QST)
PSB = (HMX, JNQ)
VNK = (JTK, QLJ)
JVH = (XQB, XVC)
GHR = (CRS, TLK)
FCD = (VMX, VMX)
JTX = (MCC, NPT)
TDJ = (DRM, KHD)
MFR = (HHC, BLZ)
SNF = (JVH, RGR)
JVQ = (RSQ, RFB)
BHL = (BNM, GNS)
QGB = (KJN, NMB)
KTM = (GPC, MCH)
TJP = (MRT, LMQ)
MRD = (BMJ, NDV)
LKS = (SXN, XBX)
QHT = (NHD, KBM)
VSN = (CNH, RHC)
SKG = (BCP, JLJ)
JMB = (PDV, FPS)
DSS = (FPP, HDH)
JRH = (CRS, TLK)
LSA = (VRQ, RDR)
FRC = (KPV, MTN)
JMJ = (XHV, HXM)
RRX = (MRL, NRG)
FTS = (XGQ, TFD)
QTS = (FMP, QDD)
RQK = (JFP, JKF)
XTS = (JCT, VGN)
KKZ = (GDB, LRB)
NDV = (LMX, VSH)
PNB = (QGG, QGG)
FPF = (XLQ, RSL)
QFK = (RXL, GHD)
MRS = (NVG, CJB)
RCP = (PKS, PKS)
HDH = (HBB, PGM)
TMF = (FVC, MMF)
PKS = (KNJ, MTL)
FVB = (LDL, JRR)
VSA = (XVJ, LPN)
BTD = (TQS, MJR)
FPP = (PGM, HBB)
NMB = (BQR, LLK)
SXM = (QQG, VMS)
LDL = (CDG, QRT)
HQJ = (RBL, TMD)
QFG = (RHJ, MKF)
CPX = (NRS, GFH)
QQF = (SKG, RKL)
SSC = (FCV, SCF)
KXH = (VDQ, RFN)
KVM = (DMS, NXK)
DBJ = (GQN, KCF)
VDQ = (BDL, JBM)
LSK = (CHB, JMH)
KBM = (BDV, XQJ)
QVA = (QRD, XVM)
PLV = (PQQ, SGT)
FVG = (FXQ, MVL)
QXJ = (FMJ, KBH)
VQD = (HCS, KLJ)
PCC = (BGT, HFQ)
JTK = (KXS, DSS)
QHF = (BVX, XDB)
MRL = (SJG, JLM)
NMK = (PXS, QQF)
LMX = (HPV, TVR)
PTV = (CCT, SBB)
MHV = (TJP, GQV)
GTX = (GQV, TJP)
KCT = (SRH, GFS)
SNS = (FPF, SLF)
BCP = (RQH, PCB)
RRK = (TXR, LGB)
DQM = (SXH, GFC)
VLJ = (CMR, BDX)
QLT = (KVJ, SNS)
QTM = (RKK, QDQ)
QQG = (FMF, CDD)
DST = (BKF, FJD)
RGZ = (RFP, RVX)
SBB = (GMX, KCP)
DTT = (PTF, DFL)
FHP = (LNF, FSK)
FCH = (FQQ, LXM)
LMQ = (XTB, HGC)
HHF = (SDS, NPD)
HXX = (QGG, BBB)
PGM = (PGC, KTS)
FXJ = (JTK, QLJ)
RBQ = (LDJ, NKP)
XTQ = (SLN, LTR)
NGK = (KBJ, MSD)
RVR = (RTX, MRS)
JCT = (MDX, HFB)
LHB = (CTX, JBL)
RSQ = (CJF, TVJ)
BQF = (XKL, NKK)
HXM = (BQB, GLF)
KDJ = (DMD, GHC)
MQB = (FDF, VJN)
AAA = (KNJ, MTL)
XVC = (QQM, MVJ)
PMP = (SJX, GLV)
XPQ = (RLS, HJX)
LMF = (TCQ, FQT)
CNG = (GTX, MHV)
LDJ = (THB, RDL)
XVQ = (PFM, NHG)
DKQ = (VBQ, HFS)
SJV = (FHP, GVF)
HMX = (HVC, NBN)
SJX = (HMD, QTM)
QVG = (FHJ, LFX)
NVK = (QHT, PTS)
KPJ = (NXK, DMS)
RBX = (VJN, FDF)
MRT = (HGC, XTB)
FMF = (LSJ, LQF)
JRR = (CDG, QRT)
RTX = (NVG, CJB)
HST = (NVX, SBC)
TDQ = (SMT, FCK)
KTS = (CKV, MTP)
TMD = (KGV, QGB)
MDL = (XHT, RLT)
PTH = (MJD, DKQ)
RFB = (CJF, TVJ)
CDD = (LSJ, LQF)
PTS = (NHD, KBM)
NPX = (KCF, GQN)
KBH = (DST, HTK)
QPQ = (MHV, GTX)
NXK = (LMK, LSK)
THF = (MSD, KBJ)
KJN = (LLK, BQR)
LXC = (RFB, RSQ)
KGC = (RXC, PFX)
RLT = (FDC, LFB)
DPK = (SCC, XCG)
NST = (VHJ, XPQ)
FNG = (DDL, CPP)
XQK = (JCJ, BCV)
JCC = (DQR, GPL)
TJB = (SHF, KPB)
GMX = (MNP, JCM)
SXH = (VSN, KGL)
KFB = (MDD, XDH)
QVV = (XCG, SCC)
RXQ = (VNN, TMK)
NXN = (SJP, KFD)
DXV = (KCB, BPN)
KVC = (QQF, PXS)
TMN = (FKX, GLJ)
BQQ = (HHK, QBC)
RVX = (RNG, KXH)
NQT = (KFB, QBQ)
XGH = (KQJ, QHF)
VQZ = (RDR, VRQ)
LPN = (SPT, XKD)
JNQ = (NBN, HVC)
RRN = (KJL, TFJ)
HHG = (CMV, PHV)
VHJ = (RLS, HJX)
KPB = (NSL, KKZ)
KMK = (LCV, TPV)
TPX = (SQK, RFH)
KTH = (JKX, NKM)
VMX = (QRD, XVM)
RBL = (QGB, KGV)
NBN = (LJH, RDT)
RLJ = (SGG, RRN)
HMV = (DBJ, NPX)
FJM = (SGM, SQV)
XVK = (RQJ, QPF)
DDN = (DSB, KTM)
PFM = (VBD, BSG)
HFS = (XNS, HMV)
BVX = (VHN, XVQ)
HFB = (VFQ, HBS)
MTP = (GHX, MFF)
GLF = (SLD, NQF)
MSD = (MPK, DQM)
LLB = (GHC, DMD)
KFV = (JCT, VGN)
FJD = (SGP, KMG)
PGC = (CKV, MTP)
KCB = (THF, NGK)
GFC = (KGL, VSN)
SLN = (BHL, SPG)
LFT = (LLB, KDJ)
PFX = (DMH, NXJ)
GRL = (NVX, SBC)
XLQ = (FCJ, RFJ)
DKD = (FXQ, MVL)
SLF = (RSL, XLQ)
BXH = (GFK, QXX)
LLF = (JKD, LNN)
TSN = (TTM, JPM)
RFQ = (QHT, PTS)
KSK = (XFB, PSD)
TCQ = (MKB, MKB)
SLD = (DTT, TSV)
VRQ = (BPL, TSN)
GBB = (XBK, MXG)
THH = (XNH, PDM)
QCN = (QHK, JLS)
TQS = (MSG, GBB)
QNJ = (KBH, FMJ)
MCX = (CCT, SBB)
NKK = (LFP, QLC)
QKX = (KPV, MTN)
XSZ = (XVM, QRD)
TMK = (XTQ, VCR)
LDD = (DQR, GPL)
GHC = (GLP, MMP)
QXX = (KCM, QTS)
JLJ = (RQH, PCB)
LJH = (GFN, VLJ)
PKG = (PDT, HGT)
KGF = (XPQ, VHJ)
FBC = (NXM, SVC)
DDL = (VCX, VXC)
CMR = (XTS, KFV)
NGC = (FPR, FBC)
PCL = (RVX, RFP)
THB = (CNG, QPQ)
LMM = (KCH, VMH)
PXS = (SKG, RKL)
LXM = (VQD, KJX)
TXG = (QNJ, QXJ)
JLM = (RBQ, CLX)
PJX = (GXH, SVD)
DJG = (DCF, VXX)
CKV = (MFF, GHX)
CTX = (MQB, RBX)
SHF = (NSL, NSL)
GDB = (PDX, JPL)
QPT = (NJH, QFG)
GPC = (SJV, NXP)
XNH = (QXN, QXN)
JLC = (MCX, PTV)
NJH = (MKF, RHJ)
RQJ = (SFX, GTK)
SNM = (QKV, QQD)
LNN = (FVD, BXL)
MFS = (HLS, PKG)
PHV = (VPV, NNM)
XNS = (DBJ, NPX)
VCG = (VMS, QQG)
KJJ = (FLR, JQG)
LCB = (FKX, GLJ)
BTF = (CTX, JBL)
RKK = (DGL, PJM)
GFH = (PCL, RGZ)
VHH = (SXM, VCG)
RFP = (RNG, KXH)
BNM = (PVJ, LMF)
BPH = (MDL, SHK)
JFP = (TRB, KGQ)
NLR = (NNJ, NLC)
TRG = (QBC, HHK)
BMJ = (LMX, VSH)
HBB = (KTS, PGC)
KSN = (NXL, NXL)
FCK = (LQL, LKS)
LSS = (JJD, VRT)
TSV = (DFL, PTF)
RFN = (BDL, JBM)
XKD = (SFH, SVJ)
QBQ = (MDD, XDH)
SQV = (VBL, MTD)
MMF = (HHG, GLS)
FCJ = (SPL, MHD)
XQJ = (RGX, JGN)
BRB = (KJK, GQQ)
JGN = (RXQ, NGM)
SHQ = (FBN, XQL)
RQG = (LBQ, SXS)
PCB = (RPH, NGH)
KBJ = (DQM, MPK)
JPV = (BFS, CXX)
CRS = (QKM, JGD)
LNF = (SST, BPH)
JCM = (XVF, MPD)
KXN = (KJJ, HCQ)
RSC = (FPR, FBC)
KGQ = (DDD, KTH)
RDT = (GFN, VLJ)
RXL = (JVM, BRB)
PHM = (SMT, FCK)
QQM = (JTX, DLL)
CHK = (GQG, SNF)
GVF = (FSK, LNF)
PDM = (QXN, VQZ)
FVD = (KFR, KFR)
MTN = (RLJ, LVJ)
NFM = (RFH, SQK)
BXL = (KFR, TJB)
LGB = (PGF, XQK)
BHS = (SNS, KVJ)
SPN = (TMD, RBL)
XBX = (FVG, DKD)
KCV = (RXL, GHD)
HCB = (DGF, NLR)
HCS = (PMS, DXV)
PQL = (PLV, JHQ)
MCH = (SJV, NXP)
CHB = (RMP, BFJ)
LMK = (JMH, CHB)
XLP = (CXX, BFS)
TVR = (CTH, GFX)
BQB = (SLD, NQF)
DSB = (GPC, MCH)
BPL = (TTM, JPM)
DKC = (JJH, XVK)
TPV = (CHK, RRL)
TCD = (FQQ, LXM)
SCC = (XFM, CFK)
RNG = (VDQ, RFN)
GFX = (GHR, JRH)
HBS = (PTM, KGC)
HSM = (VMH, KCH)
KCH = (NMK, KVC)
MQR = (HHC, HHC)
JBM = (LXS, RVR)
TFJ = (GSH, HHF)
JKX = (MXJ, MMR)
NVX = (PHK, VPX)
MJR = (MSG, GBB)
XLG = (QBQ, KFB)
GFN = (CMR, BDX)
NRS = (PCL, PCL)
JFX = (PNB, HXX)
VNN = (XTQ, VCR)
PDT = (QDG, BTD)
BVK = (LCV, TPV)
VGN = (HFB, MDX)
PTM = (RXC, PFX)
RKL = (JLJ, BCP)
VLN = (DGF, NLR)
FKX = (TFV, VPR)
RHJ = (SHQ, VSG)
VXC = (HXH, LNB)
RPH = (TDQ, PHM)
GNC = (SJP, KFD)
PMS = (KCB, BPN)
BDL = (LXS, RVR)
XTB = (KXN, RCS)
BGT = (TGX, KSK)
GXH = (TTS, FTS)
NSL = (LRB, GDB)
MTD = (KCT, FXH)
SST = (SHK, MDL)
CCQ = (JVQ, LXC)
MVX = (SVD, GXH)
KCM = (FMP, QDD)
GFK = (QTS, KCM)
XBJ = (FXJ, VNK)
VCX = (HXH, LNB)
HGD = (VKG, TJF)
SPT = (SVJ, SFH)
CJF = (QFK, KCV)
RCS = (KJJ, HCQ)
FDC = (PQM, JMB)
BFS = (VRC, XBJ)
JJH = (QPF, RQJ)
DRM = (TMN, LCB)
QXN = (VRQ, RDR)
FMP = (VLN, HCB)
QLC = (QVN, CVF)
SQK = (PHN, JHJ)
BPN = (THF, NGK)
VCL = (QHK, JLS)
DTM = (SXK, DDN)
VPR = (JTQ, FGC)
NXJ = (NVK, RFQ)
XGQ = (XLG, NQT)
XDH = (XJV, RQG)
MDX = (HBS, VFQ)
QKV = (LCX, RND)
DMV = (SKV, JLC)
SBC = (VPX, PHK)
DQC = (VXX, DCF)
VSH = (HPV, TVR)
NKJ = (VCG, SXM)
QST = (PKG, HLS)
KXS = (HDH, FPP)
RMP = (BXH, TGL)
QDQ = (PJM, DGL)
PHK = (PCQ, PSB)
PCQ = (JNQ, HMX)
QBC = (RCC, HGD)
SPL = (DJD, XGH)
PQN = (JKD, LNN)
LXS = (RTX, MRS)
PGF = (BCV, JCJ)
LFB = (JMB, PQM)
FHH = (VMX, XSZ)
TTM = (SNM, DDX)
GNG = (SPP, JHH)
MCT = (FHJ, LFX)
JHH = (NQM, CPX)
SXN = (FVG, DKD)
XQF = (FCH, TCD)
BSG = (LDD, JCC)
MMP = (BQF, NKQ)
VHN = (NHG, PFM)
MDD = (RQG, XJV)
BDX = (KFV, XTS)
KJK = (LHB, BTF)
KNJ = (PJX, MVX)
PPL = (FNG, HXS)
JJD = (TDK, CCQ)
JHQ = (SGT, PQQ)
RHC = (DTM, TTT)
GLS = (PHV, CMV)
GLJ = (VPR, TFV)
VCR = (LTR, SLN)
CCR = (RPQ, RQK)
PVJ = (TCQ, FQT)
SGG = (KJL, TFJ)
CLX = (LDJ, NKP)
XCG = (XFM, CFK)
GHD = (BRB, JVM)
NKQ = (NKK, XKL)
TLK = (QKM, JGD)
CPP = (VCX, VXC)
TGX = (XFB, PSD)
LLJ = (FCD, FHH)
LQL = (XBX, SXN)
MDH = (BDH, QGD)
SJG = (CLX, RBQ)
NKP = (RDL, THB)
FDF = (RRK, LNC)
HFQ = (KSK, TGX)
FLR = (HPG, PQL)
PNR = (LLB, KDJ)
QPD = (DTV, JMJ)
NLC = (NKJ, VHH)
HXS = (CPP, DDL)
DMH = (NVK, RFQ)
NHQ = (SPN, HQJ)
LBQ = (PCC, RVJ)
BQR = (HRX, XXH)
LVJ = (RRN, SGG)
QGD = (BVK, KMK)
HGC = (RCS, KXN)
KNX = (SQV, SGM)
KXL = (RPQ, RQK)
FBN = (MDH, GHK)
LPS = (VRT, JJD)
XHV = (BQB, GLF)
SRH = (QCN, VCL)
GPL = (KNX, FJM)
HHC = (XVJ, LPN)
FGC = (HSM, LMM)
TTT = (DDN, SXK)
MMR = (FVB, HGX)
VRT = (TDK, CCQ)
BBB = (MQR, MFR)
VKA = (LRB, GDB)
GSH = (SDS, SDS)
MFF = (GHQ, QLD)
TDK = (JVQ, LXC)
KVJ = (FPF, SLF)
SGM = (MTD, VBL)
JHJ = (JSG, TDJ)
JQG = (PQL, HPG)
VPX = (PSB, PCQ)
SCF = (XHF, QPD)
FVC = (GLS, HHG)
VBL = (KCT, FXH)
JKF = (KGQ, TRB)
FXH = (GFS, SRH)
GHQ = (RDF, PTH)
SPG = (BNM, GNS)
JCJ = (DKC, DJX)
TNL = (NDV, BMJ)
SMT = (LQL, LKS)
NPT = (NXN, GNC)
MNP = (MPD, XVF)
SDS = (RCP, RCP)
LTR = (BHL, SPG)
RVJ = (HFQ, BGT)
SVJ = (MRD, TNL)
HTK = (FJD, BKF)
FHJ = (TMF, VTF)
LNB = (LLN, RPR)
TGL = (GFK, QXX)
XFB = (RRX, BCF)
XJV = (LBQ, SXS)
QPF = (SFX, GTK)
NNM = (TRG, BQQ)
JBL = (MQB, RBX)
MCC = (NXN, GNC)
RXC = (DMH, NXJ)
NVV = (QFG, NJH)
DLL = (MCC, NPT)
VSG = (FBN, XQL)
VLV = (TCD, FCH)
KGL = (RHC, CNH)
LRB = (PDX, JPL)
HGT = (QDG, BTD)
FMJ = (HTK, DST)
FSK = (BPH, SST)
RLS = (XQF, VLV)
FQT = (MKB, LLJ)
XVJ = (XKD, SPT)'''

paths_splitted = paths.splitlines()

path ={}
for dir in paths_splitted:
    path[dir.split("=")[0].strip()] = [s.strip() for s in dir.split("=")[1].strip('()').replace('(','').split(',')]
print(path)
print("pass")

found = False
count = 0


# part 1
# start = 'AAA'
# while found == False:
#     for dir in directions:
#         if dir =='L':
#             start = path[start][0]
#             count +=1
#         elif dir =='R':
#             count+=1
#             start = path[start][1]
#         if start == 'ZZZ':
#             found = True
#             break
#     if found == True:
#         break
# print(count)

# part 2
def key_present(character):
    keys = []
    for key in path.keys():
        if key.endswith(character):
            keys.append(key)
    return keys


def path_check(key, character):
    if key.endswith(character):
        return True

print(path_check('IGZ' ,'Z'))
count = 0
all_paths = key_present('A')

all_paths = ['KKZ']
while found == False:
    for dir in directions:
        print(all_paths)
        count +=1
        found_all = []
        for index, value in enumerate(all_paths):
            start = all_paths[index]
            if dir =='L':
                all_paths[index] = path[start][0]
            elif dir =='R':
                all_paths[index] = path[start][1]
            if path_check(all_paths[index], 'A'):
                found_all.append(True)
            else:
                found_all.append(False)
        print(found_all)
        print(count)
        if all(found_all):
            found = True
            break
    if found == True:
        break

print(count)
counts_all = [20093, 12169, 13301, 20659, 16697, 17263]
lcm_result = lcm(*counts_all)
print(lcm_result)


##['PBA', 'LSA', 'VSA', 'QVA', 'AAA', 'VKA']

#PBA 2093, 12169, 13301, 20659, 16697, 17263