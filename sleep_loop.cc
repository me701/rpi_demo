#include <unistd.h> // POSIX API
#include <iostream>
#include <string>
#include <sstream>

int main(int argc, char* argv[])
{
    std::string msg = "Hello, world!";
    int num_repeats = 10; // repeats
    int num_seconds = 1 ; // seconds 
    if (argc == 4)
    {
        msg = argv[1];
        std::string buffer(argv[2]);
        std::stringstream(buffer) >> num_repeats;
        buffer= argv[3];
        std::stringstream(buffer) >> num_seconds;
    }
    for (int i = 0; i < num_repeats; ++i)
    {
        std::cout << msg << std::endl;
        sleep(num_seconds);
    }
    return 0;
}