def longest_string(string1, string2):
    # find the length of the sequnece in the string 
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

    # print the longest subsequence in the strings
    it = len(string1)-1
    jt = len(string2)-1
    result_string = ""
    while it > 0 and jt > 0:
        if string1[it] == string2[jt]:
            result_string = string1[it] + result_string
            it -= 1
            jt -= 1

        elif result[it][jt-1] >= result[it-1][jt]:
            jt -= 1
        else:
            it -= 1

        # if it == 0 or jt == 0: break
    
    return result[len(string1)-1][len(string2)-1], result_string

        
        


if __name__ == "__main__":
    string1 = 'abaaba'
    string2 = 'babbab'

    length_string, longest_substring = longest_string(string1, string2)

    print("Length of LCS is :", length_string)
    print("The string is :", longest_substring)