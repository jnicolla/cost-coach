import sys
import csv
from prettytable import PrettyTable

def script_calc(insurance, diagnosis, medications):
     plan = ''
     
     if insurance == 'Duke Select':
        plan = '11512NC0100028'  
     if insurance == 'Duke Basic':
        plan = '11512NC0100036'  
     if insurance == 'Duke Care':
        plan = '11512NC0060024'    
     if insurance == 'Duke Options':
        plan = '11512NC0060028'
    
     data = []  
   #   The uncommented code can be used to form a html table from the data  
   #   csv_f = open('./csvfiles/Step-by-Step Changes in OOPM and Deductibles for Prostate IV 150.csv', 'r')
   #   csv_f = csv_f.readlines()
   #   line_1 = csv_f[0]
   #   line_1 = line_1.split(',')
   #   x  = PrettyTable([line_1[0], line_1[1],  line_1[2], line_1[3], line_1[4], line_1[5], line_1[6], line_1[7]])
     fileToOpen = ''
     if medications == 'IV':   
        fileToOpen = './csvfiles/Step-by-Step Changes in OOPM and Deductibles for Prostate IV 150.csv'
     if medications == 'Oral':
        fileToOpen = './csvfiles/Step-by-Step Changes in OOPM and Deductibles for Prostate Oral 150.csv'

     with open(fileToOpen) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        
        for row in csv_reader:
             if row[0] == plan:
              #  print(f'For the insurance plan \t{insurance} \t{row[0]} and the metal level {row[1]}, the out of pocket maximum will be reached after {row[5]} claims and {row[6]} visits, at the catagory {row[7]}.')
                line_count += 1
               #  x.add_row([row[0], row[1],  row[2], row[3], row[4], row[5], row[6], row[7]])
               
                data.append(f'{row[6]},{row[7]}, {row[2]}')
                
             #if line_count == 0: row[0] == plan:
                #print(f'Column names are {", ".join(row)}')
                #line_count += 1
             #elif line_count == 2:
                #print(f'For the insurance plan \t{insurance} \t{row[0]} and the metal level {row[1]}, the out of pocket maximum will be reached after {row[5]} number of claims and {row[6]} visits, at the catagory {row[7]}.')
             else:
                 line_count += 1
                 
     csv_file.close()     
     
   #   html_code = x.get_html_string()
   #   html_file = open('\data_out_table\table.html', 'w')
   #   html_file = html_file.write(html_code)
   
     return data


# Following is use to test the output of this file
# if __name__=='__main__':
#    result = script_calc('Duke Select', 'Prostate Cancer', 'Oral')
#    print(result)