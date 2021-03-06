import os
import sys
import csv
from .main_script import getPath
from prettytable import 

#Script that implements the main script results, processes them and returns a 
#result in form of the array that is stored in the main app as the JSON file that
#frontend reads and outputs result to the web pages

def script_calc(insurance, diagnosis, medications):
   data = []
   # check for valid user inputs
   if insurance=='' or diagnosis=='' or medications=='':
      return ''
   plan = ''
     
   if insurance == 'Duke Select':
      plan = '11512NC0100028'  
   elif insurance == 'Duke Basic':
      plan = '11512NC0100036'  
   elif insurance == 'Duke Care':
      plan = '11512NC0060024'    
   else:
      return '' 

#   The commented code can be used to form a html table from the data  
#   csv_f = open('./csvfiles/Step-by-Step Changes in OOPM and Deductibles for Prostate IV 150.csv', 'r')
#   csv_f = csv_f.readlines()
#   line_1 = csv_f[0]
#   line_1 = line_1.split(',')
#   x  = PrettyTable([line_1[0], line_1[1],  line_1[2], line_1[3], line_1[4], line_1[5], line_1[6], line_1[7]])
   fileToOpen_rel_path = ''
   if medications == 'IV':   
      fileToOpen_rel_path = 'csvfiles/Step-by-Step Changes in OOPM and Deductibles for Prostate IV 150.csv'
   if medications == 'Oral':
      fileToOpen_rel_path = 'csvfiles/Step-by-Step Changes in OOPM and Deductibles for Prostate Oral 150.csv'
   fileToOpen = getPath(fileToOpen_rel_path) 
   with open(fileToOpen) as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')
      line_count = 1
      
      for row in csv_reader:
         if line_count%2==1 and line_count!=1:
            if row[0] == plan:
            #  x.add_row([row[0], row[1],  row[2], row[3], row[4], row[5], row[6], row[7]])
               add = row[7]
               if row[7] == '':
                  add='Initial'
               data.append(f'{row[6]},{add},{row[2]}')
         line_count+=1
               
   csv_file.close()    
#   ***code to write the output to html file*** 
#   html_code = x.get_html_string()
#   html_file = open('\data_out_table\table.html', 'w')
#   html_file = html_file.write(html_code)  ---if you want to write to html file the data results

   return data

# Following is use to test the output of this file
# if __name__=='__main__':
#    result = script_calc('Duke Select', 'Prostate Cancer', 'Oral')
#    print(result)