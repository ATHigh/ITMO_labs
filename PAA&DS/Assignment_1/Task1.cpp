#include <iostream>
#include <vector>
#include <cstdlib>
#include <omp.h>
#include <chrono>

using namespace std;

int main(int argc, char** argv) {
    if (argc != 2) {
        cerr << "Usage: " << argv[0] << " <array_size>" << endl;
        return 1;
    }

    int n = atoi(argv[1]);

    if (n <= 0) {
        cerr << "Array size must be a positive integer." << endl;
        return 1;
    }

    vector<double> a(n);

    // Initialize vector with random values between 0 and 1
    #pragma omp parallel for
    for (int i = 0; i < n; i++) {
        a[i] = static_cast<double>(std::rand()) / RAND_MAX;
        // cout << "a[" << i << "] = " << a[i] << endl;
    }

    for (int m = 1; m <= 10; m++) {
        double max_value = a[0];
        auto time_start = chrono::high_resolution_clock::now();

        #pragma omp parallel for num_threads(m) reduction(max : max_value)
        for (int i = 0; i < n; i++) {
            max_value = (max_value > a[i]) ? max_value : a[i];
        }

        auto time_stop = chrono::high_resolution_clock::now();
        auto exec_time = chrono::duration_cast<chrono::microseconds>(time_stop - time_start);
        cout << "Execution time via " << m << " thread(s) in microseconds: " << exec_time.count() << endl;
        cout << "Maximum value: " << max_value << endl;
    }

    return 0;
}

