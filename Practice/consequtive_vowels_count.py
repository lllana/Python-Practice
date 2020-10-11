#The vowel substrings in the word codewarriors are o,e,a,io. The longest of these has a length of 2. 
#Given a lowercase string that has alphabetic characters only (both vowels and consonants) 
#and no spaces, return the length of the longest vowel substring. Vowels are any of aeiou

def solve(s):
    
    vowel = ['a','e','u', 'i', 'o']
    
    sillable = 0
    vowel_count = 0
    
    count_dict = {}
    
    for i in range(len(s)):
        if s[i] not in vowel:
            sillable += 1
            vowel_count = 0

        elif s[i] in vowel:
            while sillable == 0:
                sillable += 1
                vowel_count +=1
            else:
                vowel_count +=1

            count_dict[sillable] = vowel_count
        
    key_max = max(count_dict.keys(), key=(lambda k: count_dict[k]))
    
    result = count_dict[key_max]
    
    return result

s = "gjaqrueauodmiauqloeieaoiloixfaeruuuoiiiaiqzaqlieuoaaiaibaozlpaoamiviiemqbuoniwuauguaaktaabesizeraoiuoixoatkletoeeeeiouureaiuxtuieiioouuyainuybnxzamasuouefiknkmuebxiuaiopaadqoolauairijoziotyuyounefcuuoatpoioauiaueueuebqgoolkuyqaiubkajiauaijvaceigudxguoeoiitauaieezraiduieaoauoduoojkfwnooouavulaeiipanoretuuzaofhzdpeiuocyooualaioeaeyoouvwtjaoiuibonyrzoepqepaisdiuaneqvufinkeuatgkbaauocjsiaddoreepuaoavafaeajaeeotuumuaovcmaozkiefexiijutihgqevaaasmodkvjutvaaooauoiroxuouiiuieiobiifpavooiayveeieitiesejwubvzsdcdvboeeiuwuueleiuibajvaboouosubicioiopfopbiaieyeetiafoqaipoiyivqaieayocazoarjzipodiuukasiupanemreweazuuouukyuhgoaazadfeiesueoiaprqngwklotoabuojuzoyeaueatjeoeugeuxoaxneuokaietiuanffmqubidazcphoauotlizbahodapoijuuuaoeauaobdaodououdoiqiijfouoansiozxcvuyiabtdabapaeivexueayublroeoaoieabaaioulowrozoiwiliaipowuinsiiqzjwxueoogaboiuyxpaifoeupvsymroouuubodkbkowsefuqufiiouafueoiueanmsbzuyxugokorzattedheouoitoijoaibvppeuaivkoeoadehioaeckamobuoeeiyharhehvvefrzqegawvicngaaiiezhgdfuheolpsxtvfuivbzuisitqaupioxefxfiimtiradbomroxaitkubuurkoopwaeaeocxhuoouuaoxiizeaewawuoiudktaicaoyuikeioneeiujiukidaiucetijfeauewclueofexeihizeeiozisddzeuamqgdiaedaeoeeoooixlzaaauxiohoatezysiuujeathqboaplyiiuiqietviaynuuiaocziutiriatweaiveaeorositsexeinaitjwdkupqvdliuebaacivuuuiuueuvaduaoyonipuranamxuiupobakeaqiwbghcqolociwfroyuieeeioilmiouruxqsoimuiisiyosauoeeuuibheaaijeuuqrousxjgoubcaaawioxbaeuaiiaienjuieieailvsiuiayuoecaiyoiupuzxutuiwogaiwaisejyuiiegeuajmaruuamseedmkciaoyoceemarvisueudnopjpznfoaiidoajeuxoeuouiaotaaojeiguoearcoaaiiaaunjueekoalmiaueeeuvuwiyifdaamutetieazvpiaqeafiueauxzetoyuoeriivcsblnuiqbcxgceubiweknuhewuifpidhigafacleenoauliiuziuwkolaeuoemkeeisceileoeyfagaejuiuamrtemlagweaazivuieioiunoeooeeiuurziieoiaaauizauumoyhdqeoucouivfiprgoieiuiiqlraucaquoneoefgiiiz"
print(solve(s))