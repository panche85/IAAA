'''
Fajlot se koristi za testiranje na kod (probi so tensorflow)
'''
from __future__ import print_function

import tensorflow as tf

c = tf.constant(3.14)

with tf.Session() as sess:
    print("test code")
    print("testing: %d" % sess.run(c+12))

# definirash kostruckija prvo
v1 = tf.placeholder(tf.int32)
v2 = tf.placeholder(tf.int32)

res = tf.mul(v1,v2)

# tuka se povikuva operacijata (ekvivalentno na povik na funkcija - startuvash sesija)
with tf.Session() as ime_sesija:
    print("Tuka se izvrshuva operacijata so parametri: %d" % ime_sesija.run(res, feed_dict={v1: 24, v2: 8}))
