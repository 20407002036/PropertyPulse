from .models import Users, Property

class DBStorage:
    def all(self, cls=None):
        if cls:
            return cls.objects.all()
        else:
            return Users.objects.all(), Property.objects.all()

    def new(self, obj):
        obj.save()

    def save(self):
        pass  # Since objects are saved immediately in Django's ORM, no additional action is needed here

    def delete(self, obj=None):
        if obj:
            obj.delete()

    def reload(self):
        pass  # No need to reload in Django ORM

    def close(self):
        pass  # No need to close connections in Django ORM
