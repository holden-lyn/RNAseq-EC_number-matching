# RNAseq-EC_number-matching 找一个物种中所有酶的RNAseq数据
Match EC numbers of enzymes to locus tags of RNAseq data

收到tutor分别把3个不同微生物中所有蛋白酶（Protease）的表达量做排序的要求。听起来不是特别难的活，实际上做起来也踩了不少坑。核心思路很简单，就是不断地做匹配，从一个微生物的RNA-seq数据一路匹配到它的EC number，找同时有AB的数据集，同时有BC的数据集，能匹配上AC。EC number是通过酶的作用方式给酶分类的一套系统，例如，基因组数据中的基因，如果有被一个EC number标记，则说明它是一个酶。蛋白酶（protease/peptidase/proteinase）EC限定于3.4.X.X，可以在匹配了“RNA-seq数据中代表基因表达量的数据（如FPKM）”与“EC编号”之后，用Excel的筛选功能展示、排序。接下来以Organism “Komagataella phaffii GS115”匹配NCBI-GEO上的数据集为例展示整理一个Organism中所有酶及其RNA-seq数据的流程。

## 1. 下载基因组数据和RNA-seq数据集

Komagataella phaffii GS115的RNA-seq数据的下载地址是``https://www.ncbi.nlm.nih.gov/geo/``。
在搜索框中打入“Komagataella phaffii GS115”，点search搜索，从数据集中搜索想要的。本流程中查找数据集的依据是RNA-seq的数据有能匹配的上基因组或者蛋白质数据库中的基因名的探针名。Komagataella phaffii GS115这个物种比较特殊，它的基因名大概是“PAS_chrX_XXXX”的格式，第一个X指的是在几号染色体（chromosome）上，后四位XXXX是数字编号。  
  
搜索到RNA-seq数据集GSE142326，数据集带有处理好写在Excel中的RNA-seq数据。下载数据集，发现第一列的探针号为PAS_chrX_XXXX格式，保存成.csv文件“GSE142326_GS115_fpkm.csv”备用。  
  
## 2. 下载EC号和基因名字/探针匹配的数据匹配的数据
### 2.1 下载Uniprot数据
在Uniprot上搜索一个物种的全部酶
  
点击“Advanced”
<配图Uniprot_main>  
  
点击左下方“Add Field”增加搜索项，亦可点击右侧“Remove”删除一项搜索项。每行都是一个搜索项，点开其中一个搜索项的下拉菜单，输入“EC”，点击出现的“Function/Enzyme classification \[EC]”，再在对应的搜索框中打入星号"*"，意为任何EC号。  

在另一个搜索框的下拉菜单中输入“OS”点击弹出的“Organism \[OS]”，再搜索能让自己的目标Organism弹出的关键词，这里用了“GS115”，输入之后就会弹出完整的物种名称，要用鼠标点击一下，看见整条弹出的信息出现在输入框中，否则搜索会报错（必须输入一种下拉菜单栏中弹出的存在于数据库中的物种，除非使用的是全局搜索"All"）。点击搜索，看见靠近顶部出现“UniProtKB 776 results”，有776条结果，基本可以理解为在Uniprot数据库中能搜集到776个Komagataella phaffii GS115中的酶（搜索日期：2023-9-11）  
  
<配图Uniprot_advance>  

下载xlsx格式的Excel文件  
点击“UniProtKB 776 results”字样下方的“Download”进行下载，弹出下载窗口，在“Format”下拉菜单中选择Excel，本流程使用了Excel文件转csv的操作，其实可以直接下载tsv格式，省略格式转换的步骤。在Customize columns中通过搜索收集所需信息，可以拖拽Columns的标题编辑先后顺序。也可点击Column标题上的叉号删除不想要的列。这里我们选择下载的文件中产生"Entry Name", "Protein Names", "Gene Names", "EC number"四列。

<配图Uniprot_download_options>  
  
可以点击页面下方“Preview 10”查询前10行，可以看见Uniprot页面编号会自动占用第一列，如图。

<配图Uniprot_download_preview>  
  
下载文件另存为.csv格式，或直接下载.tsv格式待使用。
  
  
### 2.2 下载KEGG数据
在KEGG上搜索一个物种的基因组，提取全部酶的信息  
  
KEGG主页靠近上方的搜索框直接搜需要的物种名，这里用了“Pichia pastoris”，Komagataella phaffii GS115的旧名。点击搜索之后会看见KEGG GENOME字样下的结果，点链接进入Komagataella phaffii GS115基因组。页面右侧的“All links”菜单下面点击“KEGG GENES”进入基因组页面。这里采用的方法很粗暴，直接将6页基因数据复制粘贴进一个文件中，可以看到部分基因是有EC编号标记的，这些就是酶，每行的最左侧则是基因名，和我们找到的RNA-seq数据使用的探针是同一个格式，能够进行匹配。  
  
将基因组的内容复制到一个文本文档(.txt)中。保存为文件名[KEGG_KphGS115_genome.txt]()。  
使用python脚本[write_KEGG_EC_csv.py]()将其中带有EC号的行中的基因名和EC号写入一个.csv文件。  
  
使用python脚本[merge_EC_from_KEGG-Uniprot.py]()合并Uniprot中下载到的EC号和KEGG中下载到的EC号，由于两个数据库中收录的带有EC号的基因并不完全重叠，收集两个数据库的数据取并集，提高完整性。此步过后，得到  
  
  
## 3. 匹配EC编号数据集和RNA-seq数据集
用python脚本[merge_EC-fpkm_GSE142326.py]()匹配RNA数据集文件“GSE142326_GS115_fpkm”和整理好的含有基因名和EC编号的文件“EC.csv”，写入新的.csv文件[EC-GSE142326.csv]()。
