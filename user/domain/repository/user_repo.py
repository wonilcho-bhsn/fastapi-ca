from abc import ABCMeta, abstractmethod
from user.domain.user import User

class IUserRepository(metaclass=ABCMeta):
    @abstractmethod
    def save(self, user:User):
        raise NotImplementedError
    
    @abstractmethod
    def find_by_email(self, email:str) -> User:
        """
        find by email. if no user found, raise 422 exception
        Args:
            email (str): _description_
        Returns:
            User: _description_
        """
        return NotImplementedError
    
    @abstractmethod
    def get_users(self, page:int, items_per_page: int) -> tuple[int, list[User]]:
        raise NotImplementedError
    
    @abstractmethod
    def find_by_id(self, id:str) -> User:
        raise NotImplementedError
    
    @abstractmethod
    def update(self, user:User):
        raise NotImplementedError
    
    @abstractmethod
    def delete(self, id:str):
        raise NotImplementedError