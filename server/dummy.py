import sys
import csv

def dummy_calc(insurance, out_of_pocket, copay, diagnosis, medications):
     print ("line_count")
     filename = "Final Plans for Scenerio Prostate IV 150.csv"
     with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        
        for row in csv_reader:
             if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
             if line_count == 2:
                print(f'For the plan \t{row[0]} and the metal level {row[1]}, the out of pocket maximum will be reached after {row[7]} number of claims and {row[8]} visits, at the catagory {row[9]}.')
                line_count += 1
     print (f'Processed {line_count} lines.')
  
     return insurance + out_of_pocket + copay + diagnosis + ' '.join(medications) 