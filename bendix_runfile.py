import pandas as pd
import bendix_function as bf

# Initialize the webdriver.
driver = bf.init_driver(path) #To do
# Go to https://www.bendix.com.au/catalogue?manufacturer=&odmeloepart=&part==&variant=&oepart=&part=
bf.navigate_to_website(driver, "https://www.bendix.com.au/catalogue?manufacturer=&odmeloepart=&part==&variant=&oepart=&part=")
search_car = "BMW"
search_type_of_car = "518 Series"
bf.select_data(driver, search_car, search_type_of_car)
# Getting sourse from html and pulling out required data
page_sourse = bf.get_html(driver)
table_header = []
table_body = []
for i in page_sourse.find_elements_by_tag_name("th"):
    table_header.append(i.text)
print(table_header)
for row in page_sourse.find_elements_by_tag_name("td"):
    table_body.append(row.text)
# Combining two list into one
array1 = [table_body[i:i+len(table_header)] for i in range(0, len(table_body), len(table_header))]
# Making DF from array and writing into csv file
s = pd.DataFrame(data=array1, columns=table_header)
s.to_csv("bendix.csv", mode= "w", index=False)


