from ...Domain.entities import DataOfEsp
from sqlalchemy import Column, Float, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class DataOfEspModel(Base):
    __tablename__ = "data_of_esp"

    id = Column(Integer, primary_key=True, index=True)
    humidity = Column(Float, nullable=False)
    temperature = Column(Float, nullable=False)
    conductivity = Column(Float, nullable=False)
    ph = Column(Float, nullable=False)
    nitrogen = Column(Float, nullable=False)
    phosphorus = Column(Float, nullable=False)
    potassium = Column(Float, nullable=False)

    def to_entity(self) -> DataOfEsp:
        """
        Converte o modelo de banco de dados para a entidade de domínio DataOfEsp.
        """
        return DataOfEsp(
            humidity=self.humidity,
            temperature=self.temperature,
            conductivity=self.conductivity,
            ph=self.ph,
            nitrogen=self.nitrogen,
            phosphorus=self.phosphorus,
            potassium=self.potassium
        )
