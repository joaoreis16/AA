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
* the generated graphs are in the folder `/graphs`
* some graphs about the results are in the folder `/plots`


### References

* https://web.stanford.edu/class/archive/cs/cs161/cs161.1138/lectures/11/Small11.pdf 
* https://www.geeksforgeeks.org/kargers-algorithm-for-minimum-cut-set-1-introduction-and-implementation/ 
* https://en.wikipedia.org/wiki/Karger%27s_algorithm 
