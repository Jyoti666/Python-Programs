dict1={"Emp_No":[1001,1002,1003,1004,1005,1006,1007],"Emp_Name":['Ashish','Sushma','Rahul','Chahat','Ranjan','Suman','Tanmay'],
      "Designation_Code":['e','c','k','r','m','e','c'],"Basic":[20000,30000,10000,12000,50000,23000,29000],
      "HRA":[8000,12000,8000,6000,20000,9000,12000],"IT":[3000,9000,1000,2000,20000,4400,10000]}

dict2={"Designation_Code":['e','c','k','r','m'],
       "DA":[20000,32000,12000,15000,40000]}
name=input('Enter Employee name:')
index=0;
for i in dict1["Emp_Name"]:
    if i == name:
        index+=1
        break
d_code=dict1["Designation_Code"][index]
index2=0
for i in dict2["Designation_Code"]:
    if i== d_code:
        da=dict2["DA"][index2]
        netsalary=(dict1["Basic"][index]+dict1["HRA"][index]+dict2["DA"][index2])-dict1["IT"][index]
        print("Net Salary:",netsalary)
        break
    index2+=1;
if name not in dict1["Emp_Name"]:
    print("Name is not present")


