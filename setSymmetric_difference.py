# 21/12/2020 symmetricDiffrence
# symmetricDiffrence iki ayrı set de A da olup Bde olmayanlar ile B de olup A da olmayanları almamızı sağlar.

setA = {1,2,3,4,5}
setB = {3,4,5,7}

print(setA ^ setB)
print(setA.symmetric_difference(setB))
print(setB.symmetric_difference(setA))
