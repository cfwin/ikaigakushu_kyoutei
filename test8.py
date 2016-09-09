# -*- coding: utf-8 -*-
#2048
import tensorflow as tf
import kyoutei_data4
from numpy.random import *

# from tensorflow.examples.tutorials.mnist import input_data



input1=kyoutei_data4.inputdata_set()
output_sv1=kyoutei_data4.outputdata_set()

# mnist = input_data.read_data_sets("/Users/ryuichi/python_program/tensor1/MNIST_data/", one_hot=True)


n1=len(input1[1]) #inputデータの要素の数
n2=len(output_sv1[1]) #output_svのデータの要素の数



print "inputのデータの個数(行)　output_svのデータの個数(行)　inputのデータの要素の個数　output_svのデータの要素の個数"
print len(input1),len(output_sv1),n1,n2

print "softmax  cross_entropy  500000  0.00005"

# 予想に必要なデータのみ引っ張ってくる!!!!!!!!
# for k in range(6)
#     for i in range(n1):
#         for j in range(6):
#             if j==0 or j==4 or j==8 or j==12 or j==16 or j==20:



  #   1 3336 斌　疲　　垢　皇 48   53    6.75   1    0.14     1.50.8
  # 02  3 4110 井　叻　　下　涕 44   45    6.78   3    0.20     1.52.1
  # 03  4 4117 注　面　　靡加搬 34   66    6.81   4    0.21     1.52.9
  # 04  5 2969 底　拍　　赖　啦 75   69    6.86   5    0.22     1.54.7
  # 05  2 3299 澎　犊　　啦　叁 47   52    6.81   2    0.17     1.55.7
  # 06  6 4830 尽　唆　　　　葫 65


# print input1
# print output_sv1
# print input1[4]


x = tf.placeholder(tf.float32, [None, n1])
W = tf.Variable(tf.zeros([n1, n2]))
b = tf.Variable(tf.zeros([n2]))

# y = tf.nn.tanh(tf.matmul(x, W)+b)
# y = tf.nn.sigmoid(tf.matmul(x, W)+b)
y = tf.nn.softmax(tf.matmul(x, W)+b)
# y = tf.matmul(x, W)+b

y_ = tf.placeholder(tf.float32, [None, n2])


# 誤差をcross_entropyの代わりにerror_funcを用いた
# cross_entropy = tf.reduce_mean(tf.reduce_sum((y_-y)*(y_-y))/2.0)
# cross_entropy = -tf.reduce_sum(y_ * tf.log(y))
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))
# cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y)))
# objective_func = tf.reduce_mean(tf.reduce_sum(tf.log(1+tf.exp(-y_*y))))


# train_step = tf.train.GradientDescentOptimizer(0.001).minimize(energy_func)
# train_step = tf.train.GradientDescentOptimizer(0.0001).minimize(objective_func)
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)


init = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init)

# print input1


feed_dict={x: input1, y_: output_sv1}


kaisu=30000
batch_xs=[0]*100
batch_ys=[0]*100

for step in range(kaisu):
    # sess.run(train_step, feed_dict=feed_dict)

    #ランダムに選ぶ
    for j in range(100):
        ransu = int (rand() * len(input1))
        # ransu = int (rand() * 30)
        batch_xs[j] = input1[ransu]
        batch_ys[j] = output_sv1[ransu]

    # feed_dict = {x: batch_xs, y_: batch_ys}

    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

    # print batch_xs

    if step % 100 == 0:
        # print sess.run(error_func, feed_dict=feed_dict)
        print str(step)+" "+str(sess.run(cross_entropy, feed_dict=feed_dict))
        # print str(step)+" "+str(sess.run(objective_func, feed_dict=feed_dict))
        # print sess.run(y, feed_dict=feed_dict)

        if step == kaisu-1:
            print sess.run(W, feed_dict=feed_dict)
        # print sess.run(b, feed_dict=feed_dict)
        # print sess.run(W, feed_dict=feed_dict)





#評価を行い教師信号と一致するか確認
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
#制度を求める
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
# accuracy = tf.reduce_mean(tf.cast(tf.equal(tf.argmax(y,1), tf.argmax(y_,1)), tf.float32))
print sess.run(correct_prediction, feed_dict={x: input1, y_: output_sv1})
print sess.run(accuracy, feed_dict={x: input1, y_: output_sv1})


#cast 四捨五入
# argmax 一番大きいやつ
# equal(x, y)　xとyがイコールがどうか bool型のテンソルを返す
# reduce_mean　横断要素の平均 dtype=tf.float32
#
# sess.run(fetches, feed_dict=None)
#         fetches　単一のグラフ要素、グラフ要素のリスト、またはその値がグラフ要素またはグラフ要素（前述）のリストである辞書を。
#         feed_dict　(前述）の値にグラフ要素をマッピングする辞​​書。



# 0.452421
