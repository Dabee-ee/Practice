import requests
from bs4 import BeautifulSoup

# indeed + start
LIMIT = 50
URL = f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and=%EA%B0%9C%EB%B0%9C%EC%9E%90&limit={LIMIT}"

def get_last_page():
  result = requests.get(URL)

  soup = BeautifulSoup(result.text, "html.parser")

  pagination = soup.find("div", {"class":"pagination"})

  links = pagination.find_all('a')
  pages = []
  for link in links[0:-1]:
     pages.append(int(link.string))
  max_page = pages[-1]
  return max_page

def extract_job(html):
    title = html.find("h2", {"class":"title"}).find("a")["title"]
    company = html.find("span", {"class":"company"})
    company_anchor = company.find("a")
    if company_anchor is not None:
      company = str(company_anchor.string)
    else:
      company = str(company.string)
    company = company.strip()
    location = html.find("div", {"class":"recJobLoc"})["data-rc-loc"]
    job_id = html["data-jk"]
    return {
      'title':title, 
      'company':company, 
      'location':location, "Link":f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and=%EA%B0%9C%EB%B0%9C%EC%9E%90&limit=50&vjk={job_id}"
      }

def extract_jobs(last_page):
  jobs = []
  for page in range(last_page):
    print(f"Scrpping sindeed: page {page}")
    result = requests.get(f"{URL}&start={page*LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class":"jobsearch-SerpJobCard"})
    for result in results:
        job = extract_job(result)
        jobs.append(job)
  return jobs


def get_jobs():
  last_page = get_last_page()
  jobs = extract_jobs(last_page)
  return jobs
