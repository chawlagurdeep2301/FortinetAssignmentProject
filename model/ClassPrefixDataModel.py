import mongoengine as me


def generatePrefixNumber(n, prefix=""):
    numPrefix = "CLASSPREFIX{}-{:05}"
    return numPrefix.format(prefix, n)


class ClassPrefixModel(me.DynamicDocument):
    meta = {'collection': 'CLASSPREFIXDATA', 'strict': False}

    prefixNumber = me.SequenceField(sequence_name="CLASSPREFIXDATA", unique=True, value_decorator=generatePrefixNumber)
    tagNumber = me.StringField()
    serviceProvider = me.StringField()
    ip_add = me.StringField()