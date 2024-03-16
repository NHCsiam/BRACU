int available[num_of_resources]= { 3, 3, 2, 1 };

    //  allocation matrix
    int allocation[num_of_processes][num_of_resources]= { { 0, 1, 0, 3 }, { 2, 0, 0, 0 },{ 3, 0, 2, 0 }, { 2, 1, 1, 5 },{ 0, 0, 2, 2 } };

    //  max matrix
    int max[num_of_processes][num_of_resources]={ { 6, 4, 3, 4 },{ 3, 2, 2, 1 },{ 9, 1, 2, 6 },{ 2, 2, 2, 8 },{ 4, 3, 3, 7 } };

    // need matrix
    for (i = 0; i < num_of_processes; i++) {
        for (j = 0; j < num_of_resources; j++) {
            need[i][j] = max[i][j] - allocation[i][j];
        }
    }