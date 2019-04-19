class AuthRouter(object):

    def db_for_read(self, model, **hints):

        if model._meta.app_label == 'student' or model._meta.app_label == 'auth':
            return 'app_db'

        # elif model._meta.app_label == 'car':
        #     return 'oracle_local_db'
        return 'app_db'
        return None

    def db_for_write(self, model, **hints):

        # if model._meta.app_label == 'student':
        #     return 'app_db'

        if model._meta.app_label == 'car':
            pass
          #  return 'oracle_local_db'
        return 'app_db'

        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'student' or \
           obj2._meta.app_label == 'car':
           return False
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):

        if app_label == 'student':
            return db == 'app_db'
        return 'app_db'
        return None