from typing import Any, List, Optional

from pydantic import BaseModel
from mosaic_minerals_model.processing.validation import MosaicMineralsInputSchema


class PredictionResults(BaseModel):
    errors: Optional[Any]
    version: str
    predictions: Optional[List[float]]


class MultipleMosaicMineralsInputs(BaseModel):
    inputs: List[MosaicMineralsInputSchema]

    class Config:
        schema_extra = {
            "example": {
                "inputs": [
                    {
                        "X": 20,
                        "Y": "RH",
                        "Z": 80.0,
                        "susc": 11622,
                        "susc_mean": "Pave",
                        "susc_max": None,
                        "susc_min": "Reg",
                        "susc_var": "Lvl",
                        "susc_std": "AllPub",
                        "susc_sum": "Inside"
                    }
                ]
            }
        }
