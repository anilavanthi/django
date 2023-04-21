from django.core.management.base import BaseCommand
from System.formuladata import import_formula_data



class Command(BaseCommand):
    help = 'Exporting FormulaUpdate, FormulaVariables, Formula from Initial json Data'

    def handle(self, *args, **kwargs):
        self.stdout.write("Export Formula json Data Started")
        import_formula_data()      
        self.stdout.write("Exporting Formula json Data Ended")




# python manage.py Import_Formula_Data