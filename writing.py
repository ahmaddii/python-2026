# File Handling : first we writing the files .txt .json .csv
import json
import csv

txt_data = "I like Pizza !" # we have declare a string which we write in the txt file

employess = ["Ahmad","Ali","Fahad","Khan Baba"]

employee = {
      
      "name": "Ahmad",
      "age": 30,
      "Job": "Software Engineer AI/ML"
}

# now we create 2d sheet for csv excel
emp = [
      ["Name", "Age" , "Job"], # first row 
      ["Ahmad", 30,  "SE"],
      ["Ali",  25,  "CS"],
      ["Candy", 20, "Admin"]]


# and then we have the relative path of the location where we want to store our ouput txt file

file_path = "/home/malikahmadrasheed/Downloads/output.csv" # absoutle path

# with is useful beucase when open blocks ends it closes the file auto with open we
# the file path in mode write as file object and write inside with the file object the txt
# and then just print the confirmetion on the logs

try:
        with open(file=file_path,mode="w",newline="") as file:

            #file.write("\n" + employess) not done directly to write the list collections to write in file so
           # json.dump(employee,file,indent=4)
            writer = csv.writer(file) # writer is the object used to write on the csv files
            for row in emp:
                  writer.writerow(row)


           # for employe in employess:
          #        file.write(employe + " \n ")

            print(f"Json File Created at {file_path}")

except FileExistsError:
      print("File Already Exists !")
