
from python.Project.Crawling.Image.TestCode.test_page_num import extract_page


PAGE = extract_page
URL = f"http://www.casemario.com/goods/goods_list.php?cateCd={PAGE}"

def extract_page():
    result_2 = []
    for number in range(30):
        if number < 10:
            result_2.append(format("00%d" % (number)))
        else :
            result_2.append(format("0%d" % (number)))
    return(result_2)
print(extract_page())

def extract_image():
    result = URL
    soup = BeautifulSoup(result, "html.parser")
    image = soup.find_all("div", {"src":"img"})
    return