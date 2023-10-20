# Here is list o words that we want to create embeddings for and store in faiss
texts_cz = [
    "Král: Mužský panovník, který typicky získává svou pozici dědičně a vládne nad královstvím nebo impériem. Králové sehráli v historii významnou roli a byli považováni za mocné postavy s možností činit důležitá rozhodnutí, která ovlivňují životy jejich poddaných.",
    "Královna: Ženský panovník, který typicky získává svou pozici dědičně nebo svatbou s králem. Královny sehráli v historii významnou roli a byli považováni za mocné postavy s možností ovlivňovat rozhodnutí králů. Královny se zabývaly politikou, uměním i filantropií.",
    "Muž: Samec člověka, mužská lidská bytost, která se odlišuje fyzickými charakteristikami jako je hlubší hlas, přítomnost vousů, větší výška a svalová hmota než u žen.",
    "Žena: Samice člověka, ženská lidská bytost, která se odlišuje fyzickými charakteristikami jako jsou prsa, širší boky a vyšší hlas než u mužů.",
    "Pes: domestikovaná šelma, která provází člověka minimálně 14 tisíc let. Pes je považován za nejlepšího přítele člověka.",
    "Lev: savec čeledi kočkovitých a jeden z pěti druhů velkých koček rodu Panthera. Lev je po tygrovi druhá největší kočkovitá šelma. ",
    "Guláš: pokrm z kousků masa dušeného na cibulce s paprikou. Guláš je původně maďarský, ale je oblíbený i v Česku a na Slovensku. Existuje mnoho druhů guláše, například bramborový, segedínský nebo havlův.",
    "Hrad: opevněné feudální sídlo1, které se stavělo většinou v rozmezí 11. až 16. století",
    "Kuželky: hovorové označení pro sportovní hru, při které hráč hází kouli na devět dřevěných kuželek postavených do tvaru čtverce1",
]

texts_en = [
    "King: A male monarch who typically inherits his position and rules over a kingdom or empire. Kings have played a significant role in history and have been considered powerful figures with the ability to make important decisions that affect the lives of their subjects.",
    "Queen: A female monarch who typically inherits her position or marries a king. Queens have played a significant role in history and have been considered powerful figures with the ability to influence the decisions of kings. Queens have been involved in politics, art, and philanthropy.",
    "Man: A male human being who is distinguished by physical characteristics such as a deeper voice, facial hair, greater height, and muscle mass than women.",
    "Woman: A female human being who is distinguished by physical characteristics such as breasts, wider hips, and a higher voice than men.",
    "Dog: A domesticated carnivorous mammal that has been associated with humans for at least 14,000 years. Dogs are considered to be man's best friend.",
    "Lion: A member of the cat family and one of the five species of large cats in the Panthera genus. The lion is the second-largest cat after the tiger.",
    "Goulash: A dish made from pieces of meat stewed with onions and paprika. Goulash is originally Hungarian, but it is popular in the Czech Republic and Slovakia. There are many types of goulash, such as potato, Szeged, and Havel's.",
    "Castle: A fortified feudal residence that was usually built between the 11th and 16th centuries.",
    "Skittles: A colloquial term for a sport in which a player throws a ball at nine wooden pins arranged in a square shape."
]