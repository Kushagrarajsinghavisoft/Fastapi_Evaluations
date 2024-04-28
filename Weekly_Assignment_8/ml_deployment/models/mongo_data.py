from mongoengine import Document, FloatField, StringField

# Define document model
class InputFeaturesDocument(Document):
    Income = FloatField()
    Recency = FloatField()
    MntWines = FloatField()
    MntFruits = FloatField()
    MntMeatProducts = FloatField()
    MntGoldProds = FloatField()
    NumWebPurchases = FloatField()
    NumCatalogPurchases = FloatField()
    AcceptedCmp3 = FloatField()
    AcceptedCmp4 = FloatField()
    AcceptedCmp5 = FloatField()
    AcceptedCmp1 = FloatField()
    AcceptedCmp2 = FloatField()
    prediction = StringField()
