import os

train_mix_scp = './data/2spk/train/mix.scp'
train_s1_scp = './data/2spk/train/spk1.scp'
train_s2_scp = './data/2spk/train/spk2.scp'

test_mix_scp = './data/2spk/dev/mix.scp'
test_s1_scp = './data/2spk/dev/spk1.scp'
test_s2_scp = './data/2spk/dev/spk2.scp'

cv_mix_scp = './data/2spk/tt/mix.scp'
cv_s1_scp = './data/2spk/tt/spk1.scp'
cv_s2_scp = './data/2spk/tt/spk2.scp'

debug_mix_scp = './data/tune/mix.scp'
debug_s1_scp = './data/tune/spk1.scp'
debug_s2_scp = './data/tune/spk2.scp'

os.makedirs(train_mix_scp.replace('mix.scp', ''), exist_ok=True)
os.makedirs(test_mix_scp.replace('mix.scp', ''), exist_ok=True)
os.makedirs(cv_mix_scp.replace('mix.scp', ''), exist_ok=True)
os.makedirs(debug_mix_scp.replace('mix.scp', ''), exist_ok=True)

train_mix = 'D:/WSJ/wsj0-mix4/2speakers/wav16k/min/tr/mix'
train_s1 = 'D:/WSJ/wsj0-mix4/2speakers/wav16k/min/tr/s1'
train_s2 = 'D:/WSJ/wsj0-mix4/2speakers/wav16k/min/tr/s2'

test_mix = 'D:/WSJ/wsj0-mix4/2speakers/wav16k/min/tt/mix'
test_s1 = 'D:/WSJ/wsj0-mix4/2speakers/wav16k/min/tt/s1'
test_s2 = 'D:/WSJ/wsj0-mix4/2speakers/wav16k/min/tt/s2'

cv_mix = 'D:/WSJ/wsj0-mix4/2speakers/wav16k/min/cv/mix'
cv_s1 = 'D:/WSJ/wsj0-mix4/2speakers/wav16k/min/cv/s1'
cv_s2 = 'D:/WSJ/wsj0-mix4/2speakers/wav16k/min/cv/s2'

tr_mix = open(train_mix_scp, 'w')
for root, dirs, files in os.walk(train_mix):
    files.sort()
    for file in files:
        tr_mix.write(file + " " + root + '/' + file)
        tr_mix.write('\n')

tr_s1 = open(train_s1_scp, 'w')
for root, dirs, files in os.walk(train_s1):
    files.sort()
    for file in files:
        tr_s1.write(file + " " + root + '/' + file)
        tr_s1.write('\n')

tr_s2 = open(train_s2_scp, 'w')
for root, dirs, files in os.walk(train_s2):
    files.sort()
    for file in files:
        tr_s2.write(file + " " + root + '/' + file)
        tr_s2.write('\n')

tt_mix = open(test_mix_scp, 'w')
for root, dirs, files in os.walk(test_mix):
    files.sort()
    for file in files:
        tt_mix.write(file + " " + root + '/' + file)
        tt_mix.write('\n')

tt_s1 = open(test_s1_scp, 'w')
for root, dirs, files in os.walk(test_s1):
    files.sort()
    for file in files:
        tt_s1.write(file + " " + root + '/' + file)
        tt_s1.write('\n')

tt_s2 = open(test_s2_scp, 'w')
for root, dirs, files in os.walk(test_s2):
    files.sort()
    for file in files:
        tt_s2.write(file + " " + root + '/' + file)
        tt_s2.write('\n')

cv_mix_file = open(cv_mix_scp, 'w')
for root, dirs, files in os.walk(cv_mix):
    files.sort()
    for file in files:
        cv_mix_file.write(file + " " + root + '/' + file)
        cv_mix_file.write('\n')

cv_s1_file = open(cv_s1_scp, 'w')
for root, dirs, files in os.walk(cv_s1):
    files.sort()
    for file in files:
        cv_s1_file.write(file + " " + root + '/' + file)
        cv_s1_file.write('\n')

cv_s2_file = open(cv_s2_scp, 'w')
for root, dirs, files in os.walk(cv_s2):
    files.sort()
    for file in files:
        cv_s2_file.write(file + " " + root + '/' + file)
        cv_s2_file.write('\n')

de_mix = open(debug_mix_scp, 'w')
for root, dirs, files in os.walk(train_mix):
    files.sort()
    for idx, file in enumerate(files):
        de_mix.write(file + " " + root + '/' + file)
        de_mix.write('\n')
        if idx > 10:
            break

de_s1 = open(debug_s1_scp, 'w')
for root, dirs, files in os.walk(train_s1):
    files.sort()
    for idx, file in enumerate(files):
        de_s1.write(file + " " + root + '/' + file)
        de_s1.write('\n')
        if idx > 10:
            break

de_s2 = open(debug_s2_scp, 'w')
for root, dirs, files in os.walk(train_s2):
    files.sort()
    for idx, file in enumerate(files):
        de_s2.write(file + " " + root + '/' + file)
        de_s2.write('\n')
        if idx > 10:
            break