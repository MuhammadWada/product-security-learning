# Simple Log Parser
***Purpose:*** Extract useful information from log files by parsing logs for keywords. Keywords denote the type of events we are looking for in the log. The uder will pass in a log file they wish to parse and the keyword of the event(s) they wish to search for. The script will then output the lines in which the keyword occurs and the full contents of that line to an output file. Furthermore, the file will include the total count of the keyword in the bottom of the file (i.e., statistics). 

The first log file we will target is the system log, [var/log/system.log]

## Inputs:
1. Path to log file
2. Keyword to search for within the log file

## Outputs:
* Line number and full line for each occurrence of the keyword
* Summary of errors (written to screen or output to a text file), error counts, filtered logs

## Edge Cases:
This catches common errors that could happen, such as:
* Empty file
* missing file
* corrupted lines
* invalid path

## CLI Flags: 

`--file`
This defines where to put in the filename

`--keyword`
Define what to search for (i.e., error)

`--output`
Specify the name and location for where to store the parsed log output

## Data Structures:
`list` for lines

`dict` for counts

## Future Extensions:
Regex support

JSON output