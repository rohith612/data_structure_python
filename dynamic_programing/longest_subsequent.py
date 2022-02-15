def longest_string(string1, string2):
    string1 = '^'+ string1
    string2 = '^'+ string2
    result = list()
    for i in range(len(string1)):
        temp = list()
        if i == 0:
            temp = [0] * int(len(string1))
            result.append(temp)
            continue

        for j in range(len(string2)):
            if j == 0:
                temp.append(0)
                continue

            if string1[i] == string2[j]:
                interns = 1 + result[i-1][j-1] 
            else:
                interns = max(result[i-1][j], temp[j-1])
            temp.append(interns)

        result.append(temp)    
    return result[len(string1)-1][len(string2)-1]


if __name__ == "__main__":
    string1 = 'abaaba'
    string2 = 'babbab'

    longest_substring = longest_string(string1, string2)

    print("Length of LCS is ", longest_substring)