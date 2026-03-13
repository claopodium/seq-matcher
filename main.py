import argparse

def NW(seq1:str, seq2:str):
    l1 = len(seq1)
    l2 = len(seq2)
    mtx = []
    label = []
    result = []

# Build the Matrix
    for i in range(l2+1):
        mtx.append([0]*(l1+1))
        label.append([[] for _ in range(l1+1)])
    for i in range(1,l1+1):
        mtx[0][i] = -i
    for i in range(1,l2+1):
        mtx[i][0] = -i

# calculate and label
    for i in range(1, l2+1):
        for j in range(1, l1+1):
            mtx[i][j] = step(mtx, label, i, j, seq1, seq2)

# backtrack
    record = []
    track(seq1, seq2, l2, l1, label, record)

def step(matrix:list, label:list, i:int, j:int, seq1:str, seq2:str):
    score_left = matrix[i][j-1]-1
    score_up = matrix[i-1][j]-1
    if (seq2[i-1] == seq1[j-1]):
        score_leftup = matrix[i-1][j-1] + 1
    else:
        score_leftup = matrix[i-1][j-1] - 1

    m = max(score_left, score_up, score_leftup)

    if (m == score_left):
        label[i][j].append("l")
    if (m == score_up):
        label[i][j].append("u")
    if (m == score_leftup):
        label[i][j].append("d")

    return m

def track(seq1, seq2, i, j, label, record):
    if (i == 0 and j == 0):
        seq_print(list(reversed(record)))
    
    if ("d" in label[i][j]):
        record.append([seq1[j-1], seq2[i-1]])
        track(seq1, seq2, i-1, j-1, label, record)
        record.pop()

    if ("l" in label[i][j]):
        record.append([seq1[j-1], "-"])
        track(seq1, seq2, i, j-1, label, record)
        record.pop()

    if ("u" in label[i][j]):
        record.append(["-", seq2[i-1]])
        track(seq1, seq2, i-1, j, label, record)
        record.pop()

def seq_print(seq:list):
    seqA, seqB = "", ""
    for i in range(len(seq)):
        seqA += seq[i][0]
        seqB += seq[i][1]
        
    print("------------")
    print(seqA)
    print(seqB)
    print("------------")


def main():
    parser = argparse.ArgumentParser(description="a simple realization of NW algorithm")

    parser.add_argument("--seq1", "-s1", type=str, help="sequence 1")
    parser.add_argument("--seq2", "-s2", type=str, help="sequence 2")

    args = parser.parse_args()

    seq1 = args.seq1
    seq2 = args.seq2

    NW(seq1, seq2)

if __name__ == "__main__":
    main()