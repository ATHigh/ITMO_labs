#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string.h>

using namespace std;

int main(int argc, char* argv[]) {
    string s = "g++ -o A0.o A0.cpp";

    if (argc > 1) {
        s = argv[1];
    }

    const char* SEPARATORS = "\n\t ";

    const char* char_array = s.c_str();

    size_t pos = 0;
    int words_count = 0;

    while ((pos = s.find_first_not_of(SEPARATORS, pos)) != string::npos) {
        pos = s.find_first_of(SEPARATORS, pos + 1);
        words_count++;
    }

    cout << "Words count = " << words_count << endl;

    return 0;
}

