from .base_model import BaseModel, Base
from .user import User
from sqlalchemy import Column, String, Text, Integer, ForeignKey


class Property(BaseModel, Base):
    """
    Property holds the model onto which all property rentals will hold
    """
    __tablename__ = 'property'
    name = Column(String(128), nullable=False)
    address = Column(String(128), nullable=False)
    description = Column(Text, nullable=True)
    num_bedrooms = Column(Integer, nullable=False)
    num_bathrooms = Column(Integer, nullable=False)
    size_sqft = Column(Integer, nullable=False)
    amenities = Column(String, nullable=True)
    status = [
        ('Available', 'Available'),
        ('Rented', 'Rented'),
    ]
    availability_status = Column(String, info=status, nullable=False)
    user_id = Column(String(128), ForeignKey('users.user_id', ondelete='CASCADE'))
    contact_email = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        """Init for the class property"""

        super().__init__(self, *args, **kwargs)

    def __setattr__(self, name, value):

        pass