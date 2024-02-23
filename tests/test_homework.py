from selene import browser, have
from tests.conftest import LOGIN, PASSWORD, BASE_URL
from utils.utils import post_request


def test_add_product_with_params():
    response = post_request("login", data={"Email": LOGIN, "Password": PASSWORD}, allow_redirects=False)
    cookies = response.cookies.get("NOPCOMMERCE.AUTH")
    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookies})
    response2 = post_request("/addproducttocart/details/16/1", data={
        "product_attribute_16_5_4": 14,
        "product_attribute_16_6_5": 15,
        "product_attribute_16_3_6": 18,
        "product_attribute_16_4_7": 44,
        "product_attribute_16_8_8": 22,
        "addtocart_16.EnteredQuantity": 1}, allow_redirects=False, cookies={"NOPCOMMERCE.AUTH": cookies})
    assert response2.status_code == 200
    browser.open(BASE_URL)
    browser.open(f"{BASE_URL}cart")
    browser.element('.product-name').should(have.text("Build your own computer"))
    browser.element(".remove-from-cart").click()
    browser.element(".update-cart-button").press_enter()


def test_add_product_without_params():
    response = post_request("login", data={"Email": LOGIN, "Password": PASSWORD},
                                 allow_redirects=False)
    cookies = response.cookies.get("NOPCOMMERCE.AUTH")
    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookies})
    response2 = post_request("addproducttocart/catalog/31/1/1", cookies={"NOPCOMMERCE.AUTH": cookies})
    assert response2.status_code == 200
    browser.open(BASE_URL)
    browser.open(f"{BASE_URL}cart")
    browser.element('.product-name').should(have.text("14.1-inch Laptop"))
    browser.element(".remove-from-cart").click()
    browser.element(".update-cart-button").press_enter()

