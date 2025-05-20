from faker import Faker
from .vprovider import VietnamProvider
from .schema_loader import load_schema

class DataGenerator:
    def __init__(self, schema_path):
        self.schema = load_schema(schema_path)
        self.faker = Faker()
        self.faker.add_provider(VietnamProvider)

    def generate(self, count):
        data = []
        for table_name, table_schema in self.schema.tables.items():
            for _ in range(count):
                row = {}
                for field_name, field_schema in table_schema.fields.items():
                    if field_schema.faker:
                        row[field_name] = getattr(self.faker, field_schema.faker)()
                    else:
                        if field_schema.type == "integer":
                            row[field_name] = self.faker.random_int(1, 1000)
                        elif field_schema.type == "string":
                            row[field_name] = self.faker.word()
                data.append(row)
        return data