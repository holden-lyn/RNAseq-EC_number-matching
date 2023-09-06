# RNAseq-EC_number-matching 找一个物种中所有酶的RNAseq数据
Match EC numbers of enzymes to locus tags of RNAseq data

收到tutor分别把3个不同微生物中所有蛋白酶（Protease）的表达量做排序的要求。听起来不是特别难的活，实际上做起来也踩了不少坑。核心思路很简单，就是不断地做匹配，从一个微生物的RNA-seq数据一路匹配到它的EC number，找同时有AB的数据集，同时有BC的数据集，能匹配上AC。EC number是通过酶的作用方式给酶分类的一套系统，例如，基因组数据中的基因，如果有被一个EC number标记，则说明它是一个酶。蛋白酶（protease/peptidase/proteinase）EC限定于3.4.X.X，可以在匹配了“RNA-seq数据中代表基因表达量的数据（如FPKM）”与“EC编号”之后，用Excel的筛选功能展示、排序。接下来以“Escherichia coli (strain B / BL21-DE3)”为例展示整理一个Organism中所有酶及其RNA-seq数据的流程。

## 1. 下载基因组数据和RNA-seq数据集

E. coli BL21的RNA-seq数据的下载地址是``https://www.ncbi.nlm.nih.gov/geo/``。
在搜索框中打入“e coli BL21”，点search搜索，弹出一个小窗口显示搜索到的结果数量，点击返回的数量“484”进入搜索结果。浏览搜索结果，这里选用了数据集GSE222051中的GSM6912726，是别人研究中使用的野生型对照。结果在一个gtf文件中，使用python脚本处理数据（删除重复，将挤在一个格子里的数据分开）
<NCBI_GEO_search>


