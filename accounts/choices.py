from djchoices import DjangoChoices, ChoiceItem


class GenderTypeChoices(DjangoChoices):
    Male = ChoiceItem(1)
    Female = ChoiceItem(2)
    Other = ChoiceItem(3)

    GENDER_LIST = [1, 2, 3]
    GENDER_CRIF_DICT = {Male.value: "M", Female.value: "F", Other.value: "T"}


GENDER_DICT = dict(GenderTypeChoices.choices)
gender_enum = dict(Male=GenderTypeChoices.Male,
                   Female=GenderTypeChoices.Female, Other=GenderTypeChoices.Other)
