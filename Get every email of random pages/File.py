import selenium


def isMail(link: str):
    if ('mailto:' in link):
        return True
    return False


elem = driver.find_elements_by_css_selector('a') # You need <a> tags if you want to be sure to find href attribute
links = [elem.get_attribute('href') for elem in elems]
mails = [link.removeprefix('mailto:') for link in links if isMail(link)]