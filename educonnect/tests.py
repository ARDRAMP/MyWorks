# import unittest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# class LoginTest(unittest.TestCase):
#     def setUp(self):
#         try:
           
#             self.driver = webdriver.Chrome()  
#             self.driver.get("http://127.0.0.1:8000/login/") 
#             time.sleep(10)
#         except Exception as e:
#             print(f"Exception during WebDriver setup: {e}")

#     def test_login_successful(self):
#         try:
           
#             WebDriverWait(self.driver, 10).until(
#                 EC.presence_of_element_located((By.ID, "email"))
#             )

#             email_input = self.driver.find_element(By.ID, "email")
#             password_input = self.driver.find_element(By.ID, "password")
#             login_button = self.driver.find_element(By.ID,"submit" )  
#             email_input.send_keys("aswin@gmail.com")
#             password_input.send_keys("Aswin@123")

#             login_button.click()

            
#             WebDriverWait(self.driver, 10).until(EC.url_to_be('http://127.0.0.1:8000/'))
#             time.sleep(10)

        
#             self.assertEqual(self.driver.current_url, 'http://127.0.0.1:8000/')
#             time.sleep(10)
#         except Exception as e:
#             print(f"Exception during test execution: {e}")

#     def tearDown(self):
#         try:
          
#             self.driver.quit()  
#         except Exception as e:
#             print(f"Exception during WebDriver teardown: {e}")

# if __name__ == "__main__":
#     unittest.main()



# import unittest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# class LoginTest(unittest.TestCase):
#     def setUp(self):
#         try:
#             self.driver = webdriver.Chrome()  
#             self.driver.get("http://127.0.0.1:8000/login/") 
#             self.driver.implicitly_wait(10)  # Implicit wait to wait for elements
#         except Exception as e:
#             print(f"Exception during WebDriver setup: {e}")

#     def test_login_successful(self):
#         try:
#             WebDriverWait(self.driver, 10).until(
#                 EC.presence_of_element_located((By.ID, "email"))
#             )

#             email_input = self.driver.find_element(By.ID, "email")
#             password_input = self.driver.find_element(By.ID, "password")
#             login_button = self.driver.find_element(By.ID, "submit")  

#             email_input.send_keys("gayathri@gmail.com")
#             password_input.send_keys("Gayathri@123")

#             login_button.click()

#             WebDriverWait(self.driver, 10).until(EC.url_to_be('http://127.0.0.1:8000/'))
#             time.sleep(10)

#             # Now, you can perform actions after successful login
#             # For example, clicking on the "Apply Leave" link
#             apply_leave_link = self.driver.find_element(By.LINK_TEXT, "Apply Leave")
#             apply_leave_link.click()
#             time.sleep(10)

#             # Wait for the "Apply Leave" page to load
#             WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "date")))

#             # Locate the date input field and enter a date
#             date_input = self.driver.find_element(By.NAME, "date")
#             date_input.send_keys("2023-12-15")  # Change this to the desired date
#             time.sleep(10)
#             # Locate the reason textarea and enter a reason
#             reason_textarea = self.driver.find_element(By.NAME, "reason")
#             reason_textarea.send_keys("fever")  # Change this to the desired reason
#             time.sleep(10)
#             # Submit the form
#             submit_button = self.driver.find_element(By.XPATH, "//button[text()='Submit']")
#             submit_button.click()
#             time.sleep(10)

#             # Wait for the page to load after submission (assuming there is a redirect)
#             WebDriverWait(self.driver, 10).until(EC.url_changes(self.driver.current_url))

#             # You can add assertions here to verify that the leave application was successful
#             assert "leave_success" in self.driver.current_url.lower()

#         except Exception as e:
#             print(f"Exception during test: {e}")

#     def tearDown(self):
#         # Close the browser window
#         self.driver.quit()

# if __name__ == "__main__":
#     unittest.main()








# import unittest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# class LoginTest(unittest.TestCase):
#     def setUp(self):
#         try:
#             self.driver = webdriver.Chrome()  
#             self.driver.get("http://127.0.0.1:8000/login/") 
#             time.sleep(10)
#         except Exception as e:
#             print(f"Exception during WebDriver setup: {e}")

#     def test_login_successful(self):
#         try:
#             WebDriverWait(self.driver, 10).until(
#                 EC.presence_of_element_located((By.ID, "email"))
#             )

#             email_input = self.driver.find_element(By.ID, "email")
#             password_input = self.driver.find_element(By.ID, "password")
#             login_button = self.driver.find_element(By.ID, "submit")  
#             email_input.send_keys("aswin@gmail.com")
#             password_input.send_keys("Aswin@123")
#             login_button.click()

#             WebDriverWait(self.driver, 10).until(EC.url_to_be('http://127.0.0.1:8000/'))

#             # Now, navigate to the Class Schedule page
#             class_schedule_link = self.driver.find_element(By.LINK_TEXT, "Class Schedule")
#             class_schedule_link.click()

#             # Wait for the "Class Schedule" page to load
#             WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "typee")))

#             # Perform actions on the Class Schedule page
#             type_input = self.driver.find_element(By.NAME, "typee")
#             date_input = self.driver.find_element(By.NAME, "date")
#             link_input = self.driver.find_element(By.NAME, "link")
#             host_key_input = self.driver.find_element(By.NAME, "host_key")
#             password_input = self.driver.find_element(By.NAME, "password")
#             message_textarea = self.driver.find_element(By.NAME, "message")
#             submit_button = self.driver.find_element(By.XPATH, "//button[text()='Submit']")

#             # Enter details for the class schedule
#             type_input.send_keys("Lecture")
#             date_input.send_keys("2023-12-16T12:00")  # Change this to the desired date and time
#             link_input.send_keys("https://example.com/class-meet")
#             host_key_input.send_keys("123456")
#             password_input.send_keys("Class@123")
#             message_textarea.send_keys("Important announcement for the class.")

#             # Submit the form
#             submit_button.click()

#             # Wait for the page to load after submission (assuming there is a redirect)
#             WebDriverWait(self.driver, 10).until(EC.url_changes(self.driver.current_url))

#             # You can add assertions here to verify that the class schedule was successfully added
#             assert "class_schedule_success" in self.driver.current_url.lower()

#         except Exception as e:
#             print(f"Exception during test execution: {e}")

#     def tearDown(self):
#         try:
#             self.driver.quit()  
#         except Exception as e:
#             print(f"Exception during WebDriver teardown: {e}")

# if __name__ == "__main__":
#     unittest.main()




# import unittest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# class LoginTest(unittest.TestCase):
#     def setUp(self):
#         try:
#             self.driver = webdriver.Chrome()  
#             self.driver.get("http://127.0.0.1:8000/login/") 
#             time.sleep(10)
#         except Exception as e:
#             print(f"Exception during WebDriver setup: {e}")

#     def test_login_successful(self):
#         try:
#             WebDriverWait(self.driver, 10).until(
#                 EC.presence_of_element_located((By.ID, "email"))
#             )

#             email_input = self.driver.find_element(By.ID, "email")
#             password_input = self.driver.find_element(By.ID, "password")
#             login_button = self.driver.find_element(By.ID,"submit" )  
#             email_input.send_keys("dilna@gmail.com")
#             password_input.send_keys("Dilna@123")

#             login_button.click()
            
#             WebDriverWait(self.driver, 10).until(EC.url_to_be('http://127.0.0.1:8000/'))
#             time.sleep(10)

#             # Click on the "Profile" link
#             profile_link = self.driver.find_element(By.LINK_TEXT, "Profile")
#             profile_link.click()
#             time.sleep(10)

#             # Wait for the "Profile" page to load
#             WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Edit")))

#             # Click on the "Edit" link
#             edit_link = self.driver.find_element(By.LINK_TEXT, "Edit")
#             edit_link.click()
#             time.sleep(10)

#             # Wait for the "Profile Update" page to load
#             WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "name")))
#             time.sleep(10)   
#             # Perform actions on the "Profile Update" page
#             name_input = self.driver.find_element(By.NAME, "name")
#             email_input = self.driver.find_element(By.NAME, "email")
#             phone_input = self.driver.find_element(By.NAME, "phone")
#             city_input = self.driver.find_element(By.NAME, "city")
#             place_input = self.driver.find_element(By.NAME, "place")
#             address_input = self.driver.find_element(By.NAME, "address")
#             st_type_input = self.driver.find_element(By.NAME, "st_type")
#             password_input = self.driver.find_element(By.NAME, "password")
#             submit_button = self.driver.find_element(By.XPATH, "//button[text()='Submit']")

#             # Update details on the "Profile Update" page
#             name_input.clear()
#             name_input.send_keys("Updated Name")
#             email_input.clear()
#             email_input.send_keys("updated_email@gmail.com")
#             phone_input.clear()
#             phone_input.send_keys("9876543210")
#             city_input.clear()
#             city_input.send_keys("Updated City")
#             place_input.clear()
#             place_input.send_keys("Updated Place")
#             address_input.clear()
#             address_input.send_keys("Updated Address")
#             st_type_input.clear()
#             st_type_input.send_keys("Updated Student Type")
#             password_input.clear()
#             password_input.send_keys("UpdatedPassword")

#             # Submit the form
#             submit_button.click()
#             time.sleep(10)
#             # Wait for the page to load after submission (assuming there is a redirect)
#             WebDriverWait(self.driver, 10).until(EC.url_changes(self.driver.current_url))

#             # You can add assertions here to verify that the profile was successfully updated
#             assert "profile_update_success" in self.driver.current_url.lower()

#         except Exception as e:
#             print(f"Exception during test execution: {e}")

#     def tearDown(self):
#         try:
#             self.driver.quit()  
#         except Exception as e:
#             print(f"Exception during WebDriver teardown: {e}")

# if __name__ == "__main__":
#     unittest.main()
