from django.core.management.base import BaseCommand, CommandError
from search.models import Main_categorie, Product


class Command(BaseCommand):
    def __init__(self):
        self.categories = ["Snacks", "Boissons", "Viandes", "Fromages", "Apéritif"]

    def grab_data(self):
        for item in self.categories:
            url_params = {
                "action": "process",
                "tagtype_0": "categories",
                "tag_contains_0": "contains",
                "tag_0": "categories",
                "sort_by": "unique_scans_n",
                "page_size": 100,
                "json": 1,
            }

        request = requests.get(
            "https://fr.openfoodfacts.org/cgi/search.pl", params=criteria_api
        )
        data = request.json()
        print(data["products"])

    def handle(self, *args, **options):
        self.grab_data()
