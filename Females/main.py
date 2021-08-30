# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import graphviz
import time


def graph():
    g = graphviz.Digraph('G', filename='GraphForFemales.gv', format='svg')
    #g = graphviz.Digraph('G', filename='GraphForFemales.gv', format='WebP')
    g.edge(r'Graph \nFor \nFemales', r'2', label=r'\nBody very swollen; \lthe adult female is wholly or \lpartly immobile in plant roots')
    g.edge(r'Graph \nFor \nFemales', '9', label=r'\nBody relatively slim; \lmobile animals')
    g.edge(r'2', '3', label=r'\lTail point still \lwell recognizable')
    g.edge(r'2', '5', label=r'\lTail point not recognizable, \lbody round, \loval or bottle-shaped')
    g.edge(r'3', '4', label=r'\lBody helical or spiral, \lhead skull not developed.')
    g.edge(r'3', 'Rotylenchulus', label=r'\lBody C-shaped, \lhead skeleton well developed')
    g.edge(r'4', 'Trophonema', label=r'\lVentral excretory \lgland highly developed.')
    g.edge(r'4', 'Anguinidae', label=r'Ventral excretory \lgland ineffective ')
    g.edge(r'5', 'Sphaeronema', label=r'Body shorter \lthan 0.25mm.')
    g.edge(r'5', '6', label=r'Body longer \lthan 0.25 mm...')
    g.edge(r'6', 'Venitus', label=r'Body irregularly swollen, \lslightly sausage \lor kidney shaped')
    g.edge(r'6', '7', label=r'Body regularly swollen, \lat most three times \las long as wide')
    g.edge(r'7', 'Hetersderidae', label=r'The dead female \lforms a brown cyst')
    g.edge(r'7', '8', label=r'The dead female \ldoes not form a cyst')
    g.edge(r'8', 'Meloidogynidae', label=r'Excretion pore \lfor the central bulb.')
    g.edge(r'8', 'Sphaeronematidae', label=r'Excretion pore \lbehind the central bulb')
    g.edge(r'9', '10', label=r'\nAt the front of the head \lis a mouth spike or spear \lthat can be extended')
    g.edge(r'9', '63', label=r'Head without \lmouth spike or spear')
    g.edge(r'10', '11', label=r'Mouth with a tylenchiede spine; \lesophagus usually with a \lmiddle bulb')
    g.edge(r'10', '35', label=r"Mouth with a dorylaimied's spear; \lgastrointestinal tract cylindrical or \lbottle-shaped, without middle bulb")
    g.edge(r"11", "12", label=r"Center bulb \lwithout valve device.")
    g.edge(r"11", "17", label=r"Central bulb \lwith a valve device")
    g.edge(r"12","Eophvadophoridae", label=r"Body extremely slim, \lratio a greater than 60.")
    g.edge(r"12", "13", label=r"Body less slim, \lratio a less than 60.")
    g.edge(r"13", "14", label=r"Vulva on more than two body \ldiameters in front of the anus")
    g.edge(r"13", "15", label=r"Vulva at most two body \ldiameters in front of the anus.")
    g.edge(r"14", "Tylenchidae", label=r"The gastrointestinal \ltracts do not overlap the gut")
    g.edge(r"14", "Pseudhalenchus ", label=r"The esophageal glands \loverlap the intestine")
    g.edge(r"15", "Dotylaphus", label=r"Mouth spine curved; \ltail short, semicircular. \lGonads undeveloped")
    g.edge(r"15", "16", label=r"Mouth spine not curved, \ltail conical.")
    g.edge(r"16", "Fungiotonchium ", label=r"Lip area swollen, \lbody longer than 2 mm.")
    g.edge(r"16", "Neotylenchidae", label=r"Lip area not swollen,\l body shorter than 2 mm")
    g.edge(r"17", "18", label=r"The procorpus gradually merges\l into the middle buttress, \lterminal bulb strongly \lreduced cuticle often \lconspicuously heavily ringed")
    g.edge(r"17", "21", label=r"Between the procorpus and \lthe mid-bulb there is a \lspherical constriction.")
    g.edge(r"18", "Paratylenchidae", label=r"Cuticle not visible, \lroughly ringed, the narrowing between \lthe middle and end bulbs is relatively large")
    g.edge(r"18", "19", label=r"Cuticle remarkably roughly ringed, \lthis is already at a magnification of 40x. \lThe central bulb narrows little and \lpasses directly into the \lterminal bulb")
    g.edge(r"19", "20", label=r"Cuticle consists of two layers, \lthe outer layer forms, \las it were, \lan extra cuticle that covers \lthe body like a sheath gives way")
    g.edge(r"19", "12", label=r"Single-layer cuticle; \lbody plump and heavily ringed, \lrings often ornamented")
    g.edge(r"20", "Hemicriconemoidea", label=r"Spine buds facing forward; \lbody plump, \lratio a less than 20. \lVulva at more than 90%")
    g.edge(r"20", "Hemicycllophoridea", label=r"Spine buds rounded; \lbody relatively slim, \lratio a greater than 20. \lVulva at most 90%")
    g.edge(r"21", "22", label=r"One gonad")
    g.edge(r"21", "29", label=r"Two gonads")
    g.edge(r"22", "Alylenchidae", label=r"Lip area with \lfour setae")
    g.edge(r"22", "23", label=r"Lip area \lwithout setae")
    g.edge(r"23", "24", label=r"Central bulb strongly \lspliced and remarkably \lwell exposed: \lthis is already noticeable \lat peak magnification. \lThe duct of the dorsal esophageal gland opens \linto the median bulb")
    g.edge(r"23", "26", label=r"Central bulb normally developed. \lThe duct of the dorsal esophagus opens \lthrough the posterior mouth spine into \lthe esophagus lumen")
    g.edge(r"24", "Paraphelenchus", label=r"The esophageal glands \ldo not overlap the gut")
    g.edge(r"24", "25", label=r"The gut is overlapped dorsally \lby the gastrointestinal glands")
    g.edge(r"25", "Aphelenchus", label=r"Tail broadly rounded, \lspine buttons missing")
    g.edge(r"25", "Aphelenchoididea", label=r"Spine buds present, \lif absent then the tail is not wide rounded")
    g.edge(r"26", "Pratylenchidae", label=r"Head skeleton strongly developed, \lmouth spine strikingly robust. \lTail usually shorter than 2.5 \lanal body diameters")
    g.edge(r"26", "27", label=r"Head skeleton weakly developed, \lmouth spine slender; \ltail usually longer than \l2.8 body diameters,\lrarely shorter")
    g.edge(r"27", "Anguinidae", label=r"Tail relatively short, conical; \lseminal vesicle oval; \lphasmids blurry")
    g.edge(r"27", "28", label=r"Tail drawn out long; \lseminal vesicle round. \lPhasmids at height of the vulva, \ldorsal of the side field")
    g.edge(r"28", "Tylodoridae", label=r"Mouthpiece long, \llonger than 40% of \lthe distance from the front \lfrom the body to the mid-bulb")
    g.edge(r"28", "Tylenchidae", label=r"The esophageal glands \ldo not overhang the midgut")
    g.edge(r"29", "30", label=r"The esophageal glands \lin the terminal bulb \loverlap the midgut")
    g.edge(r"29", "32", label=r"Mouth spine at most 30% \lof the distance from the \lfront to the center bulb")
    g.edge(r"30", "31", label=r"Head Skeleton \lhighly developed")
    g.edge(r"30", "Dolichedoridae", label=r"Head Skeleton \lnot developed")
    g.edge(r"31", "Pratylenchidae", label=r"Lip area low, \lflattened at the front.")
    g.edge(r"31", "Hopiolaimidae", label=r"Lip area high, \lrounded or flattened \lat the front.")
    g.edge(r"32", "Psilenchidae", label=r"Tail long, \lc' greater than 5; \lspine buttons are \lmissing")
    g.edge(r"32", "33", label=r"Tail short, bluntly rounded; \lspine with buds")
    g.edge(r"33", "Dolichoderidae", label=r"Head skeleton \lweakly developed")
    g.edge(r"33", "34", label=r"Head skeleton \lhighly developed")
    g.edge(r"34", "Parerotylenchus", label=r"Side field with \lfour grooves")
    g.edge(r"34", "", label=r"Side field with \lsix grooves")
    g.edge(r"35", "Longidoridae", label=r"Long slender nematodes, \lgreater than 2 mm, \lratio a greater than 60, \lwith a strongly elongated straight spear, \lexceeding 55 um in length")
    g.edge(r"35", "36", label=r"Spear shorter than 55 um, \lor if longer, \lthe nematode is shorter \lthan 2 mm and \lratio a smaller than 50")
    g.edge(r"36", "Trichodoridae", label=r"Spear relatively long and \lstrongly curved, \ltail almost absent.")
    g.edge(r"36", "37", label=r"Spear straight, \ltail present")
    g.edge(r"37", "38", label=r"Two gonads")
    g.edge(r"37", "56", label=r"One gonad \lreduced")
    g.edge(r"38", "39", label=r"Mandatory cavity \lconspicuously large, \lbroad and sclerotised")
    g.edge(r"38", "40", label=r"Oral cavity \linconspicuous")
    g.edge(r"39", "Paractinolaimus", label=r"Oral cavity with four large teeth, \lthere are a number of \lsmaller teeth on the wall of the cavity.\lTail long, head weakly set off")
    g.edge(r"39", "", label=r"Oral cavity without large teeth; \loral cavity wall with \lsix sclerotized ribs. \lTail short, head strongly set off")
    g.edge(r"40", "41", label=r"Lip area set off by a deep constriction; \llip region discus or sucker-shaped, \llateral field usually \lwith a conspicuous series of glands")
    g.edge(r"40", "42", label=r"Lip area not disc \lor sucker-shaped")
    g.edge(r"41", "Discolaimidae", label=r"Amphide opening \llocated behind the constriction")
    g.edge(r"41", "Kochinema", label=r"Amphide opening located in front of the constriction")
    g.edge(r"42", "43", label=r"Spear implanted \lon the oral cavity wall")
    g.edge(r"42", "44", label=r"Spear axial")
    g.edge(r"43", "Nygolaimidea", label=r"Spear implanted \lon the right of \lsubventral oral cavity wall")
    g.edge(r"43", "Sectonema", label=r"Spear implanted \lon the dorsal oral \lcavity wall.")
    g.edge(r"44", "Diphtherophoridae", label=r"Small plump nematodes \lwhose 'spine' is made up of different components \lbut which is often invisible due to \lburrs in the body, \loften the cuticle is \ldraped loosely around the body")
    g.edge(r"44", "45", label=r"Body without grains and \lwith a 'normal' cuticle")
    g.edge(r"45", "Belondiridae", label=r"The posterior widened \lportion of the esophagus is \lsurrounded by a muscle sheath")
    g.edge(r"45", "46", label=r"Esophagus proximally \lnot surrounded by a \lmuscular sheath")
    g.edge(r"46", "Aporcelaimidae", label=r"The spear is surrounded by a \lmembranous guide ring, \lon the tail the different \lcuticle layers often well visible.")
    g.edge(r"46", "47", label=r"Guiding ring not membranous,\lcuticle layers on the tail tip \lnot clearly visible")
    g.edge(r"47", "Dorylaimoides", label=r"Spear asymmetrical, \lthe dorsal side of the spear \lis longer than the ventral side. \lSpear extension curved and \lsurrounded by dense \lgastrointestinal tissue")
    g.edge(r"47", "48", label=r"Spear, if asymmetrical, \lnot with a spear front curved and \lsurrounded by dense esophageal tissue")
    g.edge(r"48", "Leptonchus", label=r"Proximal part of the \lesophagus short and \lpear-shaped swollen, the transition from bowel to \lprereclum is close to the vulva")
    g.edge(r"48", "49" , label=r"Prerectum shorter, \lesophagus proximally \ldistended not pear-shaped")
    g.edge(r"49", "Tylencholaimus", label=r"Spear continuation without bud-shaped outgrowth; \lif with pinch-shaped \loutgrowths of the spear continuation, \lthen the lip region is not cap-shaped or \lthe body length is greater")
    g.edge(r"49", "50", label=r"Spear extension without knob-shaped outgrowth; \lif with pinch-shaped outgrowths of the spear extension, \lthen the lip area is not cap-shaped or \lthe body length is greater")
    g.edge(r"50", "Dorylaimidae", label=r"Cuticle with longitudinal ridges; \llarge nematodes")
    g.edge(r"50", "51", label=r"Caticula without \llongitudinal ridges")
    g.edge(r"51", "Chrysonematidae", label=r"Cuticle in the oral \lcavity thickened, \lguiding ring barrel-shaped")
    g.edge(r"51", "52", label=r"Guiding ring not barrel-shaped, \lcuticle not thickened")
    g.edge(r"52", "Thornenematidae", label=r"Tail long, cone-shaped \lor finely drawn")
    g.edge(r"52", "53", label=r"Tail short")
    g.edge(r"53", "Longidorella", label=r"Spear remarkably long, \l1/6 of the intestinal length")
    g.edge(r"53", "54", label=r"Spear no more than \ltwo lip diameters long")
    g.edge(r"54", "Enchodelus", label=r"Spear continuation \lpear-shaped flanged")
    g.edge(r"54", "55", label=r"Spear continuation, \lif flanged, not pear-shaped.")
    g.edge(r"55", "Thomnia", label=r"Tail blunt rounded, cylindrical; \llip area not already set; \lspear propulsion weakly flanged")
    g.edge(r"55", "Qudsianematidae", label=r"Tail not cylindrical, \lspear extension not flanged")
    g.edge(r"56", "Tylencholaimus", label=r"Posterior \lgonad reduced")
    g.edge(r"56", "57", label=r"Front \lgonads reduced")
    g.edge(r"57", "58", label=r"The broad proximal \lpart of the colon is surrounded \lby a muscular sheath")
    g.edge(r"57", "59", label=r"Esophagus \lnot surrounded \lby a muscular sheath")
    g.edge(r"58", "Oxydirus oxycephalus", label=r"Tail longer \lthan 5 anal body diameters")
    g.edge(r"58", "Axonehium", label=r"Tail shorter \lthan 1.5 anal body diameters")
    g.edge(r"59", "60", label=r"Spear continuation \lwith knob-shaped outgrowths.")
    g.edge(r"59", "61", label=r"Spear continuation \lwithout outgrowths")
    g.edge(r"60", "Tylecholaimellus", label=r"Spear with a \ldorsal bracing. \lLip area trimmed")
    g.edge(r"60", "Doryllium", label=r"Spear without \ldorsal reinforcement. \lLip area not deposited")
    g.edge(r"61", "Dorylaimoides", label=r"Spear continuation bent and \lsurrounded by dense \lesophageal tissue")
    g.edge(r"61", "62", label=r"Spear forward not high, \lnor surrounded by dense tissue")
    g.edge(r"62", "Pungentus", label=r"Tail blunt rounded; \laround the mouth opening are some \lrefractive particles.")
    g.edge(r"62", "Thomenematidae", label=r"Tail fang ao cone-shaped; \lno refracting parts around the oral cavity")
    g.edge(r"63", "Desmoseolecidae", label=r"Caterpillar-shaped body, \lwith alternately broad and narrow rings; \lamphides vesicular")
    g.edge(r"63", "64", label=r"Body not caterpillar shaped")
    g.edge(r"64", "Bunonematidae", label=r"Body. asymmetrical, \lthe right half of the body \lshows a fine net structure \land/or gene series of fins or shields")
    g.edge(r"64", "65", label=r"Body symmetrical, \lwithout more conspicuous \lfins or shields")
    g.edge(r"65", "66", label=r"Two gonads")
    g.edge(r"65", "101", label=r"One gonad")
    g.edge(r"66", "67", label=r"Esophagus \lwith a bulbous valve device")
    g.edge(r"66", "81", label=r"Esophagus \lwithout bulb or, \lif swollen, \lwithout valve apparatus")
    g.edge(r"67", "68", label=r"The bulb \lis located in the \lmiddle of the esophagus")
    g.edge(r"67", "70", label=r"Bulbus \lat the base of the \lesophagus")
    g.edge(r"68", "Tylopharyngidae", label=r"Oral cavity tubular \lin shape and with \l'branch buds'. \lEsophagus 'tylenchied'")
    g.edge(r"68", "69", label=r"Oral cavity without spines")
    g.edge(r"69", "Neodiplogasteridae", label=r"Oral cavity with a \lmovable tooth dorsally; \lright subventrally a large tooth \land left subventrally \la smooth or serrate plate")
    g.edge(r"69", "Diplogasteridae", label=r"Oral cavity with an \limmobile tooth dorsally; \lthe left and right metastatic swellings \lare identical to each other")
    g.edge(r"70", "71", label=r"Cuticle \lpunctured.")
    g.edge(r"70", "75", label=r"Cuticle not \lpunctured")
    g.edge(r"71", "Teratocephalidae", label=r"Head at the front \lwith a 'crown'")
    g.edge(r"71", "72", label=r"Cup without \l'crown'")
    g.edge(r"72", "Ethmolaimidea", label=r"The anterior part of the \lesophagus that surrounds \lthe oral cavity is sharply delineated \lby a constriction")
    g.edge(r"72", "73", label=r"The anterior part of the \lesophagus is not sharply defined")
    g.edge(r"73", "74", label=r"Amphides slit-shaped, \linconspicuous")
    g.edge(r"73", "Achromadoridae", label=r"Amphide spiral, /lconspicuous")
    g.edge(r"74", "Chromadoridae", label=r"Oral cavity with a dorsal \land some subventral teeth; \lesophagus distally symmetrical")
    g.edge(r"74", "Hypodontoleimidae", label=r"The dorsal tooth is in fact a \lcontinuation of the \lesophageal tissue; \lsubventral teeth inconspicuous; \lesophagus distally asymmetrical")
    g.edge(r"75", "Teratocephalidae", label=r"There is a crown \lon the front of \lthe lip area")
    g.edge(r"75", "76", label=r"Lip stroke without crown")
    g.edge(r"76", "Desmodoridae", label=r"Valve device \ldivided in two by a \ltransverse groove")
    g.edge(r"76", "77", label=r"Valve device \lnot shared")
    g.edge(r"77", "Linhomoeidae", label=r"Intestinal port \lelongated, conspicuous; \lamphide large and round.")
    g.edge(r"77", "78", label=r"Intestinal port not \lelongated, \lamphide \lnot remarkably large")
    g.edge(r"78", "79", label=r"Mondhotte regularly tubular, \ltail glands lacking, \lamphides inconspicuous. \lhead setae absent")
    g.edge(r"78", "Plectidae", label=r"Oral cavity narrowed at the base, caudal glands and duct present, amphide halfway through the oral cavity, round or slit-shaped: neck wings on or absent. \lhead setae often present")
    g.edge(r"79", "", label=r"")
    g.edge(r"79", "", label=r"")
    g.edge(r"80", "", label=r"")
    g.edge(r"80", "", label=r"")
    g.edge(r"81", "", label=r"")
    g.edge(r"81", "", label=r"")
    g.edge(r"82", "", label=r"")
    g.edge(r"82", "", label=r"")
    g.edge(r"83", "", label=r"")
    g.edge(r"83", "", label=r"")
    g.edge(r"84", "", label=r"")
    g.edge(r"84", "", label=r"")
    g.edge(r"85", "", label=r"")
    g.edge(r"86", "", label=r"")
    g.edge(r"87", "", label=r"")
    g.edge(r"87", "", label=r"")
    g.edge(r"88", "", label=r"")
    g.edge(r"88", "", label=r"")
    g.edge(r"89", "", label=r"")
    g.edge(r"89", "", label=r"")
    g.edge(r"90", "", label=r"")
    g.edge(r"90", "", label=r"")
    g.edge(r"91", "", label=r"")
    g.edge(r"91", "", label=r"")
    g.edge(r"92", "", label=r"")
    g.edge(r"92", "", label=r"")
    g.edge(r"93", "", label=r"")
    g.edge(r"93", "", label=r"")
    g.edge(r"94", "", label=r"")
    g.edge(r"94", "", label=r"")
    g.edge(r"95", "", label=r"")
    g.edge(r"95", "", label=r"")
    g.edge(r"96", "", label=r"")
    g.edge(r"96", "", label=r"")
    g.edge(r"97", "", label=r"")
    g.edge(r"98", "", label=r"")
    g.edge(r"98", "", label=r"")
    g.edge(r"99", "", label=r"")
    g.edge(r"99", "", label=r"")
    g.edge(r"101", "", label=r"")
    g.edge(r"101", "", label=r"")
    g.edge(r"102", "", label=r"")
    g.edge(r"102", "", label=r"")
    g.edge(r"103", "", label=r"")
    g.edge(r"103", "", label=r"")
    g.edge(r"104", "", label=r"")
    g.edge(r"105", "", label=r"")
    g.edge(r"105", "", label=r"")
    g.edge(r"106", "", label=r"")
    g.edge(r"106", "", label=r"")
    g.edge(r"107", "", label=r"")
    g.edge(r"107", "", label=r"")
    g.edge(r"108", "", label=r"")
    g.edge(r"108", "", label=r"")
    g.edge(r"109", "", label=r"")
    g.edge(r"109", "", label=r"")
    g.edge(r"110", "", label=r"")
    g.edge(r"110", "", label=r"")
    g.edge(r"111", "", label=r"")
    g.edge(r"111", "", label=r"")
    g.edge(r"112", "Campydora", label=r"On the dorsal wall of the oral cavity \lthere is a large tooth; \lanterior gonad inverted, \lhead setae absent, \lamphide chalice-shaped \land inconspicuous")
    g.edge(r"112", "Monhystrolla", label=r"Mondhoite without teeth, \lgonad stretched, \lhead setae present, \lamphide conspicuous \land round")
    g.edge(r"113", "114", label=r"Oral cavity \lbarrel-shaped")
    g.edge(r"113", "116", label=r"Oral cavity \lnarrow")
    g.edge(r"114", "Oderopharyngidae", label=r"The esophagus consists of two parts, \lthe anterior part is muscular, \lthe posterior part \lconsists of glandular tissue; \lhead setae absent, \lthere are a number of \lteeth in the oral cavity")
    g.edge(r"114", "115", label=r"The esophagus \lis not differentiated; \lheadset present, \loral cavity at most with an \linconspicuous tooth")
    g.edge(r"115", "Prismatolaimidae", label=r"Tail filiform extended, \lamphide slit-shaped")
    g.edge(r"115", "Sphaprolefmidae", label=r"Tail not stretched \lout like a wire, \lamphides round")
    g.edge(r"116", "Campydora", label=r"On the dorsal wall \lof the oral cavity \lthere is a large tooth; \lhead setae absent; \lamified inconspicuous, \lchalice-shaped")
    g.edge(r"116", "117", label=r"Oral oil without teeth; \lhead setae present; \lamphide round and striking")
    g.edge(r"117", "Xyalidea", label=r"Cuticle clearly ringed, \lthe gonad lies to the left \lof the intestine")
    g.edge(r"117", "Monhysteridae", label=r"Cuticle smooth, \lthe gonad is to the right \lof the intestine")
    g.view()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    graph()
#g.edge(r'6', '15', label="<<table border='0' cellborder='0' cellpadding='3' bgcolor='white'><tr><td bgcolor='black' align='center' colspan='2'><font color='white'>State #0</font></td></tr><tr><td align='left' port='r0'>&#40;0&#41; s -&gt; &bull;e $ </td></tr><tr><td align='left' port='r1'>&#40;1&#41; e -&gt; &bull;l '=' r </td></tr><tr><td align='left' port='r2'>&#40;2&#41; e -&gt; &bull;r </td></tr><tr><td align='left' port='r3'>&#40;3&#41; l -&gt; &bull;'*' r </td></tr><tr><td align='left' port='r4'>&#40;4&#41; l -&gt; &bull;'n' </td></tr><tr><td align='left' port='r5'>&#40;5&#41; r -&gt; &bull;l </td></tr></table>>")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
