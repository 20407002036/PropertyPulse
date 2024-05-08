from .base_model import BaseModel
from .storage import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Text, ForeignKey


class Review(BaseModel, Base):
    """THis will hold reviews from the users"""

    __tablename__ = 'reviews'

    rental = Column(String(128), nullable=False)
    reviewTxt = Column(Text, nullable=False)
    user_id = Column(String(128), ForeignKey('user.id', ondelete='CASCADE'), nullable=False)

    

    def __inti__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return f"<Review {self.id} {self.reviewTxt}>"
