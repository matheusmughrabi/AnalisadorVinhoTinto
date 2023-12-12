from pydantic import BaseModel, Field


class VinhoDto(BaseModel):
    fixed_acidity: float = Field(..., alias='fixedAcidity')
    volatile_acidity: float = Field(..., alias='volatileAcidity')
    chlorides: float
    total_sulfur_dioxide: float = Field(..., alias='totalSulfurDioxide')
    sulphates: float
    alcohol: float

    class Config:
        allow_population_by_field_name = True