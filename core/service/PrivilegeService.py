from core.entity.concrect.Privilege import Privilege
from .PermissionService import PermissionService

class PrivilegeService:
    
    def __init__(self):
        self.permissionService = PermissionService()    
        
    def getPrivilege(privilege: Privilege):
        return Privilege.objects.get(permission = privilege.permission, entity=privilege.entity)
        
    def existPrivilege(self, privilege: Privilege):
        return self.existPrivilege(privilege)
    
    def save(privilege: Privilege): 
        privilege.save()
        return privilege    

    def saveOrUpdate(self, privilege: Privilege):
        privilege.permission = self.permissionService.saveOrUpdate( privilege.permission )
        return self.getPrivilege(privilege) if self.existPrivilege(privilege)  else self.save(privilege)
        
        
           

