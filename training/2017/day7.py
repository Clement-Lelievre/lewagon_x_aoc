"My implementation of Advent of Code, year 2017 day 7: recursive traversal algorithm"
from collections import defaultdict

INPUT = """suvtxzq (242) -> tdoxrnb, oanxgk
smjsfux (7)
oanxgk (68)
tvvfszm (66)
xprwsaf (266) -> uynuje, hhxlqcl
imkbcte (256) -> aeoojsr, muxff
uyxvzt (1046) -> uemmhd, ctdjc, gxqkboz, nvudb, dadueoc
ancik (61)
oysettw (152) -> fjojctd, eiiis, eilacwy
chfkzye (88)
maytl (149) -> uprsewo, obkvvy
qdyxf (95)
ssqhzgo (183) -> idwscr, jwmobb
hmtesft (62)
prayxh (377) -> bybrtqt, ftlxelc
rxlcg (16) -> soscup, gvqhsi
vhrxv (76)
bpmgs (81)
tngrxak (82)
odlmlp (19)
uocgh (78)
qdiuck (203) -> opxgy, evfob
hmpgq (86)
agrorp (98)
fnubw (7991) -> uyxvzt, xzzbz, zqbno, fxftvvi
pjdwe (71)
agmcum (9)
plxbhxv (91) -> pburz, crbuu, ancik, oglzi
tjvdz (68)
fwjrt (93)
smubum (79)
yojgof (34)
obkvvy (46)
lbhigx (32)
yixnd (10)
uysrm (255) -> vjzzaxi, mnegwoy
ggfpru (99)
pffjr (75)
bzoui (45) -> qzzuio, dzkcq
vrpls (22)
umrlyk (196) -> eygeo, xmhogfl
nkjocfh (81)
dzkcq (24)
ffpmvco (95)
fdlcwg (78)
gbvlb (214) -> sdjtpgj, ijhxyp
idhmz (17)
jouimd (55)
jnetreq (185)
xejdjnu (87)
gyeakaj (84)
gcdvju (22)
dadueoc (54) -> ywbagad, amkkd
ebpdat (63)
jcyop (522) -> qzegoz, rjbsi, fbbhkn, fafmv, pgiscip, fvzlw, etyllx
ozyiajn (137) -> iotjdfw, ulqoxr
pomtfpc (46)
baukd (52)
xgrkt (77)
mvbiu (37)
xhgxlcb (31)
xwmmdbs (48)
kxrwmdo (35)
kmmaqz (93)
vuoipf (1917) -> hgzal, evjtjkw, qstxfxv, yqzlm, agwseuk
zaoep (284) -> ffsrpnc, cvddep, mqlmpi
jnkjy (150) -> tdfetjs, gcpjvg, ztfmse
xjjge (142) -> yeavyk, cxfsjtx
xxcmska (51)
vjqrn (95) -> pnfmax, uhdvcqk, tetvxtx, ypjre
ffanqao (86)
evcrg (88)
htzab (142) -> douazak, wrqgf
xnvjeq (71)
oamdc (98)
goxkdq (343) -> vxbul, yfapady
evjtjkw (61) -> linzo, fzrps
ctmsdh (80)
apijq (57) -> ggbavjl, kvyvm, yfjodsp, dtiqmg, ehqjjsl, eggrxn, eaxgw
ctdjc (156)
jfagd (35)
ciwaqy (49)
fcydda (279)
nzkxl (10) -> wruuxfs, zviebo, fdxmq
kwlrqf (46) -> ngzhx, jnmwff, yacsqd, zbredd, gsabtz, gaodhdn, daziob
tgctm (2340) -> gtolwfw, zrjkvhs, jvrfyh
weasj (213) -> gzzmpmt, btmauhd, dvdfe, wqswycq
nbpifq (19) -> iujht, evacloi, geevgr
sjjfw (250) -> jpbod, xxcmska, hqkqg
mcltn (23)
tjqces (74)
epxsima (142) -> rpcpu, uyqja
uprsewo (46)
ikufikz (18)
oxtcw (60)
ftjsi (52)
cksrupl (216) -> bcqrh, bqcpk, smjsfux
iwrxh (793) -> wkrunp, ciwaqy
jgemyt (395) -> spzcts, zxdwxi
sdjtpgj (27)
tkbvq (229) -> vtvrufl, vmask, qzdgae, ltxdrag
fmxgjyi (67)
doioysi (37)
kvyvm (231) -> cfofvmk, mrfxp, aiifb
ahxab (11)
csjgde (313) -> ixqosm, ziclyc
trkehb (234) -> qhivkhk, odnxu
gaepxdo (10) -> dssmkge, dcfod, mnzrs
xneou (37) -> qdmwhp, ykuovbf, nnrup, kmmaqz
wcsvv (125) -> xlcwwh, wkpcmj
ynabij (365) -> guenoww, hyupti
vyksxor (74)
jajnukt (141) -> jzsuszj, kypvxgj, prpur, bbvcyqt
qvvfdz (235) -> mzxzvj, ayhtq
qwuwet (44)
wsnnpt (93)
kchxaz (50)
excue (94) -> vbklmbl, cvebrdn, tsejpo, auvkftn, odgaq, mikabr, plafq
inpzr (283) -> bttuf, mtpjiqv
ceahs (149) -> iywmq, ednoc, opoav
oxokip (59)
bjhbaeq (15) -> jbeccla, yghmpm
fafmv (164) -> pmcxf, sgcszn
kfdlwmd (76)
wezrbzw (90)
mjfmma (80)
unwxho (93) -> ycbensb, dqqvw, xggqps, wopctnz
xddneql (98)
ugaao (293) -> igxnbx, iuwfcfn
idwscr (27)
hkifor (56)
wvamomg (66)
fzrps (64)
oqatq (34)
cjlll (25)
fusrhst (85)
lglzu (65) -> tgoxupv, aqcvcmu
jicds (19)
dlorovb (88)
tjpyzok (48)
ewetx (18) -> aivthrm, dehctx, xejdjnu
ohjpwlf (89)
ayrmt (6)
drfiyc (208) -> ajvtod, mbsom, svgsp
llbrfnj (35)
ojvela (47) -> pfdhuej, eftexh, dlorovb, ihxxanb
mzdorez (75)
feecvjl (68)
bhjgta (936) -> jtemqlc, ztqfg, zaoep, knfjqwi
wrqgf (50)
cchsvcu (2393) -> vbahlkz, nsaunto, iidrfg
ehqjjsl (225) -> iiihrc, cmlrqjx
uwqgz (59) -> juadxcz, doulax
hlbyzqi (98)
dqwfuzn (785) -> utecy, smpbfj
sabrmjw (539) -> ynabij, yorve, tdfla, xneou, urxki, caaul
szvvmv (59)
nwvfcq (8)
olnfb (95)
gcgai (217) -> hmgnq, doioysi
rzyceeb (75) -> cpvmv, vyqeu
eaxgw (359) -> sumkuu, qyxyyfe
xezfgjm (386) -> lfmshq, btunou, fnkvv, jcetf
xgwbi (34)
hhxlqcl (69)
jjutz (85) -> ppmtmra, lrhov, gahmpi
aeede (82)
vhpqug (48)
gwcznw (78)
iiihrc (84)
ponhl (56)
xkljy (165) -> qeaafc, luobrd
sgdqadb (365) -> gzbpbzh, semuybr
vlstbi (265)
doulax (35)
awgit (71)
ukgraro (27)
itqxypr (40)
tqjnarz (86) -> ulgusti, tngrxak, jpchi
cjcnjv (22)
upalmon (65)
mybgqcz (34)
ensbsjj (10194) -> zjdlixd, enpvalm, bhjgta
jbexqrg (43)
odvadyf (28)
yhkvwfh (14) -> efnhbg, lfgtisg
aeuhflj (20)
lxugv (93)
qxubf (223) -> woauuj, etlyn
woauuj (72)
lhldwh (35)
ehxoyp (6)
svhudk (55)
jtlqjwb (90)
bhgjfjp (43)
wojfh (76)
cxhplek (28)
eiiis (60)
lfmshq (86) -> jgjis, tezrxeh, kfdlwmd
qhoznbt (52)
ifcvuo (305) -> dyimr, zjybiy
zelat (1852) -> dtovks, jkjkxjo, etihx, xwukld
ptkhfgv (76)
yfwlsm (40) -> diodh, wqwuh, xddneql, oamdc
udnuwf (44)
topay (77)
rpqtlka (10)
uclzd (258)
uqcsmi (138) -> orfvwfh, mvvdw, wxqcjau
jkjkxjo (97)
sjizhzd (385)
awhtxfi (67)
mfkyyn (22)
khxovd (70) -> pnednw, oxtcw, zculjs
btuuf (36)
tbmtw (7374) -> jcyop, gnpvu, qokpqcj, dpulvm
dyimr (47)
ktiqs (60)
uqrmg (38) -> xgwbi, mybgqcz, yojgof, qssip
kypvxgj (37)
ymmmd (119) -> posqxf, xnvjeq, rmuwew
mazuw (20)
ahxil (180) -> ayrmt, ehxoyp
ytjvi (30)
gfrjfp (10456) -> vglmk, ncewylf, ofqyppk, lrrznr, krvxpc
sumkuu (17)
sogmnn (1837) -> hmpgq, ffanqao
ulqoxr (77)
dnzvald (12)
fhsmv (87)
cgoclfi (44)
qeaafc (36)
ovsdyv (241)
hrykmkz (59)
dpqsx (224) -> topay, ioinp
ihrnca (85)
bpndvbp (22)
fbtzaic (11651) -> nzkxl, mdbtyw, dqwfuzn
smpbfj (64)
krnlmf (22)
mqlmpi (12)
cmlrqjx (84)
yorve (285) -> yhwiyr, hmtesft
katupgz (23)
prpur (37)
iidrfg (133)
iofnddc (65)
houiwqu (64)
exzvkxu (26)
topcav (93) -> zmuxeo, glmtq
uoowx (48)
xkvgp (17)
paplmio (91)
igxnbx (46)
ftbzlvu (93)
bucdl (107)
bydph (90) -> bhyawz, etgphv
fqoary (30) -> ldcqple, gfrjfp, uvfrdrm, flnwg, dzihru, kyjva, ncuauw
soiwb (22)
iqgctux (839) -> vjqrn, hfbyx, kfibzch, fctrumt, oraqucr, ewetx, fpmlwfh
zxdwxi (39)
gzzmpmt (43)
pujxta (22)
cvebrdn (192) -> hyblgwq, dafsjnc
tpdpnu (63)
glmtq (74)
fdxmq (28) -> lisgic, mpsbosw, hykydhr
kloyc (30)
tfrrlt (27)
lwbtd (39)
xykzz (93)
ppoiun (196) -> glton, rscybf
gimfzpl (98)
adjeeo (66) -> svlzb, grluwcw, bqytirn, lzovhs
mbsom (14)
dvcdvss (76)
ypjre (46)
micrqvl (15)
ezzme (89)
dnkuuf (237) -> fitxh, iofnddc
rjbsi (176)
qdhlpqn (54) -> jrnzibg, urdzsm, pxzxws, eounhdc, goxkdq
zatst (36) -> udjinl, hwssapq
ismlzl (8)
uyqja (34)
zxuzl (808) -> lvheqh, syjwi, usqget, gowyxis
pbwqe (166) -> dbwnqzs, swzwgb, eeufykm
bzpuxrk (52)
qzzuio (24)
dtpnpq (104) -> lowahta, obidwky
lhumvsh (23)
ntintc (19)
bvytf (157) -> unjnjhh, xuhgu, aeede
gitpug (56)
vtvrufl (9)
duwrtfc (16)
uahwv (40)
fjojctd (60)
pburz (61)
btunou (210) -> qhoznbt, ftjsi
ieacu (179) -> fetmzid, cnzqk
gwzoe (72)
eplazoz (77)
uxppyj (83)
dvdfe (43)
dkorpg (39)
ipgte (85)
spzcts (39)
lwxoin (169) -> yvbxww, fmgdkun
iatnsa (34)
daziob (265) -> pikkduj, qjxczyx
knvtk (26)
qjxczyx (78)
gtolwfw (96) -> mbfhki, uftzqia
ussukc (8)
fsaitmn (425) -> ckeqik, lmqhg, zfkliql, ahhtyrn
dczlybu (17)
fcqyuld (69)
ibrkwsx (81)
mroyq (17)
bboim (1467) -> bydph, ppzdpud, lfmuqxa
dochk (175) -> ichsx, xyorm, oxhcne
grluwcw (78)
vkzmdxf (23) -> lwxoin, qdiuck, qjqmpw, kfjckfy
gmcrj (69) -> polkn, gejdtfw, cfuudsk, fqoary
lisgic (91)
nhkfwk (48)
eeufykm (25)
ytvur (98)
pikkduj (78)
hkstlva (19) -> stzau, zpaybpo, ibrkwsx
xmhogfl (31)
wqimeek (93)
eycqvhz (95)
xzufzqj (35)
iohhnkq (78)
ftlxelc (13)
jfknc (97) -> sjizhzd, efhdsgs, weasj, hrxzek, ugaao, sgdqadb, xxljznv
fmgdkun (24)
vwjspf (7)
vvyffam (13) -> nwecq, buodib, ypujb, ndjueqb
dqjepow (1158) -> waikg, ljyobyk, xbnecm, pssff, cqoxq, uokpbvj
piyyydu (250) -> lodjokj, oakblco, rlgru, aawuak
uxfcrt (240) -> ahxab, pbsabz
lmteo (50) -> coleqoq, ohseo
jprrnd (76)
juadxcz (35)
bubuic (62)
cqzhj (23)
nvudb (62) -> uebysc, cjxuwe
rantzzr (7)
tyddsz (261)
ixqosm (75)
dtrdb (264) -> bhgjfjp, jbexqrg
aqljjk (60)
gcpjvg (35)
xdrpbh (75)
yfapady (24)
gwlskzx (445) -> tqcdt, agmcum
xxljznv (29) -> ezzme, xvxezl, zjzldd, rfigs
ztqfg (71) -> xdfwfmo, lugxki, uxppyj
fnkvv (152) -> dfdawtk, mxpnyo
aeoojsr (15)
uymdisn (31)
jnkqo (49) -> tvcul, stfsit
otsbf (98)
lwgppcz (67)
ecuhckx (806) -> ddnfy, tzseb, mbxffzk
hqkqg (51)
nsaunto (13) -> uahwv, fveuo, bihjuos
mdbtyw (396) -> zqcrxm, lfbocy, uqrmg
bnlxpgs (41)
dafsjnc (53)
ofeqif (87)
plafq (112) -> wqimeek, fgeakc
oazne (238) -> pddmke, cugsuk, vyvwpp
unjnjhh (82)
hlxglt (97)
oglzi (61)
rmzdg (90) -> gfxra, oqxprqa, jfknc, mwmyxd, iqgctux, cchsvcu
aszlk (6)
xkzympi (80)
fcajmx (79)
iygrvcq (84)
xvxezl (89)
wqswycq (43)
wkpcmj (30)
gydhlh (67) -> igeuou, ggfpru
yhjbr (15)
blmrnzv (75)
guenoww (22)
ibygguq (75)
uaouhj (50)
kmvtp (80) -> ztcoo, evcrg, seqpyc, awkci
pnptpzb (18) -> qvvfdz, fgbkh, jnkjy, uprknk, uqcsmi, mwixu
rxeesk (97)
puiuyvv (64) -> hydsxwk, tjqces, sfkznca
oxtuf (84)
rhomwvz (72)
zoeyj (230) -> rznjgnj, ztocqs, itqxypr
xdfwfmo (83)
mzxzvj (10)
uyauqa (476) -> gbvlb, inbnp, nbpifq, kxbgcn
eggrxn (13) -> bfuell, oqkcc, qpshatb, ffpmvco
bcqrh (7)
bulumce (106) -> xeeor, lqyjcz, lsnyoe
dvqaks (35) -> mkzpyhk, excue, zxuzl, ukdun, xoxpsax, opyyn, unvguy
zbredd (391) -> micrqvl, yhjbr
rwulpg (106) -> uymdisn, xhgxlcb
rfigs (89)
xoxpsax (970) -> lmteo, htzab, vllceh, zotuf, xjjge
ygfdkew (34)
ahhtyrn (12)
ckeqik (12)
lqyjcz (87)
gaodhdn (421)
moqjbf (23)
wcjly (254) -> kunjdjs, bubuic
urdzsm (347) -> mfkyyn, pujxta
ipbtx (94)
ichsx (38)
cfofvmk (54)
slavm (402)
oakblco (32)
pbsabz (11)
ffsrpnc (12)
kfabmu (85)
gsabtz (357) -> lbhigx, jklgnxw
tfjnjpk (63) -> jgcpvo, qppcrmh, gwzoe
nmzgz (91)
uante (22)
ruann (26)
tezrxeh (76)
usqget (73) -> jtlqjwb, uzqerzq, fadrtgp
rpwxt (50)
evacloi (83)
cqoxq (275)
pnfmax (46)
pdqytmz (99)
hidxzy (50)
zrjkvhs (70) -> yxqgha, tlghvt
kaahj (67)
qkoobj (784) -> puiuyvv, imkbcte, zroqzf
uynuje (69)
wgrjyq (285) -> iwajq, adqhyes
etgphv (31)
tdfla (393) -> ussukc, ismlzl
qzdgae (9)
aivthrm (87)
kfjckfy (217)
nxydw (159) -> hrykmkz, mkidiho
bkxeyq (72)
inbnp (180) -> ueadckf, udnuwf
bdvlgx (543) -> psrozz, efjmuv, plxbhxv
pfdhuej (88)
ekojj (148) -> oeuror, ajhda
srvqwf (112) -> rbjjv, duhoci
hvyklmf (9)
bvpxgrf (80) -> mnryxre, orjnwip, qaznr
reyxj (84)
yqzlm (37) -> ptkhfgv, ikmdjtw
yhwiyr (62)
ygdeams (32) -> rhomwvz, gwnlt
jvrfyh (100) -> mvbiu, druuhf
zlwjs (81)
oogzvyg (23)
rkauf (32)
hfbyx (247) -> wldfv, xmufd
jtokzu (35)
hyeteeg (367) -> xwmmdbs, vhpqug
gowyxis (313) -> vtazp, opdzu
riszb (81)
hgzal (59) -> imslgj, bktvx
lvxmqy (90) -> lyyqnt, gwcznw, fdlcwg, nifsnge
bihjuos (40)
mnryxre (36)
nkaejjm (32)
wxgwp (88) -> ofeqif, dxdioa
oqxprqa (1180) -> ntigfy, mnfrudu, uknimmc, qnljlu
jbeccla (46)
tlikogo (25) -> lldzrv, qkcqxgk, wpypfwm, hbwuw
easqs (41)
jtemqlc (320)
wldfv (16)
gcepcso (498) -> ekojj, owexd, fypjed, epxsima, ppoiun
vtbkd (123)
cfwrezj (254) -> tjpyzok, uoowx
bqcpk (7)
wkrunp (49)
lsnyoe (87)
diodh (98)
etidy (167) -> hqpzd, ponhl
qucjvpl (6)
xzzbz (629) -> ifcvuo, ojvela, vdmezfc
lfbocy (174)
mgqrq (95)
hykydhr (91)
ohseo (96)
udjinl (78)
yeoia (5411) -> kwlrqf, sabrmjw, whvre
tvcul (96)
hqept (94)
ljyobyk (77) -> zvmbtmg, pdqytmz
mwixu (117) -> fcqyuld, cssuc
qssip (34)
zmuxeo (74)
uvfrdrm (12966) -> kvqdnuq, zelat, bheam
duhoci (69)
ccvnkwy (92) -> dpbwe, zsflxau
lfgtisg (39)
exgjf (50)
uivov (22)
cvvewfi (13)
mkzpyhk (1136) -> podrlpj, tyddsz, tkxpetn, pnmuf
sxeywx (84)
cbezt (388) -> cjcnjv, gcdvju
dvpfc (28)
eounhdc (97) -> otsbf, ytvur, lilwts
gxflenw (73)
ncewylf (1774) -> btuuf, omzdv
uftzqia (39)
ulxsfq (340) -> hmphp, ivrypwl, duwrtfc, vpcawb
uebysc (47)
tkxpetn (93) -> oxtuf, ytrmqx
qgjpqt (48)
dmrvdna (27)
qrfqnq (81)
ykuovbf (93)
hdiot (14)
oraqucr (279)
wruuxfs (58) -> zlwjs, pfahvas, mtrumh
odnxu (12)
bttuf (42)
cpvmv (83)
huxkort (327) -> dczlybu, cdeyujt, idhmz
prtbd (38) -> ipgte, tkjlunx, fusrhst, btnvmr
krvxpc (424) -> ssqhzgo, xkljy, pjflk, lfkqyf, cksrupl, qivrvv
pcjppf (203) -> hcyhv, cedao
vdmezfc (399)
gvqhsi (88)
sjrlj (66)
lotiapl (90)
xtprb (52)
ofqyppk (186) -> ymmmd, oysettw, ceahs, tqjnarz, vyoxvhv
umwyc (78)
etyllx (53) -> rclzxhh, qoybzxh, easqs
yeogm (76)
iujht (83)
bfvriie (48)
cfqpega (94)
mikabr (170) -> zmksfeg, houiwqu
aawuak (32)
zbizc (99) -> ygivo, fmxgjyi, lwgppcz, kaahj
nwyys (50)
ztcoo (88)
linzo (64)
gfdnli (84)
gahmpi (52)
waikg (275)
ednoc (61)
namjj (29) -> umwyc, uocgh
mbfhki (39)
gnbmemw (123)
wamfc (48)
geevgr (83)
gnpvu (20) -> mmvft, pcjppf, jajnukt, dochk, hngooro, gaepxdo
ffmjzxx (28)
aiifb (54)
hcyhv (43)
zmksfeg (64)
eilacwy (60)
yxqgha (52)
posqxf (71)
rujthq (92)
fppes (65)
fmtsssj (75)
nnrup (93)
agwseuk (132) -> jicds, ntintc, odlmlp
vxbul (24)
wqwuh (98)
vgfqulp (199) -> mzdorez, ibygguq
idbcgs (175) -> xkvgp, buzeugv
hrxzek (184) -> skdiibp, lgjtrj, awhtxfi
tzseb (23) -> legxh, kfabmu, ihrnca
mnzrs (93)
hqvgt (129)
stfsit (96)
fetmzid (15)
hydsxwk (74)
orysz (40) -> xjkgmv, knvtk
snblhv (99)
ivrypwl (16)
vyvwpp (13)
opxgy (7)
xeeor (87)
zsflxau (50)
bheam (2222) -> iitdq, aszlk, qucjvpl
wygvotv (16)
ixukvkp (92) -> uaouhj, yotjazk
ltxdrag (9)
pfvxd (89)
dpulvm (1175) -> xuuft, xwblt, invrcvf
oyatv (57)
atwpqc (35)
brbzgkm (16)
ijvmnd (12)
wqqqxn (18) -> aqivm, ozyiajn, gcgai
fbbhkn (84) -> pomtfpc, rjqihtl
xuuft (41) -> kjxwxam, dvcdvss
zohacp (1362) -> ovsdyv, yuwdebl, jnkqo, topcav, jsbcdkn, azgii
tsejpo (90) -> bzpuxrk, goyce, rwbqd, mfrcmg
ioinp (77)
zjdlixd (831) -> mpfrdzc, oazne, zwyrvyj, vebkntv, nxydw
sfkznca (74)
cvddep (12)
mnegwoy (47)
mkidiho (59)
xyorm (38)
rpcpu (34)
akqzb (79)
rmuwew (71)
glton (7)
hpvsz (57)
oauxbtz (23)
gvibwl (52)
hwssapq (78)
ecyyqsp (80) -> qwuwet, cgoclfi
pzxhj (145) -> qhwwv, ktiqs
rbjjv (69)
twsfo (151) -> namjj, jnetreq, wcsvv, lglzu
dzihru (11994) -> bwvmae, kpfjraq, ztxlw, bboim
rybeva (11)
imslgj (65)
odgaq (172) -> tpdpnu, ebpdat
rutvyr (9470) -> ecuhckx, morwid, daziqx
yacsqd (33) -> hlxglt, cbxczib, rxeesk, kgepl
adqhyes (89)
uprknk (65) -> ccezie, eycqvhz
wpypfwm (81)
oxhcne (38)
xggqps (95)
lojhip (66)
qivrvv (61) -> gqwepeb, chfkzye
rlgru (32)
cqiexk (154) -> pjdwe, awgit, kqxvtvy
fctrumt (259) -> yixnd, rpqtlka
vwfoi (34)
xxrxf (84)
ayhtq (10)
whvre (2803) -> olnfb, mgqrq
cbxczib (97)
zusipm (188)
kdsrjc (142) -> ytjvi, kloyc, oghvi, hbdmcdc
cxfsjtx (50)
unvguy (761) -> unwxho, jgemyt, fsaitmn
qtwwe (14)
zjybiy (47)
nygkk (857) -> zatst, ixukvkp, rxlcg, wqcsaan, ccvnkwy, ahxil
lowahta (36)
rscybf (7)
ytrmqx (84)
odkjk (108) -> nwvfh, xquwlv, hghuq, dsozgr
cedao (43)
ehfoqf (66)
knfjqwi (280) -> mazuw, mtjcvaf
obidwky (36)
pclycj (13)
vhlpr (17)
vjzzaxi (47)
coleqoq (96)
yeavyk (50)
idvkl (29)
rwbqd (52)
sppbe (23)
rjqihtl (46)
wqcsaan (114) -> dkorpg, lwbtd
lugxki (83)
gnmkuj (75)
tyfoz (94)
ubhvop (89)
fpmomi (94)
nzdilp (99)
uoybmh (349)
tdfetjs (35)
ziclyc (75)
zpaybpo (81)
mbqewjq (250)
jrnzibg (370) -> rantzzr, vwjspf, iguatq
bjllzfr (10)
pbvmk (125) -> xzufzqj, jtokzu, jfagd, atwpqc
cnzqk (15)
btnvmr (85)
xlhbak (14779) -> hqvgt, zhxqgb, vvyffam, uwqgz
qpshatb (95)
otzkp (92)
stzau (81)
pxheyj (16)
zakeqj (7554) -> ltmvmwe, pnptpzb, gcepcso, bdvlgx, yhwegl, uyauqa
jkeqz (34)
ckkcgp (180) -> nzdilp, snblhv
vyeryld (9)
wxqcjau (39)
cssuc (69)
gicuckw (80)
fxftvvi (989) -> fcydda, tfjnjpk, etidy
ltmvmwe (756) -> qavfiun, yqcaue, ybppeq
kyjva (16122) -> wqqqxn, vkzmdxf, twsfo, iwrxh
jflahw (84) -> tjiqr, csjgde, wgrjyq, hyeteeg, gwlskzx, fuohb
cbxgol (42)
xwblt (193)
podrlpj (261)
kfibzch (54) -> dpnlf, mcjbnfk, blmrnzv
bdvlhq (21) -> akqzb, fcajmx, smubum
qhwwv (60)
ubsmxso (78)
mtpjiqv (42)
ccezie (95)
fgeakc (93)
jyppp (57)
sqvfg (56)
ycbensb (95)
rznjgnj (40)
luobrd (36)
uknimmc (235) -> gyeakaj, sxeywx
zzsqh (78)
lvheqh (261) -> jtviekh, kyeul
koeufzg (84)
ggbavjl (21) -> iojwg, xykzz, pjvsofk, lxugv
crbuu (61)
ubpoy (68)
opdzu (15)
dfdawtk (81)
edafmn (27)
rndpfmx (300) -> pgxiavo, cjlll
iuzmx (16)
dsozgr (81)
ygivo (67)
tqytfku (79) -> krnlmf, dxyhphf
pmiwkyg (41)
bwvmae (33) -> piyyydu, ckkcgp, mqzkogj, adjeeo, uztqohr
xlcwwh (30)
auvkftn (282) -> nwvfcq, ophcgq
qdmwhp (93)
ztfmse (35)
ppzdpud (68) -> cbxgol, goohdry
ibnunt (56)
qdwhkl (72)
bktvx (65)
eftexh (88)
jwmobb (27)
dgjtv (29)
cjxuwe (47)
mbxffzk (210) -> vwfoi, oqatq
omzdv (36)
jsbcdkn (61) -> eumtjne, venip, aqljjk
qnljlu (83) -> ctmsdh, arxafnu, ximwl, xkzympi
uhdvcqk (46)
ncuauw (14760) -> xezfgjm, tjtrq, qkoobj
morwid (92) -> trkehb, uclzd, umrlyk, axrrydf, tjqdup, bdvlhq
intews (29)
lterpwd (34) -> bwmlg, intews
kunjdjs (62)
jlxwojc (7)
buodib (29)
qzegoz (28) -> wiprvsa, vyksxor
bwjrqs (56) -> wvamomg, sjrlj
opoav (61)
dpbwe (50)
dssmkge (93)
ajhda (31)
qjnow (217) -> rpwxt, exgjf, nwyys
efjmuv (195) -> lhldwh, bcyndtf, llbrfnj, kxrwmdo
eeozf (11)
vpcawb (16)
jpbod (51)
qavfiun (114) -> fmtsssj, pffjr
ywbagad (51)
tetvxtx (46)
ukdun (568) -> bvytf, prayxh, sjjfw, lxwaq
qhivkhk (12)
ndjueqb (29)
swzwgb (25)
mrfxp (54)
qkcqxgk (81)
lfmuqxa (98) -> dmrvdna, tfrrlt
tkjlunx (85)
avcwghu (94)
jgcpvo (72)
uzqerzq (90)
qoybzxh (41)
ldghw (48)
lrjdbp (23)
hfejf (13)
invrcvf (49) -> bkxeyq, qdwhkl
opyyn (1428) -> zusipm, bvpxgrf, wdvmvhe, bwjrqs
amkkd (51)
vnxmgtu (91)
pnednw (60)
eumtjne (60)
siknup (52)
xwukld (97)
mxpnyo (81)
iojwg (93)
daziqx (1364) -> orysz, lterpwd, yhkvwfh
nlusd (23)
zviebo (213) -> bpndvbp, vrpls, zeauw, uante
ntigfy (376) -> vyeryld, jgzpdx, hvyklmf
atzunin (78)
bcyndtf (35)
iitdq (6)
azgii (241)
qmkyl (12)
dlzrs (18)
zqcrxm (135) -> pclycj, hfejf, hpcvu
vbklmbl (298)
jlmbjs (52)
yrbypdv (89)
vyoxvhv (24) -> eplazoz, ftkqwci, xgrkt, nedbp
eadmwtp (22)
kqxvtvy (71)
hpcvu (13)
yuwdebl (67) -> fhsmv, eifgc
tucqq (80) -> vpywo, vuoipf, jflahw, fgpgrxr, tgctm
yfjodsp (373) -> bjllzfr, ldjeual
ulgusti (82)
yvbxww (24)
ihbybvd (84) -> eptpjci, gicuckw, mjfmma, ayismka
ciygx (23)
iwajq (89)
bncdukb (79) -> fwjrt, ftbzlvu
zhxqgb (115) -> tdvopw, jlxwojc
efnhbg (39)
pgiscip (30) -> gxflenw, bpaelk
jnmwff (233) -> tyfoz, hqept
gwnlt (72)
bybrtqt (13)
buzeugv (17)
jzsuszj (37)
dbwnqzs (25)
illkoi (56)
tlghvt (52)
vglmk (96) -> iygpmov, dtrdb, rndpfmx, cfwrezj, zoeyj
xquwlv (81)
lilwts (98)
aqivm (67) -> illkoi, gitpug, ibnunt, sqvfg
vsprxrs (175) -> fpxda, dyyccwq
ihxxanb (88)
semuybr (10)
cdeyujt (17)
xufnd (90)
etihx (97)
mnfrudu (207) -> agrorp, hlbyzqi
bfwgsag (27)
xjkgmv (26)
pnmuf (173) -> soiwb, htinuz, eadmwtp, uivov
rfxyb (48)
igeuou (99)
aqcvcmu (60)
ewomrs (84)
cugsuk (13)
weeom (20)
mpsbosw (91)
mmvft (275) -> zyxbmy, gdftnih
nifsnge (78)
lrhov (52)
psrozz (223) -> adccmtd, hkifor
enpvalm (14) -> dnkuuf, qjzipyw, znoap, bulumce, qxubf, nnktssm
jpxtrww (23)
zroqzf (264) -> rybeva, eeozf
nfcrpf (22)
jgjis (76)
zqbno (81) -> tlikogo, uoybmh, vgfqulp, mstjkgi, uysrm
fvzlw (76) -> kchxaz, hidxzy
legxh (85)
iomsug (78)
skdiibp (67)
dyyccwq (96)
kjxwxam (76)
oeuror (31)
lodjokj (32)
mvvdw (39)
exadxz (41) -> xxrxf, koeufzg
pmcxf (6)
oqkcc (95)
mbfvaw (22)
xbnecm (227) -> brbzgkm, iuzmx, wygvotv
kpfjraq (923) -> srvqwf, drfiyc, khxovd, mbqewjq
pfahvas (81)
dehctx (87)
bpaelk (73)
jndcfc (90)
axrrydf (190) -> tsqfitq, ffqzxf, dviucr, mroyq
ukcqez (129) -> paplmio, nmzgz, vnxmgtu
jklgnxw (32)
fypjed (98) -> cxhplek, ffmjzxx, dvpfc, odvadyf
uwxvsjd (313) -> edafmn, bfwgsag
iguatq (7)
flnwg (30) -> ghdzwq, kziosg, apijq, zohacp, dkspw, zmzmna, dqjepow
soscup (88)
lrrznr (536) -> ymmun, uxfcrt, wxgwp, kdsrjc, hkstlva
dkspw (918) -> prtbd, huxkort, suvtxzq, dpqsx, wcjly
goyce (52)
ueadckf (44)
zikbees (13)
uwfkgbm (98)
gdftnih (7)
zvmbtmg (99)
pfjaob (78)
gzbpbzh (10)
znoap (205) -> bpmgs, riszb
btmauhd (43)
eptpjci (80)
gejdtfw (65882) -> yeoia, fbtzaic, tbmtw, rutvyr, tucqq
ypujb (29)
hqpzd (56)
dtiqmg (301) -> katupgz, lrjdbp, oauxbtz, sppbe
yqcaue (60) -> ubpoy, feecvjl, tjvdz
goohdry (42)
glcfzs (27)
vllceh (173) -> cqzhj, jpxtrww, lhumvsh
utecy (64)
kzmsh (38) -> upalmon, fppes
iotjdfw (77)
vyqeu (83)
vmask (9)
ftkqwci (77)
tjiqr (87) -> avcwghu, cfqpega, ipbtx, fpmomi
polkn (91947) -> dvqaks, fnubw, xlhbak
xmufd (16)
mtrumh (81)
vebkntv (87) -> qdyxf, xqkov
ffqzxf (17)
mstjkgi (178) -> jyppp, oyatv, hpvsz
awkci (88)
kziosg (2380) -> pbscvh, bjhbaeq, hhvng, bucdl
fpuaei (23)
ngzhx (334) -> idvkl, dgjtv, uptfdfp
zfkliql (12)
pssff (95) -> lotiapl, jndcfc
bqytirn (78)
caaul (211) -> ehfoqf, tvvfszm, lojhip
wiprvsa (74)
lmqhg (12)
hhvng (73) -> vhlpr, nxalp
arxafnu (80)
svlzb (78)
lldzrv (81)
bfuell (95)
yhwegl (584) -> jjutz, maytl, pbwqe, rzyceeb
xqkov (95)
orfvwfh (39)
tqcdt (9)
oghvi (30)
qjqmpw (37) -> wezrbzw, xufnd
ikmdjtw (76)
gxqkboz (88) -> ygfdkew, etvxdqn
ajvtod (14)
efhdsgs (385)
iuwfcfn (46)
orjnwip (36)
kyeul (41)
qppcrmh (72)
hbdmcdc (30)
jcetf (126) -> lvrzba, xxieckm
xxieckm (94)
uokpbvj (223) -> exzvkxu, ruann
evfob (7)
rclzxhh (41)
rjkehq (163) -> fpuaei, oogzvyg
ximwl (80)
zeauw (22)
ophcgq (8)
jtviekh (41)
druuhf (37)
nedbp (77)
vbahlkz (133)
ymmun (198) -> rkauf, nkaejjm
mcjbnfk (75)
mpfrdzc (251) -> cvvewfi, zikbees
uemmhd (124) -> pxheyj, cwxvww
qyxyyfe (17)
qjzipyw (11) -> yrbypdv, ubhvop, ohjpwlf, pfvxd
fgpgrxr (2583) -> wsnnpt, vlcrv, bzoui
etvxdqn (34)
tdoxrnb (68)
bwmlg (29)
nwvfh (81)
dqqvw (95)
venip (60)
dxdioa (87)
ybppeq (224) -> weeom, aeuhflj
fpmlwfh (231) -> qmkyl, pfvnpy, ijvmnd, dnzvald
pfvnpy (12)
owexd (48) -> nkjocfh, qrfqnq
douazak (50)
mwmyxd (2288) -> ecyyqsp, kzmsh, rwulpg
fgbkh (163) -> moqjbf, mcltn, nlusd, ciygx
qokpqcj (542) -> ulxsfq, xprwsaf, ihbybvd
pgxiavo (25)
adccmtd (56)
zwyrvyj (173) -> xtprb, gvibwl
yghmpm (46)
dtovks (97)
ayismka (80)
wehkpx (90) -> zzsqh, iohhnkq, iomsug, atzunin
ldcqple (13659) -> qdhlpqn, nygkk, sogmnn
kgepl (97)
cnstz (176)
vlcrv (27) -> rtdffxh, mbfvaw, nfcrpf
tjqdup (258)
syjwi (289) -> ukgraro, glcfzs
fveuo (40)
vtazp (15)
fpxda (96)
dviucr (17)
fitxh (65)
ztocqs (40)
fuohb (367) -> nhkfwk, rfxyb
nwecq (29)
fadrtgp (90)
rtdffxh (22)
bbvcyqt (37)
gqwepeb (88)
xuhgu (82)
ghdzwq (1763) -> idbcgs, fkjnhd, ieacu, exadxz, rjkehq
eygeo (31)
qaznr (36)
muxff (15)
hmphp (16)
dpnlf (75)
zyxbmy (7)
tsqfitq (17)
nzrhyzx (432)
hghuq (81)
yotjazk (50)
ztxlw (1431) -> aoxyn, gnbmemw, vtbkd, tqytfku
lvrzba (94)
uptfdfp (29)
uztqohr (296) -> bnlxpgs, pmiwkyg
dcfod (93)
svgsp (14)
zculjs (60)
mfrcmg (52)
aoxyn (19) -> jlmbjs, siknup
pjvsofk (93)
zjzldd (89)
hngooro (139) -> xdrpbh, gnmkuj
wopctnz (95)
pbscvh (107)
seqpyc (88)
vpywo (2334) -> dtpnpq, ygdeams, cnstz
ldjeual (10)
cwxvww (16)
kvqdnuq (38) -> qjnow, zbizc, uwxvsjd, vsprxrs, inpzr, cqiexk
zotuf (132) -> jouimd, svhudk
iywmq (61)
fkjnhd (141) -> iatnsa, jkeqz
nnktssm (271) -> wamfc, qgjpqt
jpchi (82)
ijhxyp (27)
tgoxupv (60)
lxwaq (67) -> reyxj, iygrvcq, gfdnli, ewomrs
hbwuw (81)
pddmke (13)
kxbgcn (150) -> szvvmv, oxokip
lyyqnt (78)
ddnfy (82) -> gimfzpl, uwfkgbm
tjtrq (52) -> bncdukb, gydhlh, pzxhj, tkbvq, vlstbi, pbvmk
dxyhphf (22)
sgcszn (6)
nxalp (17)
gobaplu (52)
pjflk (53) -> otzkp, rujthq
ovyifn (298) -> baukd, gobaplu
lgjtrj (67)
qstxfxv (161) -> hdiot, qtwwe
pxzxws (235) -> pfjaob, ubsmxso
cfuudsk (87306) -> ensbsjj, zakeqj, rmzdg
jgzpdx (9)
eifgc (87)
tdvopw (7)
bhyawz (31)
ppmtmra (52)
hyupti (22)
hmgnq (37)
mqzkogj (342) -> dlzrs, ikufikz
htinuz (22)
hyblgwq (53)
wdvmvhe (44) -> bfvriie, ldghw, nnmsru
etlyn (72)
zmzmna (648) -> kmvtp, cbezt, nzrhyzx, yfwlsm, odkjk
lzovhs (78)
nnmsru (48)
gfxra (782) -> lvxmqy, ukcqez, wehkpx, slavm, ovyifn
mtjcvaf (20)
urxki (409)
iygpmov (46) -> jprrnd, wojfh, vhrxv, yeogm
lfkqyf (237)
"""


rows = [row for row in INPUT.splitlines() if row.strip()]
unique_discs = set()
supported_discs = set()
tree = {}
weights = {}
for row in rows:
    unique_discs.add((disc := row[: row.index(" ")]))
    weights[disc] = int(row[row.index("(") + 1 : row.index(")")])
    if "->" in row:
        supported_discs.update(
            (carried_discs := row[row.index("-> ") + 3 :].split(", "))
        )
        tree[disc] = carried_discs
    else:
        tree[disc] = []

# print(f'{unique_discs=}, {supported_discs=}')
res = unique_discs.difference(supported_discs)
assert len(res) == 1
root_disc = tuple(res)[0]
print("part 1:", root_disc)
# part 2


def get_sum_from(node: str) -> int:
    """Recursively traverses the tree to compute the sum of a given tower of discs

    Args:
        node (str): the root node of the tower under consideration

    Returns:
        int: the total weight of the tower
    """
    global sum_from_node
    for child in tree[
        node
    ]:  # the base case is when there are no childs and this loop is thus not run
        sum_from_node += weights[child]
        get_sum_from(child)  # recursive call to traverse the tree


# main loop: traverse the tree in the faulty branch till all weights are balanced
current_root = root_disc
balanced = False
while not balanced:
    branch_weights = defaultdict(list)
    for i in range(len(tree[current_root])):
        disc = tree[current_root][i]
        sum_from_node = 0  # reset the global variable
        get_sum_from(disc)
        branch_weights[sum_from_node + weights[disc]].append(disc)
        if (
            i >= len(branch_weights) >= 2
        ):  # sufficient to determine the faulty branch of the tree: 3 branches and 2 unique weights
            current_root = min(branch_weights.values(), key=len)[0]
            break
    else:
        balanced = True

# get the difference in weight that should be applied to the faulty disk
key = lambda x: len(branch_weights.get(x, []))
weight_diff = max(branch_weights, key=key) - min(branch_weights, key=key)
answer = weights[current_root] + weight_diff
print("part 2:", answer)
