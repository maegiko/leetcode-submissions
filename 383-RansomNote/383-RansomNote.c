// Last updated: 08/04/2026, 12:39:53
bool canConstruct(char* ransomNote, char* magazine) {

    int r_length = strlen(ransomNote);
    int m_length = strlen(magazine);
    bool char_exist;

    for (int i = 0; i < r_length; i++) {
        char_exist = false;
        for (int j = 0; j < m_length; j++) {
            if (ransomNote[i] == magazine[j]) {
                magazine[j] = '0';
                char_exist = true;
                break;
            } 
        }

        if (char_exist == false) {
            return false;
        }
    }
    return true;
}

