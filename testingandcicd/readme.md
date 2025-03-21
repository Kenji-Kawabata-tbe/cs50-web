202050320 14:11
202050321 lesson done

cd airline/alrline
python manage.py test

selenium
cd selenium/
python
>>> from tests import *
>>> from selenium.webdriver.common.by import By

>>> uri = file_uri("counter.html")
>>> driver.get(uri)

>>> driver.title
>>> driver.page_source
>>> driver.find_element_by_id("increase")

# Find and store the increase and decrease buttons:
>>> increase = driver.find_element(By.ID, "increase")
>>> decrease = driver.find_element(By.ID, "decrease")

# Simulate the user clicking on the two buttons
>>> increase.click()
>>> increase.click()
>>> decrease.click()

# We can even include clicks within other Python constructs:
>>> for i in range(25):
...     increase.click()


cd selenium/
python tests.py

cd testingandcicd/airline/
docker-compose up
