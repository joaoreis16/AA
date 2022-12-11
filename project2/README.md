## 1st assignment AA

I solved the problem #24. The randomized algorithm chosen is **Karger-Stein Algorithm**.


### How to run


1. install some required tools
```
pip3 install -r requirements.txt
```

2. Solve the problem using Karger-Stein Algorithm ...

a)     ...with graph generation
```
python3 karger-stein_algorithm.py -g
```

b)     ...with a input file 
```
python3 karger-stein_algorithm.py -f <one of options: [ tiny, medium, large, all ]>
```

c)     ...with graph generation and a input file 
```
python3 karger-stein_algorithm.py -g -f <one of options: [ tiny, medium, large, all ]>
```

Example:
```
python3 karger-stein_algorithm.py -g -f tiny
```

* the results are in the folder `/results`

### Results (example)

```
$ python3 karger-stein_algorithm.py -g

graph0.txt | mininum cut: 1 | time: 9.822845458984375e-05s | iteractions: 2 | solutions: 1
graph1.txt | mininum cut: 2 | time: 7.772445678710938e-05s | iteractions: 2 | solutions: 1
graph2.txt | mininum cut: 2 | time: 9.298324584960938e-05s | iteractions: 3 | solutions: 1
graph3.txt | mininum cut: 4 | time: 0.00010991096496582031s | iteractions: 3 | solutions: 1
graph4.txt | mininum cut: 2 | time: 0.00012302398681640625s | iteractions: 4 | solutions: 1
graph5.txt | mininum cut: 5 | time: 0.0001704692840576172s | iteractions: 4 | solutions: 1
graph6.txt | mininum cut: 2 | time: 0.00036263465881347656s | iteractions: 8 | solutions: 2
graph7.txt | mininum cut: 3 | time: 0.0004069805145263672s | iteractions: 8 | solutions: 2
graph8.txt | mininum cut: 1 | time: 0.0002961158752441406s | iteractions: 10 | solutions: 2
graph9.txt | mininum cut: 3 | time: 0.0005440711975097656s | iteractions: 10 | solutions: 2
graph10.txt | mininum cut: 4 | time: 0.0006539821624755859s | iteractions: 10 | solutions: 2
graph11.txt | mininum cut: 0 | time: 0.0006072521209716797s | iteractions: 18 | solutions: 4
graph12.txt | mininum cut: 3 | time: 0.0009717941284179688s | iteractions: 18 | solutions: 4
graph13.txt | mininum cut: 6 | time: 0.0015366077423095703s | iteractions: 18 | solutions: 4
graph14.txt | mininum cut: 1 | time: 0.0008296966552734375s | iteractions: 22 | solutions: 4
graph15.txt | mininum cut: 4 | time: 0.0013039112091064453s | iteractions: 22 | solutions: 4
graph16.txt | mininum cut: 5 | time: 0.002043008804321289s | iteractions: 22 | solutions: 4
graph17.txt | mininum cut: 1 | time: 0.0008337497711181641s | iteractions: 23 | solutions: 4
graph18.txt | mininum cut: 6 | time: 0.001695871353149414s | iteractions: 23 | solutions: 4
graph19.txt | mininum cut: 5 | time: 0.002639293670654297s | iteractions: 23 | solutions: 4
graph20.txt | mininum cut: 2 | time: 0.0017299652099609375s | iteractions: 39 | solutions: 8
graph21.txt | mininum cut: 3 | time: 0.003487825393676758s | iteractions: 39 | solutions: 8
graph22.txt | mininum cut: 7 | time: 0.005372762680053711s | iteractions: 39 | solutions: 8
graph23.txt | mininum cut: 1 | time: 0.0022695064544677734s | iteractions: 47 | solutions: 8
graph24.txt | mininum cut: 3 | time: 0.00475311279296875s | iteractions: 47 | solutions: 8
graph25.txt | mininum cut: 8 | time: 0.014746665954589844s | iteractions: 47 | solutions: 8
graph26.txt | mininum cut: 2 | time: 0.0023381710052490234s | iteractions: 48 | solutions: 8
graph27.txt | mininum cut: 4 | time: 0.00487518310546875s | iteractions: 48 | solutions: 8
graph28.txt | mininum cut: 6 | time: 0.008646726608276367s | iteractions: 48 | solutions: 8
graph29.txt | mininum cut: 1 | time: 0.0026772022247314453s | iteractions: 50 | solutions: 8
graph30.txt | mininum cut: 5 | time: 0.006543397903442383s | iteractions: 50 | solutions: 8
graph31.txt | mininum cut: 9 | time: 0.011481046676635742s | iteractions: 50 | solutions: 8
graph32.txt | mininum cut: 0 | time: 0.003416299819946289s | iteractions: 82 | solutions: 16
graph33.txt | mininum cut: 1 | time: 0.005186796188354492s | iteractions: 82 | solutions: 16
graph34.txt | mininum cut: 4 | time: 0.013187170028686523s | iteractions: 82 | solutions: 16
graph35.txt | mininum cut: 9 | time: 0.019832849502563477s | iteractions: 82 | solutions: 16
graph36.txt | mininum cut: 1 | time: 0.004253387451171875s | iteractions: 98 | solutions: 16
graph37.txt | mininum cut: 1 | time: 0.0066797733306884766s | iteractions: 98 | solutions: 16
graph38.txt | mininum cut: 5 | time: 0.02206134796142578s | iteractions: 98 | solutions: 16
graph39.txt | mininum cut: 10 | time: 0.03215932846069336s | iteractions: 98 | solutions: 16
graph40.txt | mininum cut: 0 | time: 0.00422358512878418s | iteractions: 83 | solutions: 16
graph41.txt | mininum cut: 1 | time: 0.006443023681640625s | iteractions: 99 | solutions: 16
graph42.txt | mininum cut: 6 | time: 0.017370939254760742s | iteractions: 99 | solutions: 16
graph43.txt | mininum cut: 10 | time: 0.04218554496765137s | iteractions: 99 | solutions: 16
graph44.txt | mininum cut: 1 | time: 0.0044422149658203125s | iteractions: 101 | solutions: 16
graph45.txt | mininum cut: 3 | time: 0.01342010498046875s | iteractions: 101 | solutions: 16
graph46.txt | mininum cut: 5 | time: 0.024988412857055664s | iteractions: 101 | solutions: 16
graph47.txt | mininum cut: 12 | time: 0.07045912742614746s | iteractions: 101 | solutions: 16
graph48.txt | mininum cut: 1 | time: 0.011507511138916016s | iteractions: 105 | solutions: 16
graph49.txt | mininum cut: 3 | time: 0.009818792343139648s | iteractions: 105 | solutions: 16
graph50.txt | mininum cut: 7 | time: 0.02395796775817871s | iteractions: 105 | solutions: 16
graph51.txt | mininum cut: 12 | time: 0.060060739517211914s | iteractions: 105 | solutions: 16
graph52.txt | mininum cut: 1 | time: 0.00507354736328125s | iteractions: 106 | solutions: 16
graph53.txt | mininum cut: 2 | time: 0.010922908782958984s | iteractions: 106 | solutions: 16
graph54.txt | mininum cut: 6 | time: 0.028751850128173828s | iteractions: 106 | solutions: 16
graph55.txt | mininum cut: 12 | time: 0.06178092956542969s | iteractions: 106 | solutions: 16
graph56.txt | mininum cut: 1 | time: 0.009864330291748047s | iteractions: 170 | solutions: 32
graph57.txt | mininum cut: 2 | time: 0.019798994064331055s | iteractions: 170 | solutions: 32
graph58.txt | mininum cut: 7 | time: 0.05848979949951172s | iteractions: 170 | solutions: 32
graph59.txt | mininum cut: 13 | time: 0.09930634498596191s | iteractions: 170 | solutions: 32
graph60.txt | mininum cut: 1 | time: 0.012633562088012695s | iteractions: 202 | solutions: 32
graph61.txt | mininum cut: 2 | time: 0.024327516555786133s | iteractions: 202 | solutions: 32
graph62.txt | mininum cut: 7 | time: 0.06321978569030762s | iteractions: 202 | solutions: 32
graph63.txt | mininum cut: 12 | time: 0.2317502498626709s | iteractions: 202 | solutions: 32
graph64.txt | mininum cut: 1 | time: 0.012076377868652344s | iteractions: 203 | solutions: 32
graph65.txt | mininum cut: 2 | time: 0.02817678451538086s | iteractions: 203 | solutions: 32
graph66.txt | mininum cut: 8 | time: 0.08126258850097656s | iteractions: 203 | solutions: 32
graph67.txt | mininum cut: 13 | time: 0.1868581771850586s | iteractions: 203 | solutions: 32
graph68.txt | mininum cut: 1 | time: 0.019266366958618164s | iteractions: 205 | solutions: 32
graph69.txt | mininum cut: 3 | time: 0.03314328193664551s | iteractions: 205 | solutions: 32
graph70.txt | mininum cut: 6 | time: 0.07798457145690918s | iteractions: 205 | solutions: 32
graph71.txt | mininum cut: 14 | time: 0.15599822998046875s | iteractions: 205 | solutions: 32
graph72.txt | mininum cut: 1 | time: 0.014679908752441406s | iteractions: 209 | solutions: 32
graph73.txt | mininum cut: 4 | time: 0.03381681442260742s | iteractions: 209 | solutions: 32
graph74.txt | mininum cut: 9 | time: 0.10264253616333008s | iteractions: 209 | solutions: 32
graph75.txt | mininum cut: 15 | time: 0.2171952724456787s | iteractions: 209 | solutions: 32
graph76.txt | mininum cut: 1 | time: 0.014922857284545898s | iteractions: 217 | solutions: 32
graph77.txt | mininum cut: 2 | time: 0.03660917282104492s | iteractions: 217 | solutions: 32
graph78.txt | mininum cut: 7 | time: 0.12104249000549316s | iteractions: 217 | solutions: 32
graph79.txt | mininum cut: 16 | time: 0.24744009971618652s | iteractions: 217 | solutions: 32
graph80.txt | mininum cut: 2 | time: 0.016460180282592773s | iteractions: 218 | solutions: 32
graph81.txt | mininum cut: 3 | time: 0.039759159088134766s | iteractions: 218 | solutions: 32
graph82.txt | mininum cut: 8 | time: 0.13535571098327637s | iteractions: 218 | solutions: 32
graph83.txt | mininum cut: 15 | time: 0.2987818717956543s | iteractions: 218 | solutions: 32
graph84.txt | mininum cut: 2 | time: 0.02583622932434082s | iteractions: 220 | solutions: 32
graph85.txt | mininum cut: 4 | time: 0.04799532890319824s | iteractions: 220 | solutions: 32
graph86.txt | mininum cut: 11 | time: 0.1688985824584961s | iteractions: 220 | solutions: 32
graph87.txt | mininum cut: 17 | time: 0.3195018768310547s | iteractions: 220 | solutions: 32
graph88.txt | mininum cut: 1 | time: 0.029517412185668945s | iteractions: 348 | solutions: 64
graph89.txt | mininum cut: 2 | time: 0.07997345924377441s | iteractions: 348 | solutions: 64
graph90.txt | mininum cut: 9 | time: 0.23902583122253418s | iteractions: 348 | solutions: 64
graph91.txt | mininum cut: 17 | time: 0.5006623268127441s | iteractions: 348 | solutions: 64
graph92.txt | mininum cut: 0 | time: 0.03142809867858887s | iteractions: 349 | solutions: 64
graph93.txt | mininum cut: 4 | time: 0.08665275573730469s | iteractions: 349 | solutions: 64
graph94.txt | mininum cut: 9 | time: 0.23703646659851074s | iteractions: 349 | solutions: 64
graph95.txt | mininum cut: 17 | time: 0.6139860153198242s | iteractions: 349 | solutions: 64
graph96.txt | mininum cut: 1 | time: 0.043242454528808594s | iteractions: 413 | solutions: 64
graph97.txt | mininum cut: 3 | time: 0.1186678409576416s | iteractions: 413 | solutions: 64
graph98.txt | mininum cut: 11 | time: 0.38959455490112305s | iteractions: 413 | solutions: 64
graph99.txt | mininum cut: 18 | time: 0.7143590450286865s | iteractions: 413 | solutions: 64
graph100.txt | mininum cut: 2 | time: 0.054913997650146484s | iteractions: 415 | solutions: 64
graph101.txt | mininum cut: 3 | time: 0.13466167449951172s | iteractions: 415 | solutions: 64
graph102.txt | mininum cut: 10 | time: 0.4692082405090332s | iteractions: 415 | solutions: 64
graph103.txt | mininum cut: 19 | time: 0.9946043491363525s | iteractions: 415 | solutions: 64
graph104.txt | mininum cut: 2 | time: 0.05605340003967285s | iteractions: 419 | solutions: 64
graph105.txt | mininum cut: 4 | time: 0.13247084617614746s | iteractions: 419 | solutions: 64
graph106.txt | mininum cut: 9 | time: 0.4314079284667969s | iteractions: 419 | solutions: 64
graph107.txt | mininum cut: 21 | time: 0.9994933605194092s | iteractions: 419 | solutions: 64
graph108.txt | mininum cut: 1 | time: 0.05544638633728027s | iteractions: 420 | solutions: 64
graph109.txt | mininum cut: 2 | time: 0.1277475357055664s | iteractions: 420 | solutions: 64
graph110.txt | mininum cut: 12 | time: 0.48888134956359863s | iteractions: 420 | solutions: 64
graph111.txt | mininum cut: 18 | time: 1.0461030006408691s | iteractions: 420 | solutions: 64
graph112.txt | mininum cut: 2 | time: 0.0599362850189209s | iteractions: 428 | solutions: 64
graph113.txt | mininum cut: 5 | time: 0.17735981941223145s | iteractions: 428 | solutions: 64
graph114.txt | mininum cut: 12 | time: 0.55478835105896s | iteractions: 428 | solutions: 64
graph115.txt | mininum cut: 22 | time: 1.075563907623291s | iteractions: 428 | solutions: 64
graph116.txt | mininum cut: 2 | time: 0.05864882469177246s | iteractions: 444 | solutions: 64
graph117.txt | mininum cut: 3 | time: 0.20755815505981445s | iteractions: 444 | solutions: 64
graph118.txt | mininum cut: 10 | time: 0.6497223377227783s | iteractions: 444 | solutions: 64
graph119.txt | mininum cut: 22 | time: 1.287036418914795s | iteractions: 444 | solutions: 64
graph120.txt | mininum cut: 1 | time: 0.06673765182495117s | iteractions: 445 | solutions: 64
graph121.txt | mininum cut: 3 | time: 0.1898515224456787s | iteractions: 445 | solutions: 64
graph122.txt | mininum cut: 12 | time: 0.7223460674285889s | iteractions: 445 | solutions: 64
graph123.txt | mininum cut: 20 | time: 1.4997992515563965s | iteractions: 445 | solutions: 64
graph124.txt | mininum cut: 1 | time: 0.07190918922424316s | iteractions: 447 | solutions: 64
graph125.txt | mininum cut: 4 | time: 0.18184638023376465s | iteractions: 447 | solutions: 64
graph126.txt | mininum cut: 15 | time: 0.8098776340484619s | iteractions: 447 | solutions: 64
graph127.txt | mininum cut: 24 | time: 1.5100102424621582s | iteractions: 447 | solutions: 64
graph128.txt | mininum cut: 2 | time: 0.07523012161254883s | iteractions: 451 | solutions: 64
graph129.txt | mininum cut: 5 | time: 0.26910924911499023s | iteractions: 451 | solutions: 64
graph130.txt | mininum cut: 15 | time: 0.991302490234375s | iteractions: 451 | solutions: 64
graph131.txt | mininum cut: 21 | time: 1.834928274154663s | iteractions: 451 | solutions: 64
graph132.txt | mininum cut: 1 | time: 0.07639575004577637s | iteractions: 452 | solutions: 64
graph133.txt | mininum cut: 4 | time: 0.23333978652954102s | iteractions: 452 | solutions: 64
graph134.txt | mininum cut: 13 | time: 1.5417282581329346s | iteractions: 452 | solutions: 64
graph135.txt | mininum cut: 27 | time: 2.6825177669525146s | iteractions: 452 | solutions: 64
graph136.txt | mininum cut: 2 | time: 0.17681431770324707s | iteractions: 708 | solutions: 128
graph137.txt | mininum cut: 5 | time: 0.39829015731811523s | iteractions: 708 | solutions: 128
graph138.txt | mininum cut: 12 | time: 1.4664580821990967s | iteractions: 708 | solutions: 128
graph139.txt | mininum cut: 24 | time: 3.522916555404663s | iteractions: 708 | solutions: 128
graph140.txt | mininum cut: 2 | time: 0.17907977104187012s | iteractions: 710 | solutions: 128
graph141.txt | mininum cut: 6 | time: 0.42992615699768066s | iteractions: 710 | solutions: 128
graph142.txt | mininum cut: 16 | time: 1.503622055053711s | iteractions: 710 | solutions: 128
graph143.txt | mininum cut: 27 | time: 3.667776107788086s | iteractions: 710 | solutions: 128
graph144.txt | mininum cut: 2 | time: 0.1764669418334961s | iteractions: 838 | solutions: 128
graph145.txt | mininum cut: 6 | time: 0.6643049716949463s | iteractions: 838 | solutions: 128
graph146.txt | mininum cut: 14 | time: 1.6646645069122314s | iteractions: 838 | solutions: 128
graph147.txt | mininum cut: 29 | time: 4.54273533821106s | iteractions: 838 | solutions: 128
graph148.txt | mininum cut: 2 | time: 0.17838239669799805s | iteractions: 839 | solutions: 128
graph149.txt | mininum cut: 5 | time: 0.5350778102874756s | iteractions: 839 | solutions: 128
graph150.txt | mininum cut: 15 | time: 1.9870378971099854s | iteractions: 839 | solutions: 128
graph151.txt | mininum cut: 30 | time: 4.995828628540039s | iteractions: 839 | solutions: 128
graph152.txt | mininum cut: 2 | time: 0.2030348777770996s | iteractions: 843 | solutions: 128
graph153.txt | mininum cut: 5 | time: 0.4917151927947998s | iteractions: 843 | solutions: 128
graph154.txt | mininum cut: 17 | time: 2.0848121643066406s | iteractions: 843 | solutions: 128
graph155.txt | mininum cut: 30 | time: 5.054779767990112s | iteractions: 843 | solutions: 128
graph156.txt | mininum cut: 2 | time: 0.19460129737854004s | iteractions: 851 | solutions: 128
graph157.txt | mininum cut: 6 | time: 0.624345064163208s | iteractions: 851 | solutions: 128
graph158.txt | mininum cut: 18 | time: 2.737319231033325s | iteractions: 851 | solutions: 128
graph159.txt | mininum cut: 31 | time: 5.094897508621216s | iteractions: 851 | solutions: 128
graph160.txt | mininum cut: 2 | time: 0.20389699935913086s | iteractions: 852 | solutions: 128
graph161.txt | mininum cut: 5 | time: 0.5421247482299805s | iteractions: 852 | solutions: 128
graph162.txt | mininum cut: 16 | time: 2.1551461219787598s | iteractions: 852 | solutions: 128
graph163.txt | mininum cut: 28 | time: 6.247256755828857s | iteractions: 852 | solutions: 128
graph164.txt | mininum cut: 3 | time: 0.24750661849975586s | iteractions: 854 | solutions: 128
graph165.txt | mininum cut: 6 | time: 0.6693956851959229s | iteractions: 854 | solutions: 128
graph166.txt | mininum cut: 16 | time: 2.5490384101867676s | iteractions: 854 | solutions: 128
graph167.txt | mininum cut: 29 | time: 6.359643220901489s | iteractions: 854 | solutions: 128

Total Execution Time = 89.9937162399292s
```


### References

* https://web.stanford.edu/class/archive/cs/cs161/cs161.1138/lectures/11/Small11.pdf 
* https://www.geeksforgeeks.org/kargers-algorithm-for-minimum-cut-set-1-introduction-and-implementation/ 
* https://en.wikipedia.org/wiki/Karger%27s_algorithm 
* https://slideplayer.com/slide/15146715/ 
