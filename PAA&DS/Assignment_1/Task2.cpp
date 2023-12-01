#include <iostream> 
#include "omp.h" 
#include <cstdlib> 
#include <vector> 
#include <string> 
 
using namespace std; 
 
void multiply_matrix(const vector<vector<double>>& A, const vector<vector<double>>& B, vector<vector<double>>& C, const string& loops_order, int num) 
{ 
#pragma omp parallel for num_threads(num) 
    for (int i = 0; i < C.size(); i++) 
        for (int j = 0; j < C[i].size(); j++) 
            for (int k = 0; k < A[i].size(); k++) 
                C[i][j] += A[i][k] * B[k][j]; 
} 
 
int main(int argc, char* argv[]) 
{ 
    int size = 10; 
 
    if (argc > 1) 
    { 
        size = atoi(argv[1]); 
    } 
 
    double one_thread_exec_time; 
    vector<vector<double>> A(size, vector<double>(size)); 
    vector<vector<double>> B(size, vector<double>(size)); 
    vector<vector<double>> C(size, vector<double>(size)); 
 
    for (int i = 0; i < size; i++) 
    { 
        for (int j = 0; j < size; j++) 
        { 
            A[i][j] = rand(); 
            B[i][j] = rand(); 
        } 
    } 
 
    string orders[] = { "ijk", "jki", "ikj" }; 
    for (const auto& loops_order : orders) 
    { 
        cout << loops_order << "\n"; 
        for (int thread_count = 1; thread_count <= 10; thread_count++) 
        { 
            for (int i = 0; i < size; i++) 
            { 
                fill(C[i].begin(), C[i].end(), 0); 
            } 
 
            double start_time = omp_get_wtime(); 
 
            multiply_matrix(A, B, C, loops_order, thread_count); 
 
            double exec_time = omp_get_wtime() - start_time; 
            if (thread_count == 1) 
            { 
                one_thread_exec_time = exec_time; 
            } 
            double efficiency = one_thread_exec_time / (exec_time + 0.0000001); 
            cout << "Threads count: " << thread_count << "  Execution time: " << exec_time << "  Efficiency: " << efficiency << "\n"; 
        } 
    } 
 
    return 0; 
}
