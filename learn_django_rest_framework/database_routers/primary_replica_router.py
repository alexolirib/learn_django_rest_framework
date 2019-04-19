import random


class PrimaryReplicaRouter(object):

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'car':
            return 'oracle_local_db'

        if model._meta.app_label == 'auth':
            return 'default'

        return random.choice(["default"])

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'car':
            return 'oracle_local_db'

        if model._meta.app_label == 'auth':
            return 'default'
        return "default"

    def allow_relation(self, obj1, obj2, **hints):

        db_list = ('default')

        if obj1._state.db in db_list and obj2._state.db in db_list:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):

        if db == 'oracle_local_db':
            return False
        return True
