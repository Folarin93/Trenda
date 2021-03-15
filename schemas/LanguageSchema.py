from main import mar
from models.Language import Languages

class LanguageSchema(mar.SQLAlchemyAutoSchema):
    class Meta:
        model = Languages

language_schema = LanguageSchema()
languages_schema = LanguageSchema(many=True)


