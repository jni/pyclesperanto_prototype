import clesperanto as cle
import numpy as np


test = cle.push(np.asarray([
[1, 1, 1],
[1, 2, 1],
[1, 1, 1]
]))

test2 = cle.create(test)
cle.maximum_sphere(test, test2, 1, 1, 1)

#print("B test")
#print(cle.pull(test))

#print("B test2")
#print(cle.pull(test2))

a = cle.pull(test2)
assert (np.min(a) == 1)
assert (np.max(a) == 2)


cle.set(test, 5)
#print(test)
#print(cle.pull(test))

a = cle.pull(test)
assert (np.min(a) == 5)
assert (np.max(a) == 5)
assert (np.mean(a) == 5)

print ("ok maximum sphere")

test = cle.push(np.asarray([
    [1, -1],
    [1, -1]
]))

test2 = cle.create(test)
cle.absolute(test, test2)

print(test2)

a = cle.pull(test2)
assert (np.min(a) == 1)
assert (np.max(a) == 1)
assert (np.mean(a) == 1)
print ("ok absolute")




test = cle.push(np.asarray([
    [1, 0],
    [1, 0]
]))

test1 = cle.push(np.asarray([
    [1, 1],
    [0, 0]
]))

test2 = cle.create(test)
cle.binary_and(test, test1, test2)

print(test2)

a = cle.pull(test2)
assert (np.min(a) == 0)
assert (np.max(a) == 1)
assert (np.mean(a) == 0.25)
print ("ok binary_and")




test1 = cle.push(np.asarray([
    [1, 1],
    [1, 0]
]))

test2 = cle.create(test1)
cle.binary_not(test1, test2)

print(test2)
a = cle.pull(test2)
assert (np.min(a) == 0)
assert (np.max(a) == 1)
assert (np.mean(a) == 0.25)
print ("ok binary_not")






test1 = cle.push(np.asarray([
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0]
]))

test2 = cle.create(test1)
cle.binary_edge_detection(test1, test2)

print(test2)
a = cle.pull(test2)
assert (np.min(a) == 0)
assert (np.max(a) == 1)
assert (np.mean(a) - 12 / 36 < 0.001)
print ("ok binary_edge_detection")













test = cle.push(np.asarray([
    [1, 0],
    [1, 0]
]))

test1 = cle.push(np.asarray([
    [1, 1],
    [0, 0]
]))

test2 = cle.create(test)
cle.binary_or(test, test1, test2)

print(test2)

a = cle.pull(test2)
assert (np.min(a) == 0)
assert (np.max(a) == 1)
assert (np.mean(a) == 0.75)
print ("ok binary_or")









test = cle.push(np.asarray([
    [1, 0],
    [1, 0]
]))

test1 = cle.push(np.asarray([
    [1, 1],
    [0, 0]
]))

test2 = cle.create(test)
cle.binary_subtract(test, test1, test2)

print(test2)

a = cle.pull(test2)
assert (np.min(a) == 0)
assert (np.max(a) == 1)
assert (np.mean(a) == 0.25)
print ("ok binary_subtract")


test = cle.push(np.asarray([
    [1, 0],
    [1, 0]
]))

test1 = cle.push(np.asarray([
    [1, 1],
    [0, 0]
]))

test2 = cle.create(test)
cle.binary_xor(test, test1, test2)

print(test2)

a = cle.pull(test2)
assert (np.min(a) == 0)
assert (np.max(a) == 1)
assert (np.mean(a) == 0.5)
print ("ok binary_xor")




test = cle.push(np.asarray([
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]))

test1 = cle.push(np.asarray([
    [0, 1, 0],
    [1, 2, 1],
    [0, 1, 0]
]))

test2 = cle.create(test)
cle.convolve(test, test1, test2)

print(test2)

a = cle.pull(test1)
b = cle.pull(test2)
assert (np.min(a) == np.min(b))
assert (np.max(a) == np.max(b))
assert (np.mean(a) == np.mean(b))
print ("ok convolve")












test1 = cle.push(np.asarray([
    [1, 1],
    [1, 0]
]))

test2 = cle.create(test1)
cle.copy(test1, test2)

print(test2)
a = cle.pull(test2)
assert (np.min(a) == 0)
assert (np.max(a) == 1)
assert (np.mean(a) == 0.75)
print ("ok copy")




test1 = cle.push(np.asarray([
    [
        [1, 4],
        [0, 4]
    ],
    [
        [1, 3],
        [1, 2]
    ]
]))

test2 = cle.create((2, 2))
cle.copy_slice(test1, test2, 0)

print(test2)
a = cle.pull(test2)
assert (np.min(a) == 0)
assert (np.max(a) == 1)
assert (np.mean(a) == 0.75)
print ("ok copy slice from 3d")



test1 = cle.push(np.asarray([
        [4, 4],
        [4, 4]
]))

test2 = cle.create((2, 2, 2))
cle.set(test2, 0)
cle.copy_slice(test1, test2, 0)

print(test2)
a = cle.pull(test2)
assert (np.min(a) == 0)
assert (np.max(a) == 4)
assert (np.mean(a) == 2)
print ("ok copy slice to 3d")




