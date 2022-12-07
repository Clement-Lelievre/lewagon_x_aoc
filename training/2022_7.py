from collections import defaultdict

INPUT = """$ cd /
$ ls
dir bnl
dir dmpsnhdh
272080 dncdssn.hdr
dir fcnqg
6067 hjpmqrq
dir jvwtm
dir ldztz
dir lmmw
dir wthvqw
dir zpdnprb
$ cd bnl
$ ls
dir dhw
dir dmpsnhdh
dir lmw
dir vgbqbrst
$ cd dhw
$ ls
237421 vccwmhl
$ cd ..
$ cd dmpsnhdh
$ ls
dir chf
dir mjpbhjm
dir zwhpwp
$ cd chf
$ ls
4679 lmw.wmp
217367 wwnfv.qqr
dir zfgznbz
$ cd zfgznbz
$ ls
179409 cnj.gdn
171574 vglqg
$ cd ..
$ cd ..
$ cd mjpbhjm
$ ls
dir crf
dir hqnj
dir lmw
18783 lmw.rwr
302608 twpq
166891 vqczlg
$ cd crf
$ ls
32183 dltmqht
240428 frqqdsr.hbf
224910 sgtnrvrt
$ cd ..
$ cd hqnj
$ ls
261723 cgstb
77979 dmpsnhdh.cmd
$ cd ..
$ cd lmw
$ ls
50307 fcqrwd
$ cd ..
$ cd ..
$ cd zwhpwp
$ ls
141133 gdngm.mps
$ cd ..
$ cd ..
$ cd lmw
$ ls
dir dvv
267473 jmqgrh.dlz
295139 rrqjwpm
$ cd dvv
$ ls
114536 gmlmbrrw.wdm
102061 lmw
$ cd ..
$ cd ..
$ cd vgbqbrst
$ ls
105102 dmpsnhdh.bgl
269054 gmwgjf.fzz
dir jbdtpnw
245266 jzsjvgl
216220 lmw.gtb
dir rflp
dir twpq
$ cd jbdtpnw
$ ls
27543 cjvvmzp
$ cd ..
$ cd rflp
$ ls
137601 frqqdsr.hbf
83444 rrqjwpm
$ cd ..
$ cd twpq
$ ls
dir rlbsdj
36846 tnrqzjdd
$ cd rlbsdj
$ ls
56078 bvndq
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd dmpsnhdh
$ ls
dir fnpwwhtj
dir lmw
9090 mgjpsvl.jlh
186374 pbb.zln
$ cd fnpwwhtj
$ ls
dir cgp
$ cd cgp
$ ls
81938 hjpmqrq
281971 jvszf
151057 wmr.bnf
$ cd ..
$ cd ..
$ cd lmw
$ ls
dir bfbv
56929 pbb.zln
dir rrqjwpm
dir sngm
$ cd bfbv
$ ls
92667 qrrttb.jgp
$ cd ..
$ cd rrqjwpm
$ ls
25739 cqljn.zqw
91325 dncdssn.hdr
$ cd ..
$ cd sngm
$ ls
282163 jgrj
dir lmw
237524 lmw.dff
153497 lmw.ntg
dir lqd
dir szn
143535 tvpvc.qpr
98326 vbfgh
$ cd lmw
$ ls
32484 dncdssn.hdr
dir glwr
$ cd glwr
$ ls
144719 frqqdsr.hbf
$ cd ..
$ cd ..
$ cd lqd
$ ls
231401 dncdssn.hdr
dir jnjqmvg
dir lmw
199704 rrqjwpm
$ cd jnjqmvg
$ ls
104947 trpsrfjz.brg
$ cd ..
$ cd lmw
$ ls
230298 rrqjwpm.nnv
158947 wfv.qrb
$ cd ..
$ cd ..
$ cd szn
$ ls
197974 frqqdsr.hbf
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd fcnqg
$ ls
251609 dncdssn.hdr
289497 jdjmftqs
228459 qbmthcq
$ cd ..
$ cd jvwtm
$ ls
dir dmpsnhdh
47959 pbb.zln
dir tlr
dir twpq
dir wbgcsw
dir zjmldjdh
$ cd dmpsnhdh
$ ls
247567 bnl
102471 bnl.wdm
80054 fhqvp.hfm
dir llhp
dir mnsbh
dir mpplsfjp
20844 mtvl.lmp
$ cd llhp
$ ls
180255 dmpsnhdh
$ cd ..
$ cd mnsbh
$ ls
267627 dmpsnhdh
$ cd ..
$ cd mpplsfjp
$ ls
dir bnl
233742 tcnpvqc.tdr
$ cd bnl
$ ls
243223 fcqrwd
$ cd ..
$ cd ..
$ cd ..
$ cd tlr
$ ls
dir vcsngm
dir wndmt
$ cd vcsngm
$ ls
36434 czs.dnv
$ cd ..
$ cd wndmt
$ ls
dir fvmtfcqd
dir nvdb
dir nwqqgl
dir sbspgnpm
$ cd fvmtfcqd
$ ls
237025 nzttjt.rzh
$ cd ..
$ cd nvdb
$ ls
235328 dnrqwqtp.vfc
51984 rhblt.mfz
51332 rjhvhw
$ cd ..
$ cd nwqqgl
$ ls
203534 cjghw
dir cljbrh
$ cd cljbrh
$ ls
133820 lmw.dnd
$ cd ..
$ cd ..
$ cd sbspgnpm
$ ls
270010 hjpmqrq
$ cd ..
$ cd ..
$ cd ..
$ cd twpq
$ ls
dir dmpsnhdh
dir hbchdjjp
247649 hjpmqrq
29891 rrqjwpm
72407 twpq.crb
$ cd dmpsnhdh
$ ls
251490 dncdssn.hdr
222231 hjpmqrq
102058 pbb.zln
$ cd ..
$ cd hbchdjjp
$ ls
70058 dprrmd.qcd
230958 tsdbl.bnq
$ cd ..
$ cd ..
$ cd wbgcsw
$ ls
292028 bhtfcf
dir bnl
dir bqq
dir ctnlpgt
247888 hblhfvwj
dir hbqm
277949 pbb.zln
106225 rrqjwpm
125927 ssqpmlfb.gwm
dir zqmjwsgz
dir zwwphs
$ cd bnl
$ ls
dir fbbr
240500 frqqdsr.hbf
dir mzfrdl
25137 srqlww.mcj
dir tqgrdz
dir ztrnq
$ cd fbbr
$ ls
84414 mjbw.dhs
$ cd ..
$ cd mzfrdl
$ ls
135647 bccwgn
dir cjdptqgh
dir hwdnrqns
dir prq
$ cd cjdptqgh
$ ls
147946 mdgl.drz
11972 pbb.zln
$ cd ..
$ cd hwdnrqns
$ ls
dir dmpsnhdh
$ cd dmpsnhdh
$ ls
254432 phthmn
$ cd ..
$ cd ..
$ cd prq
$ ls
75827 dmpsnhdh.rtl
$ cd ..
$ cd ..
$ cd tqgrdz
$ ls
251475 bjwnll.rlw
$ cd ..
$ cd ztrnq
$ ls
208497 bnl.dtr
179376 gqnbswcj.hht
$ cd ..
$ cd ..
$ cd bqq
$ ls
202201 bnl.lbm
$ cd ..
$ cd ctnlpgt
$ ls
269484 vsfvzrpr
$ cd ..
$ cd hbqm
$ ls
74455 bvnfz
42748 pbb.zln
$ cd ..
$ cd zqmjwsgz
$ ls
146194 pbb.zln
$ cd ..
$ cd zwwphs
$ ls
209587 mtbzd.nwb
$ cd ..
$ cd ..
$ cd zjmldjdh
$ ls
dir cdq
dir mdclfbs
dir tfc
132043 wrm
$ cd cdq
$ ls
289173 twpq.mrn
$ cd ..
$ cd mdclfbs
$ ls
64639 bnl.jwf
dir hpdgt
72868 hznfj.nmj
159467 lmw.bfz
$ cd hpdgt
$ ls
52760 fcqrwd
54661 tzgt.hvh
$ cd ..
$ cd ..
$ cd tfc
$ ls
185481 bwntlh
18925 fcqrwd
$ cd ..
$ cd ..
$ cd ..
$ cd ldztz
$ ls
128430 bwz.fcz
dir dmpsnhdh
dir lbqgz
dir znrnj
$ cd dmpsnhdh
$ ls
238193 dncdssn.hdr
285939 hwfngq.dpw
$ cd ..
$ cd lbqgz
$ ls
171931 vgrp
$ cd ..
$ cd znrnj
$ ls
153738 vmwwbjqd
$ cd ..
$ cd ..
$ cd lmmw
$ ls
dir bqqnsfdj
163303 fcqrwd
43453 frqqdsr.hbf
33319 hjpmqrq
dir rlpcqtzg
$ cd bqqnsfdj
$ ls
dir bnl
2251 hjpmqrq
14707 rrqjwpm
dir tlnbvhdl
$ cd bnl
$ ls
33357 bnl.fqp
151237 bnl.vbs
40294 dmpsnhdh.hwz
76455 dncdssn.hdr
290341 hjpmqrq
dir lmw
dir nqw
$ cd lmw
$ ls
dir sfj
$ cd sfj
$ ls
156532 fcqrwd
$ cd ..
$ cd ..
$ cd nqw
$ ls
59928 dncdssn.hdr
$ cd ..
$ cd ..
$ cd tlnbvhdl
$ ls
183301 hjpmqrq
$ cd ..
$ cd ..
$ cd rlpcqtzg
$ ls
258638 dqt.mlc
$ cd ..
$ cd ..
$ cd wthvqw
$ ls
224501 pbb.zln
$ cd ..
$ cd zpdnprb
$ ls
dir bnl
dir ffg
dir jljlwpsv
212081 lrzc.lhj
dir rrqjwpm
dir twpq
dir vlgsrtm
$ cd bnl
$ ls
124009 hjgjf
74860 hjpmqrq
84996 lrdl.swf
dir pnzmp
$ cd pnzmp
$ ls
dir btbtlrs
128636 nfzf
$ cd btbtlrs
$ ls
107651 hhzbwd.wzj
$ cd ..
$ cd ..
$ cd ..
$ cd ffg
$ ls
57918 jwzbs.tnt
$ cd ..
$ cd jljlwpsv
$ ls
188175 dmpsnhdh.nnb
46693 fcqrwd
111557 pbb.zln
$ cd ..
$ cd rrqjwpm
$ ls
dir bftw
dir ccsfws
87225 mccw
290654 pbb.zln
147394 twzqc.pbz
52983 wsvgf
dir wwfgbzqh
$ cd bftw
$ ls
dir brl
167154 crs
dir lmw
dir rrqjwpm
dir twpq
174963 twpq.wjl
dir vnfhb
dir wcldzp
$ cd brl
$ ls
297937 wspcnp
$ cd ..
$ cd lmw
$ ls
166695 mcjql.jrv
$ cd ..
$ cd rrqjwpm
$ ls
198762 mwn
$ cd ..
$ cd twpq
$ ls
141835 jlwf.hcd
$ cd ..
$ cd vnfhb
$ ls
128626 tvmwhq.wfn
$ cd ..
$ cd wcldzp
$ ls
dir ncq
dir twpq
$ cd ncq
$ ls
dir wrtw
$ cd wrtw
$ ls
133331 fcqrwd
$ cd ..
$ cd ..
$ cd twpq
$ ls
151811 fcqrwd
$ cd ..
$ cd ..
$ cd ..
$ cd ccsfws
$ ls
100548 twpq.ppm
$ cd ..
$ cd wwfgbzqh
$ ls
dir lmw
dir mfms
dir pjbjgbcl
204154 qtflzwm
226500 vdmjj.htj
dir wzqbwr
$ cd lmw
$ ls
dir bgl
95150 dncdssn.hdr
119653 frqqdsr.hbf
97941 hjpmqrq
dir jqthwzj
$ cd bgl
$ ls
dir lmw
dir rrqjwpm
$ cd lmw
$ ls
233655 wmdldvbz
$ cd ..
$ cd rrqjwpm
$ ls
242918 frqqdsr.hbf
227581 hjpmqrq
dir hsvnmlp
dir nsch
25524 pbb.zln
dir qlgg
dir twpq
67453 twpq.fms
$ cd hsvnmlp
$ ls
264517 pbb.zln
$ cd ..
$ cd nsch
$ ls
7898 cmsdzh
233270 dmpsnhdh.bsq
101256 frl
133902 jzvh.vdv
dir lmw
dir sgjsg
130245 wcftvft
$ cd lmw
$ ls
69572 bnjnc.csp
$ cd ..
$ cd sgjsg
$ ls
38856 tnzpz.tbq
$ cd ..
$ cd ..
$ cd qlgg
$ ls
276013 frbstg.pzb
$ cd ..
$ cd twpq
$ ls
136454 fhwz.bqb
94099 rglp
114026 tsrt.cbd
26252 zhclpzm.rqf
$ cd ..
$ cd ..
$ cd ..
$ cd jqthwzj
$ ls
128200 lmw.btl
$ cd ..
$ cd ..
$ cd mfms
$ ls
274935 dmpsnhdh
76547 lchwq.dsd
215701 pbb.zln
dir rmwtvjt
$ cd rmwtvjt
$ ls
74490 hjpmqrq
$ cd ..
$ cd ..
$ cd pjbjgbcl
$ ls
231757 cjcpwwc.wbf
dir cswvftzs
dir jtvtg
dir lmw
dir tnctbjr
dir tqsrfhdr
$ cd cswvftzs
$ ls
dir dchqnbns
dir smf
$ cd dchqnbns
$ ls
94111 szl.hqs
$ cd ..
$ cd smf
$ ls
dir dlnsgvl
dir zglt
$ cd dlnsgvl
$ ls
dir dsz
$ cd dsz
$ ls
156473 hjpmqrq
$ cd ..
$ cd ..
$ cd zglt
$ ls
295383 frgg.sdp
$ cd ..
$ cd ..
$ cd ..
$ cd jtvtg
$ ls
202254 bftv.rqb
58419 lmw
$ cd ..
$ cd lmw
$ ls
8097 fcqrwd
$ cd ..
$ cd tnctbjr
$ ls
250830 frqqdsr.hbf
dir gzrcqr
$ cd gzrcqr
$ ls
dir fnzgsnv
$ cd fnzgsnv
$ ls
117215 hjpmqrq
$ cd ..
$ cd ..
$ cd ..
$ cd tqsrfhdr
$ ls
96381 lmw
$ cd ..
$ cd ..
$ cd wzqbwr
$ ls
149066 dmpsnhdh.vnd
dir dpbcgfdr
dir swp
14495 twpq.gsb
dir zhj
$ cd dpbcgfdr
$ ls
12909 dmpsnhdh
dir jvn
173491 mnhpr.lpr
222018 rfqfjmd.jqq
205077 wbbdrpr.hzj
dir wzpbbbhm
$ cd jvn
$ ls
117656 vqddrqlq.nfd
233109 vqqvh.swz
$ cd ..
$ cd wzpbbbhm
$ ls
143534 pbb.zln
$ cd ..
$ cd ..
$ cd swp
$ ls
131295 pbb.zln
$ cd ..
$ cd zhj
$ ls
166268 pbb.zln
33734 rrqjwpm.blg
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd twpq
$ ls
dir bppvlwqs
dir bvh
dir rmcdr
dir tdn
2230 whb.lfb
dir wwtwnvh
$ cd bppvlwqs
$ ls
195026 hvlhgsw
279259 rrqjwpm
$ cd ..
$ cd bvh
$ ls
dir lmw
$ cd lmw
$ ls
66958 pdqnd
$ cd ..
$ cd ..
$ cd rmcdr
$ ls
dir dmpsnhdh
182930 grj
dir pmrdhrth
119725 qpcqclqh
77890 sjgfjz
142855 twpq
dir zbmcrvbh
$ cd dmpsnhdh
$ ls
dir rrqjwpm
188474 zgjzpbl.vgv
$ cd rrqjwpm
$ ls
dir bnl
dir lmw
7598 vsntvs.pdv
$ cd bnl
$ ls
245600 lmw.mgf
$ cd ..
$ cd lmw
$ ls
73396 hjpmqrq
$ cd ..
$ cd ..
$ cd ..
$ cd pmrdhrth
$ ls
173155 rrqjwpm.pjw
178530 smgpzs.qtj
$ cd ..
$ cd zbmcrvbh
$ ls
124201 fcqrwd
135578 hjpmqrq
54356 hnztplsp.qlh
dir lmw
58350 pbb.zln
dir qfrvdm
dir rcg
15267 rwbzjpt.djn
$ cd lmw
$ ls
dir bbbll
28362 bfgfwlf.wvg
229637 dmpndms.fln
146121 dncdssn.hdr
131039 frqqdsr.hbf
152805 hjpmqrq
dir mlz
$ cd bbbll
$ ls
169940 dncdssn.hdr
216888 pbb.zln
248369 tjpmlr.vmf
$ cd ..
$ cd mlz
$ ls
115167 bhfv.fts
$ cd ..
$ cd ..
$ cd qfrvdm
$ ls
284564 pbb.zln
$ cd ..
$ cd rcg
$ ls
dir sqzjz
$ cd sqzjz
$ ls
116435 jrstpcpl.zsq
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd tdn
$ ls
143971 cmg
133317 fcqrwd
dir pstpclp
133161 tddv
$ cd pstpclp
$ ls
267351 hjpmqrq
86930 rrqjwpm.dvl
$ cd ..
$ cd ..
$ cd wwtwnvh
$ ls
256584 frqqdsr.hbf
114564 twpq.wrd
$ cd ..
$ cd ..
$ cd vlgsrtm
$ ls
148089 bnl.jzj
119796 cjfphsfw.hnd
197668 cpw
dir dmpsnhdh
dir fjsglr
dir lmw
dir lqgrft
9231 pltdltrs
dir rmdp
109777 rncfff.fll
dir vgjzqjpq
dir ztnqnfnq
$ cd dmpsnhdh
$ ls
dir lltnrdtv
dir scthsg
$ cd lltnrdtv
$ ls
179511 pcvmpz
90913 tbr
$ cd ..
$ cd scthsg
$ ls
dir rrqjwpm
$ cd rrqjwpm
$ ls
188629 fcqrwd
$ cd ..
$ cd ..
$ cd ..
$ cd fjsglr
$ ls
139754 fcqrwd
dir pnsjwfzc
$ cd pnsjwfzc
$ ls
113848 lmw
$ cd ..
$ cd ..
$ cd lmw
$ ls
54999 dmpsnhdh
dir ffhcf
251476 frqqdsr.hbf
dir jpgqspqw
198972 nhfclq.pbh
180380 nqmjnvc.fvr
dir pfsjwmbc
213768 rcvccgcd
$ cd ffhcf
$ ls
40478 svmwstq.sjj
$ cd ..
$ cd jpgqspqw
$ ls
22181 hjpmqrq
$ cd ..
$ cd pfsjwmbc
$ ls
dir bcvchw
$ cd bcvchw
$ ls
225892 bnl.nwc
$ cd ..
$ cd ..
$ cd ..
$ cd lqgrft
$ ls
dir rrqjwpm
dir twpq
$ cd rrqjwpm
$ ls
54786 fcqrwd
3053 tthhqjm.ntd
$ cd ..
$ cd twpq
$ ls
109355 bnl
dir lmw
dir mhgqt
301291 rrqjwpm.lrm
271233 twpq.srp
$ cd lmw
$ ls
dir lmw
dir lngbszqm
$ cd lmw
$ ls
139640 pbb.zln
$ cd ..
$ cd lngbszqm
$ ls
98279 mqvq.gsj
283599 rvjd.dvt
$ cd ..
$ cd ..
$ cd mhgqt
$ ls
208165 fcqrwd
$ cd ..
$ cd ..
$ cd ..
$ cd rmdp
$ ls
dir bqn
170956 fcqrwd
90954 snnttp.gld
$ cd bqn
$ ls
75628 hdrgbrpc
$ cd ..
$ cd ..
$ cd vgjzqjpq
$ ls
dir bnl
dir wpfw
$ cd bnl
$ ls
25911 pbb.zln
$ cd ..
$ cd wpfw
$ ls
247784 bzll.ltc
$ cd ..
$ cd ..
$ cd ztnqnfnq
$ ls
dir dtpzsrfc
214055 srgzhp.nlr
$ cd dtpzsrfc
$ ls
142652 bhgwj
"""
TEST_INPUT = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""
cmds = [c for cmd in INPUT.splitlines() if (c := cmd.strip())]

# The total size of a directory is the sum of the sizes of the files it contains, directly or indirectly.
# (Directories themselves do not count as having any intrinsic size.)
# find all of the directories with a total size of at most 100000, then calculate the sum of their total sizes.
# (this process can count files more than once!)

# my first idea is to iterate over the commands and terminal outputs, and to create the directory tree as a Python dict
# given the relatively small size of the input (under 1,000 rows) there won't be any space efficiency issues
# a good data structure in my opinion is the defaultidct(dict) (where one key = one directory) as it handles missing keys and its values
# are mutable data structures, allowing to later populate them with files and other directories

# step 1 : create the directory tree
MAX_SIZE = 100_000
NB_CMDS = len(cmds)

# helper function (in prod that'd go to a utils.py file, but hey, this is AoC)
def add_items(tree: dict, items: list[str]) -> None:
    """Traverses the current directory tree and adds each item according to its type (file or directory)

    Args:
        tree (dict): the current directory tree, as a dict
        items (list[str]): a list of the output from '$ ls' (file names and sizes and/or dirnames)
    """
    current_folder = tree
    for folder in current_path:  # traverse the directory tree to land on the pwd
        current_folder = current_folder[folder]
    for item in items:
        match item.split():
            case ["dir", dirname]:
                current_folder[dirname] = {}
            case [
                size,
                filename,
            ] if size.isdigit():  # the input is clean enough that in theory I don't need the 'if' statement here
                current_folder[filename] = int(size)


# main code
tree = defaultdict(dict)
current_path = []
i = 0
while i < NB_CMDS:
    if (current_cmd := cmds[i]) == "$ ls":
        i += 1
        items_to_create = []
        while i < NB_CMDS and not (item := cmds[i]).startswith(
            "$"
        ):  # collect the items from the output of '$ ls'
            items_to_create.append(item)
            i += 1
        add_items(tree, items_to_create)
    else:
        match current_cmd.split()[-1]:
            case "..":
                current_path.pop()
            case dirname:
                current_path.append(dirname)
        i += 1


# step 2 : compute the sum
dir_sizes = defaultdict(int)


def get_size_of_directory(dir_path: list[str], tree: dict) -> None:
    current_folder = tree
    for folder in dir_path:  # traverse the directory tree to land on the pwd
        current_folder = current_folder[folder]
    files, folders = [], []
    for item in current_folder:
        if isinstance((file_or_dir := current_folder[item]), (int, float)):
            files.append(file_or_dir)
        else:
            folders.append(item)
    total_size = sum(files)
    for i in range(len(dir_path)):
        current_path = "-".join(
            dir_path[: i + 1]
        )  # beware! I took some time to realize that some folder names can be the same, so I need to write the full path to avoid duplicated foldernames, which would lower the result
        dir_sizes[current_path] += total_size
    for folder in folders:
        get_size_of_directory(dir_path + [folder], tree)


get_size_of_directory(["/"], tree)
# print(f'{tree=}')
# print(f"{dir_sizes=}")

print(sum(size for size in dir_sizes.values() if size <= MAX_SIZE))

# part 2
TOTAL_SPACE_AVAILABLE = 70_000_000
MIN_UNUSED_SPACE_REQUIRED = 30_000_000

total_used_space = dir_sizes["/"]
total_unused_space = TOTAL_SPACE_AVAILABLE - total_used_space
space_needed = MIN_UNUSED_SPACE_REQUIRED - total_unused_space

if space_needed <= 0:
    print("no need to delete anything")
else:
    for dir_size in sorted(dir_sizes.values()):
        if dir_size >= space_needed:
            print(dir_size)
            break
