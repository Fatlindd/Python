
# DSPAM_Confidence checks how many lines is whith text X-DSPAM-Confidence: 
# getFloatNumber get float numbers in lines of file and calculate the total sum
# The readlines() method in Python is used to read all the lines from a file 
# and return them as a list of strings.

def averageSpamConfidence(file):
    with open(file, 'rt') as f:
        lines = f.readlines()

    DSPAM_Confidence = 0
    getFloatNumber = 0
    for line in lines:
        if line.startswith('X-DSPAM-Confidence: '):
            checkForFloatNumber = line[20:26]
            getFloatNumber = getFloatNumber + float(checkForFloatNumber)
            DSPAM_Confidence += 1
    print(f'Average of spam confidence: {getFloatNumber / DSPAM_Confidence}')

# file_name = 'Files/mbox-short.txt'
file_name = input('> Your file name: ')
averageSpamConfidence(file_name)