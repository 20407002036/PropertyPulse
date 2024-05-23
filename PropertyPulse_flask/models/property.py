from .base_model import BaseModel
from .storage import Base
# from .user import User
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Text, Integer, ForeignKey, Enum, DECIMAL


class Property(BaseModel, Base):
    """
    Property holds the model onto which all property rentals will hold
    """
    __tablename__ = 'property'

    name = Column(String(128), nullable=False)
    address = Column(String(128), nullable=False)
    description = Column(Text, nullable=True)
    rent_price = Column(DECIMAL(10, 2))
    num_bedrooms = Column(Integer, nullable=False)
    num_bathrooms = Column(Integer, nullable=False)
    size_sqft = Column(Integer, nullable=False)
    amenities = Column(String(128), nullable=True)
    
    availability_status = Column(Enum('available', 'rented'), default='available')
    user_id = Column(String(128), ForeignKey('users.id'), nullable=False)
    contact_email = Column(String(128), nullable=False)


    def __init__(self, *args, **kwargs):
        """Init for the class property"""

        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):

        super().__setattr__(name, value)