from django.contrib.auth.models import Permission

class PermissionService:
    
    def getByCodename(permission: Permission):
        return Permission.objects.get(codename = permission.codename)

    def existByCodename(self, permission: Permission): 
        return self.getPermissionByCodename(permission).exists()
    
    def save(permission: Permission): 
        permission.save()
        return permission
    
    def saveOrUpdate(self, permission: Permission):
        return self.getByCodename(permission) if self.existByCodename(permission)  else self.save(permission)