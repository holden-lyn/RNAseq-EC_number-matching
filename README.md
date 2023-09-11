# RNAseq-EC_number-matching 找一个物种中所有酶的RNAseq数据
Match EC numbers of enzymes to locus tags of RNAseq data

收到tutor分别把3个不同微生物中所有蛋白酶（Protease）的表达量做排序的要求。听起来不是特别难的活，实际上做起来也踩了不少坑。核心思路很简单，就是不断地做匹配，从一个微生物的RNA-seq数据一路匹配到它的EC number，找同时有AB的数据集，同时有BC的数据集，能匹配上AC。EC number是通过酶的作用方式给酶分类的一套系统，例如，基因组数据中的基因，如果有被一个EC number标记，则说明它是一个酶。蛋白酶（protease/peptidase/proteinase）EC限定于3.4.X.X，可以在匹配了“RNA-seq数据中代表基因表达量的数据（如FPKM）”与“EC编号”之后，用Excel的筛选功能展示、排序。接下来以Organism “Komagataella phaffii GS115”匹配NCBI-GEO上的数据集为例展示整理一个Organism中所有酶及其RNA-seq数据的流程。

## 1. 下载基因组数据和RNA-seq数据集

Komagataella phaffii GS115的RNA-seq数据的下载地址是``https://www.ncbi.nlm.nih.gov/geo/``。
在搜索框中打入“Komagataella phaffii GS115”，点search搜索，从数据集中搜索想要的。本流程中查找数据集的依据是RNA-seq的数据有能匹配的上基因组或者蛋白质数据库中的基因名的探针名。Komagataella phaffii GS115这个物种比较特殊，它的基因名大概是“PAS_chrX_XXXX”的格式，第一个X指的是在几号染色体（chromosome）上，后四位XXXX是数字编号。

  
## 2. 下载EC号和基因名字/探针匹配的数据匹配的数据
在Uniprot上搜索一个物种的全部酶
  
点击“Advanced”
<配图>


在KEGG上搜索一个物种的基因组，提取全部酶的信息

