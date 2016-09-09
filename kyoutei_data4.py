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

