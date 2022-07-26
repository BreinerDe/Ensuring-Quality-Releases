# #!/usr/bin/env python
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By

datetime.now().strftime("%m-%d-%y %H:%M:%S")

login_url = 'https://www.saucedemo.com/'
inventory_url = 'https://www.saucedemo.com/inventory.html'
cart_url = 'https://www.saucedemo.com/cart.html'

def create_driver():
    print ('Starting the browser...')
    options = ChromeOptions()
    options.add_argument("--headless") 
    return webdriver.Chrome(options=options)
    

# Start browserr and login
def test_login (driver, user, password):
    print ('Test: logging in. Navigating to the  page to  {}'.format(login_url))
    driver.get(login_url)
    print ('Logging in with user: {},  password: {}'.format(user, password))
    driver.find_element(By.ID,'user-name').send_keys(user)
    driver.find_element(By.ID,'password').send_keys(password)
    driver.find_element(By.ID,'login-button').click()
    assert inventory_url in driver.current_url
    print ('Test Login Successfull.')
    

def test_add_items_to_cart(driver):
    items_in_cart = []
    print ('Test: add items to cart')
    elements = driver.find_elements(By.CLASS_NAME,'inventory_item')
    for item in elements:
        item_name = item.find_element(By.CLASS_NAME,'inventory_item_name').text
        items_in_cart.append(item_name)
        item.find_element(By.CLASS_NAME,'btn_inventory').click()
        print('Added {} to cart'.format(item_name))
    cart_element = driver.find_element(By.CLASS_NAME,'shopping_cart_badge')
    assert int(cart_element.text) == len(elements)
    print ('Navigate to to shopping cart')
    driver.find_element(By.CLASS_NAME,'shopping_cart_link').click()
    print ('Assert location is cart page. ')
    assert cart_url in driver.current_url
    print ('Assert items are in cart. ')
    for item in driver.find_elements(By.CLASS_NAME,'inventory_item_name'):
        assert item.text in items_in_cart
    print ('Test Add Items in cart Successfull.')


def test_remove_items_from_cart(driver):
    print ('Test: removing items from cart')
    print ('Navigate to cart and assert items are in cart.')
    driver.find_element(By.CLASS_NAME,'shopping_cart_link').click()
    print ('Assert location is cart page.')
    assert cart_url in driver.current_url

    print("Items in Cart: {}".format(len(driver.find_elements(By.CLASS_NAME,'cart_item'))))
    
    print('Remove all items from cart.')
    for item in driver.find_elements(By.CLASS_NAME,'cart_item'):
        item_name = item.find_element(By.CLASS_NAME,'inventory_item_name').text
        item.find_element(By.CLASS_NAME,'cart_button').click()
        print('Removed {} from cart'.format(item_name))

    print('Assert cart is empy')
    print("Items in Cart: {}".format(len(driver.find_elements(By.CLASS_NAME,'cart_item'))))
    assert len(driver.find_elements(By.CLASS_NAME,'cart_item')) == 0
    print('Cart empty.')
    print ('Test Remove Items from cart Success.')


def run_ui_tests():
    driver = create_driver()
    print("Browser started successfully.")
    print("UI Tests started")
    
    print("*********** - test logging in user")
    test_login(driver, 'standard_user', 'secret_sauce')
    print("*********** - test adding items to cart")
    test_add_items_to_cart(driver)
    print("*********** - test removving items from cart")
    test_remove_items_from_cart(driver)

    print("UI Tests completed.")
    driver.quit()

if __name__ == "__main__":
    run_ui_tests()
