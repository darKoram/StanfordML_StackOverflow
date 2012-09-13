import os.path

data_path = "/home/kesten/VCP/Git/ML/StackExchangeClosureChallenge/data"
file_name = "train-sample.csv"
output_file = "short_sample.csv"

with open(os.path.join(data_path, file_name)) as myfile:
    f = open(os.path.join(data_path, output_file), 'w+')
    head=[myfile.next() for x in xrange(13)]
    #for i in range(13):
        #f.write(head[i])
        #print head[i]
    f.close()
    print head
