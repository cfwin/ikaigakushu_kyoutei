# -*- coding: utf-8 -*-

#テキストから読み込む行数を変えるのに変数をおいた。
aaa=0
def inputdata_set():

    input1=[[]]
    f = open("input_kyoutei.txt","r")
    list1 = f.readlines()
    f.close()
    # print list1
    print len(list1)

    #配列の箱の確保。最後の要素は[]となってしまうため、箱の生成はデータの要素の個数より1つだけ小さくする
    for i in range(len(list1)-1-aaa):
        input1.append([])

    #inputデータの格納
    for i in range(len(list1)-aaa):
        a=list1[i].split(',')

        # テキストデータをそのまま読み込むならこれ。値が大きいのは小さくしよう
        # for j in range(len(a)-1):
        #     if float(a[j])>1000:
        #         input1[i].append(float(a[j])/100.0)
        #         # print float(a[j])/100.0,
        #     elif float(a[j])>100:
        #         input1[i].append(float(a[j])/10.0)
        #     elif float(a[j])>10:
        #         input1[i].append(float(a[j]))
        #     elif float(a[j])>1:
        #         input1[i].append(float(a[j])*10.0)
        #     else:
        #         input1[i].append(float(a[j])*100.0)


                # print a[j],
        #テキストのデータを2進数に変換して読み込むならこっち。zfill()で文字数を変える
        for j in range(len(a)-1):

            if j==0 or j==4 or j==8 or j==12 or j==16 or j==20:
            # print a[j]
                # print int(float(a[j]))

                bin_list = list(format(int(float(a[j])),'b').zfill(13))
                # print a[j]
                for k in range(len(bin_list)):
                    input1[i].append(int(bin_list[k]))
                    print bin_list[k],


            elif j==3 or j==7 or j==11 or j==15 or j==19 or j==23:
                st=int(float(a[j])*100)

                bin_list = list(format(st,'b').zfill(10))
                # print a[j]
                for k in range(len(bin_list)):
                    input1[i].append(st)
                    print bin_list[k],

                                        # print "ssssssssssssssss",
# 0 4 8  12 16 20
# 1 5 9  13 17 21
# 2 6 10 14 18 22
            else:
                bin_list = list(format(int(float(a[j])),'b').zfill(7))
                for k in range(len(bin_list)):
                    input1[i].append(int(bin_list[k]))
                    # print "ddddddddddddddd",
                    print bin_list[k],
        print ""







            #テキストのデータを2進数に変換して読み込むならこっち。zfill()で文字数を変える
            #
            # if j==0 or j % 3==0:
            #     bin_list = list(format(int(a[j]),'b').zfill(13))
            #     for k in range(len(bin_list)):
            #         input1[i].append(int(bin_list[k]))
            #         print bin_list[k],
            #
            # # elif  j==1 or j==4 or j==7 or j==10 or j==13 or j==16:
            # #     bin_list = list(format(int(a[j]),'b').zfill(7))
            # #     for k in range(len(bin_list)):
            # #         input1[i].append(int(bin_list[k]))
            # #         print bin_list[k],
            #
            # else:
            #     bin_list = list(format(int(a[j]),'b').zfill(7))
            #     for k in range(len(bin_list)):
            #         input1[i].append(int(bin_list[k]))
            #         print bin_list[k],



    print input1
    # print len(a)

    return input1

# #input,outputのデータの読み込み
# f1 = open("kyoutei_input.txt","r")
# list1 = f1.readlines()
# f1.close()

def outputdata_set():

    output1=[[]]

    f = open("output_sv_kyoutei.txt","r")
    list2 = f.readlines()
    f.close()
    # print len(list2)

    # print len(list2)
    #配列の箱の確保。最後の要素は[]となってしまうため、箱の生成はデータの要素の個数より1つだけ小さくする
    for i in range(len(list2)-1-aaa):
        output1.append([])

    #outputデータの格納
    for i in range(len(list2)-aaa):
        a=list2[i].split(',')
        for j in range(len(a)-1): #最後が0で埋まっているなら-1する
            if a[j]=="1":
                output1[i].append(float(1))
            else:
                output1[i].append(float(0))
    print "aaaaaaaaaaaaaaaaa"
    print len(list2[5])
    print output1[1]
    print a


    print output1
    return output1

# def inputdata_set():
#     input1=[
# [4137,13,16,4153,70,72,4847,39,45,4875,45,19,3269,35,73,4186,41,71],
# [3620,44,68,3346,52,15,3463,24,35,4787,32,56,3891,64,63,4880,25,61],
# [4271,36,62,4700,74,24,4104,42,66,4561,19,57,3798,15,75,3459,26,50],
# [4311,47,58,4732,54,20,2887,53,34,4709,11,43,3726,68,65,3797,71,25],
# [3858,55,40,4581,66,17,4184,34,29,3493,27,60,3419,21,14,3866,63,37],
# [4760,40,42,3269,35,73,3662,14,12,3660,18,13,4815,37,36,4862,20,74],
# [3942,22,67,4847,39,45,4759,72,46,3620,44,68,4757,30,69,4561,19,57],
# [3327,23,54,4732,54,20,4177,62,64,3891,64,63,4875,45,19,4677,12,59],
# [3903,51,70,4271,36,62,3684,48,18,4153,70,72,3797,71,25,4880,25,61],
# [4581,66,17,4759,72,46,4209,31,26,4009,56,38,3798,15,75,4787,32,56],
# ]
#     return input1
#
# def outputdata_set():
#     output1=[
# [4,2,6,5,1,3],
# [1,5,2,3,4,6],
# [4,1,2,5,6,3],
# [5,1,2,3,4,6],
# [1,2,3,6,5,4],
# [2,3,1,4,5,6],
# [2,5,1,4,3,6],
# [1,4,5,2,6,3],
# [6,2,1,3,4,5],
# [1,4,2,6,3,5],
# ]
#     return output1
