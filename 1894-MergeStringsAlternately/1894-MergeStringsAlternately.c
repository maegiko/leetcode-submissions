// Last updated: 08/04/2026, 12:39:44

char * mergeAlternately(char * word1, char * word2){
    int word1_len = strlen(word1);
    int word2_len = strlen(word2);
    int merge_len = word1_len + word2_len + 1;

    char *merge = malloc(sizeof(char) * merge_len);
    int i = 0;
    int j = 0;
    int k = 0;

    while (i < word1_len || j < word2_len) {
        if (i < word1_len) {
            merge[k] = word1[i];
            i++;
            k++;
        }

        if (j < word2_len) {
            merge[k] = word2[j];
            j++;
            k++;
        }
    }
    merge[k] = '\0';
    return merge;
}