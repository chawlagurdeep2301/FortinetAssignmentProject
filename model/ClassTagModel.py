import mongoengine as me


def generateTagnumber(n, prefix=""):
    numPrefix = "CLASSTAG{}-{:05}"
    return numPrefix.format(prefix, n)


class ClassTagModel(me.DynamicDocument):
    meta = {'collection': 'CLASSTAGDATA', 'strict': False}

    tagNumber = me.SequenceField(sequence_name="CLASSTAG", unique=True, value_decorator=generateTagnumber)
    serviceProvider = me.StringField()
    cloudProvider = me.StringField()
    cloudProviderName = me.StringField()