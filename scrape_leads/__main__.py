from scraper_leads_gelbeseiten import scrape_gelbesieten
from get_user_input import get_company_type, get_company_location

def main (operation_type='scrape_leads', lead_pool='gelbe_seiten'):

	if operation_type == 'scrape_leads':
		print('Iniciate Lead Generation Scraping')
		if lead_pool == 'gelbe_seiten':
			company_type = get_company_type()
			location = get_company_location()
			df = scrape_gelbesieten(company_type, location)
			filename = company_type + "_" + location
			df.to_excel("./leads/" + filename + ".xlsx", index=False)

	print('Operation has completed')

if __name__ == '__main__':
	main()