"""  


import a module named datetime to work with dates as date objects.






The datetime object has a method for formatting date objects into readable strings.

The method is called strftime(), and takes one parameter, format, to specify the format of the returned string





%a	Weekday, short version	Wed	
%A	Weekday, full version	Wednesday	
%w	Weekday as a number 0-6, 0 is Sunday	3	
%d	Day of month 01-31	31	
%b	Month name, short version	Dec	
%B	Month name, full version	December	
%m	Month as a number 01-12	12	
%y	Year, short version, without century	18	
%Y	Year, full version	2018	
%H	Hour 00-23	17	
%I	Hour 00-12	05	
%p	AM/PM	PM	
%M	Minute 00-59	41	
%S	Second 00-59	08	
%f	Microsecond 000000-999999	548513	
%z	UTC offset	+0100	
%Z	Timezone	CST	
%j	Day number of year 001-366	365	
%U	Week number of year, Sunday as the first day of week, 00-53	52	
%W	Week number of year, Monday as the first day of week, 00-53	52	
%c	Local version of date and time	Mon Dec 31 17:41:00 2018	
%x	Local version of date	12/31/18	
%X	Local version of time	17:41:00	
%%	A % character	%	
%G	ISO 8601 year	2018	
%u	ISO 8601 weekday (1-7)	1	
%V	ISO 8601 weeknumber (01-53)	01 """


import datetime
tim = datetime.datetime.now()
print(tim)
print(tim.strftime("%a"))
print(tim.strftime("%A"))
print(tim.strftime("%w"))
print(tim.strftime("%d"))
print(tim.strftime("%b"))
print(tim.strftime("%B"))
print(tim.strftime("%m"))
print(tim.strftime("%y"))
print(tim.strftime("%Y"))
print(tim.strftime("%H"))
print(tim.strftime("%I"))
print(tim.strftime("%p"))
print(tim.strftime("%M"))
print(tim.strftime("%S"))
print(tim.strftime("%f"))
print(tim.strftime("%z"))
print(tim.strftime("%Z"))
print(tim.strftime("%j"))
print(tim.strftime("%U"))
print(tim.strftime("%W"))
print(tim.strftime("%c"))
print(tim.strftime("%x"))
print(tim.strftime("%X"))
print(tim.strftime("%%"))
print(tim.strftime("%G"))
print(tim.strftime("%u"))
print(tim.strftime("%V"))
