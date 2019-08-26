//  hw5.cpp
//  CMSC 331 HW 5
//  Created by Dane Magbuhos on 10/30/18.

// Description: This program reads in a file and determines 
//              if each string input is a valid decimal or
//              octal number.

#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <iterator>
#include <map>

using namespace std;

int main() {

    vector<string> data;
    string line, input;
    unsigned long length, index;
    fstream file;
    int transition;

    // Valid Entries
    map<string, int> entry;
    entry["+"] = 0;
    entry["-"] = 1;
    entry["0"] = 2;
    entry["1"] = 3;
    entry["2"] = 4;
    entry["3"] = 5;
    entry["4"] = 6;
    entry["5"] = 7;
    entry["6"] = 8;
    entry["7"] = 9;
    entry["8"] = 10;
    entry["9"] = 11;

    // States' Responses
    string response [6] = {"Rejected", "Rejected",
			   "Accepted", "Accepted",
			   "Accepted", "Rejected"};
    
    
    // State Transition Table
    // Characters         +,-,0,1,2,3,4,5,6,7,8,9
    int states[6][12] = {{1,1,5,5,5,5,5,5,5,5,5,5},  // State S (Starting State)
			 {5,5,2,3,3,3,3,3,3,3,3,3},  // State A (Decimal Transiion State 1)
			 {5,5,5,4,4,4,4,4,4,4,5,5},  // State B (Octal Transition State 2)
			 {5,5,3,3,3,3,3,3,3,3,3,3},  // State C (Decimal Accepting State)
			 {5,5,4,4,4,4,4,4,4,4,5,5},  // State D (Octal Accepting State)
			 {5,5,5,5,5,5,5,5,5,5,5,5}}; // State E (Reject State)


    // Opens data file
    file.open("test-data.txt");
   
    // Adds examined strings into vector
    while(getline(file, line, ' ')){
        
        data.push_back(line);
    }

    // Closes file before conducting analysis
    file.close();
  
   
    vector<string>::iterator iter;

    // Iterates through vector and examines each string
    for(iter = data.begin(); iter != data.end(); iter++){
      
      // Prepares each string for analysis
      input = *iter;
      length = input.length();
      index = 0;
      transition = 0;

      // Determines if input is valid
      while(index < length){

	// Typecasts character into string
	string value (1, input[index]);

	// Compares string character to state transition table 
	transition = states[transition][entry[value]];
	index++;
      }

      // Outputs results from examination
      cout << response[transition] << ": " << input << endl;
      
    } 

  return 0;

}
