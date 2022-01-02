# Most Active Cookie Parser
Most Active Cookie Parser parses the input file and with the input date, gets the most active cookie from the data.

The data is required to be a csv file with the format:

----------------------
cookie,timestamp\
AtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00\
SAZuXPGUrfbcn5UA,2018-12-09T10:13:00+00:00\
5UAVanZf6UtGyKVS,2018-12-09T07:25:00+00:00\
AtY0laUfhglK3lC7,2018-12-09T06:19:00+00:00\
SAZuXPGUrfbcn5UA,2018-12-08T22:03:00+00:00\
4sMM2LxV07bPJzwf,2018-12-08T21:30:00+00:00\
fbcn5UAVanZf6UtG,2018-12-08T09:30:00+00:00\
4sMM2LxV07bPJzwf,2018-12-07T23:30:00+00:00
---------------------------
There is a Makefile which describes how to run the tests on the tool, 
how to get the coverage report on the code, and other functions.

A shell script also exists called `parser.sh` which can be called to execute the command.\
For E.g.:\
`./parser.sh -f cookie_log.csv -d 2018-12-09`
 