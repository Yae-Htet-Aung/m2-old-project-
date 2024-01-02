1 department
2 job
3 contract
4 employee 
5 recruitment

apps            foreign keys                tags 
----            ------------                ----
job 		    << department				# employee
contract 		<< job, department 			# employee
employee 	    << job, department 			# contract
recruitment 	<< employee				    #  job, department
expense 		<< department
attendance	    << employee
payroll 		<< employee, contract 


ADDED NEW FEATURES * 
------------------
in hr_department,
- 

in hr_job
- 

in hr_contract,
- detail view is dynamic. It changes according to contract type; employee or contractor or subcontractor!
- uploaded attachments are displayed in contract list and detail views of hr_contract!
- if a new attachment is UPDATED, the old attachment is DELETED and replaced with a new one in the same directory!
- if no attachment is uploaded, a default attachment is shown!

in hr_employee,
- uploaded pictures are displayed in employee list and detail views of hr_employee!
- uploaded employee's pictures are saved in the employee folder under the media folder!
- if a new picture is UPDATED, the old picture is DELETED and replaced with a new one in the same directory!
- if no picture is uploaded, a default picture is shown!

in hr_recruitment,
- uploaded employee's resume files are saved in the resume folder under the media folder!
- if a new resume file is UPDATED, the old resume file is DELETED and replaced with a new one in the same directory!

in hr_expense,

in hr_attendance,

in hr_payroll,
