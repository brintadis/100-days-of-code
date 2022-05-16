import time
from selenium import webdriver

chrome_driver_path = "YOUR CHROME DRIVER PATH"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

# Get cookie item to click on
cookie = driver.find_element_by_id("cookie")

# Get upgrate ids list
items = driver.find_elements_by_css_selector("#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
five_min = time.time() + 60*5


while True:
    cookie.click()

    # Check every 5 secs
    if time.time() > timeout:
        all_prices = driver.find_elements_by_css_selector("#store b")
        item_prices = []

        # Converting a price into an int
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(price.text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        # Creating price to id dictionary
        cookie_upgrages = {item_prices[n]: item_ids[n] for n in range(len(item_prices))}

        # Out cookie bank
        money_element = driver.find_element_by_id("money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        # Creating a dict of all the affordable upgrades
        affordable_upgrades = {}
        for cost, id in cookie_upgrages.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id
        
        # Purchasing the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]
        driver.find_element_by_id(to_purchase_id).click()

        # Updating timer 
        timeout = time.time() + 5

    # After 5 mins print "cookie per second" and break
    if time.time() > five_min:
        print(driver.find_element_by_id("cps").text)
        break