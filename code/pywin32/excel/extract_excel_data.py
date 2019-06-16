import win32com.client
import glob
import sys, io

# Open up Excel and make it visible (actually you don't need to make it visible)
excel = win32com.client.Dispatch('Excel.Application')
excel.Visible = True

# Select the path of the folder with all the files
files = glob.glob("folder_path/*.xlsx")

# Redirect the stdout to a file
orig_stdout = sys.stdout
bk = io.open("Answers_Report.txt", mode="w", encoding="utf-8")
sys.stdout = bk

# Go through all the files in the folder
for file in files:
	print(file.split('\\')[1])
	wb_data = excel.Workbooks.Open(file) 
  
  # Get the answers to the Q1A
	mission=wb_data.Worksheets("1ayb_MisiónyVisiónFutura").Range("C6")
	vision =wb_data.Worksheets("1ayb_MisiónyVisiónFutura").Range("C7")
	print("Question 1A")
	print("Mission:",mission)
	print("Vision:" ,vision)
	print()

  # Get the answers to the Q1B
	oe1=wb_data.Worksheets("1ayb_MisiónyVisiónFutura").Range("C14")
	ju1=wb_data.Worksheets("1ayb_MisiónyVisiónFutura").Range("D14")
	oe2=wb_data.Worksheets("1ayb_MisiónyVisiónFutura").Range("C15")
	ju2=wb_data.Worksheets("1ayb_MisiónyVisiónFutura").Range("D15")
	print("Question 1B")
	print("OEN1:",oe1, "- JUSTIF:",ju1)
	print("OEN2:",oe2, "- JUSTIF:",ju2)
	print()

  # Get the answers to the Q2A
	mision=wb_data.Worksheets("2a_MisionyVisionSI").Range("C6")
	vision=wb_data.Worksheets("2a_MisionyVisionSI").Range("C7")
	print("Question 2A")
	print("Mission SI:",mision)
	print("Vision SI:",vision)
	print()
  
  # Get the answers to the Q3A
	print("Question 3A")
	for i in range(5,13): 
		proy=wb_data.Worksheets("3a_ProySI").Range("B"+str(i))
		desc=wb_data.Worksheets("3a_ProySI").Range("D"+str(i))
		mcfr=wb_data.Worksheets("3a_ProySI").Range("E"+str(i))
		tipo=wb_data.Worksheets("3a_ProySI").Range("F"+str(i))	
		print("\tProyect:",proy)
		print("\tDesc:",desc)
		print("\tMacFarlan:",mcfr,"- Tipo",tipo)
		print()
    
  # Close the file without saving
	wb_data.Close(True)

# Restoring the stdout
sys.stdout = orig_stdout
bk.close()

# Create a new Excel file for the grading template
wb_template = excel.Workbooks.Add()

# Headers of the template
wb_template.Worksheets(1).Range("A1").Value = 'File'
wb_template.Worksheets(1).Range("B1").Value = 'Q1A'
wb_template.Worksheets(1).Range("C1").Value = 'C1A'
wb_template.Worksheets(1).Range("D1").Value = 'Q1B'
wb_template.Worksheets(1).Range("E1").Value = 'C1A'
wb_template.Worksheets(1).Range("F1").Value = 'Q2A'
wb_template.Worksheets(1).Range("G1").Value = 'C2A'
wb_template.Worksheets(1).Range("H1").Value = 'Q3A'
wb_template.Worksheets(1).Range("I1").Value = 'C3A'

# Add the path of each file into the template
for idx, arch in enumerate(files):
	wb_template.Worksheets(1).Range("A"+str(idx+2)).Value = arch.replace('\\','/')	

# Save the grading template without alerts
excel.DisplayAlerts = False
wb_template.SaveAs(r'folder_path\Grades_Template.xlsx')

# Close the file and the program
wb_template.Close()
excel.DisplayAlerts = True
excel.Quit()
